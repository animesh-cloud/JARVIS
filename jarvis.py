from spotify_control import play_music, pause_music, skip_track, currently_playing
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
from spotify_control import resume_music
import wikipedia 
import pyjokes
import datetime
import json


# Init engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file)

memory = load_memory()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"🗣️ You said: {query}")
    except Exception as e:
        print("❌ Couldn't understand. Try again.")
        return ""
    return query.lower()
def confirm_action():
    speak("Are you sure?")
    response = take_command()
    return 'yes' in response or 'do it' in response or 'go ahead' in response


def respond_to_command(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif 'open instagram' in command:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")
         
    elif 'open chrome' in command:
        speak("Opening Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'open spotify' in command:
        speak("Opening Spotify")
        os.startfile(r"C:\Users\Lenovo\AppData\Roaming\Spotify\Spotify.exe")

    elif 'open code' in command or 'open vs code' in command:
        speak("Opening Visual Studio Code")
        os.startfile("C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'open valorant' in command:
        speak("Launching Valorant. Time to carry the team, Animesh.")
        os.startfile("D:\\Games\\Riot Games\\Riot Client\\RiotClientServices.exe")
    
    elif 'play music' in command:
        speak("Playing music on Spotify.")
        play_music()

    elif 'pause music' in command:
         speak("Pausing Spotify.")
         pause_music()

    elif 'skip' in command or 'next song' in command:
        speak("Skipping to next track.")
        skip_track()

    elif 'what is playing' in command or 'currently playing' in command:
        currently_playing()

    elif 'stop' in command or 'exit' in command:
        speak("Shutting down. Bye Animesh.")
        exit()
    elif 'resume music' in command or 'continue playing' in command:
        speak("Resuming music on Spotify.")
        resume_music() 
    elif 'joke' in command or 'make me laugh' in command:
        joke = pyjokes.get_joke()
        print("JARVIS:", joke)
        speak(joke)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif 'date' in command:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")
    elif 'shut down' in command or 'shutdown' in command:
        speak("You want me to shut down the system.")
        if confirm_action():
               speak("Shutting down. Goodbye, Animesh.")
               os.system("shutdown /s /t 1")
        else:
               speak("Shutdown cancelled.")
    elif 'restart' in command or 'reboot' in command:
        speak("You want me to restart the system.")
        if confirm_action():
               speak("Restarting now.")
               os.system("shutdown /r /t 1")
        else:
               speak("Restart cancelled.")
    elif 'lock' in command or 'lock pc' in command:
        speak("You want me to lock the PC.")
        if confirm_action():
               speak("Locking the computer.")
               os.system("rundll32.exe user32.dll,LockWorkStation")
        else:
               speak("Lock cancelled.")
    elif 'remember' in command:
        try:
            key_value = command.replace("remember", "").strip()
            if "is" in key_value:
                key, value = key_value.split("is")
                key = key.strip()
                value = value.strip()
                memory[key] = value
                save_memory(memory)
                speak(f"Got it. I'll remember that {key} is {value}.")
            else:
                speak("Please tell me what to remember using 'X is Y' format.")
        except:
            speak("Sorry, I couldn't remember that.")

    elif 'what is' in command or 'do you remember' in command:
        found = False
        for key in memory:
            if key in command:
                speak(f"You told me that {key} is {memory[key]}.")
                found = True
                break
        if not found:
            speak("I don't remember that yet.")


    else:
        try:
            speak("Searching Wikipedia...")
            result = wikipedia.summary(command, sentences=2)
            print("JARVIS:", result)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
             speak(f"That was a bit vague. Maybe you meant {e.options[0]}")
        except wikipedia.exceptions.PageError:
             speak("I couldn't find anything relevant.")
        except Exception as e:
             speak("Something went wrong.")
             print("Error:", e)

   

# MAIN LOOP
speak("Jarvis is online and ready.")
while True:
    command = take_command()
    if command:
        respond_to_command(command)
