# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import yagmail
import os
import time
from datetime import datetime as dt

my_email = os.getenv('email')
my_password = os.getenv('password2')

sender = 'app7flask@gmail.com'
receiver = 'fbcmakfsd@emltmp.com'

subject = """
This is the subject!
"""
contents = """
Here is the content of the email! 
Hi!
"""
while True:
  now = dt.now()
  if now.hour == 13 and now.minute == 18:
    yag = yagmail.SMTP(user=my_email, password=my_password)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)