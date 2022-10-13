
import sqlite3

conn = sqlite3.connect('audio.db')

c = conn.cursor()

def create_table():
    with conn:
        c.execute("""CREATE TABLE audios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text,
            text text,
            extension text,
            type text, 
            path text
            )""")

def insert_audio(audio):
    with conn:
        c.execute("INSERT INTO audios (name, text, extension, type, path) VALUES (:name, :text, :extension, :type, :path)", 
        {'name':audio.name, 'text':audio.text, 'extension':audio.extension, 'type':audio.type, 'path':audio.path})
        return c.lastrowid

def get_all_audio():
    c.execute("SELECT * FROM audios")
    return c.fetchall()

def get_audio_by_name(name):
    c.execute("SELECT * FROM audios WHERE name=:name", {'name': name})
    return c.fetchall()

def get_audio_by_id(id):
    c.execute("SELECT * FROM audios WHERE id=:id", {'id': id})
    return c.fetchall()