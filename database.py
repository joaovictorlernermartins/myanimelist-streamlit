import sqlite3 as db
import streamlit as st

database = db.connect('dados.db', check_same_thread=False)
cursor = database.cursor()

#cursor.execute("CREATE TABLE my_animes (id integer primary key autoincrement, name text not null unique, weekday text, link text, linkimg text)")

# name, weekday, link, linkimg
def insert_anime(name, weekday, link, linkimg):
    cursor.execute('INSERT INTO my_animes(name, weekday, link, linkimg) VALUES("'+name+'","'+weekday+'","'+link+'","'+linkimg+'")')
    database.commit() 
    st.success('Anime adicionado!')


def fetch_all_animes():
    res = cursor.execute('SELECT * FROM my_animes')
    animes = res.fetchall()
    return animes


def get_anime(name):
    res = cursor.execute(f"SELECT * FROM my_animes WHERE name='{name}'")
    animes = res.fetchall()
    return animes

def get_dayweek(weekday):
    res = cursor.execute(f"SELECT * FROM my_animes WHERE weekday='{weekday}'")
    anime = res.fetchall()
    return anime
