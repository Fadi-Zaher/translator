from googletrans import Translator
from termcolor import colored

translator = Translator()
while True:
    print("1 - Hebrew to English \n2 - English to Hebrew\n:")
    choice = input()

    if choice == '1':
        print("word/sentence:")
        to_translate = input()
        if to_translate != "quit":
            result = translator.translate(to_translate, 'en', 'auto')
            print(colored(result.text, "green") + '\n')
            continue
        break
    elif choice == '2':
        print("word/sentence:")
        to_translate = input()
        if to_translate != "quit":
            result = translator.translate(to_translate, 'he', 'auto')
            print(colored(result.text, "green") + '\n')
            continue
        break
    else:
        print("please choose one of the options\n")
        continue
