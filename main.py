import tweepy
import keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service('/Users/raymondtao/Downloads/chromedriver_mac_arm64/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://www.oddsshark.com/nba/odds")

names = driver.find_elements(By.CLASS_NAME, 'participant-name')

for e in names:
    print(e.text)

'''
client = tweepy.Client(consumer_key = keys.api_key,
                    consumer_secret = keys.api_secret,
                    access_token = keys.access_token,
                    access_token_secret = keys.access_token_secret)

response = client.create_tweet(text='hello world')
'''
