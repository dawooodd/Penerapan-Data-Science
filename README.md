# Proyek Akhir: Menyelesaikan Permasalahan Human Resources - Jaya Jaya Maju

## Business Understanding

### Latar Belakang
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di berbagai penjuru negeri. Sebagai entitas korporasi yang bertumbuh pesat, pengelolaan modal manusia (*Human Capital*) menjadi fondasi esensial untuk menjaga keberlanjutan operasional, keunggulan bersaing, dan pencapaian target bisnis perusahaan.

### Permasalahan Bisnis
Meskipun telah berskala besar, Jaya Jaya Maju menghadapi kendala serius dalam retensi talenta. Perusahaan mengalami **tingkat turnover (*attrition rate*) yang mencapai 16.9%** (secara signifikan melampaui batas toleransi batas maksimal yang ditetapkan manajemen sebesar **10%**). Tingginya perputaran karyawan ini menimbulkan dampak negatif yang signifikan, antara lain:
1. **Biaya Finansial (*Turnover Cost*):** Tingginya pengeluaran untuk rekrutmen, orientasi, serta pelatihan karyawan pengganti (*replacement cost* umumnya mencapai 1.5 - 2x gaji tahunan karyawan terkait).
2. **Hilangnya Pengetahuan Institusional (*Loss of Knowledge*):** Kehilangan talenta kunci menurunkan efisiensi tim dan menghambat keberlangsungan proyek penting.
3. **Disrupsi Produktivitas & Moral Tim:** Beban kerja karyawan yang bertahan meningkat drastis untuk menutupi kekosongan, memicu stres berkelanjutan dan efek domino pengunduran diri.

### Cakupan Proyek
Untuk mengatasi permasalahan tersebut, proyek *Data Science & HR Analytics* ini mencakup tahapan *end-to-end* sebagai berikut:
1. **Exploratory Data Analysis (EDA):** Mengidentifikasi akar penyebab (*root causes*) dan pola perilaku kepegawaian yang mendorong tingginya tingkat *attrition*.
2. **Machine Learning Modeling:** Mengembangkan model klasifikasi prediktif berbasis *Pipeline* scikit-learn (Random Forest, Gradient Boosting, Logistic Regression) untuk mendeteksi karyawan yang memiliki risiko tinggi untuk keluar.
3. **Model Deployment & Inference Script:** Menyediakan script mandiri `prediction.py` yang dapat memindai karyawan aktif secara berkala dan memberikan rekomendasi tindakan mitigasi yang terpersonalisasi.
4. **Business Dashboard Design:** Merancang arsitektur dashboard analitik interaktif di Metabase untuk memonitor metrik turnover dan faktor-faktor pemicunya secara *real-time*.
5. **Actionable Recommendations:** Merumuskan rekomendasi bisnis strategis dan terukur bagi departemen HR untuk menekan *attrition rate* kembali ke bawah 10%.

---

### Persiapan & Setup Environment

#### 1. Struktur Direktori Proyek
```text
Penerapan-Data-Science/
│
├── employee_data.csv               # Dataset utama kepegawaian
├── notebook.ipynb                  # Jupyter Notebook (EDA, Preprocessing, Modeling, Evaluation)
├── prediction.py                   # Script inferensi mandiri untuk prediksi turnover
├── requirements.txt                # Berkas dependensi Python
├── README.md                       # Dokumentasi lengkap proyek
├── nasich_dicoding-dashboard       # File screenshot business dashboard
proyek
└── model/
    ├── model.joblib                # Serialized machine learning pipeline (Random Forest)
    └── model_meta.json             # Metadata fitur dan parameter model
```

#### 2. Setup Environment Python
Pastikan Python versi 3.10+ telah terinstal pada sistem Anda. Pasang seluruh pustaka yang diperlukan dengan menjalankan perintah berikut di terminal:

```bash
pip install -r requirements.txt
```

---

## Business Dashboard

Untuk membantu manajer HR memantau dinamika tenaga kerja dan mengintervensi faktor risiko pengunduran diri secara real-time, dirancang sebuah **Business Dashboard** interaktif berbasis cloud menggunakan **Google Looker Studio**.

