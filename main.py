import wave
import os
import pandas as pd
import pyaudio
import speech_recognition as speech


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = speech.Recognizer()


def initSpeech():
    print("Listening...")
    play_audio("audio/click.wav")

    with speech.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    play_audio("audio/click.wav")
    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Sorry, I couldn't understand you")
        command = "N/A"

    return command


def identifier(command):
    directory = './lyrics/'
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            f = open(directory + filename)
            lines = f.read()
            if (command or command.lower()) in lines:
                print("This is '" + filename.replace(".txt", "").title() + "' by Phoebe Bridgers")
                continue
            else:
                continue
        else:
            continue


command = initSpeech()
identifier(command)

