import tkinter as tk
from PIL import Image, ImageTk
import paho.mqtt.client as mqtt
import speech_recognition as sr
import threading

def mostrar_imagem(caminho):
    img = Image.open(caminho).resize((400, 400))  
    img_tk = ImageTk.PhotoImage(img)
    label.config(image=img_tk)
    label.image = img_tk  


def on_message(client, userdata, msg):
    evento = msg.payload.decode()
    if msg.topic == "kaeru/fome":
        mostrar_imagem("imagens/ensolarado.png")
    elif msg.topic == "kaeru/felicidade":
        mostrar_imagem("imagens/noite_estrelada.png")


def reconhecer_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Fale um comando para o Tamafrog:")
        audio = r.listen(source, timeout=5, phrase_time_limit=4)
        try:
            comando = r.recognize_google(audio, language="pt-BR").lower()
            print(f"Você disse: {comando}")
        except sr.UnknownValueError:
            print("Não entendi o comando")
            return
        
        if "dia" in comando:
            mostrar_imagem("imagens/ensolarado.png")
            client.publish("kaeru/dia_ensolarado", "tomou banho de sol")
        elif "noite" in comando:
            mostrar_imagem("imagens/noite_estrelada.png")
            client.publish("kaeru/noite_estrelada", "tomou banho de lua")
        else:
            print("Comando não reconhecido")


broker = "localhost" 
client = mqtt.Client()
client.connect(broker, 1883, 60)
client.subscribe("kaeru/#")
client.on_message = on_message
client.loop_start()  


janela = tk.Tk()
janela.title("Tamafrog")
label = tk.Label(janela)
label.pack()


botao = tk.Button(janela, text="Falar", command=lambda: threading.Thread(target=reconhecer_voz).start())
botao.pack(pady=10)


janela.mainloop()
