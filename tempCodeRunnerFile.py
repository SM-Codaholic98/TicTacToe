text_speech = pyttsx3.init()
a = "welcome to tic tac toe game"
text_speech.setProperty("rate", 110)
text_speech.say(a)
text_speech.runAndWait()