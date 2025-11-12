import speech_recognition

def record(r, mic, time):
    with mic as source:
        audio = r.record(source=mic, duration=time)
    return audio


