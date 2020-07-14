import wave
import pyaudio
import speech_recognition as speech


# file = pyglet.resource.media('audio/hasty-ba-dum-tss.mp3')
# file.play()

# pyglet.app.run()


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
    play_audio("./audio/click.wav")

    with speech.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    play_audio("./audio/click.wav")
    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Sorry, I couldn't understand you")

    print("Your command:", command)

initSpeech()

