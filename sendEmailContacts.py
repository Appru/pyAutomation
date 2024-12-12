import yagmail
import os
import pandas

my_email = os.getenv('email')
my_password = os.getenv('password2')

contents = """

Hello you little so and so

thanks

"""
yag = yagmail.SMTP(user = "j.appru@gmail.com", password = "mltrnlxegylemnjr")
df = pandas.read_csv("data/contacts.csv")
print(df)
for index, row in df.iterrows():
    yag.send(to = row['email'], subject = "hello! "+row["name"], contents = contents)
    print("email SENT")

#mltrnlxegylemnjr