import argparse
import json
import os
import sys
import joblib
import numpy as np
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'model.joblib')
META_PATH = os.path.join(BASE_DIR, 'model', 'model_meta.json')
DEFAULT_THRESHOLD = 0.35

def load_model(model_path=MODEL_PATH):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at '{model_path}'. Please train the model first.")
    return joblib.load(model_path)

def load_metadata(meta_path=META_PATH):
    if os.path.exists(meta_path):
        with open(meta_path, 'r') as f:
            return json.load(f)
    return {}

def categorize_risk(prob: float) -> str:
    if prob >= 0.60:
        return 'HIGH RISK'
    elif prob >= 0.35:
        return 'MEDIUM RISK'
    else:
        return 'LOW RISK'

def generate_hr_recommendation(row: pd.Series, prob: float) -> str:
    actions = []
    if prob < 0.35:
        return 'Maintain engagement & standard career progression'
    
    if row.get('OverTime') == 'Yes':
        actions.append('Rebalance workload / eliminate chronic overtime')
    if row.get('StockOptionLevel', 1) == 0:
        actions.append('Grant equity/stock options retention package')
    if row.get('MonthlyIncome', 10000) < 4000:
        actions.append('Conduct salary benchmarking & compensation review')
    if row.get('YearsWithCurrManager', 5) <= 1:
        actions.append('Manager 1-on-1 alignment & onboarding mentorship')
    if row.get('WorkLifeBalance', 3) <= 2:
        actions.append('Offer flexible working arrangements / wellness support')
    if not actions:
        actions.append('Conduct proactive stay interview')
    return '; '.join(actions)

def predict_attrition(data: pd.DataFrame, pipeline=None, threshold=DEFAULT_THRESHOLD) -> pd.DataFrame:
    if pipeline is None:
        pipeline = load_model()
    
    input_df = data.copy()
    emp_ids = input_df['EmployeeId'].values if 'EmployeeId' in input_df.columns else range(1, len(input_df) + 1)
    
    drop_cols = ['Attrition', 'EmployeeId', 'EmployeeCount', 'Over18', 'StandardHours']
    features_df = input_df.drop(columns=[c for c in drop_cols if c in input_df.columns], errors='ignore')
    
    probas = pipeline.predict_proba(features_df)[:, 1]
    preds = (probas >= threshold).astype(int)
    
    results = pd.DataFrame({
        'EmployeeId': emp_ids,
        'Attrition_Probability_Pct': np.round(probas * 100, 2),
        'Predicted_Attrition': preds,
        'Predicted_Status': ['Will Leave' if p == 1 else 'Will Stay' for p in preds],
        'Risk_Tier': [categorize_risk(p) for p in probas]
    })
    
    actions = [generate_hr_recommendation(row, probas[i]) for i, (_, row) in enumerate(input_df.iterrows())]
    results['HR_Recommended_Action'] = actions
    return results

