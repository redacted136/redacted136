#pip install sounddevice
import ybc_speech_recognition as ysr


audio = ysr.record(5)
result = ysr.get_audio_info(audio)
print(result)