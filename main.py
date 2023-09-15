import tweepy
import keys
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load credentials from a configuration file and initialize Twitter client
client = tweepy.Client(consumer_key = keys.api_key,
                    consumer_secret = keys.api_secret,
                    access_token = keys.access_token,
                    access_token_secret = keys.access_token_secret)
chrome_driver_path = keys.chrome_driver_path

# Check for missing credentials
if not all([consumer_key, consumer_secret, access_token, access_token_secret, chrome_driver_path]):
    logger.error("Missing Twitter API credentials or Chrome driver path.")
    exit(1)

# Initialize Chrome driver
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

def scrape_odds(url):
    driver.get(url)
    names = driver.find_elements(By.CLASS_NAME, 'participant-name')
    odds = driver.find_elements(By.CLASS_NAME, 'odds-moneyline')

    moneyline = [i.text for i in odds if i.text != '- -']
    teams = [i.text for i in names]

    return teams, moneyline

def tweet_odds(team1, team2, moneyline1, moneyline2):
    tweet_text = f"{team1} vs. {team2}\nMoneyline: {moneyline1} {team1}, {moneyline2} {team2}"
    client.create_tweet(text=tweet_text)
    logger.info(f"Tweeted: {tweet_text}")

if __name__ == "__main__":
    odds_url = "https://www.oddsshark.com/nba/odds"
    teams, moneyline = scrape_odds(odds_url)

    for i in range(0, len(teams), 2):
        team1 = teams[i]
        team2 = teams[i + 1]
        moneyline1 = moneyline[i]
        moneyline2 = moneyline[i + 1]

        tweet_odds(team1, team2, moneyline1, moneyline2)

    driver.quit()
    moneyline2 = moneyline[i + 1]

    response = client.create_tweet(text=f"{team1} vs. {team2}\nMoneyline: {moneyline1} {team1}, {moneyline2} {team2}")
