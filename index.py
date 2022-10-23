import streamlit as st
import pandas as pd
from app.extraction.getFiles import get_all_files
from app.database.database import clean_table, insert_audio, get_all_audio
from app.process.getText import get_text

def format_all_audios(audios):
    allAudios = pd.DataFrame((audios))
    allAudios.columns = ["ID", "Nome", "Texto", "Exensão", "Tipo", "Caminho", "Hash MD5", "Hash SHA256", "Duração", "Data de Criação", "Data da Última Modificação", "Tamanho (Bytes)"]
    allAudios = allAudios.drop("ID", axis=1)
    return allAudios

st.title('Escritor de áudio')

st.text_input("Pasta", key="name", placeholder='Em qual pasta estão os áudios que deseja analisar? (Pasta padrão: audios)')

path = "./"+st.session_state.name+"/" 

if st.session_state.name:
    clean_table()
    st.write('Aqui estão as informações que obtive:')
    files = get_all_files(path)

    for file in files:
        get_text(file)
        insert_audio(file)

    allAudios = format_all_audios((get_all_audio()))

    st.write(allAudios)

