# ase_datasetjavarepository
Dataset metric software for ASE Task
# Dataset Sibamacode (Software Metric Analysis: Base Code)

## Deskripsi

Dataset Sibamacode (**Si**mple **Ba**se **Ma**trix **Code**) berisi metrik perangkat lunak statis yang diekstraksi dari kode sumber berbasis berkas (file-level). Dataset ini bertujuan untuk mendukung penelitian empiris dalam bidang teknik perangkat lunak, khususnya untuk memprediksi kualitas kode, kompleksitas, dan kemungkinan adanya *defect*.

## Struktur Data
* **Nama File Dataset:** `dataset_sibamacode.csv`
* **Jumlah Sampel/Baris:** 33 berkas kode.
* **Jumlah Metrik/Kolom:** 36 metrik.
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

## Atribusi dan Lisensi

Dataset ini didedikasikan untuk penggunaan dalam riset dan edukasi. Jika Anda menggunakan data ini dalam publikasi, harap mengutip sumbernya.
