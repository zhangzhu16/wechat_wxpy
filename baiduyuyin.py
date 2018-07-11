import requests
import base64
import json
from pydub import AudioSegment
from urllib import parse

AppID = 11189655
APIKey = "kEGZMg45PdwQ9WxE9VHSyp7I"
SecretKey = "8zayrhUBQuEXpSsVjZ8FKcW5ezIe3T40"

baidu_server = "https://aip.baidubce.com/oauth/2.0/token?"
grant_type = "client_credentials"
client_id = APIKey
client_secret = SecretKey
headers = {'Content-Type': 'application/json'}

token_url = baidu_server+"grant_type="+grant_type+"&client_id="+client_id+"&client_secret="+client_secret
response = requests.post(token_url)
Access_Token = response.json()['access_token']
print(Access_Token)


def mp3_to_wav(filepath):
    voice = AudioSegment.from_mp3(filepath)
    voice_path = voice.export("post.wav", format="wav")
    return voice_path


#  语音识别
def post_recording(filename):
    mp3_to_wav(filename)
    with open("post.wav", 'rb') as file:
        voice_data = file.read()
        voice_base64 = base64.b64encode(voice_data).decode('utf8')   # 编码(bytes)后还要解码(得到string）
        speech_len = len(voice_data)
    post_data = {
            "format": "wav",
            "rate": 8000,
            "dev_pid": 1537,
            "channel": 1,
            "token": Access_Token,
            "cuid": "robot1",
            "speech": voice_base64,
            "len": speech_len
    }
    response_data = requests.post('http://vop.baidu.com/server_api', data=json.dumps(post_data), headers=headers)
    response_text = response_data.json()['result'][0]
    return response_text


# 语音合成
def text_to_audio(message):
    tex_ = message
    tex = parse.quote(tex_)
    print(tex)
    tok = Access_Token
    cuid = 'robot'
    ctp = 1
    lan = 'zh'
    vol = 5
    per = 4
    url = "http://tsn.baidu.com/text2audio?"
    audio_url = url+"tex="+tex+"&lan="+lan+"&tok="+tok+"&cuid="+cuid+"&ctp="+str(ctp)+"&vol="+str(vol)+"&per="+str(per)
    print(audio_url)
    audio = requests.get(audio_url)
    with open('a.mp3', 'wb') as f:
        for chunk in audio:
            f.write(chunk)
    #  return audio

KEY = '6cd088d85dc84596bef960d84615bcf8'

'''备用KE 解决次数限制
8edce3ce905a4c1dbb965e6b35c3834d
eb720a8970964f3f855d863d24406576
1107d5601866433dba9599fac1bc0083
71f28bf79c820df10d39b4074345ef8c
'''


def get_response(msg):
    apiurl = 'http://www.tuling123.com/openapi/api'
    data = {
            'key': KEY,
            'info': msg,
            'userid': '张柱',
            }
    try:
        r = requests.post(apiurl, data=data).json()
        return r.get('text')
    except:
        return

if __name__ == '__main__':
    response = get_response('哈哈')
    print(response)

