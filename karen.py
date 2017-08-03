import pyttsx3
from helper import *
import webbrowser
    
if __name__ == '__main__':
    
    GreetMe(name)

    while True:
        
        query = MyCommand().lower()

        if 'google' in query:
            if 'open google' in query:
                speak('Loading up Google for you.')
                webbrowser.open_new_tab('google.com')
            elif 'search google' in query:
                speak("What would you like me to search for you?")
                command = MyCommand()
                url = google(query)
                webbrowser.open_new_tab(url)
            else:
                url = google(query)
                webbrowser.open_new_tab(url)

        elif 'youtube' in query:
            if 'open youtube' in query:
                speak('Loading up Twitter for you.')
                webbrowser.open_new_tab('youtube.com')
            elif 'search youtube' in query:
                speak("What would you like me to search for you?")
                command = MyCommand()
                url = youtube(command)
                webbrowser.open_new_tab(url)
            else:
                url = youtube(query)
                webbrowser.open_new_tab(url)

        elif 'twitter' in query:
            speak('Loading up Twitter for you.')
            webbrowser.open_new_tab('twitter.com')

        elif 'netflix' in query:
            speak('Loading up Netflix for you.')
            webbrowser.open_new_tab('netflix.com')
        
        elif 'inbox' in query:
            webbrowser.open_new_tab('gmail.com')

        elif 'song' or 'music' in query:
            playsong()

        elif 'email' in query:
            sendemail()
        
        elif 'reminder' in query:
            reminder()

        elif 'screenshot' in query:
            screenshot()

        elif 'fact' in query:
            x = randfacts.getFact()
            speak(x)
        
        elif 'dictionary' in query:
            dictionary()

        elif 'hello' in query or 'hi' in query or 'hey' in query:
            speak("Hi {}, how can I help you?".format(name))
        
        elif 'charge' in query or 'power' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent) 
            timeleft = secs2hours(battery.secsleft)
            speak("{} until shutdown.".format(timeleft))
        
        elif 'weather' in query:
            weather()
        
        elif 'find' in query and 'phone' in query:
            findphone()
        
        elif 'news' in query:
            news()
        
        elif 'record' in query:
            if 'audio' in query:
                recaudio()
            elif 'screen' in query:
                recvideo()
            else:
                speak("I'm not entirely sure what you'd like me to record")
        
        elif 'who are you' in query:
            speak("I am a natural language user interface created by Tony Stark.")

        elif 'end' in query:
            speak("Goodbye, {}".format(name))
            sys.exit()
        
        elif 'shutdown' in query:
            speak("Shutting down.")
            if platform == "darwin":
                os.system('poweroff')
            elif platform == "win32":
                os.system('shutdown /p /f')