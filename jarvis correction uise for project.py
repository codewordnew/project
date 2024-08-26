import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyautogui
import pyjokes
from pydictionary import dictionary, Dictionary
from instaloader  import instaloader



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        speak("say that again please...")
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening!")

    speak("I am jarvis sir, how may I help you")


def sendEmail(to, content):
    server=smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('thakurmanav383email@gmail.com','password')
    server.sendemail('youremail@gmail.com'.to, content)
    server.close()

def dowload(username):
    #Creat an instance of the instaloader class to insteract with instagram profiles.
    mod = instaloader.Instaloader()

    #Download the profile of the specified 'username' and save it in the current working directory.
    # Set 'profile_pic_only' to True to download only the profile picture.
    mod.download_profile(username,profile_pic_only=True)




#dowload("MY PHOTO.jpg")





if __name__=="__main__":

    wishMe()

    #while True:
    if 1:
        

        query = takecommand().lower()

        if ' according to wikipedia' in query:
            speak('searching wikipedia....')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.yotube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\thaku\\Music\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is{strTime}")

        elif 'open vs code' in query:
            codepath="C:\\Users\\thaku\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

            #speak("hello sir")

        elif 'youtube Search' in query:
            query=query.replace("jarvis","")
            query=query.replace("youtube search","")
            web='https://www.youtube.com/results?search_query='+querywebbrowser.open(web)
            speak("Done Sir")

        elif 'google search' in query:
            query=query.replace("jarvis","")
            query=query.replace("google search","")
            pywhatkit.search(query)
            speak("done sir")

        elif "play" in query or "song" in query or "music" in query:
            query=query.replace("play","")
            query=query.replace("song","")
            query=query.replace("music","")
            pywhatkit.playonyt(query)
            speak(f"Ok sir , Playing{query} on youtube")

        elif "screenshot" in query:
            speak("OK sir")
            pywhatkit.take_screenshot("screenshot")
            speak("here,take a look")

        elif "show history" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('h')
            pyautogui.keyUp('ctrl')

        elif "joke" in query:
            speak("of Course Here we go!")
            speak(pyjokes.get_joke())

            

        elif "meaning" in query and "of" in query:
            prob=query.replace("what is the","")
            prob=prob.replace("meaning of","")
            prob=prob.replace("jarvis","")
            dict=Dictionary(prob.strip())
            meanings_list=dict.meanings()
            print(meanings_list)

        elif "synonym" in query and "of" in query:
            prob=query.replace("what is the","")
            prob=prob.replace("synonym of","")
            prob=prob.replace("jarvis","")
            dict=Dictionary(prob.strip())
            synonym_list=dict.synonyms()
            print(synonym_list)
