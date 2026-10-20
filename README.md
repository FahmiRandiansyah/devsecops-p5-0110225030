# SecureCalc CLI & Validation Engine

![DevSecOps Pipeline](https://github.com/USERNAME/REPO_NAME/actions/workflows/devsecops.yml/badge.svg)

## 1. Deskripsi Aplikasi & Fungsi
**SecureCalc CLI** adalah aplikasi konsol berbasis Python yang menyediakan fungsi kalkulasi matematika dasar, validasi format data/input, serta penataan log (*audit logging*). Aplikasi ini dirancang dengan struktur modular untuk mensimulasikan komponen perangkat lunak enterprise yang siap diintegrasikan ke dalam pipeline DevSecOps.

### Fitur Utama:
- **Core Calculator (`src/calculator.py`)**: Menangani operasi aritmatika dasar (Penjumlahan, Pengurangan, Perkalian, Pembagian) dengan penanganan *edge cases* seperti *division by zero*.
- **Input Validator (`src/validator.py`)**: Memvalidasi integritas data input, memastikan variabel berada dalam tipe dan rentang yang aman.
- **System Logger (`src/logger.py`)**: Menjadwalkan dan merekam jejak eksekusi aplikasi serta *error handling* untuk tujuan audit keamanan.
- **Main Application (`main.py`)**: Entry point utama aplikasi yang mengintegrasikan seluruh komponen src.
- **Unit Testing (`tests/test_calculator.py`)**: Pengujian otomatis fungsi kalkulator dan penanganan eror.

---

## 2. Bahasa & Framework yang Digunakan
- **Bahasa Pemrograman:** Python 3.10+
- **Testing Framework:** `pytest` (v7.0.0+)
- **SAST Tools:** Bandit (Python Security Static Analysis)
- **CI/CD Automation:** GitHub Actions (`ubuntu-latest` runner)

---

## 3. Cara Menjalankan Aplikasi

### Prasyarat
- Python 3.10 atau versi yang lebih baru dipasang di sistem lokal.
- Git.

### Langkah-Langkah Instalasi & Eksekusi:

1. **Clone Repository:**
   ```bash
   git clone https://github.com/[USERNAME]/devsecops-p5-[NIM].git
   cd devsecops-p5-[NIM]
   ```

2. **Buat & Aktifkan Virtual Environment (Disarankan):**
   ```bash
   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi Utama:**
   ```bash
   python main.py
   ```

5. **Jalankan Unit Test:**
   ```bash
   pytest
   ```

---

## 4. Overview Pipeline CI/CD (DevSecOps)

Pipeline DevSecOps diimplementasikan menggunakan **GitHub Actions** pada `.github/workflows/devsecops.yml`. Pipeline ini secara otomatis terpicu pada setiap aktivitas `push` ke branch `main` serta pendorongan `pull_request` ke branch `main`.

```
+------------------+      +-----------------------+      +------------------------+
|   Developer      |      |      Job 1: Build     |      |    Job 2: SAST Scan    |
|  (Push / PR to)  | ---> |   - Setup Python      | ---> |   - Install Bandit     |
|   'main' branch  |      |   - Install Dep       |      |   - Run Security Scan  |
+------------------+      |   - Run pytest        |      |   - Quality Gate Check |
                          +-----------------------+      +------------------------+
                                                                     |
                                                                     v
                                                          [ Pipeline Pass / Fail ]
```

### Rincian Job Pipeline:
1. **Job `build`**:
   - Menggunakan runner `ubuntu-latest`.
   - Mengunduh kode sumber via `actions/checkout@v4`.
   - Konfigurasi lingkungan Python via `actions/setup-python@v5`.
   - Menginstall pustaka dependensi dari `requirements.txt`.
   - Menjalankan *Unit Testing* menggunakan `pytest` untuk memastikan tidak ada logika aplikasi yang rusak.

2. **Job `sast-scan`**:
   - Memiliki dependensi `needs: build` (hanya berjalan jika job build & test berhasil).
   - Menjalankan alat SAST **Bandit** untuk menganalisis AST (*Abstract Syntax Tree*) kode Python.
   - Mengidentifikasi potensi kerentanan keamanan seperti *hardcoded secrets*, penggunaan fungsi tak aman (*insecure functions*), atau ekspresi berbahaya.
   - **Quality Gate Enforcement**: Pipeline diatur untuk gagal (*fail*) apabila Bandit menemukan isu keamanan berkatagori *Medium* atau *High Severity*.


Uji Event pull_request