import sys
import base64
import urllib.request
import json
import wave
import os

tts_url ='http://rospeex.ucri.jgn-x.jp/nauth_json/jsServices/VoiceTraSS'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = { 'User-Agent' : user_agent }


if __name__ == '__main__':
    message = sys.argv[1]

    tts_command = {'method': 'speak',
                   'params': ['1.1',
                              {'language': 'ja', 'text': message, 'voiceType': "*", 'audioType': "audio/x-wav"}]}
    
    obj_command = json.dumps(tts_command).encode('utf-8')       
    req = urllib.request.Request(tts_url, obj_command, headers)
    received = urllib.request.urlopen(req).read().decode('utf-8') 

    obj_received = json.loads(received)
    tmp = obj_received['result']['audio']
    speech = base64.decodestring(tmp.encode('utf-8'))

    f = open("out.wav", 'wb')
    f.write(speech)
    f.close

    os.system('afplay out.wav; rm -rf out.wav')
