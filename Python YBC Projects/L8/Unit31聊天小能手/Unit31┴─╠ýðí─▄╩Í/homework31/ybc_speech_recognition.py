import  requests
import sounddevice as sd
from scipy.io.wavfile import write

def record(s):
    fs = 16000  # 采样率
    print('正在录音中...请说话，时长为5秒钟')
    myrecording = sd.rec(int(s * fs), samplerate=fs, channels=1)
    sd.wait()  # 等待录音结束
    write('output.mp3', fs, myrecording)  # 保存为mp3文件
    print('录音已保存为“output.mp3”文件')
    return 'output.mp3'

def get_audio_info(audio):
    print('语音识别中...')
    url = 'https://www.yuanfudao.com/ada-student-app-api/api/speech/audio-to-text'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
         'Content - Type': 'multipart / form - data'
    }
    files = {
        'voice': open(audio,'rb')
    }
    r = requests.post(url, headers=headers, files=files)
    if r.status_code == 200:
        audio_info_data = r.json()
        print('转文字结果如下：')
        return audio_info_data['text']



