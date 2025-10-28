# Dataset Sibamacode (Software Metric Analysis: Base Code)

## Deskripsi
TUGAS ASE 2 : SOFTWARE DEFECT PREDICTION.

Dataset Sibamacode (**Si**mple **Ba**se **Ma**trix **Code**) berisi metrik perangkat lunak statis yang diekstraksi dari kode sumber berbasis berkas (file-level). Dataset ini bertujuan untuk mendukung penelitian empiris dalam bidang teknik perangkat lunak, khususnya untuk memprediksi kualitas kode, kompleksitas, dan kemungkinan adanya *defect*.

## Struktur Data
* **Nama File Dataset:** `dataset_sibamacode.csv`
* **Jumlah Sampel/Baris:** 33 berkas kode.
* **Jumlah Metrik/Kolom:** 36 metrik (termasuk kolom 'defects' yang ditambahkan).
* **Delimiter:** Titik koma (`;`).

---

## Daftar Metrik dan Singkatan (ID)

Dataset ini mengadopsi kombinasi metrik perangkat lunak umum (Halstead, LOC, dan OO) serta menambahkan satu metrik prediksi (*defects*).

### Metrik Prediksi (Target)

| Singkatan (ID) | Nama Metrik | Deskripsi |
|:---:|:---|:---|
| **`defects`** | Defects | Variabel biner: **`True`** jika metrik kunci tertentu (`scc`) mengindikasikan kompleksitas yang dapat diuji; **`False`** sebaliknya. |

### Metrik Kontrol & Kompleksitas

| Singkatan (ID) | Nama Metrik | Keterangan |
|:---:|:---|:---|
| **`scc`** | Sum Cyclomatic Complexity | Jumlah total kompleksitas siklomatik dalam berkas. |
| **`mcc`** | Max Cyclomatic Complexity | Kompleksitas siklomatik maksimum pada unit eksekusi manapun. |
| **`mn`** | Max Nesting | Tingkat kedalaman *nesting* (bersarang) maksimum dari blok kode. |
| **`acc`** | Average Cyclomatic Complexity | Rata-rata kompleksitas siklomatik per unit eksekusi. |
| **`eu`** | Executable Units | Jumlah unit eksekusi (seperti fungsi atau metode). |
| **`f`** | Functions | Jumlah total fungsi. |

### Metrik Lines of Code (LOC)

| Singkatan (ID) | Nama Metrik | Keterangan |
|:---:|:---|:---|
| **`cl`** | Code Lines | Jumlah total baris kode. |
| **`l`** | Lines | Jumlah total baris (kode + komentar + kosong). |
| **`bl`** | Blank Lines | Jumlah total baris kosong. |
| **`cml`** | Comment Lines | Jumlah total baris komentar. |
| **`ccr`** | Comment to Code Ratio | Rasio Baris Komentar terhadap Baris Kode. |
| **`ecl`** | Executable Code Lines | Jumlah Baris Kode yang Dapat Dieksekusi. |
| **`dcl`** | Declarative Code Lines | Jumlah Baris Kode Deklaratif. |
| **`s`** | Statements | Jumlah total *statement*. |
| **`es`** | Executable Statements | Jumlah *statement* yang Dapat Dieksekusi. |
| **`ds`** | Declarative Statements | Jumlah *statement* Deklaratif. |
| **`sc`** | Semicolons | Jumlah total titik koma (proksi untuk *statement*). |
| **`acl`** | Average Code Lines | Rata-rata baris kode per unit eksekusi. |
| **`al`** | Average Lines | Rata-rata total baris per unit eksekusi. |
| **`abl`** | Average Blank Lines | Rata-rata baris kosong per unit eksekusi. |
| **`acm`** | Average Comment Lines | Rata-rata baris komentar per unit eksekusi. |

### Metrik Halstead

| Singkatan (ID) | Nama Metrik | Keterangan |
|:---:|:---|:---|
| **`n`** | Halstead Length (N) | Panjang program (total operator + total *operand*). |
| **`n1`** | Halstead Total Operators (N1) | Jumlah total operator. |
| **`n2`** | Halstead Total Operands (N2) | Jumlah total *operand*. |

### Metrik Desain Object-Oriented (OO)

| Singkatan (ID) | Nama Metrik | Keterangan |
|:---:|:---|:---|
| **`cs`** | Classes | Jumlah total kelas dalam berkas. |
| **`m`** | Methods | Jumlah total metode (*class* dan *instance*). |
| **`cm`** | Class Methods | Jumlah total metode kelas (statis). |
| **`im`** | Instance Methods | Jumlah total metode *instance*. |
| **`pvm`** | Private Methods | Jumlah total metode privat. |
| **`prm`** | Protected Methods | Jumlah total metode *protected*. |
| **`pum`** | Public Methods | Jumlah total metode publik. |
| **`dm`** | Default Methods | Jumlah total metode *default* (tergantung bahasa). |
| **`cv`** | Class Variables | Jumlah total variabel kelas (statis). |
| **`iv`** | Instance Variables | Jumlah total variabel *instance*. |

