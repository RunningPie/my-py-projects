import os
import speech_recognition as sr
import pywhatkit
import wikipedia
from datetime import datetime
import time
import os
from gtts import gTTS
from playsound import playsound

audio_dir = "D:/.../audio files"
now = datetime.now()

# define a listen function
def listen():
    # set recognizer (r) as sr.Recognizer()
    r = sr.Recognizer()
    r.pause_threshold = 0.6
    r.record = 25
    r.energy_threshold = 1000
    # set device microphone as source
    with sr.Microphone() as source:
        if lang == "en":
            print("I am listening....")
        elif lang == "ja":
            print("私は聞いています...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio, language=lang)
        if lang == "en":
            print("You said: ", data)
        elif lang == "ja":
            print("あなたは言った：", data)
    except sr.UnknownValueError:
        if lang == "ja":
            respond("ごめんなさい、聞こえませんでした", name="UVE")
        elif lang == "en":
            respond("Sorry, I couldn't catch that", name="UVE_ja")
        data = "URE"
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

# define a response function
def respond(audioString, name=now.strftime("%m%d%Y %H%M%S")):
    global lang
    tts = gTTS(text=audioString, lang=lang)
    if name != now.strftime("%m%d%Y %H%M%S"):
        filename = audio_dir+"\speech "+name+now.strftime("%m%d%Y %H%M%S")+".mp3"
    if not os.path.exists(filename):
        tts.save(filename)
    playsound(filename)
    print(audioString)

def wiki_search():
    global lang
    if lang == "en":
        wikipedia.set_lang("en")
        respond("What topic would you like to search for?", "wiki prompt")
        topic = listen()
        while topic == "URE":
            respond("What topic would you like to search for?", "wiki prompt")
            topic = listen()
        if "cancel" in topic.lower():
            pass
        else:
            try:
                respond(wikipedia.summary(topic, sentences=2), "search res")
                print(wikipedia.summary(topic, sentences=2))
            except wikipedia.exceptions.DisambiguationError as DE:
                for opt in DE.options:
                    respond(str(opt), "option"+str(DE.options.index(opt)))
                wiki_search()
    elif lang == "ja":
        wikipedia.set_lang("ja")
        respond("何を調べたいですか？", "uiki prompt")
        topic = listen()
        while topic == "URE":
            respond("何を調べたいですか？", "uiki prompt")
            topic = listen()
        if "キャンセル" in topic.lower():
            pass
        else:
            try:
                respond(wikipedia.summary(topic, sentences=2), "kensaku kekka")
                print(wikipedia.summary(topic, sentences=2))
            except wikipedia.exceptions.DisambiguationError as DE:
                respond("見つかりませんでした. 多分これらの1つですか？", "aimai")
                for opt in DE.options:
                    respond(str(opt), "option"+str(DE.options.index(opt)))
                wiki_search()

def digital_assistant(data):
    global lang
    try:
        if lang == "ja":
            if "元気" in data:
                listening = True
                respond(".,私は元気です、 ありがとう", "genki")
            if "何時" in data:
                listening = True
                if now.strftime("%p").lower() == "am":
                    am_or_pm = "午後"
                elif now.strftime("%p").lower() == "pm":
                    am_or_pm = "午後"
                respond("今は"+am_or_pm+now.strftime("%I")+"時です", "jikan")
            if [i for i in ["で調", "検索"] if i in data] != []:
                listening = True
                wiki_search()
                respond("それは私がウィキペディアで見つけたものです", "toko kensaku")
            if "変更" in data:
                respond("どの言語に変更しますか?", "gengo henko")
                lang_ans = listen()
                while lang_ans == "URE":
                    respond("どの言語に変更しますか?", "gengo henko")
                    lang_ans = listen()
                if "英語" in lang_ans.lower():
                    lang = "en"
                    respond("I'm now talking in English", "en change s")
                elif "日本" in lang_ans.lower():
                    lang = "ja"
                    respond("もう日本語でしゃべってる", "nihongo de s")
                else:
                    respond("私たちはまだその言語を持っていません", "gengo henko shipai")
                listening = True
            if [i for i in ["やめる", "十分"] if i in data] != []:
                listening = False
                respond("はい、またね", "matane")
                print("リスニングを停止しました")
                return listening
            return listening
        elif lang == "en":
            if "how are you" in data:
                listening = True
                respond("I'm fine. Thank you", "fine")
            if "time" in data:
                listening = True
                respond("It is "+now.strftime("%I %p"), "time")
            if "search" in data:
                listening = True
                wiki_search()
                respond("That's what I found on wiki", "post search")
            if "change language" in data:
                respond("What language would you like to change to?", "change lang")
                lang_ans = listen()
                while lang_ans == "URE":
                    respond("What language would you like to use?", "change lang")
                    lang_ans = listen()
                if "english" in lang_ans.lower():
                    lang = "en"
                    respond("I'm already talking in English", "already en")
                elif "japan" in lang_ans.lower():
                    lang = "ja"
                    respond("私は今日本語を話している", "change ja success")
                else:
                    respond("Sorry we don't have that language yet", "lang na")
                listening = True
            if [i for i in ["stop", "that's all"] if i in data] != []:
                listening = False
                respond("Okay, see you next time!", "bye")
                print("Listening stopped")
                return listening
            return listening
    except UnboundLocalError as ULE:
        if lang == "en":
            respond("Do you want me to stop listening?", "stop listen")
            stop = input("Do you want me to stop listening? (y/n) ")
        elif lang == "ja":
            respond("聞くのやめようか？", "yameru")
            stop = input("聞くのやめようか？ (y/n) ")
        if stop.lower() == "y":
            listening = False
            return listening
        else:
            listening = True
            return listening

time.sleep(2)
lang = "en"
respond("Hello, I am Sakura, your virtual voice assistant", "welcome")
respond("Before you can use this VA, we need to set some things up", "setup")
respond("What's your name?", "ask name")
name = listen()
while name == "URE":
    respond("What's your name? or would you like to type it in?", "confirm name")
    name = listen()
if "type" in name.lower():
    name = input("Type in your name: ")
respond("Is "+name+" correct?", "yn name")
yn_name = listen()
while yn_name == "URE":
    respond("Is "+name+" correct?", "yn name")
    yn_name = listen()
if "no" in yn_name:
    respond("Please type in your correct name", "name correction")
    name = input("Type in your name: ")
    respond("Okay, let's proceed", "proceed")
elif "yes" in yn_name:
    respond("Okay, let's proceed", "proceed")
respond("What language would you like to use? English or Japanese?", "ask lang")
lang_ans = listen()
while lang_ans == "URE":
    respond("What language would you like to use?", "confirm lang")
    lang_ans = listen()
if "english" in lang_ans.lower():
    lang = "en"
elif "japan" in lang_ans.lower():
    lang = "ja"
if lang == "en":
    respond("Hello " + name + ". How can I help you today?", "greeting")
elif lang == "ja":
    respond("こんにちは " + name + ". 私はあなたのために何ができますか？", "aisatsu")
listening = True
while listening == True:
    data = listen()
    listening = digital_assistant(data)
