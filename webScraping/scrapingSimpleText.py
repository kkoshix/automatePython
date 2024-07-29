# webdriver allows us to instruct the behavior of the web browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('C:\\Users\\Admin\\Desktop\\chrome\\chromedriver-win64\\chromedriver.exe')
def get_driver(url):
    #Set options to make browsing easier
    options = webdriver.ChromeOptions()
    #hide Chrome is being controlled by automated test software
    options.add_argument("disable-infobars") 
    # Start the browser maximized
    options.add_argument("start-maximized")

    options.add_argument("disable-dev-shm-usage")
    # Bypass OS security model
    options.add_argument("no-sandbox")
    # Remove the automation control message
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    # Avoid detection by setting the AutomationControlled blink feature to disabled
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver

def main(url):
    driver = get_driver(url)
    element = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div/div/div[1]/h2")
    #element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element

url = input("Paste your url: ") #try https://www.facebook.com/
res = main(url)
print(res,"\n",res.text)