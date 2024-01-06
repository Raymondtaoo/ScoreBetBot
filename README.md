# ScoreBetBot


## Screenshots

<img src="https://github.com/Raymondtaoo/ScoreBetBot/assets/123979366/d34884c2-bac4-48e7-ad43-69272399f7d6" width="373" height="500"/>

## Overview

ScoreBetBot is a Python program designed to fetch information on bet lines and odds for NBA games and tweet them using the Twitter API. It utilizes the Selenium library to access a Chrome WebDriver, which allows it to scrape data from a specific website. This readme provides essential information for setting up and using ScoreBetBot.

## Prerequisites

Before running ScoreBetBot, you need to ensure you have the following:

1. **Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Tweepy API Keys**: Obtain API keys for Twitter by creating a developer account on the [Twitter Developer platform](https://developer.twitter.com/en/apps). You will need the following keys:

   - Consumer Key (API Key)
   - Consumer Secret (API Secret)
   - Access Token
   - Access Token Secret

3. **Selenium**: Install the Selenium library for Python using pip:

   ```bash
   pip install selenium
   ```
4. **Chrome WebDriver**: ScoreBetBot requires the Chrome WebDriver to control the Chrome browser. Download the appropriate version of Chrome WebDriver for your system from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/). Ensure that the WebDriver version matches your Chrome browser version. Place the WebDriver executable in a directory accessible by your Python environment.

## Configuration

1. **Twitter API Keys**: Open the `keys.py` file and replace the placeholders with your Twitter API keys.
```bash
api_key = "YOUR_CONSUMER_KEY"
api_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

2. **Chrome WebDriver Path**: Update the `Service` initialization line in your Python script with the correct path to the Chrome WebDriver executable.
```bash
s = Service('/path/to/chromedriver')
```
## Usage

1. Run the ScoreBetBot script to fetch NBA game odds and tweet them.
```bash
python scorebetbot.py
```

2. The script will scrape the team names and moneyline odds, and then create tweets for each game.

## Important Note

- **Web Scraping**: Keep in mind that web scraping may violate the terms of service of some websites. Ensure that you have the necessary permissions or rights to access and scrape data from the website you intend to use with ScoreBetBot.

## Disclaimer

ScoreBetBot is provided as-is, and the developers assume no liability for its usage. Use ScoreBetBot responsibly and in compliance with all applicable laws and regulations.
