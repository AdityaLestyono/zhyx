import streamlit as st

st.write("""
# Aplikasi Mempersulit Hidup
ini adalah aplikasi yang sedikit berguna yang @addityal buat 
jangan Lupa Follow Yak""")

angka = st.number_input("Masukan Angka Pertama :" ,0)
angkaa= st.number_input("Maukan Angka Kedua :",0)

hitung = st.button("hitung penjumlahan ")

if hitung :
    hasil = angka + angkaa

    st.success(f"Hasil Penjumlahan nya Adalah : {hasil} ")
    st.balloons()   

ApaanNih= st.button("jangan Di Pencet")
if ApaanNih:
        st.write("di bilang jangan di penct tolol awokwowkokwokwko")
        st.warning()
