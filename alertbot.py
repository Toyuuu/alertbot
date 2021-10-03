#Coded by Toyu#9922
#https://github.com/Toyuuu/alertbot

import selenium
from bs4 import BeautifulSoup
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

#CHANGE | Locations settings
item_name = "<product name>"
item_store = "<products store>"
location = "<webdriver location here>"
website = "<item website url>"
tag = "<text tag>"
class_ = "<text class>"
class_data = "<data inside of class>"
text = "<item text>"

#DONT CHANGE | Selenium Settings
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
browser = webdriver.Chrome(location, options=options)
ua = UserAgent()
while True:
    browser.delete_all_cookies()
    random = ua.random
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": ua.random})
    browser.get(website)
    html = browser.page_source
    
    soup = BeautifulSoup(html, "html.parser")
    button = soup.find_all(tag, {class_ : class_data})
    info = [span.get_text() for span in button]
    line = [item.strip() for item in info if str(item)]
    if text in line:
        print(f"{item_name in stock at {item_store}!")
        time.sleep(3600)
    else:
        print(f"{item_name} not in stock!")
	