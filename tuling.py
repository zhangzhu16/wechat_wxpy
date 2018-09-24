import os
import time
import random

import requests
from wxpy import Bot, Friend, TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO, FRIENDS, embed

from baiduyuyin import post_recording, text_to_audio, get_response

pics = ([str(i) + '.gif' for i in range(1, 10)] +
        [str(j) + '.jpeg' for j in range(1, 4)] +
        [str(k) + '.jpg' for k in range(1, 3)])

bot=Bot(cache_path=True)

groups = []
group_1 = bot.groups().search('Iprintf 的大蟒蛇')
print(group_1)
if group_1:
    groups.append(group_1[0])
#  group_2 = bot.groups().search('南山吃鸡战斗群')[0]
group_3 = bot.groups().search('一家亲')
if group_3:
    groups.append(group_3[0])

print(groups)



@bot.register(chats=[Friend], msg_types=[TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], except_self=False)
def tuling_reply1(msg):
    default_reply = 'OK'
    print(msg)
    if msg.type == TEXT:
        reply = get_response(msg.text)
        msg.chat.send(reply)
    elif msg.type == RECORDING:
        msg.get_file(msg.file_name)   # 下载语音
        recording_text = post_recording(msg.file_name)
        reply = get_response(recording_text)
        #  text_to_audio(reply)
        #  msg.chat.send_file('a.mp3')
        msg.chat.send(reply)
    elif msg.type == PICTURE:
        msg.chat.send_image('./biaoqing/' + random.choice(pics))
    elif msg.type == NOTE:
        if '收到红包' in msg.text:
            msg.chat.send_image('./biaoqing/hongbao.' + random.choice(['gif', 'jpeg']))
        if '撤回' in msg.text:
            msg.chat.send_image('./biaoqing/chehui.gif')
    elif msg.type == MAP:
        msg.chat.send(msg.text + '\n好的,我收到了')
    elif msg.type == SHARING:
        msg.chat.send(msg.text + '\n好的,我知道了')
    elif msg.type == VIDEO:
        msg.chat.send('你发的这个视频还不错。')
    else:
        msg.chat.send(default_reply)

@bot.register(chats=groups, msg_types=[TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], except_self=True)
def tuling_reply2(msg):
    default_reply = '我收到了 '
    print(msg)
    if msg.type == TEXT:
        reply = get_response(msg.text)
        msg.chat.send(reply)
    elif msg.type == RECORDING:
        msg.get_file(msg.file_name)   # 下载语音
        recording_text = post_recording(msg.file_name)
        reply = get_response(recording_text)
        msg.chat.send(reply)
    elif msg.type == PICTURE:
        msg.chat.send_image('./biaoqing/' + random.choice(pics))
    elif msg.type == NOTE:
        if '收到红包' in msg.text:
            msg.chat.send('哈哈😄，大佬发红包了!')
            msg.chat.send_image('./biaoqing/hongbao.' + random.choice(['gif', 'jpeg']))
        if '撤回' in msg.text:
            msg.chat.send_image('./biaoqing/chehui.gif')
    elif msg.type == MAP:
        #  print(msg.text)
        msg.chat.send(msg.text + '\n好的,我知道了')
    elif msg.type == SHARING:
        msg.chat.send(msg.text + '\n好的,我知道了')
    elif msg.type == VIDEO:
        msg.chat.send('你发的这个视频还不错。')
    else:
        msg.chat.send(default_reply)


# 注册好友请求类消息
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    new_friend = bot.accept_friend(msg.card)
    # 或 new_friend = msg.card.accept()
    new_friend.send('哈哈，我自动接受了你的好友请求')
    new_friend.send_image('./biaoqing/tongguo.gif')

#  #整点报时
#  while True:
    #  hour = time.strftime('%H', time.localtime(time.time()))
    #  minutes = time.strftime('%M', time.localtime(time.time()))
    #  seconds = time.strftime('%S', time.localtime(time.time()))
    #  if (hour == '07' and minutes == '30' and seconds == '00'):
        #  nowTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        #  group_1.send('早上好！\n起床啦，为您整点报时：\n{}\n------- 今日天气--------\n{}'.format(nowTime, get_response('佛山顺德天气')))
        #  group_2.send('早上好！\n起床啦，为您整点报时：\n{}\n--------今日天气--------\n{}'.format(nowTime, get_response('深圳南山天气')))
    #  elif(hour == '13' and minutes == '30' and seconds == '00'):
        #  nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        #  for group in [groups_1, group_2]:
            #  group.send('下午好！\n该干活了，为您整点报时：\n{}\n--------轻松一下--------\n{}'.format(nowTime, get_response('讲个笑话')))
    #  elif (hour == '00' and minutes == '00' and seconds == '00'):
        #  nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        #  for group in [group_1, group_2]:
            #  group.send('晚上好！\nIt\'s time to sleep，为您整点报时：\n{}\n--------晚安全世界--------'.format(nowTime))
    #  time.sleep(1)


#bot.start()
embed()
#  os.system("pause")