- **Tautan Dashboard Publik:** [Link to Looker Studio Dashboard](https://datastudio.google.com/s/vCx8_JSsIdM)



1. **Section 1 - Executive KPI Summary Cards:**
   - *Total Active Employees*: Jumlah keseluruhan karyawan aktif saat ini.
   - *Historical Attrition Rate*: 16.9% (dengan indikator status merah karena melebihi threshold 10%).
   - *High & Medium Risk Employees*: Jumlah karyawan aktif saat ini yang diprediksi berada pada zona bahaya turnover.
   - *Salary Disparity Gap*: Selisih rata-rata kompensasi antara karyawan bertahan ($6,983) dan yang keluar ($4,873).
2. **Section 2 - Driver Operasional (Root Cause):**
   - *OverTime vs Attrition Bar Chart*: Memperlihatkan bahwa lembur merupakan katalis turnover terkuat (31.9% vs 10.8%).
   - *Job Role Breakdown*: Mengisolasi departemen dan posisi paling rentan, terutama *Sales Representative* (43.1%) dan *Laboratory Technician* (26.1%).
3. **Section 3 - Kompensasi & Insentif Saham:**
   - *Job Level Distribution*: Menampilkan bahwa karyawan pemula (Level 1) paling rentan mengalami *turnover* akibat ketidakpuasan gaji awal.
   - *Stock Option Level Comparison*: Menunjukkan bahwa pemberian opsi saham level 1 dan 2 berhasil menekan turnover hingga di bawah 10%.
4. **Section 4 - Kepuasan Kerja & Masa Kerja (Tenure):**
   - *Tenure Attrition Curve*: Menunjukkan bahwa retensi paling kritis terjadi pada rentang masa kerja 1-3 tahun dan 1 tahun pertama bersama manajer baru.

---

## Conclusion

Berdasarkan hasil analisis data eksploratif (EDA) dan pemodelan prediktif machine learning pada data kepegawaian Jaya Jaya Maju, diperoleh kesimpulan penting berikut:

1. **Akar Penyebab Utama Turnover (*Root Causes*):**
   - **Beban Lembur (*Chronic OverTime*):** Karyawan dengan status lembur memiliki tingkat turnover **31.9%**, hampir **3 kali lipat** dibandingkan karyawan non-lembur (**10.8%**).
   - **Kerapuhan Posisi Lapangan & Teknis:** Posisi *Sales Representative* mengalami turnover ekstrem (**43.1%**), disusul *Laboratory Technician* (**26.1%**) dan *Human Resources* (**20.0%**).
   - **Disparitas Finansial pada Posisi Pemula (*Entry-Level Disadvantage*):** Karyawan pada *Job Level 1* memiliki turnover tertinggi (**27.4%**). Median gaji karyawan yang keluar hanya **$3,388/bulan**, berbanding jauh dengan karyawan yang bertahan (**$5,210/bulan**).
   - **Efektivitas Opsi Saham (*Golden Handcuffs*):** Karyawan yang tidak memiliki kepemilikan saham (*Stock Option Level 0*) mencatat turnover **25.7%**, sedangkan karyawan dengan opsi saham Level 1 dan Level 2 memiliki turnover yang sangat rendah (**<10%**).
   - **Fenomena *Tenure Shock* (Tahun 1-3):** Pengunduran diri terkonsentrasi sangat masif pada karyawan dengan masa kerja 1 hingga 3 tahun dan yang baru bekerja di bawah 1 tahun dengan manajer langsung saat ini.

2. **Kinerja Model Prediktif:**
   - Model **Random Forest Pipeline** dengan penanganan ketidakseimbangan kelas (*balanced subsample*) dan *threshold tuning* (0.35) berhasil mencapai performa diskriminasi **ROC-AUC sebesar ~0.80**.
   - Model ini mampu membedakan profil karyawan berisiko secara andal tanpa mengorbankan stabilitas generalisasi, siap digunakan sebagai instrumen audit retensi berkala.

---

### Rekomendasi Action Items

Guna menyelesaikan permasalahan turnover dan menurunkan *attrition rate* kembali ke bawah 10%, berikut adalah 5 rekomendasi tindakan strategis dan terukur bagi Manajemen HR Jaya Jaya Maju:

1. **Penerapan Kebijakan Audit Beban Kerja & Pembatasan Lembur (*Workload & OverTime Rebalancing*)**
   - *Tindakan:* Mengaudit jam kerja mingguan dan menetapkan kuota maksimal lembur per individu. Departemen Sales dan Operasional wajib mendistribusikan beban kerja secara seimbang atau menambah staf paruh waktu/asisten penjualan jika beban harian berlebih.
   - *Target:* Menurunkan proporsi karyawan lembur reguler sebesar 40% dan menekan turnover kelompok lembur dari 31.9% menjadi <15%.

2. **Restrukturisasi Kompensasi & Paket Retensi Khusus untuk Sales Representative & Entry Level**
   - *Tindakan:* Melakukan *market salary benchmarking* pada jabatan *Job Level 1* dan *Sales Representative*. Ubah struktur kompensasi dari skema berbasis komisi murni yang fluktuatif menjadi gaji pokok yang lebih kompetitif ditambah bonus performa bertahap (*tiered incentives*).
   - *Target:* Menurunkan turnover *Sales Representative* dari 43.1% menjadi <20% dalam kurun waktu 12 bulan.

3. **Demokratisasi Program Kepemilikan Saham Karyawan (*Employee Stock Ownership Plan - ESOP*)**
   - *Tindakan:* Menurunkan syarat kepemilikan opsi saham yang sebelumnya terbatas pada level senior. Tawarkan *Stock Option Level 1* kepada karyawan berkinerja baik (*Performance Rating 3 & 4*) yang telah melewati masa kerja 1 tahun dengan skema *vesting period* 3-4 tahun.
   - *Target:* Menurunkan kelompok karyawan tanpa saham (*Level 0*) dan memanfaatkan efek retensi jangka panjang untuk menekan turnover hingga di bawah 10%.

4. **Program Akselerasi Onboarding & Penguatan Kapabilitas Kepemimpinan Manajer (*Manager-Employee Alignment*)**
   - *Tindakan:* Membangun program bimbingan (*buddy & mentorship system*) selama 12 bulan pertama masa kerja untuk mengatasi *tenure shock*. Memberikan pelatihan *people management* kepada para supervisor/manajer agar rutin menyelenggarakan sesi *one-on-one stay interview* setiap kuartal.
   - *Target:* Meningkatkan retensi karyawan pada rentang tahun ke-1 hingga ke-3 sebesar minimal 35%.

5. **Pengoperasian Sistem Peringatan Dini Retensi Berbasis AI (*Predictive Retention Early-Warning System*)**
   - *Tindakan:* Mengintegrasikan script `prediction.py` ke dalam alur kerja bulanan/kuartalan HR. Karyawan yang teridentifikasi dalam kategori *High Risk* (>60%) atau *Medium Risk* (35-60%) secara otomatis dialokasikan untuk intervensi personal (konseling karir, penyesuaian fleksibilitas kerja, atau tinjauan kompensasi) sebelum mereka mengajukan pengunduran diri.
   - *Target:* Mengintervensi minimal 80% karyawan berisiko tinggi sebelum fase pengunduran diri aktif.

---

## Panduan Menjalankan Script Prediksi (Inference)

Untuk melakukan prediksi turnover pada data karyawan baru atau data karyawan aktif saat ini, gunakan script `prediction.py`.

### 1. Menjalankan Demonstrasi Prediksi (Sample Profiles)
Jalankan script tanpa argumen tambahan untuk menguji model terhadap 3 profil karyawan dengan karakteristik risiko yang kontras:
```bash
python prediction.py
```

### 2. Memprediksi Risiko Karyawan Aktif dari File Dataset
Jalankan script dengan parameter `--file` dan filter khusus `--unlabeled-only` untuk memprediksi 412 data karyawan aktif saat ini:
```bash
python prediction.py --file employee_data.csv --unlabeled-only --output hasil_prediksi_karyawan_aktif.csv
```

### 3. Memprediksi Dataset Karyawan Kustom
```bash
python prediction.py --file path/to/karyawan_baru.csv --output hasil_prediksi.csv
```

### 4. Output Hasil Prediksi
Script menghasilkan output tabel yang rapi di terminal dan menyimpan berkas CSV dengan kolom-kolom berikut:
- `EmployeeId`: Nomor identifikasi karyawan.
- `Attrition_Probability_Pct`: Estimasi probabilitas keluar (0.00% - 100.00%).
- `Predicted_Attrition`: Flag biner (1: Akan Keluar, 0: Bertahan) berdasarkan ambang batas optimal 0.35.
- `Predicted_Status`: Label status ("Will Leave" / "Will Stay").
- `Risk_Tier`: Kategori risiko (`LOW RISK` [<35%], `MEDIUM RISK` [35-60%], `HIGH RISK` [>=60%]).
- `HR_Recommended_Action`: Rekomendasi tindakan intervensi spesifik yang disesuaikan dengan faktor risiko individu karyawan terkait.
