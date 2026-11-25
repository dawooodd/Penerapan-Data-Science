# Proyek Akhir: Menyelesaikan Permasalahan Human Resources - Jaya Jaya Maju

## Business Understanding

### Latar Belakang
Jaya Jaya Maju merupakan salah satu perusahaan multinasional terkemuka yang telah berdiri sejak tahun 2000. Saat ini, perusahaan telah berkembang pesat dan menaungi lebih dari 1.000 karyawan yang tersebar di berbagai unit operasional di seluruh penjuru negeri. Sebagai entitas korporasi berskala besar, pengelolaan modal manusia (*Human Capital*) yang efektif memegang peranan fundamental dalam menjaga stabilitas kinerja bisnis, efisiensi operasional, serta daya saing korporasi.

### Permasalahan Bisnis
Walaupun telah menjadi perusahaan yang cukup besar dan mapan, Jaya Jaya Maju masih menghadapi kendala serius dalam mengelola dan mempertahankan karyawannya. Hal ini berimbas pada tingginya rasio pengunduran diri (*attrition rate*) yang mencapai **lebih dari 10%**.

Tingginya angka turnover yang melampaui ambang batas toleransi perusahaan ini menimbulkan dampak negatif dan kerugian nyata bagi organisasi:
1. **Tingginya Biaya Pergantian Karyawan (*Turnover Cost*):** Pengeluaran besar untuk proses rekrutmen, orientasi, serta pelatihan karyawan pengganti (*replacement cost* diestimasikan mencapai 1.5 hingga 2 kali lipat dari gaji tahunan posisi terkait).
2. **Penurunan Efisiensi Operasional:** Terjadinya kekosongan posisi kerja yang menghambat kontinuitas proyek strategis dan menurunkan produktivitas tim.
3. **Disrupsi Moral & Beban Kerja Tim:** Karyawan yang bertahan terbebani akumulasi pekerjaan tambahan (*workload overload*), meningkatkan risiko stres berkepanjangan (*burnout*) dan memicu efek domino pengunduran diri lanjutan.

Berdasarkan permasalahan bisnis tersebut, proyek data science ini diarahkan untuk menjawab pertanyaan-pertanyaan utama berikut:
1. Faktor-faktor operasional, demografis, dan kompensasi apa sajakah yang menjadi akar penyebab (*root causes*) di balik tingginya *attrition rate* di Jaya Jaya Maju?
2. Bagaimana cara memantau faktor-faktor pemicu turnover (*attrition drivers*) tersebut secara visual, efektif, dan berkelanjutan bagi manajemen?
3. Bagaimana membangun model prediktif machine learning untuk mendeteksi risiko *attrition* karyawan sejak dini agar departemen HR dapat melakukan tindakan retensi preventif?

### Cakupan Proyek
Untuk mengatasi permasalahan tersebut secara komprehensif, proyek *Data Science & HR Analytics* ini mengimplementasikan alur kerja analitik *end-to-end* yang mencakup:
1. **Exploratory Data Analysis (EDA):** Mengidentifikasi pola perilaku dan faktor pemicu utama turnover karyawan melalui analisis statistik dan visualisasi data.
2. **Interactive Business Dashboard:** Memvisualisasikan metrik kunci kepegawaian dan faktor pemicu turnover menggunakan business dashboard berbasis cloud.
3. **Machine Learning Predictive Modeling:** Mengembangkan model klasifikasi prediktif berbasis *Pipeline* scikit-learn (Random Forest Classifier) yang dioptimasi untuk mendeteksi profil karyawan yang memiliki probabilitas tinggi untuk keluar.
4. **Inference Script Deployment:** Menyediakan script mandiri `prediction.py` yang siap digunakan oleh tim HR untuk menilai risiko retensi karyawan secara berkala dan memberikan rekomendasi intervensi personal.
5. **Rekomendasi Strategis:** Menyusun rekomendasi tindakan konkret berbasis data (*data-driven action items*) yang terukur untuk menekan *attrition rate* kembali ke bawah 10%.

### Persiapan

#### Sumber Data
Dataset yang digunakan berasal dari rekam jejak kepegawaian PT Jaya Jaya Maju yang memuat informasi demografis, kepuasan kerja, metrik operasional, kompensasi, dan status kepegawaian.
- **Tautan Repositori Data Resmi:** https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

#### Setup Environment
Pastikan Anda telah menyiapkan environment Python (versi 3.9 atau lebih baru) dan menginstal seluruh pustaka yang tercantum pada berkas `requirements.txt` menggunakan salah satu metode di bawah ini:

##### 1. Setup Environment Menggunakan Anaconda (Conda)
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

