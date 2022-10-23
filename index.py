import streamlit as st
from app.extraction.getFiles import get_all_files
from app.database.database import clean_table, insert_audio, get_all_audio
from app.presentation.formatFront import format_all_audios, set_background
from app.process.getText import get_text

st.set_page_config(layout="wide")
set_background("app/presentation/images/biblioteca2.jpg")

col1, col2 = st.columns([1,3])
col1.image("app/presentation/images/escriba.jpg", width=300)
col2.markdown(f'<h1 style="color:#7c3c1c;font-size:52px;">Detetive Escriba</h1>', unsafe_allow_html=True)

col2.text_input("Pasta", key="name", label_visibility="hidden", placeholder='Em qual pasta estão os áudios que deseja analisados? (Pasta padrão: audios)')
path = "./"+st.session_state.name+"/" 


if st.session_state.name:
    clean_table()

    files = get_all_files(path)

    for file in files:
        get_text(file)
        insert_audio(file)

    allAudios = format_all_audios(get_all_audio())
    st.markdown(f'<h2 style="color:#7c3c1c;font-size:24px;">Aqui estão as informações que obtive:</h2>', unsafe_allow_html=True)
    st.write(allAudios)

else:
    st.markdown(f'<h2 style="color:#7c3c1c;font-size:24px;">Aqui estarão as informações que eu obtiver:</h2>', unsafe_allow_html=True)
