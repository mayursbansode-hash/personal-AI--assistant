import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import musicLibrary

recognizer = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def processCommand(c):

    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
   
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif"what is time" in c.lower():
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Yess Boss, The time is {time}")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


    elif"what is today's date" in c.lower():
        time = datetime.datetime.now().strftime("%d:%B %Y")
        speak(f"Yess Boss, The time is {time}")

    elif "calculate" in c.lower():

        expression = c.lower().replace("calculate", "")
        expression = expression.replace("plus", "+")
        expression = expression.replace("minus", "-")
        expression = expression.replace("into", "*")
        expression = expression.replace("multiplied by", "*")
        expression = expression.replace("divided by", "/")

        result = eval(expression)
        speak(f"Yess Boss, The answer is {result}")
       
    


if __name__ == "__main__":
    speak("Hii Boss.....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
  

        print("recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            print("You said", word)
            if(word.lower() == "maxtron"):
                 print("detected")
                 speak("Yess Boss, Maxx here")
                 
                 
                 # Listen for command
                 with sr.Microphone() as source:
                    print("Maxx Active...", word)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("command", command)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    print("Processing command...")
                    processCommand(command)
        
        
        except sr.UnknownValueError:
          print("Aawaz samajla nahi, punha bola.")
          
        except sr.RequestError as e:
            print("Google Speech Service problem:", e)
            speak("i dont understand")

        except Exception as e:
            print("ERROR TYPE:", type(e).__name__)
            print("ERROR DETAILS:", repr(e))
 
 








               