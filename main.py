import os
import openai
from dotenv import load_dotenv
import time
import speech_recognition as sr
import pyttsx3
import numpy as np

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model = 'gpt-3.5-turbo'

r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
name = "wisnu"

greetings = [f"Halo, ada yang bisa saya bantu, {name}?",
             "Ya, ada yang bisa saya bantu?",
             "Halo! Bagaimana kabar hari ini?",
             f"Selamat datang, Kapten {name}! Bagaimana kondisi kapal hari ini?",
             f"Hai, {name}! Ada yang bisa saya bantu?"]

def listen_for_wake_word(source):
    print("Mendengarkan 'Hey POS'...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if "hey pos" in text.lower():
                print("Wake word terdeteksi.")
                engine.say(np.random.choice(greetings))
                engine.runAndWait()
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass

def listen_and_respond(source):
    print("Mendengarkan...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"Anda mengatakan: {text}")
            if not text:
                continue

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"{text}"}],
                language="id-ID"  # Tambahkan parameter language dengan kode Bahasa Indonesia
            )
            response_text = response.choices[0].message.content
            print(f"Respon OpenAI: {response_text}")

            engine.say(response_text)
            engine.runAndWait()

            if not audio:
                listen_for_wake_word(source)
        except sr.UnknownValueError:
            time.sleep(2)
            print("Diam ditemukan, berhenti bicara, mendengarkan...")
            listen_for_wake_word(source)
            break
            
        except sr.RequestError as e:
            print(f"Tidak dapat meminta hasil; {e}")
            engine.say(f"Tidak dapat meminta hasil; {e}")
            engine.runAndWait()
            listen_for_wake_word(source)
            break

with sr.Microphone() as source:
    listen_for_wake_word(source)
