import telebot
from time import sleep
from bs4 import BeautifulSoup
import requests
import threading
def get():
    ss={}
    url = "https://khamsat.com/community/requests"
    page = requests.get(url)
    trs  = BeautifulSoup(page.content ,  "html.parser") .find_all('tr', {"class":"forum_post"})
    for tr in trs:
        index = trs.index(tr,0,len(trs))
        if index == 6:
            break
        ss[index] = {  
            'id':str(tr["id"]) .split('-')[1] ,
            "address" : tr.findChildren('a',{"class":"ajaxbtn"})[0].text,
            "content":"",
            "link":"https://khamsat.com/{}".format(tr.findChildren('a',{"class":"ajaxbtn"})[0]['href']),
            "user":tr.findChildren('a',{"class":"user"})[0].text,
            "spend": tr.findChildren('span')[0]['title'],
            "time": tr.findChildren('span')[0].text
        }
        content = requests.get(ss[index]["link"])
        content = BeautifulSoup(content .content,  "html.parser") .find('article', {"class":"replace_urls"}).text
        ss[index]["content"] = content
    return  ss
id=['540069', '540112', '540105', '539783', '540059', '540096', '540091', '539999', '540100', '540073', '540099', '540113', '540101', '539975', '540089', '540015', '540102', '540087', '540396', '540347', '540388', '540395', '540394', '540334', '540369', '540280', '540171', '540398', '542173', '542170', '542171', '542160', '541872', '542168']
bot = telebot.TeleBot('2082247439:AAG2S9ePBwPVycUXERXEwUTG8B0IVFNZdDY')
def send():
    threading.Timer(60, send).start()
    data ={}
    mess=""
    data  =  get()
    for i in data:
      print(str(data[i]['id']) in id)
      if data[i]['id'] in id :
        continue
      mess  = "*{}\n*{}\n*{}\n*{}\n{}\n\n{}".format(data[i]['address'] , data[i]['user'] ,data[i]['spend'],data[i]['time'],data[i]['content'] ,data[i]['link']  )
      bot.send_message(-1001520641833,mess)
      mess = ""
      id.append(data[i]['id'])
      sleep(0.1)
    
    print(id)

send()



@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, text="https://t.me/khamsat_not_found_request")
    # send()

print("working...")
bot.polling(True)
