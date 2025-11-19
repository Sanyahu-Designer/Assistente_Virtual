# Sistema de Assistência Virtual - SARA

Sistema de assistência virtual desenvolvido para o curso de Machine Learning da DIO, utilizando Processamento de Linguagem Natural (PLN).

## Funcionalidades

- **Text-to-Speech (TTS)**: Conversão de texto em áudio
- **Speech-to-Text (STT)**: Reconhecimento de voz para texto
- **Comandos de Voz**:
  - Pesquisa no Wikipedia
  - Abertura do YouTube
  - Acesso ao site pessoal (https://sanyahudesigner.com.br)
  - Localização de farmácias próximas
  - Consulta de horário e data

## Tecnologias Utilizadas

- Python 3.x
- SpeechRecognition
- gTTS (Google Text-to-Speech)
- PyAudio
- Wikipedia API
- PyWhatKit
- Geocoder

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/Sanyahu-Designer/Assistente_Virtual.git  

2. Instale as dependências:
pip install -r requirements.txt

3. Execute o sistema:
python assistente_virtual.py

4. Comandos Disponíveis:
"Pesquisar [termo] no Wikipedia"
"Abrir YouTube"
"Pesquisar [termo] no YouTube"
"Abrir meu site"
"Localizar farmácia"
"Que horas são?"
"Qual a data de hoje?"
"Sair" para encerrar"

Desenvolvido por:
Sandro Augusto Vascão - Formação Machine Learning Specialist - DIO
