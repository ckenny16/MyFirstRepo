import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak ("Enter a drake song asap")

song = pg.prompt("Enter a drake song below")

if song == "6 man":
    speak.Speak("That is a lit song.")

elif song == "One Dance":
    speak.Speak("do not be wack")

elif song == "Nice for what":
    speak.Speak("not my favorite, but a pretty dope song")


speak.Speak("what video would you like to watch?")

video = pg.promt("enter below")

speak.Speak("Ok, lets look for " + video + " on YouTube.")

wb.open("https://www.youtube.com/results?search_query=" + video)
