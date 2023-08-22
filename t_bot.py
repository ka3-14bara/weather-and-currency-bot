import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup

f = open("ok.txt", 'r')

tok =''
for i in f:
    tok += i

bot = telebot.TeleBot(tok)

def weather():
    url = 'https://wttr.in/naberezhnyye_chelny'

    weather_parameters = {
        '0': '',
        'T': '', 
        'M': '',
        'lang': 'ru'
    }
    response = requests.get(url, params = weather_parameters)
    return response

class Currency:
    usd_rub = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    eur_rub = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=555979541&sxsrf=AB5stBh0-8HsKO-h6WdNFSuNhweknNC_nQ%3A1691781127649&ei=B4jWZMSQJ9u9wPAPobSKkA0&oq=tdhj%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiEXRkaGrQuiDRgNGD0LHQu9GOKgIIADINEAAYDRiABBixAxiDATIHEAAYDRiABDIHEAAYDRiABDIHEAAYDRiABDIHEAAYDRiABDIHEAAYDRiABDIHEAAYDRiABDIHEAAYDRiABDIHEAAYDRiABDIHEAAYDRiABEi3KlCLF1j4G3AEeAGQAQCYAV2gAeUCqgEBNLgBAcgBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhDwgIGEAAYBxgewgIIEAAYBxgeGArCAgoQABgHGB4YChgqwgINEAAYCBgHGB4Y8QQYCsICChAAGAUYBxgeGAriAwQYACBBiAYBkAYK&sclient=gws-wiz-serp'
    cny_rub = 'https://www.google.com/search?q=%D1%8E%D0%B0%D0%BD%D1%8C+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=555979541&sxsrf=AB5stBjgAelGVCYT-WsFXSLlByGsQSdm5A%3A1691781293562&ei=rYjWZLPQIPWbwPAP5LiVYA&oq=%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiDdC6INGA0YPQsdC70Y4qAggGMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB5IwTJQqRpYqRpwAngBkAEAmAFeoAFeqgEBMbgBAcgBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhD4gMEGAAgQYgGAZAGCg&sclient=gws-wiz-serp'
    
    usd_price = 0
    eur_price = 0
    cny_price = 0
    

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self, usd = usd_rub, eur = eur_rub, cny = cny_rub):

        self.usd_price = (self.get_price(usd))
        self.eur_price = (self.get_price(eur))
        self.cny_price = (self.get_price(cny))

    def get_price(self, url: str) -> str:

        self.link = url
    
        full_page = requests.get(self.link, headers=self.headers)

        soup_curr = BeautifulSoup(full_page.content, 'html.parser')

        convert_html = soup_curr.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        res_currency = convert_html[0].text
        return res_currency
    
