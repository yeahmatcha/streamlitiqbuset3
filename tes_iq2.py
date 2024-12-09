import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_excel("Datatesiq.xlsx")

# Fungsi untuk cek data berdasarkan Skor Mentah
def check_iq(skor_mentah):
    result = df[df['Skor Mentah'] == skor_mentah]
    if not result.empty:
        return result.iloc[0]['Nilai IQ'], result.iloc[0]['Keterangan'], result.iloc[0]['Outcome']
    else:
        return None, None, None  # Jika skor mentah tidak ditemukan

# Fungsi untuk clear input
def clear_fields():
    st.session_state.skor_mentah = "-"
    st.session_state.nilai_iq = None
    st.session_state.keterangan = None
    st.session_state.outcome = None

# Streamlit Antarmuka
st.title("Tes IQ")
st.markdown("Masukkan Skor Mentah Anda untuk mendapatkan nilai IQ, keterangan, dan outcome.")

# Daftar nilai tertentu untuk dropdown, dengan opsi default '-'
nilai_tertentu = ["-"] + [12, 17, 18, 20, 23, 25, 27, 28, 30, 32, 33, 35, 37, 38, 40, 42, 43, 45, 47, 48, 50, 52, 53, 55, 57, 58, 60, 62, 63, 68, 70]

# State Management untuk menyimpan input dan hasil
if "skor_mentah" not in st.session_state:
    st.session_state.skor_mentah = "-"
if "nilai_iq" not in st.session_state:
    st.session_state.nilai_iq = None
if "keterangan" not in st.session_state:
    st.session_state.keterangan = None
if "outcome" not in st.session_state:
    st.session_state.outcome = None

# Dropdown untuk Skor Mentah
skor_mentah = st.selectbox("Pilih Skor Mentah:", nilai_tertentu, index=nilai_tertentu.index(st.session_state.skor_mentah))

# Tombol Cek dan Clear di dua kolom
col1, col3 = st.columns([9, 1])

# Tombol "Cek Nilai IQ"
with col1:
    if st.button("Cek Nilai IQ"):
        if skor_mentah != "-":
            nilai_iq, keterangan, outcome = check_iq(skor_mentah)
            if nilai_iq is not None:
                st.session_state.nilai_iq = nilai_iq
                st.session_state.keterangan = keterangan
                st.session_state.outcome = outcome
            else:
                st.error("Skor Mentah tidak ditemukan dalam dataset.")
        else:
            st.warning("Silakan pilih Skor Mentah terlebih dahulu.")

# Tombol "Clear"
with col3:
    if st.button("Clear"):
        clear_fields()

# Menampilkan hasil jika data tersedia
if st.session_state.nilai_iq is not None:
    with st.expander("Hasil Tes IQ", expanded=True):
        # Tambahkan jarak di atas elemen pertama dalam expander
        st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Nilai IQ")
            st.markdown(
                f"""
                <div style='
                    border: 1px solid #ccc; 
                    padding: 10px; 
                    border-radius: 5px; 
                    background-color: #7a7676; 
                    margin: 10px;'>
                    {st.session_state.nilai_iq:.2f}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.subheader("Keterangan")
            st.markdown(
                f"""
                <div style='
                    border: 1px solid #ccc; 
                    padding: 10px; 
                    border-radius: 5px; 
                    background-color: #7a7676; 
                    margin: 10px;'>
                    {st.session_state.keterangan}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col3:
            st.subheader("Outcome")
            st.markdown(
                f"""
                <div style='
                    border: 1px solid #ccc; 
                    padding: 10px; 
                    border-radius: 5px; 
                    background-color: #7a7676; 
                    margin: 10px;'>
                    {st.session_state.outcome}
                </div>
                """,
                unsafe_allow_html=True,
            )


