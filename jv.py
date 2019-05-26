import pyttsx3
import datetime
#import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)
#print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wiseme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Mornnig, sir")
        speak("Good Mornnig,sir")
    elif hour>=12 and hour<18:
        print("Good Aftenoon, sir")
        speak("Good Aftenoon,sir")

    else:
        print("Good evenning, sir")
        speak("Good evenning,sir")
    print("Hi i am jarvis. Tell me, How may I help you sir ? ") 
    speak("Hi i am jarvis. Tell me,How may i help you sir") 


def take_cm():
    print("***Let me Know your Quary !?")
    command = input("...")
    return command


if __name__ == "__main__":
    wiseme()
    while True:
        command = take_cm().lower()
        #Here is the logic of exicution
        if "wikipedia" in command:
            command = command.replace("wikipedia","")
            speak("Searching in wikipedia")
            print("Searching in wikipedia...")
            results = wikipedia.summary(command, sentences='4')
            print(results)
            speak(results)

        elif "open youtube" in command:
            print("Openning ...")
            speak("Openning, youtube...")        
            webbrowser.open("www.youtube.com")
            
        elif "play music" in command:
            music = "E:\\Music" #specify the address of music
            songs = os.listdir(music)
            ran = random.randint(0,753)
            print("Playing music...")
            speak("Playing, A music for you...")
            os.startfile(os.path.join(music,songs[ran]))

        elif "open stackoverflow" in command:
            print("Openning, stakoverflow...")
            webbrowser.open("stackoverflow.com")

        elif "the time" in command:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'Sir, the Time is {time_now}')
            speak(f'Sir, the Time is {time_now}')
    
        elif "open code" in command:
            #Address of vs code
            code_path = "C:\\Users\\ad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            print("Opennig...")
            speak("Openning, vscode...")
            os.startfile(code_path)

        elif "open photoshop" in command:
            #address specification
            photo_path = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2018\\Photoshop.exe"
            print("Openning ...")
            speak("Openning, photoshop...")
            os.startfile(photo_path)
        
        elif "open chrome" in command:
            #address specification
            ch_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            print("Opening ...")
            speak("Openning, chrome...")
            os.startfile(ch_path)
        
        elif "open vlc" in command:
            #address
            vlc_path ="C:\\Program Files\\VideoLAN\VLC\\vlc.exe"
            print("Opening ...")
            speak("Openning, vlc...")
            os.startfile(vlc_path)
        
        elif "play video" in command:
            v_path = "E:\\Inspiration"
            videos = os.listdir(v_path)
            v_ran = random.randint(0,25)
            print("Opening...")
            speak("Playing, video...")
            os.startfile(os.path.join(v_path, videos[v_ran]))

        elif "exit" in command:
            print("Have a good time with you, dhanyabaad sir")
            speak("Have a good time with you, dhanyabaad sir")
            break

        elif "open book" in command:
            book_path = "D:\\Acadmic BOOKS"
            books = os.listdir(book_path)
            b_ran = random.randint(0,6)
            print("Openning...")
            speak("Openning, A Book for you...")
            os.startfile(os.path.join(book_path,books[b_ran])) 
        
        elif "open typing master" in command:
            ty_path = "C:\\Program Files (x86)\\TypingMaster\\tmaster.exe"
            print("Openning ...")
            speak("Openning ...")
            os.startfile(ty_path)
            
        else:
            print("Sorry, I don't Understand that Please Pardon :)")
            speak("Sorry, I don't Understand that Please Pardon :)")