---

## Statistik Dataset Kunci

Bagian ini menyajikan statistik deskriptif untuk metrik utama, memberikan wawasan cepat tentang rentang dan distribusi data.

### Statistik Deskriptif Metrik Utama

| Statistik | Code Lines | Sum Cyclomatic Complexity | Max Cyclomatic Complexity | Max Nesting |
|:---|---:|---:|---:|---:|
| **count** | 33 | 33 | 33 | 33 |
| **mean** | 190.64 | 22.64 | 6.24 | 1.82 |
| **std** | 161.75 | 18.64 | 4.21 | 1.31 |
| **min** | 16 | 0 | 0 | 0 |
| **25% (Q1)** | 67 | 9 | 2 | 1 |
| **50% (Median)** | 131 | 20 | 7 | 2 |
| **75% (Q3)** | 306 | 38 | 10 | 3 |
| **max** | 604 | 68 | 11 | 4 |

### Distribusi Nilai Kolom 'Defects (True/False)'

| Nilai | Jumlah File | Persentase |
|:---|---:|---:|
| **True** | 16 | 49.4% |
| **False** | 17 | 50.6% |

---

## Penggunaan
Dataset ini dapat digunakan untuk berbagai tugas klasifikasi dalam Machine Learning, seperti:
1. **Prediksi *Defect*:** Mengklasifikasikan berkas kode ke dalam kategori *defects* (True/False) berdasarkan metrik perangkat lunak.
2. **Analisis Kompleksitas:** Mengidentifikasi metrik mana yang paling berkorelasi dengan tingginya Cyclomatic Complexity atau tingkat *nesting* (*mn*).
3. **Evaluasi Desain:** Menganalisis bagaimana metrik OO berkorelasi dengan metrik LOC dan Complexity.

## Kesimpulan

Eksperimen menggunakan dataset Sibamacode menunjukkan bahwa algoritma *machine learning*, khususnya Random Forest dengan teknik SMOTE untuk menangani ketidakseimbangan data, sangat efektif dalam memprediksi cacat perangkat lunak berdasarkan metrik kode statis. Random Forest unggul dalam metrik *Recall* dan *F1-Score*, menjadikannya pilihan terbaik untuk mendeteksi modul kode yang berpotensi cacat, sehingga mengurangi risiko *bug* kritis lolos ke tahap produksi.

Analisis *feature importance* dari Random Forest mengungkapkan bahwa metrik seperti *Sum Cyclomatic Complexity* (`scc`), *Max Cyclomatic Complexity* (`mcc`), *Executable Code Lines* (`ecl`), dan *Code Lines* (`cl`) memiliki pengaruh signifikan terhadap prediksi cacat. Hal ini menunjukkan bahwa kompleksitas dan ukuran modul kode merupakan faktor utama penyebab cacat.

Berikut adalah visualisasi *feature importance* dari model Random Forest:

<img width="386" height="306" alt="image" src="https://github.com/user-attachments/assets/3e1f2a7e-200c-4ce5-9482-9ee9fc2df1aa" />

Selain itu, *Confusion Matrix* dari model Random Forest menunjukkan kemampuan model dalam mendeteksi kelas *Defect* (True) dengan lebih baik dibandingkan Regresi Logistik, terutama dalam meminimalkan *False Negatives*:

<img width="358" height="269" alt="image" src="https://github.com/user-attachments/assets/deb4323e-2d01-477c-83fe-19bf6d029aab" />

<img width="343" height="264" alt="image" src="https://github.com/user-attachments/assets/0fc34a0f-0d36-4985-994b-436cee0249b5" />

Secara praktis, temuan ini memiliki dua implikasi utama:
1. **Prioritas Pengujian**: Model ini dapat digunakan dalam alur kerja *Quality Assurance* (QA) untuk memprioritaskan pengujian pada modul kode yang diprediksi berisiko tinggi (*Defect*=True).
2. **Panduan Kualitas Kode**: Hasil analisis *feature importance* mendorong praktik *refactoring* untuk menyederhanakan modul kode yang terlalu kompleks dan menetapkan batas atas untuk metrik seperti `scc` selama *code review*.

## Atribusi dan Lisensi

Dataset ini didedikasikan untuk penggunaan dalam riset dan edukasi. Jika Anda menggunakan data ini dalam publikasi, harap mengutip sumbernya.
