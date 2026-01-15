# 1. Gunakan image dasar Python 3.10 yang ringan (slim)
FROM python:3.10-slim

# 2. Set folder kerja di dalam container
WORKDIR /app

# 3. Copy file requirements ke dalam container
COPY requirements.txt .

# 4. Install semua library yang dibutuhkan
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy seluruh isi folder proyek Anda ke dalam folder /app di container
COPY . .

# 6. Ekspos port 8000 (sesuai port FastAPI)
EXPOSE 8000

# 7. Perintah untuk menjalankan aplikasi saat container menyala
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]