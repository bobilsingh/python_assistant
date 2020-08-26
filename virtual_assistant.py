import os
import pyttsx3

print("Hello i am your virtual assistant:")
pyttsx3.speak("Hello i am your virtual assistant")
while True:
 pyttsx3.speak("what can i do for you  ")
 p = input(" what can i do for you :  ")
	
	
 if(("open" in p)or("run" in p)or("start" in p))and("launch" in p) and ("chrome"in p):
    os.system("start chrome")
    pyttsx3.speak(" chrome is launched")

 elif(("open" in p)or("run" in p)or("show" in p)) and ("services"in p):
    print("welcome to my services ")
    pyttsx3.speak("welcome to my services ")
    print("\n************************************************************* \n")
    print("you want to use chrome from here ")
    pyttsx3.speak("you want to use chrome from here")
    print("you can see my current device location")
    pyttsx3.speak("you can see my current device location ")
    print("you want to use google meet from here")
    pyttsx3.speak("you want to use google meet from here ")
    print("you want to use notepad  from here ")
    pyttsx3.speak("you want to use notepad  from here ")
    print("you want to use facebook from here ")
    pyttsx3.speak("you want to use facebook from here ")
    print("you want to use gmail from here")
    pyttsx3.speak("you want to use gmail from here ")
    print("you want to use google maps  from here")
    pyttsx3.speak(" you want to use google maps  from here")
    print("you want to see my linkedin profile from here")
    pyttsx3.speak(" you want to see my linkedin profile from here")
    print("you want to play your favourite song from here")
    pyttsx3.speak(" you want to play your favourite song from here ")
    print("you want to use whatshapp from here \n")
    pyttsx3.speak(" you want to use whatshapp from here")
    pyttsx3.speak(" these are my services ")

 elif(("show" in p)or("write" in p)or("your" in p)) and ("name"in p):
    print("Hello I Am virtual assistant ")
    pyttsx3.speak("Hello I Am Virtual Assistant")

 elif ("show" in p) or ("current" in p) or ("location" in p) and ("device" in p):
        pyttsx3.speak("This code will show the current device location")
        #show the device current location
        import requests
        res = requests.get('https://ipinfo.io')
        data = res.json()
        city = data['city']
        location = data['loc'].split('.')
        latitude = location[0]
        longitude = location[1]
        print("Latitude :", latitude)
        print("Longitude :",longitude)
        print("City :",city)
        pyttsx3.speak("Latitude")
        pyttsx3.speak(latitude)
        pyttsx3.speak("Longitude")
        pyttsx3.speak(longitude)
        pyttsx3.speak("City :")
        pyttsx3.speak(city)

 elif(("open" in p)or("run" in p)or("start" in p)) and("notepad"in p):
    os.system("notepad")
    pyttsx3.speak(" notepad is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and ("facebook"in p):
    os.system("start chrome facebook.com")
    pyttsx3.speak("facebook is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and (("whatsapp" in p)or("whatsapp web"in p)):
    os.system("start chrome web.whatsapp.com")
    pyttsx3.speak("whatsapp is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and ("youtube"in p):
    os.system("start chrome youtube.com")
    pyttsx3.speak("youtube is launched")

 elif(("open" in p)or("start" in p)) and ("gmail"in p):
    os.system("start chrome gmail.com")
    pyttsx3.speak("your gmail is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and ("googlemeet"in p):
    os.system("start chrome meet.google.com")
    pyttsx3.speak("googlemeet is launched")

 elif(("open" in p)or("run" in p)or("start" in p)) and ("linkedin"in p):
    os.system("start chrome https://www.linkedin.com/in/bobilsingh/")
    pyttsx3.speak("linkedin is launched") 

 elif(("open" in p)or("run" in p)or("start" in p)) and (("googlemap" in p)or("google map"in p)):
    os.system("start chrome https://www.google.co.in/maps/@28.9873942,77.6289195,12z")
    pyttsx3.speak("google map is launched")

 elif(("open" in p)or("play" in p)or("run" in p)or("start" in p)) and (("favourite song")or("favourite"in p)):
    os.system("start chrome https://www.youtube.com/watch?v=IAN1Cy5pnJ4")
    pyttsx3.speak("injoy your favourite song ")

 elif("exit" in p):
    print(" THANKS FOR USING MY SERVICES")
    pyttsx3.speak("   THANKS FOR USING MY SERVICES   ")
    break
 else:	
    print("not valid")
    pyttsx3.speak("not valid service")