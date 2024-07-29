from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:\\Users\\Admin\\Desktop\\chrome\\chromedriver-win64\\chromedriver.exe')

def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("window-size=1280x720")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(url=url)
    return driver

def auto(url):
    driver = get_driver(url)
    time.sleep(3)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return element

def cleanText(word):
    out = float(word.split(": ")[1])
    return out

url  = input("Paste URL: ") #https://automated.pythonanywhere.com/
res = auto(url)
print(cleanText(res.text))
    