from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import threading
import yagmail
import os

print ("Starting")

service = Service('chromedriver.exe')
def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument('--headless=new')
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(service=service, options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver



def findPrice():
    driver = get_drvier()
    time.sleep(3)
    price = driver.find_element(By.XPATH, value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
    price_text = price.text
    remove_percent = price_text.replace("%","")
    print("CURRENT STOCK PRICE " +remove_percent)
    
    return remove_percent

def send_email():
  my_email = os.getenv('email')
  my_password = os.getenv('password2')
  receiver = "j.appru@gmail.com"
  contents = """
  DEAR CEO,
  YOUR STOCK PRICE IS DOWN BELOW -0.10%.

  RESTART THE PYTHON SCRIPT AT ONCE

  PLEASE ACT NOW
  """
  yag = yagmail.SMTP(user = my_email, password = my_password)
  yag.send(to = receiver, subject = "STOCK PRICE DOWN", contents = contents)
  print("email sent")
  

while True:
  #print("test")
  stock_num = float(findPrice())
  #dummy_price = -0.12
  if stock_num > -0.1:
    print("we are all good!")
  if stock_num <= -0.1:
    send_email()
    
  time.sleep(10)




