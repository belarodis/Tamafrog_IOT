import paho.mqtt.client as mqtt
import speech_recognition as sr

# configuração do broker
broker = "localhost"  # ou IP do Mosquitto
client = mqtt.Client()
client.connect(broker, 1883, 60)

# inicializa reconhecimento de voz
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Fale um comando para o Tamafrog:")
    audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language="pt-BR").lower()
        print(f"Você disse: {comando}")
    except sr.UnknownValueError:
        print("Não entendi o comando")
        comando = ""

# mapear comando para tópicos
if "alimentar" in comando:
    client.publish("kaeru/fome", "comeu")
elif "brincar" in comando:
    client.publish("kaeru/felicidade", "brincou")
elif "sonecar" in comando:
    client.publish("kaeru/cansado", "dormiu")
elif "limpar" in comando:
    client.publish("kaeru/limpeza", "banhou")
elif "exercitar" in comando:
    client.publish("kaeru/atividade", "malhou")
else:
    print("Comando não reconhecido")
