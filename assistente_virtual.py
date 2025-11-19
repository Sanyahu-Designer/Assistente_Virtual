# Instalação das bibliotecas necessárias
!pip install gtts pygame speechrecognition pyaudio wikipedia pywhatkit geocoder phonenumbers

import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import webbrowser
import wikipedia
import pywhatkit
import geocoder
import time
import requests
from datetime import datetime
import json

class AssistenteVirtual:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.nome_assistente = "SARA"
        
        # Ajustar para ruído ambiente
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
        
        print(f"{self.nome_assistente} inicializada! Diga 'SARA' para ativar.")
    
    def text_to_speech(self, texto):
        """Converte texto em áudio (TTS)"""
        try:
            # Criar arquivo de áudio temporário
            tts = gTTS(text=texto, lang='pt-br')
            filename = "temp_audio.mp3"
            tts.save(filename)
            
            # Reproduzir áudio
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            
            # Esperar áudio terminar
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            # Limpar arquivo temporário
            pygame.mixer.quit()
            if os.path.exists(filename):
                os.remove(filename)
                
        except Exception as e:
            print(f"Erro no TTS: {e}")
    
    def speech_to_text(self):
        """Converte fala em texto (STT)"""
        try:
            with self.microphone as source:
                print("Ouvindo...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            texto = self.recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto.lower()
            
        except sr.WaitTimeoutError:
            print("Tempo de espera esgotado")
            return ""
        except sr.UnknownValueError:
            print("Não entendi o que você disse")
            return ""
        except Exception as e:
            print(f"Erro no STT: {e}")
            return ""
    
    def pesquisar_wikipedia(self, query):
        """Pesquisa no Wikipedia"""
        try:
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(query, sentences=2)
            return f"Segundo a Wikipedia: {resultado}"
        except Exception as e:
            return f"Desculpe, não encontrei informações sobre {query} no Wikipedia"
    
    def abrir_youtube(self, pesquisa=None):
        """Abre o YouTube ou pesquisa no YouTube"""
        try:
            if pesquisa:
                pywhatkit.playonyt(pesquisa)
                return f"Abri o YouTube e pesquisei por {pesquisa}"
            else:
                webbrowser.open("https://www.youtube.com")
                return "Abri o YouTube para você"
        except Exception as e:
            return "Erro ao abrir o YouTube"
    
    def abrir_site_pessoal(self):
        """Abre o site pessoal"""
        try:
            webbrowser.open("https://sanyahudesigner.com.br")
            return "Abri o seu site pessoal"
        except Exception as e:
            return "Erro ao abrir o site"
    
    def localizar_farmacia(self):
        """Localiza farmácias próximas"""
        try:
            # Obter localização aproximada pelo IP
            g = geocoder.ip('me')
            if g.ok:
                lat, lng = g.latlng
                # Simular busca por farmácias próximas
                mapa_url = f"https://www.google.com/maps/search/farmácia/@{lat},{lng},15z"
                webbrowser.open(mapa_url)
                return "Abri o mapa com as farmácias mais próximas da sua localização"
            else:
                webbrowser.open("https://www.google.com/maps/search/farmácia")
                return "Abri o mapa para você pesquisar farmácias manualmente"
                
        except Exception as e:
            return "Erro ao localizar farmácias"
    
    def obter_horario(self):
        """Retorna o horário atual"""
        agora = datetime.now()
        horario = agora.strftime("%H:%M")
        return f"Agora são {horario}"
    
    def obter_data(self):
        """Retorna a data atual"""
        agora = datetime.now()
        data = agora.strftime("%d/%m/%Y")
        return f"Hoje é {data}"
    
    def processar_comando(self, comando):
        """Processa os comandos de voz"""
        resposta = ""
        
        if "wikipedia" in comando or "pesquisar" in comando:
            termo = comando.replace("pesquisar", "").replace("wikipedia", "").replace("sobre", "").strip()
            if termo:
                resposta = self.pesquisar_wikipedia(termo)
            else:
                resposta = "O que você gostaria de pesquisar na Wikipedia?"
        
        elif "youtube" in comando:
            if "pesquisar" in comando:
                termo = comando.replace("pesquisar", "").replace("youtube", "").replace("no", "").strip()
                resposta = self.abrir_youtube(termo)
            else:
                resposta = self.abrir_youtube()
        
        elif "site" in comando or "sanyahu" in comando:
            resposta = self.abrir_site_pessoal()
        
        elif "farmácia" in comando or "farmacia" in comando:
            resposta = self.localizar_farmacia()
        
        elif "horas" in comando or "horário" in comando:
            resposta = self.obter_horario()
        
        elif "data" in comando:
            resposta = self.obter_data()
        
        elif "sair" in comando or "parar" in comando:
            resposta = "Até logo! Foi um prazer ajudar."
        
        else:
            resposta = "Desculpe, não entendi o comando. Posso ajudar com: Wikipedia, YouTube, seu site, farmácias, horário ou data."
        
        return resposta
    
    def executar(self):
        """Loop principal da assistente"""
        self.text_to_speech(f"Olá! Eu sou a {self.nome_assistente}. Como posso ajudar?")
        
        while True:
            print("\nAguardando comando...")
            comando = self.speech_to_text()
            
            if comando:
                if self.nome_assistente.lower() in comando:
                    self.text_to_speech("Sim, estou aqui! Como posso ajudar?")
                    continue
                
                if "sair" in comando or "parar" in comando:
                    resposta = self.processar_comando(comando)
                    self.text_to_speech(resposta)
                    break
                
                resposta = self.processar_comando(comando)
                print(f"{self.nome_assistente}: {resposta}")
                self.text_to_speech(resposta)

# Função principal
def main():
    print("=== SISTEMA DE ASSISTÊNCIA VIRTUAL SARA ===")
    print("Desenvolvido para o curso de Machine Learning - DIO")
    print("Comandos disponíveis:")
    print("- 'Pesquisar [termo] no Wikipedia'")
    print("- 'Abrir YouTube' ou 'Pesquisar [termo] no YouTube'")
    print("- 'Abrir meu site'")
    print("- 'Localizar farmácia'")
    print("- 'Que horas são?'")
    print("- 'Qual a data de hoje?'")
    print("- 'Sair' para encerrar")
    print("\n")
    
    assistente = AssistenteVirtual()
    
    try:
        assistente.executar()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário")
    except Exception as e:
        print(f"Erro: {e}")

# Executar o programa
if __name__ == "__main__":
    main()
