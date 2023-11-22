import streamlit as st
import sqlite3 as db
import database as sv
from streamlit_option_menu import option_menu

#import database as db  # local import

#--------------PAGE CONFIG--------------#
st.set_page_config(
    page_title="My Animes Calendar",
    page_icon="🈴",
    layout="centered"
)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


#--------------FUNCTIONS--------------#
daysWeek = ['Selecione','Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo']

if 'button' and 'button2' not in st.session_state:
    st.session_state.button = False
    st.session_state.button2 = False

def adicionar_anime():
    st.session_state.button = not st.session_state.button
    st.session_state.button2 = False

def editar_anime():
    st.session_state.button2 = not st.session_state.button2
    st.session_state.button = False

def inicio():
    st.session_state.button2 = False
    st.session_state.button = False

def get_name_animes():
    items = sv.fetch_all_animes()
    animes = [item[1] for item in items]
    return animes

def get_anime(name,index):
    items = sv.get_anime(name)
    anime = [item[index] for item in items]
    return anime





#--------------PAGE--------------#

st.title('Meu Calendário de Animes')
col1, col2, col3, col4, col5 = st.columns(5)
col1.button('Home', on_click=inicio)
col4.button('Add Animes', on_click=adicionar_anime)
col5.button('Edit Animes', on_click=editar_anime)

if st.session_state.button:
        # Formulário dos dados
        submitForm = False
        with st.form("addAnime", clear_on_submit=submitForm):
            st.header('Adicionar anime')
            animeName = st.text_input('Nome do anime:', key='name')
            animeDay = st.selectbox('Dia da semana:', daysWeek, key='weekday')
            animeLink = st.text_input('Link do anime:', key='link')
            animeImg = st.text_input("Link foto do anime:", key='linkimg')
            submitButton = st.form_submit_button('Enviar')

            # Verifica se está preenchido
            if submitButton and animeName != "" and animeDay != "Selecione" and animeLink != "" and animeImg != "":
                submitForm = True
                #Prepara os dados para db
                name = str(st.session_state["name"])
                weekday = str(st.session_state["weekday"])
                link = str(st.session_state["link"])
                linkimg = str(st.session_state["linkimg"])
                # Insere os dados no database
                sv.insert_anime(name, weekday, link, linkimg)                       
            elif submitButton:
                st.error('Revise os dados!')

elif st.session_state.button2:
        submitForm = False
        with st.form("editAnime", clear_on_submit=submitForm):
            st.header('Editar anime')
            animeName = st.selectbox('Nome do anime:', get_name_animes())
            col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
            button = col7.form_submit_button('Abrir')
            if button:
                animeGet = sv.get_anime(animeName)
                anime = animeGet[0]
                animeId = anime[0]
                animeDay = st.selectbox('Dia da semana:', daysWeek)
                st.markdown('<h6 style="text-align: center; color: white;">Atual: '+anime[2]+'</h6>', unsafe_allow_html=True)
                animeLink = st.text_input('Link do anime:', value=anime[3])
                animeImg = st.text_input("Link foto do anime:", value=anime[4])
                col1, col2, col3 = st.columns(3)
                col2.markdown('[![Click me]('+anime[4]+')]('+anime[3]+')')
                col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
                col1.write('Id: '+str(animeId)+'')
                saveButton = col7.form_submit_button('Salvar')
                deleteButton = col6.form_submit_button('Deletar')
                # Verifica se está preenchido
                # if submitButton and animeName != "" and animeDay != "Selecione" and animeLink != "" and animeImg != "":
                #     submit_form(True)
                #     #Prepara os dados para db
                #     name = str(st.session_state["name"])
                #     weekday = str(st.session_state["weekday"])
                #     link = str(st.session_state["link"])
                #     linkimg = str(st.session_state["linkimg"])
                #     # Insere os dados no database
                #     sv.insert_anime(name, weekday, link, linkimg)                       
                # elif submitButton:
                #     st.error('Revise os dados!')      
else:
    st.header('Meus Animes')
    animes = sv.fetch_all_animes()
    weekday = st.selectbox('Selecione o dia da semana:', daysWeek)
    
    if weekday == 'Selecione':
        columns = st.columns(3)
        i = 0
        for anime in animes:
                columns[i].markdown('[![Click me]('+anime[4]+')]('+anime[3]+')')
                columns[i].markdown('<h6 style="text-align: center; color: white;">'+anime[1]+'</h6>', unsafe_allow_html=True)
                columns[i].markdown('<h6 style="text-align: center; color: gray;">'+anime[2]+'</h6>', unsafe_allow_html=True)
                if i == 2:
                    i = 0
                else:
                    i += 1


    else:
        animes = sv.get_dayweek(weekday)
        columns = st.columns(3)
        i = 0
        for anime in animes:
                columns[i].markdown('[![Click me]('+anime[4]+')]('+anime[3]+')')
                columns[i].markdown('<h6 style="text-align: center; color: white;">'+anime[1]+'</h6>', unsafe_allow_html=True)
                columns[i].markdown('<h6 style="text-align: center; color: gray;">'+anime[2]+'</h6>', unsafe_allow_html=True)
                if i == 2:
                    i = 0
                else:
                    i += 1
            
            

        # anime = st.selectbox("Selecione o anime:", get_name_animes())
        # submitButton = st.form_submit_button("Ver anime")
        # if submitButton:
        #     # Get data from database
        #     anime_name = get_anime(anime,0)
        #     weekday = get_anime(anime,1)
        #     link = get_anime(anime,2)
        #     linkimg = get_anime(anime,3)
        #     st.image(linkimg, width=300)
        #     st.subheader(weekday)
        #     st.subheader(link)
    




    

