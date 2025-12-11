import speech_recognition as sr
import webbrowser

rec = sr.Recognizer()

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print('Pode falar agora')
    audio = rec.listen(mic)

    resultados = rec.recognize_google(audio, language='pt-BR', show_all=True)

    texto = resultados['alternative'][0]['transcript']

    print(texto)
    
    if 'youtube' in texto.lower():
        webbrowser.open('https://www.youtube.com/')
    if 'tekken' in texto.lower():
        webbrowser.open('steam://rungameid/389730')
    if 'folha' in texto.lower():
        webbrowser.open('https://www.folha.uol.com.br/')
    
    
