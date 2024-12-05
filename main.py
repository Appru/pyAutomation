from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import threading

print ("hello")

service = Service('C:\\Users\\Jem\\Desktop\\Udemy\\Python Automation\\chromedriver.exe')


def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(service=service, options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
    """extract only temp """
    output = float(text.split(": ")[1])
    return output


def main():
  driver = get_drvier()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  driver.find_element(by = "id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(3)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/h1[2]")
  clean_element = clean_text(element.text)
  print()
  
  now = time.strftime("%Y%m%d-%H%M%S")
  now2 = "./data/"+now+".txt"
  f = open(now2, "a")
  f.write(str(clean_element))
  f.close()
  driver.close()
  print(now2)
 


while(True):
  print (main())
  time.sleep(5)