# Tamafrog IoT

Um pet virtual interativo que responde a comandos de voz e comunica via MQTT.

## Como usar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o programa:

```bash
python script.py
```

3. Clique no botão "Falar" e diga:
   - "dia" - para mostrar o cenário ensolarado
   - "noite" - para mostrar o cenário estrelado

## Requisitos

- Python 3.x
- Microfone para comandos de voz
- Broker MQTT (configurado para localhost:1883)

## Estrutura do projeto

```
├── script.py              # Aplicação principal
├── requirements.txt       # Dependências Python
├── imagens/              # Imagens do Tamafrog
│   ├── ensolarado.png
│   └── noite_estrelada.png
└── tamafrog_logs.ndjson  # Logs das ações
```
