# 🎬Amazon Prime Video Scraper
![GitHub](https://img.shields.io/github/license/srang992/Amazon-Prime-Video-Scraper) 
![GitHub last commit](https://img.shields.io/github/last-commit/srang992/Amazon-Prime-Video-Scraper)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/srang992/Amazon-Prime-Video-Scraper)
![GitHub file size in bytes](https://img.shields.io/github/size/srang992/Amazon-Prime-Video-Scraper/chromedriver.exe?color=green&label=chromedriver%20size)

## 📚About
This repository contains the Python script by which you can scrape the Movies and Tv shows according to their categories.

## 🤔How to Use?

You have to clone this repository. Then, install the dependencies by running the below command in the terminal of the IDE.
```bash
pip install -r requirements.txt
```
After that, open the python script named AmazonPrimeSpider.py and change the values mentioned below.
### 👉Inside the Class
- **name:** Which name do you want to give to your bot. If you like the default name, keep it.
- **custom_settings:** it is a python dictionary containing all the important settings you should keep in mind while using the spider. You can add other settings if you want. The existing settings and why they are used are listed below.

| **Keys** | **Description** |
|---|---|
| USER_AGENT | If you want to scrape large amount of data, this is the important setting for you. It will help you to mask your bot as a web browser. |
| ROBOTSTXT_OBEY | This setting tells the bot if he has to obey the robots.txt file or not. Most of the websites maintain this text file which contains all the rules for accessing the websites. |
| DOWNLOAD_DELAY | Using this, bot can figure out how much he has to wait before he scrape the data. |
| AUTOTHROTTLE_ENABLED | this extension helps the bot to wait if there is any problem with the website or the network. |
| AUTOTHROTTLE_START_DELAY | The initial download delay if there is any issue in the website. |
| AUTOTHROTTLE_MAX_DELAY | The maximum download delay to be set in case of high latencies |
| AUTOTHROTTLE_TARGET_CONCURRENCY | The average number of requests Scrapy should be sending in parallel to each remote server. |

### 👉Inside _start_requests_ method
Here you have to change the _url_ variable. If you want to scrape movies of multiple categories, replace the code of this method with the code below.
```python
# Create a list of urls
urls = ["https//www.example1.com", 
        "https//www.example2.com"] 

# open urls using for loop
for url in urls:
    yield scrapy.Request(url=url, callback=self.after_fetch)
```
### 👉Inside _after_fetch_ method
Here you have to change the path of the chromedriver. If the location of the chromedriver is in the same directory as your python script, you don't have to modify the path. Just leave it as it is. If not you vave to modify it.
```python
# If the location of the chromedriver is in the
# same directory as your python script, leave it as it is.
driver = webdriver.Chrome('chromedriver.exe')

# otherwise, change the path
driver = webdriver.Chrome('Enter Your Path for chromedriver')
```
You can download chromedriver from [here]("https://chromedriver.storage.googleapis.com/index.html?path=111.0.5563.64/").

## Deployment

If you are done with this. Run the command below in the terminal of the ide.

```bash
scrapy runspider AmazonPrimeSpider.py -o MoviesAmazon.json
```
Make sure to remove the contents of _MoviesAmazon.json_ file before running the command.

## Load Scraped Data
If you want to load the scraped data in Jupyter Notebook, you have to run the below code.
```python
import pandas as pd
data = pd.read_json("ActionComedyMoviesIMDB2.json")
```

## Authors

- [Subhradeep Rang](https://www.github.com/srang992)

