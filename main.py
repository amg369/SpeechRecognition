import wave
import pyaudio
import speech_recognition as speech

# For playing the "click" sound prior to listening.
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

# Listens through the mic
def initSpeech():
    print("Listening...")
    play_audio("./audio/click.wav")

    with speech.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    play_audio("./audio/click.wav")
    command = ""
    
# If the speech cannot be recognized, it goes to google.
    try:
        command = r.recognize_google(audio)
    except:
        print("Sorry, I couldn't understand you")
    
    # Returns the regonized speech in the console
    print("Your command:", command)

initSpeech()

