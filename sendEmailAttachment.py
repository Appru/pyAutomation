import yagmail
import os

my_email = os.getenv('email')
my_password = os.getenv('password2')
receiver = "fayobo1976@bawsny.com"

subject = "TEST123"
contents = ["""

Hello you little so and so

thanks

""",'data/new-new-new-data.csv']

yag = yagmail.SMTP(user = my_email, password = my_password)
yag.send(to = receiver, subject = subject, contents = contents)
print("email SENT")

