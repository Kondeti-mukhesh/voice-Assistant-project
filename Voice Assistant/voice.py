import speech_recognition as sr
import pyttsx3
import requests
import datetime
import webbrowser

#assistant speking
engine=pyttsx3.init()
print("Assistant:Hello! I am your personal assistant. How can I assist you today?")
engine.say("Hello! I am your personal assistant. How can I assist you today?")
engine.runAndWait()

while True:
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=2)
        print("please speak something.........")
        try:
           audio=recognizer.listen(source,timeout=5,phrase_time_limit=10)
           text=recognizer.recognize_google(audio,language="en-US").lower()
           print("You:",text)
           
        except sr.UnknownValueError:
            print("Assistant: Sorry, I did not understand that.")
            engine.say("Sorry, I did not understand that.")
            engine.runAndWait()

    #check the weather using voice assistant
    if "weather" in text:
        city="warangal"
        api_key="32204b77b4288b74b754520d0d54558a"
        base_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response=requests.get(base_url)

        if response.status_code==200:
            data=response.json()
            weather=data["weather"][0]["description"]
            temp=data["main"]["temp"]
            print(f"Assistant: The weather in {city} is {weather} with a temperature of {temp}°C")
            engine.say(f"The weather in {city} is {weather} with a temperature of {temp}°C")

        else:
            engine.say("Sorry, I could not fetch the weather.")
            print("Assistant:Sorry, I could not fetch the weather")
        engine.runAndWait()

    #check the top news using voice assistant
    elif "news" in text:
        api_key_news="817c11b2c13f4820b9ad6279e0609521"
        url_news=f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key_news}"
        response=requests.get(url_news)

        if response.status_code==200:
            articles=response.json().get("articles",[]) #here news api present array
            headlines = [
            f"{article['title']} (Source: {article['source']['name']})"
            for article in articles[:5]
            ]
            print("Assistant:Here are the top 5 news headlines:")
            for i,headlines in enumerate(headlines,1):
                print(f"{i}. {headlines}")
            engine.say("Here are the top 5 news headlines:"+",".join(headlines))
        
        else:
            print("Assistant: Sorry, I could not fetch the news.")
            engine.say("Sorry, I could not fetch the news.")
            engine.runAndWait()

    #chech the time using vioce assistant
    elif "time" in text:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Assistant: The current time is {time}")
        engine.say(f"The current time is {time}")
        engine.runAndWait()
    
    # Open YouTube
    elif "youtube" in text:
        print("Assistant: Opening YouTube...")
        engine.say("Opening YouTube...")
        engine.runAndWait()
        webbrowser.open("https://www.youtube.com")
    

    # Open browser
    elif "browser" in text:
        print("Assistant: Opening browser...")
        engine.say("Opening browser...")
        engine.runAndWait()
        webbrowser.open("https://www.google.com")
        
    elif "exit" or "quit" in text:  #exit is a non-empty string
        print("Assistant: Goodbye! Have a nice day!")
        engine.say("Goodbye! Have a nice day!")
        break



