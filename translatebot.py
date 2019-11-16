from googletrans import Translator
import random
import os

#Language codes for all the languages Google Translate Supports
language_codes = [
"af",   "ga",
"sq",	"it",
"ar",	"ja",
"az",	"kn",
"eu",	"ko",
"bn",	"la",
"eo",	"ru",
"et",	"sr",
"tl",	"sk",
"fi",	"sl",
"fr",	"es",
"gl",	"sw",
"ka",	"sv",
"de",	"ta",
"el",	"te",
"gu",	"th",
"ht",	"tr",
"iw",	"uk",
"hi",	"ur",
"hu",	"vi",
"is",	"cy",
"id",	"yi",
"be",	"lv",
"bg",	"lt",
"ca",	"mk",
"zh-CN",	"ms",
"zh-TW",	"mt",
"hr",	"no",
"cs",	"fa",
"da",	"pl",
"nl",	"pt",
"en",	"ro",
"eo",	"ru",
"et",	"sr",
"tl",	"sk",
"fi",	"sl",
"fr",	"es",
"gl",	"sw",
"ka",	"sv",
"de",	"ta",
"el",	"te",
"gu",	"th",
"ht",	"tr",
"iw",	"uk",
"hi",	"ur",
"hu",	"vi",
"is",	"cy",
"id",	"yi"]

def clear():
    #Clear the screen depending on the operating system
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_text():
    print("Enter the text you want to be converted (leave an empty line when you're done):")
    text = ""
    #Keep reading input until there is a blank line
    while True:
        new_input = input()
        if new_input != "":
            text += f"{new_input}\n"
        else:
            return text

def get_amount():
    while True:
        try:
            amount = int(input("How many times do you want it to be translated? "))
            return amount
        except ValueError:
            print("That is not a valid input!")

def translate(text, amount):
    #Create translator
    translator = Translator()

    for i in range(amount):
        clear()
        print(f"{i+1} of {amount} completed")
        #Pick a random language code to translate to
        text = translator.translate(text, dest=random.choice(language_codes)).text
    #Translate back to English for displaying at the end
    text = translator.translate(text, dest="en").text
    return text

def main():
    text = get_text()
    amount = get_amount()
    
    translated = translate(text, amount)
    clear()
    print(translated)
    input()

if __name__ == "__main__":
    main()
