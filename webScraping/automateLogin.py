from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:\\Users\\Admin\\Desktop\\chrome\\chromedriver-win64\\chromedriver.exe')

def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("windows-size=1280x720")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url=url)
    return driver

def main(url, username, password):
    driver = get_driver(url)
    driver.find_element(by="id", value="id_username").send_keys(username)
    time.sleep(1.5)
    driver.find_element(by="id", value="id_password").send_keys(password + Keys.RETURN)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(5)

url = input("Paste URL: ") #https://automated.pythonanywhere.com/login
username = input("username: ") #automated
password = input("password: ") #automatedautomated
main(url, username, password)