##### 2. Setup Environment Menggunakan Shell / Terminal (Pipenv)
```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## Business Dashboard

Untuk memberikan visibilitas eksekutif bagi manajer HR dalam memantau dinamika tenaga kerja dan mengintervensi faktor risiko pengunduran diri secara proaktif, telah dibangun **Business Dashboard** interaktif berbasis cloud menggunakan **Google Looker Studio**.

- **Tautan Dashboard Publik:** [Tautan Looker Studio Dashboard](https://datastudio.google.com/s/hH7lVIotteQ)

Dashboard ini memvisualisasikan faktor-faktor utama pemicu attrition (*attrition drivers*), antara lain:
1. **Executive KPI Scorecards:** Menampilkan Total Karyawan Aktif, Baseline Attrition Rate (vs Batas Toleransi 10%), Estimasi Karyawan Berisiko, dan Kesenjangan Kompensasi Bulanan.
2. **Katalis Beban Lembur (*OverTime*):** Grafik komparasi tingkat turnover antara kelompok karyawan lembur vs tidak lembur.
3. **Pemetaan Jabatan Kritis (*Job Role Vulnerability*):** Identifikasi posisi dengan turnover paling ekstrem, khususnya *Sales Representative* dan *Laboratory Technician*.
4. **Dinamika Finansial & Opsi Saham:** Distribusi turnover berdasarkan jenjang jabatan (*Job Level*) serta efektivitas retensi kepemilikan opsi saham (*Stock Option Level*).
5. **Kurva Masa Kerja (*Tenure Decay Curve*):** Titik rawan pengunduran diri yang terkonsentrasi kuat pada rentang awal masa kerja karyawan.
6. **Interactive Filter Controls:** Dilengkapi pemfilter interaktif berdasarkan Departemen, Jabatan (*Job Role*), Jenis Kelamin, dan Status Pernikahan.

*(Catatan: Pastikan opsi berbagi pada Google Looker Studio telah diatur ke "Anyone on the internet with the link can view").*

---

## Menjalankan Sistem Machine Learning

Model machine learning telah dibungkus ke dalam pipeline scikit-learn (`model/model.joblib`) yang menggabungkan standardisasi fitur numerik, one-hot encoding fitur kategorikal, serta klasifikasi menggunakan Random Forest dengan penanganan ketidakseimbangan kelas.

### 1. Instalasi Dependensi
Pastikan seluruh pustaka dependensi yang tercantum pada `requirements.txt` telah terpasang:
```bash
pip install -r requirements.txt
```

### 2. Menjalankan Demonstrasi Prediksi (Sample Profiles)
Jalankan script `prediction.py` tanpa argumen tambahan untuk menguji sistem inferensi pada 3 profil sampel karyawan (karyawan risiko tinggi, menengah, dan rendah):
```bash
python prediction.py
```

### 3. Memprediksi Risiko Karyawan Aktif dari File Dataset
Untuk memindai data karyawan aktif yang belum memiliki label `Attrition` pada dataset `employee_data.csv` dan mengekspor hasilnya:
```bash
python prediction.py --file employee_data.csv --unlabeled-only --output hasil_prediksi_karyawan_aktif.csv
```

### 4. Memprediksi Berkas CSV Karyawan Kustom
Untuk menjalankan prediksi pada berkas data kepegawaian baru:
```bash
python prediction.py --file path/to/karyawan_baru.csv --output hasil_prediksi.csv
```

### 5. Struktur Output Prediksi
Script menghasilkan output tabel terstruktur di konsol dan mengekspor file CSV dengan atribut:
- `EmployeeId`: Nomor identifikasi karyawan.
- `Attrition_Probability_Pct`: Estimasi probabilitas keluar (0.00% - 100.00%).
- `Predicted_Attrition`: Flag biner (1 = Akan Keluar, 0 = Bertahan) berdasarkan ambang batas optimal (0.35).
- `Predicted_Status`: Label status ("Will Leave" atau "Will Stay").
- `Risk_Tier`: Kategori risiko (`LOW RISK` [<35%], `MEDIUM RISK` [35-60%], `HIGH RISK` [>=60%]).
- `HR_Recommended_Action`: Rekomendasi intervensi terpersonalisasi untuk departemen HR.

---

## Kesimpulan

Berdasarkan analisis data eksploratif (EDA) dan evaluasi pemodelan prediktif pada data kepegawaian Jaya Jaya Maju, diperoleh 4 kesimpulan konkret mengenai pemicu utama turnover karyawan:

- **Beban Lembur Berlebihan (*Chronic OverTime*):** Karyawan dengan status kerja lembur memiliki tingkat turnover sebesar **31.9%**, hampir **tiga kali lipat** lebih tinggi dibandingkan karyawan non-lembur (**10.8%**). Lembur kronis menjadi katalis utama penurunan kepuasan kerja dan kelelahan mental (*burnout*).
- **Kerentanan Jabatan Tertentu (*Job Role Vulnerability*):** Eksodus talenta terkonsentrasi sangat tinggi pada posisi garda depan dan teknis, dipimpin oleh **Sales Representative (43.1%)**, disusul **Laboratory Technician (26.1%)**, dan **Human Resources (20.0%)**.
- **Disparitas Finansial & Posisi Pemula (*Entry-Level Disadvantage*):** Karyawan pada jenjang **Job Level 1** mencatat tingkat turnover tertinggi (**27.4%**). Terdapat kesenjangan kompensasi bulanan yang mencolok: median pendapatan karyawan yang keluar hanya **$3,388/bulan**, berbanding jauh dengan karyawan yang bertahan sebesar **$5,210/bulan** (selisih lebih dari $1,800/bulan).
- **Kejutan Masa Kerja Awal & Efektivitas Opsi Saham (*Tenure Shock & ESOP*):** Pengunduran diri paling masif terkonsentrasi pada **1 hingga 3 tahun pertama masa kerja**. Selain itu, karyawan tanpa kepemilikan opsi saham (**Stock Option Level 0**) memiliki turnover **25.7%**, sedangkan pemegang saham Level 1 dan 2 memiliki turnover di bawah **10%**, membuktikan peran vital kepemilikan saham sebagai instrumen retensi jangka panjang.

---

### Rekomendasi Action Items

Untuk mereduksi *attrition rate* Jaya Jaya Maju hingga konsisten berada di bawah batas toleransi 10%, berikut adalah 5 rekomendasi strategis dan terukur bagi Manajer HR:

1. **Audit Beban Kerja & Pembatasan Jam Lembur (*OverTime Capping & Workload Rebalancing*)**
   - *Tindakan:* Berlakukan batas maksimal lembur mingguan (maksimal 8-10 jam/minggu) dan lakukan audit distribusi beban kerja rutin di divisi Sales dan R&D. Jika kelebihan beban bersifat struktural, rekrut tenaga pendukung operasional (*sales support / administrative assistant*).
   - *Target:* Menurunkan proporsi staf lembur sebesar 40% dan menekan turnover kelompok lembur dari 31.9% menjadi <15%.

2. **Restrukturisasi Kompensasi untuk Posisi Sales Representative & Job Level 1**
   - *Tindakan:* Lakukan *salary benchmarking* terhadap pasar. Alihkan skema kompensasi *Sales Representative* dari komisi murni yang berfluktuasi tinggi ke peningkatan gaji pokok (*base salary*) kompetitif yang dipadukan dengan bonus performa bertingkat (*tiered incentive*).
   - *Target:* Menurunkan turnover posisi *Sales Representative* dari 43.1% menjadi <20% dalam kurun waktu 12 bulan.

3. **Demokratisasi Program Opsi Saham Karyawan (*ESOP Re-tiering*)**
   - *Tindakan:* Perluas kriteria kepemilikan *Stock Option Level 1* yang sebelumnya terpusat pada tingkat manajerial ke karyawan berkinerja baik (*Performance Rating 3 & 4*) yang telah melewati masa kerja 1 tahun dengan skema *vesting period* 3-4 tahun.
   - *Target:* Meminimalkan proporsi karyawan di Level 0 dan memanfaatkan efek retensi jangka panjang (*golden handcuffs*) untuk menjaga turnover total <10%.

4. **Program Pendampingan 1 Tahun Pertama & Stay Interview (*First-Year Retention & Mentorship*)**
   - *Tindakan:* Terapkan program orientasi dan bimbingan (*buddy & mentorship system*) intensif selama 12 bulan pertama untuk memitigasi fenomena *tenure shock*. Wajibkan para manajer langsung menyelenggarakan sesi *one-on-one stay interview* secara kuartalan guna mendengarkan aspirasi dan kendala karyawan secara proaktif.
   - *Target:* Meningkatkan retensi karyawan pada rentang masa kerja tahun ke-1 hingga ke-3 sebesar minimal 30%.

5. **Operasionalisasi Sistem Peringatan Dini Retensi Berbasis AI (*Predictive Retention Early-Warning*)**
   - *Tindakan:* Integrasikan script `prediction.py` ke dalam siklus evaluasi kuartalan HR. Karyawan yang teridentifikasi dalam kategori *High Risk* (>60%) atau *Medium Risk* (35-60%) secara otomatis dialokasikan untuk intervensi personal (konseling jalur karir, peninjauan beban kerja, atau penyesuaian fleksibilitas kerja) sebelum fase pengunduran diri formal terjadi.
   - *Target:* Mengidentifikasi dan mengintervensi minimal 80% karyawan berisiko tinggi sebelum mereka mengajukan surat pengunduran diri.