class Cryptocurrency:
    btc_usd = 'https://www.google.com/search?q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%BA%D1%83%D1%80%D1%81+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sca_esv=555979541&sxsrf=AB5stBhKVmj2cvQmSIX9eFRBH-MvensfIg%3A1691781328549&ei=0IjWZLGVH5LOwPAP5caM6Ao&oq=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%BD+%D0%BA&gs_lp=Egxnd3Mtd2l6LXNlcnAiD9Cx0LjRgtC60L7QvSDQuioCCAAyDBAAGIoFGEMYRhiCAjINEAAYigUYsQMYgwEYQzINEAAYgAQYsQMYgwEYCjIHEAAYigUYQzINEAAYigUYsQMYgwEYQzIKEAAYgAQYsQMYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCkjIKVAAWNoccAF4AZABAZgB3gSgAaQMqgEJNC4yLjIuNS0xuAEByAEA-AEBwgIHECMYigUYJ8ICCxAAGIAEGLEDGIMBwgILEC4YgAQYxwEY0QPCAhEQLhiABBixAxiDARjHARjRA8ICBRAAGIAEwgILEC4YgAQYsQMYgwHCAgQQIxgnwgITEC4YigUYsQMYgwEYxwEY0QMYQ8ICEBAAGIAEGBQYhwIYsQMYgwHCAggQLhiABBixA8ICCBAAGIoFGLEDwgIIEAAYgAQYsQPiAwQYACBBiAYB&sclient=gws-wiz-serp'
    eth_usd = 'https://www.google.com/search?q=%D1%8D%D1%84%D0%B8%D1%80+%D0%BA%D1%83%D1%80%D1%81+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sca_esv=555979541&sxsrf=AB5stBie0DtPBmtOAAQmh5gFGi6iUj05Tg%3A1691781401533&ei=GYnWZJCKH4KrwPAP7fWR2Ac&ved=0ahUKEwjQ-uXrqNWAAxWCFRAIHe16BHsQ4dUDCA8&uact=5&oq=%D1%8D%D1%84%D0%B8%D1%80+%D0%BA%D1%83%D1%80%D1%81+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&gs_lp=Egxnd3Mtd2l6LXNlcnAiI9GN0YTQuNGAINC60YPRgNGBINC6INC00L7Qu9C70LDRgNGDMgwQABiKBRhDGEYYggIyBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBRAAGIAEMgUQABiABDIIEAAYCBgHGB4yCBAAGAgYBxgeMggQABgIGAcYHjIIEAAYCBgHGB5Img9Q9gdY9AxwAXgBkAEAmAHcAaAB3AOqAQUzLjAuMbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhDwgIWEC4YigUYxwEY0QMYyAMYsAMYQ9gBAeIDBBgAIEGIBgGQBgu6BgQIARgI&sclient=gws-wiz-serp'
    doge_usd = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%B3%D0%BA%D0%BE%D0%B8%D0%BD+%D0%BA%D1%83%D1%80%D1%81+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sca_esv=555979541&sxsrf=AB5stBiHLS2eSxzJs3URtgeXStKSKO8e2A%3A1691781430008&ei=NonWZP4QxKnA8A_Svai4Cg&ved=0ahUKEwj-g7H5qNWAAxXEFBAIHdIeCqcQ4dUDCA8&uact=5&oq=%D0%B4%D0%BE%D0%B3%D0%BA%D0%BE%D0%B8%D0%BD+%D0%BA%D1%83%D1%80%D1%81+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&gs_lp=Egxnd3Mtd2l6LXNlcnAiKdC00L7Qs9C60L7QuNC9INC60YPRgNGBINC6INC00L7Qu9C70LDRgNGDMgcQABgNGIAEMgoQABgIGAcYHhgKSJQgUK8LWNIYcAJ4AZABAZgB7QSgAYsKqgEJNS4wLjEuNS0xuAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICChAAGIoFGLADGEPCAhYQLhiKBRjHARjRAxjIAxiwAxhD2AEBwgIGEAAYBxgewgIIEAAYCBgHGB7CAgcQIxiwAhgnwgIGEAAYHhgNwgIIEAAYCBgeGA3iAwQYACBBiAYBkAYMugYECAEYCA&sclient=gws-wiz-serp'

    btc_price = 0
    eth_price = 0
    doge_price = 0

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self, btc = btc_usd, eth = eth_usd, doge = doge_usd):

        self.btc_price = (self.get_price_cryp(btc))
        self.eth_price = (self.get_price_cryp(eth))
        self.doge_price = (self.get_price_cryp(doge))

    def get_price_cryp(self, url: str) -> str:
            
        self.link = url

        full_page = requests.get(self.link, headers=self.headers)

        soup_curr = BeautifulSoup(full_page.content, 'html.parser')

        convert_html = soup_curr.findAll("span", {"class": "pclqee"})

        res_currency = convert_html[0].text
        return res_currency

@bot.message_handler(commands = ['start'])
def start(msg, res = False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('USD/EUR/CNY')
    item2 = types.KeyboardButton('BTC/ETH/DOGE')
    item3 = types.KeyboardButton('Weather')
    markup.add(item1, item2, item3)
    bot.send_message(msg.chat.id, 'Добро пожаловать'.format(msg.from_user), reply_markup=markup)
    
@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text.strip() == 'USD/EUR/CNY':
        bot.send_message(message.chat.id, text = f'You choose USD/EUR/CNY. Please wait a minute.')
        c = Currency()
        bot.send_message(message.chat.id, text = f'USD: {c.usd_price} ₽\nEUR: {c.eur_price} ₽\nCNY: {c.cny_price} ₽')
    elif message.text.strip() == 'BTC/ETH/DOGE':
        bot.send_message(message.chat.id, text = 'You choose BTC/ETH/DOGE. Please wait a minute.')
        c = Cryptocurrency()
        bot.send_message(message.chat.id, text = f'BTC: {c.btc_price} $\nETH: {c.eth_price} $\nDOGE: {c.doge_price} $')
    elif message.text.strip() == 'Weather':
        bot.send_message(message.chat.id, text = 'You choose Weather')
        bot.send_message(message.chat.id, text = f'{weather().text}')
    else:
        bot.send_message(message.chat.id, text = 'Unknown request')
        
bot.polling(none_stop=True)