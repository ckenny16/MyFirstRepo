import pyautogui as pg

import win32com.client as wncl

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Ford is a living ticked")
