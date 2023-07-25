import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from googletrans import Translator
from bs4 import BeautifulSoup
import requests
import random

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

jokes = [
    'Why did the scarecrow win an award? Because he was outstanding in his field!',
    'Why don’t scientists trust atoms? Because they make up everything!',
    'Why did the chicken cross the playground? To get to the other slide!',
    'Why did the cookie go to the doctor? Because it was feeling crumbly!',
]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def calculate(expression):
    return eval(expression)

    
def translate_text(text, dest_language):
    translator = Translator(service_urls=['translate.google.com'])
    translated_text = translator.translate(text, dest=dest_language).text
    return translated_text
    
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning girl!")
        
    elif hour>=12 and hour<18:
        speak("A very Good Afternoon dear")
        
    else:
        speak("Good Evening")   
     
    speak("Hello Raavi, I am Iris, your all time favourite companion")
    
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        
      print("Recognizing...")    
      query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
      print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None" 
    return query

 
if __name__=="__main__" :
   # speak("Hello, the cutest the most pretty girl, Ms. Raavi Singh. How are you?")
   wishMe()
   while True:
      query= takeCommand().lower()


      
      if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
      if 'multiplied by' in query:
       nums = query.split('multiplied by')
       result = int(nums[0]) * int(nums[1])
       speak(f"The result of {nums[0]} multiplied by {nums[1]} is {result}")

      elif 'divided by' in query:
       nums = query.split('divided by')
       result = int(nums[0]) / int(nums[1])
       speak(f"The result of {nums[0]} divided by {nums[1]} is {result}")

            
      elif 'calculate' in query or 'math' in query:
            speak("Sure, what do you want me to calculate?")
            expression = takeCommand()
            try:
                result = eval(expression)
                speak(f"The answer is {result}")
            except:
                speak("Sorry, I couldn't calculate that. Please try again.")
                
    
            
      elif 'open youtube' in query:
            webbrowser.open("youtube.com") 
            
      elif 'open google' in query:
            webbrowser.open("google.com")   
            
      elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")
            
      elif 'open notepad' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(codePath)
            
      
            
      elif 'translate' in query:
            speak('What should I translate?')
            text = takeCommand()
            translated_text = translate_text(text, 'hi')
            speak(f'The translated text is {translated_text}')
            print(translated_text)
            
      elif 'tell me a joke' in query:
       joke = random.choice(jokes)
       speak(joke)
       print(joke)
            
        
      elif 'news from times of india' in query:
       speak("Getting the latest news from Times of India...")
       url = "https://timesofindia.indiatimes.com/home/headlines"
       news = webbrowser.open_new_tab(url)
       speak("Here are the latest news headlines. Have a look!")
      
      if 'weather' in query:
       speak('Please tell me your city name')
       city = takeCommand().lower()
       city = city.replace(" ", "+")
       url = f"https://www.google.com/search?q={city}+weather"
       html = requests.get(url).content
       soup = BeautifulSoup(html, 'html.parser')
       temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
       weather = soup.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).text
       speak(f"The current temperature in {city} is {temperature} and the weather is {weather}")
       print(f"The current temperature in {city} is {temperature} and the weather is {weather}")
   
  


            
            
            
            
            
            
            
            
            
      