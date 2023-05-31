import tweepy
import keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

client = tweepy.Client(consumer_key = keys.api_key,
                    consumer_secret = keys.api_secret,
                    access_token = keys.access_token,
                    access_token_secret = keys.access_token_secret)

s = Service('/Users/raymondtao/Downloads/chromedriver_mac_arm64/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://www.oddsshark.com/nba/odds")

names = driver.find_elements(By.CLASS_NAME, 'participant-name')
odds = driver.find_elements(By.CLASS_NAME, 'odds-moneyline')

moneyline = []
for i in odds:
    moneyline.append(i.text)
moneyline = [item for item in moneyline if item != '- -']
teams = []
for i in names:
    teams.append(i.text)


for i in range(0, len(teams), 2):
    team1 = teams[i]
    team2 = teams[i + 1]
    moneyline1 = moneyline[i]
    moneyline2 = moneyline[i + 1]

    response = client.create_tweet(text=f"{team1} vs. {team2}\nMoneyline: {moneyline1} {team1}, {moneyline2} {team2}")
