# Machine Learning & Scraper Worker

Modul data pipeline independen untuk Sistem Monitoring Ancaman. Bertugas melakukan scraping data berita/media sosial (X/Portal Berita), ekstraksi entitas bernama spasial (Named Entity Recognition via Spacy), serta geocoding koordinat lokasi.

## Struktur Direktori

```text
machine-learning/
├── scraper/             # Modul crawling & scraper data
├── nlp/                 # Modul Spacy NER & geocoding koordinat
├── .env.example         # Contoh format environment variables
├── .gitignore           # Konfigurasi file yang diabaikan git
├── main.py              # Entry point runner & cron pipeline
├── requirements.txt     # Daftar dependensi library Python
└── README.md            # Dokumentasi modul
```

## Prasyarat
- Python >= 3.10 (Direkomendasikan Python 3.11+)

## Panduan Instalasi & Setup Lingkungan

1. Masuk ke direktori machine-learning:
   ```bash
   cd MachineLearning
   ```

2. Buat Virtual Environment:
   ```bash
   python -m venv venv
   ```

3. Aktifkan Virtual Environment:
   - **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (Command Prompt):**
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   - **Linux / macOS:**
     ```bash
     source venv/bin/activate
     ```

4. Instal Dependensi:
   ```bash
   pip install -r requirements.txt
   ```

5. Unduh Model Spacy (opsional/sesuai kebutuhan):
   ```bash
   python -m spacy download xx_ent_wiki_sm
   ```

6. Konfigurasi Environment Variables:
   Salin file `.env.example` menjadi `.env` lalu sesuaikan isinya:
   ```bash
   cp .env.example .env
   ```

7. Menjalankan Smoke Test:
   ```bash
   python main.py
   ```
