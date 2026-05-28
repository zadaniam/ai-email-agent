#Kategorisasi Email dengan AI Agent menggunakan Groq API
#Email masih hardcoded untuk contoh

import os
from groq import Groq
from dotenv import load_dotenv

# 1. Memuat berkas .env untuk mengambil API Key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Contoh data input: Teks email masuk yang akan dibaca oleh AI Agent
email_masuk = (
    "Halo! Kami dari Toko Sepatu Maju ingin menawarkan diskon besar-besaran "
    "hingga 70% khusus untuk hari ini saja. Klik link ini untuk membeli!"
)

# 3. Kirim perintah ke AI dengan instruksi peran (System Prompt)
respons = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system", 
            "content": (
                "Anda adalah AI Agent penyaring email profesional. "
                "Tugas Anda adalah membaca email masuk, lalu tentukan kategorinya "
                "(Pilih salah satu: Pekerjaan, Promosi, Pribadi, atau Spam) "
                "dan berikan ringkasan singkat email tersebut dalam 1 kalimat saja."
            )
        },
        {
            "role": "user", 
            "content": f"Tolong analisis email berikut ini: {email_masuk}"
        }
    ]
)

# 4. Tampilkan hasil kerja AI Agent di terminal
print("--- HASIL ANALISIS AGEN ---")
print(respons.choices[0].message.content)
