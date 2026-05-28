# Gunakan image Python resmi yang ringan
FROM python:3.10-slim

# Atur direktori kerja di dalam server
WORKDIR /app

# Salin file kebutuhan pustaka ke server
COPY requirements.txt .

# Instal pustaka Python yang dibutuhkan
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi ke server
COPY . .

# Beritahu port yang digunakan oleh Streamlit
EXPOSE 7860

# Jalankan Streamlit dengan konfigurasi port Hugging Face
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
