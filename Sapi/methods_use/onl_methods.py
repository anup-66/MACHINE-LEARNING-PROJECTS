import requests as req
import wikipedia as wiki
import pywhatkit as py
from email.message import EmailMessage
import smtplib as sm
from decouple import config as con
EMAIL = con('EMAIL')
PASSWORD = con('PASSWORD')
WEATHER= con("WEATHER")
def find_my_ip():
    ip_address = req.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(speech):
    ans = wiki.summary(speech, sentences=2)
    return ans


def play_on_youtube(video):
    py.playonyt(video)

def Google_search(speech):
    ans = py.search(speech)
    return ans

def send_whatsapp_message(number, message):
    py.sendwhatmsg_instantly(f"+91{number}", message)

def send_mail(send_to_add,sub,msg):
    try:
        email = EmailMessage()
        email.set_content(msg)
        email['TO'] = send_to_add
        email['subject'] = sub
        email['From'] = "anup7970hm@gmail.com"
        send = sm.SMTP("smtp.gamil.com",587)
        send.starttls()
        send.login("anup7970hm@gmail.com","anup@6536")
        send.send_message(email)
        send.close()
        return True
    except Exception:
        print(Exception)
        return False





def weather_report(city):
    res = req.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=93023b37dded2d4ae7fbbe7ef9baf4c4&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def get_random_joke():
    # headers = {
    #     'Accept': 'application/json', headers=headers
    # }
    # res = req.get("https://icanhazdadjoke.com/").json()
    # # res = req.get("https://icanhazdadjoke.com/").json()
    # # f = r"https://official-joke-api.appspot.com/random_ten"
    # # data = req.get(f).json()
    # # tt = json.loads(data.text)
    # # return data
    res= req.get("https://icanhazdadjoke.com/search",
                                 headers={"Accept": "application/json"}).json()
    results = res["results"]
    return results[0]['joke']


def getadvice():
    res = req.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']