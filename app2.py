import os
import streamlit as st
from groq import Groq
# KITA TIDAK MEMERLUKAN 'from dotenv import load_dotenv' LAGI DI SINI

# Mengambil API Key langsung dari sistem keamanan Hugging Face
client = Groq(api_key=os.environ.get("GROQ_API_KEY")) 

def analisis_email_dengan_ai(teks_email):
    # Logika AI Agent yang sudah Anda buat berhasil tadi
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
            {"role": "user", "content": teks_email}
        ]
    )
    return respons.choices[0].message.content

# 2. MEMBUAT TAMPILAN WEB (STREAMLIT)
st.title("🤖 AI Agent: Penyaring Email Otomatis")
st.write("Masukkan teks email di bawah untuk dianalisis oleh AI Agent Anda secara real-time.")

# Kotak input teks untuk pengguna di web
email_user = st.text_area("Tempel Teks Email Di Sini:", height=150)

# Tombol aksi
if st.button("Jalankan Agen AI"):
    if email_user.strip() == "":
        st.warning("Silakan masukkan teks email terlebih dahulu!")
    else:
        with st.spinner("Agen AI sedang membaca dan berpikir..."):
            # Panggil fungsi AI
            hasil_analisis = analisis_email_dengan_ai(email_user)
            
            # Tampilkan hasil di kotak hijau yang indah di halaman web
            st.subheader("📊 Hasil Analisis Agen:")
            st.success(hasil_analisis)
