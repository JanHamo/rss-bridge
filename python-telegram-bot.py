import feedparser
import time
from telegram import Bot

# إعداد الوصول إلى تلغرام
TELEGRAM_API_TOKEN = '6786850193:AAFibh97aX_pPdIJY_dP9ddUcjEc4mzWX6U'
CHANNEL_ID = 'https://t.me/DchartxxBot'

# إعداد تلغرام
bot = Bot(token=TELEGRAM_API_TOKEN)

# قائمة ثابتة من RSS Feeds لحسابات تويتر التي تتابعها
rss_feeds = {
    'GodsBurnt': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=GodsBurnt&format=Atom',
    'Kaosonx': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=Kaosonx&format=Atom',
    'IGGYAZALEA': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=IGGYAZALEA&format=Atom',
    'TheSolSaver': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=TheSolSaver&format=Atom',
    'tall_sol': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=tall_sol&format=Atom',
    'Koorahmeta': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=Koorahmeta&format=Atom',
    'Ace1000X': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=Ace1000X&format=Atom',
    'KingAnt777': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=KingAnt777&format=Atom',
    'cryptoxjen': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=cryptoxjen&format=Atom',
    'Caitlyn_Jenner': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=Caitlyn_Jenner&format=Atom',
    'morpheuswhale': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=morpheuswhale&format=Atom',
    'blknoiz06': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=blknoiz06&format=Atom',
    'barkmeta': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=barkmeta&format=Atom',
    'DaoKwonDo': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=DaoKwonDo&format=Atom',
    'matt_loeber': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=matt_loeber&format=Atom',
    'RadarHits': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=RadarHits&format=Atom',
    'SECGov': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=SECGov&format=Atom',
    'TTrades_edu': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=TTrades_edu&format=Atom',
    'Exaado': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=Exaado&format=Atom',
    'theMMXMtrader': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=theMMXMtrader&format=Atom',
    'Ashcryptoreal': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=Ashcryptoreal&format=Atom',
    'aldorra_mo72240': 'https://JanHamo.github.io/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=aldorra_mo72240&format=Atom',
}


# تخزين أحدث تغريدة مرئية لكل حساب لتجنب التكرار
latest_tweets = {username: None for username in rss_feeds.keys()}

# دالة لجلب التغريدات الجديدة من RSS
def fetch_new_tweets():
    for username, feed_url in rss_feeds.items():
        feed = feedparser.parse(feed_url)
        if feed.entries:
            latest_entry = feed.entries[0]
            if latest_entry.id != latest_tweets[username]:
                latest_tweets[username] = latest_entry.id
                message = f"New tweet from {username}: {latest_entry.title}\n{latest_entry.link}"
                bot.send_message(chat_id=CHANNEL_ID, text=message)

# الفحص الدوري كل 3 دقائق
while True:
    fetch_new_tweets()
    time.sleep(3 * 60)  # تحويل الدقائق إلى ثوانٍ