def get_sample_data() -> pd.DataFrame:
    return pd.DataFrame([
        {
            'EmployeeId': 9001, 'Age': 28, 'BusinessTravel': 'Travel_Frequently',
            'DailyRate': 400, 'Department': 'Sales', 'DistanceFromHome': 25,
            'Education': 2, 'EducationField': 'Marketing', 'EnvironmentSatisfaction': 1,
            'Gender': 'Male', 'HourlyRate': 45, 'JobInvolvement': 2, 'JobLevel': 1,
            'JobRole': 'Sales Representative', 'JobSatisfaction': 1, 'MaritalStatus': 'Single',
            'MonthlyIncome': 2400, 'MonthlyRate': 16000, 'NumCompaniesWorked': 3,
            'OverTime': 'Yes', 'PercentSalaryHike': 11, 'PerformanceRating': 3,
            'RelationshipSatisfaction': 1, 'StockOptionLevel': 0, 'TotalWorkingYears': 3,
            'TrainingTimesLastYear': 1, 'WorkLifeBalance': 1, 'YearsAtCompany': 1,
            'YearsInCurrentRole': 1, 'YearsSinceLastPromotion': 0, 'YearsWithCurrManager': 0
        },
        {
            'EmployeeId': 9002, 'Age': 45, 'BusinessTravel': 'Travel_Rarely',
            'DailyRate': 1100, 'Department': 'Research & Development', 'DistanceFromHome': 4,
            'Education': 4, 'EducationField': 'Life Sciences', 'EnvironmentSatisfaction': 4,
            'Gender': 'Female', 'HourlyRate': 85, 'JobInvolvement': 4, 'JobLevel': 4,
            'JobRole': 'Manufacturing Director', 'JobSatisfaction': 4, 'MaritalStatus': 'Married',
            'MonthlyIncome': 13500, 'MonthlyRate': 21000, 'NumCompaniesWorked': 1,
            'OverTime': 'No', 'PercentSalaryHike': 18, 'PerformanceRating': 3,
            'RelationshipSatisfaction': 4, 'StockOptionLevel': 2, 'TotalWorkingYears': 22,
            'TrainingTimesLastYear': 3, 'WorkLifeBalance': 3, 'YearsAtCompany': 15,
            'YearsInCurrentRole': 8, 'YearsSinceLastPromotion': 2, 'YearsWithCurrManager': 7
        },
        {
            'EmployeeId': 9003, 'Age': 32, 'BusinessTravel': 'Travel_Rarely',
            'DailyRate': 650, 'Department': 'Research & Development', 'DistanceFromHome': 14,
            'Education': 3, 'EducationField': 'Medical', 'EnvironmentSatisfaction': 2,
            'Gender': 'Male', 'HourlyRate': 65, 'JobInvolvement': 3, 'JobLevel': 2,
            'JobRole': 'Laboratory Technician', 'JobSatisfaction': 2, 'MaritalStatus': 'Single',
            'MonthlyIncome': 4200, 'MonthlyRate': 15000, 'NumCompaniesWorked': 2,
            'OverTime': 'Yes', 'PercentSalaryHike': 12, 'PerformanceRating': 3,
            'RelationshipSatisfaction': 2, 'StockOptionLevel': 0, 'TotalWorkingYears': 7,
            'TrainingTimesLastYear': 2, 'WorkLifeBalance': 2, 'YearsAtCompany': 3,
            'YearsInCurrentRole': 2, 'YearsSinceLastPromotion': 1, 'YearsWithCurrManager': 1
        }
    ])

def main():
    parser = argparse.ArgumentParser(description='Inference Engine for HR Attrition - Jaya Jaya Maju')
    parser.add_argument('--file', type=str, default=None, help='CSV file with employee records')
    parser.add_argument('--unlabeled-only', action='store_true', help='Filter for unlabeled active employees')
    parser.add_argument('--threshold', type=float, default=DEFAULT_THRESHOLD, help='Attrition decision threshold')
    parser.add_argument('--output', type=str, default=None, help='Export results to CSV file')
    args = parser.parse_args()

    print('=' * 80)
    print('  JAYA JAYA MAJU - HR EMPLOYEE ATTRITION INFERENCE ENGINE')
    print('=' * 80)
    pipeline = load_model()
    meta = load_metadata()
    print(f"[*] Loaded Model: {meta.get('model_name', 'RandomForestClassifier')}")
    print(f"[*] Test ROC-AUC: {meta.get('roc_auc_test', 'N/A')}")
    print(f"[*] Threshold: {args.threshold}")

    if args.file:
        print(f"[*] Loading data from: {args.file}")
        df = pd.read_csv(args.file)
        if args.unlabeled_only and 'Attrition' in df.columns:
            df = df[df['Attrition'].isna()].copy()
            print(f"[*] Filtered to {len(df)} unlabeled active employees.")
    else:
        print('[*] No file specified. Running demonstration on sample employee profiles.')
        df = get_sample_data()

    results = predict_attrition(df, pipeline=pipeline, threshold=args.threshold)
    print('\n' + '=' * 80)
    print('  PREDICTION RESULTS')
    print('=' * 80)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 55)
    print(results.to_string(index=False))

    print('\n' + '-' * 80)
    print('Risk Distribution:')
    for tier, count in results['Risk_Tier'].value_counts().items():
        print(f"  - {tier:12s}: {count:4d} employees ({count/len(results)*100:.1f}%)")
    
    if args.output:
        results.to_csv(args.output, index=False)
        print(f"\n[Success] Results saved to {args.output}")
    print('=' * 80)

if __name__ == '__main__':
    main()
