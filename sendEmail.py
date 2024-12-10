import yagmail
import os

my_email = os.getenv('email')
my_password = os.getenv('password2')


receiver = "j.appru@gmail.com"

subject = "TEST"
contents = """

Hello you little ass

thanks

"""

yag = yagmail.SMTP(user = my_email, password = my_password)
yag.send(to = receiver, subject = subject, contents = contents)
print("email SENT")

