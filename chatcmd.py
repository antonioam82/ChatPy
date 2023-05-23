#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import time
import pyperclip
from colorama import Fore, Style, init
import openai

init()

def setup_openai(api_key, engine):
    openai.api_key = api_key
    model_lst = openai.Model.list()
    if engine not in [i['id'] for i in model_lst['data']]:
        raise ValueError(Fore.RED + Style.BRIGHT +f"BAD MODEL SELECTED: {engine} not valid" + Fore.RESET + Style.RESET_ALL)
    return engine

def copy(response):
    try:
        pyperclip.copy(response)
        print(Fore.YELLOW +"COPIED TO CLIPBOARD" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + str(e) + Fore.RESET + Style.RESET_ALL)

def typewriter(message):
    print(Fore.GREEN)
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print(Fore.RESET)

def get_completion(engine, prompt, max_tokens):
    try:
        completion = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=max_tokens)
        return str(completion.choices[0].text)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + str(e) + Fore.RESET + Style.RESET_ALL)

def commands():
    print(Fore.YELLOW)
    print("                           --------------------------COMMAND LIST--------------------------")
    print("                           COPY                                          copy last response")
    print("                           PRINT <file name>                        save response in a file")
    print("                           HELP                                            see command list")
    print("                           END                                                 exit program")
    print("                           <prompt>                               make question to the chat")
    print("                           ----------------------------------------------------------------"+Fore.RESET)

def save_response(file,response):
    try:
        with open(file, "w") as document:
            document.write(response.split('\n',1)[1])
        print(Fore.YELLOW + f"Saved document as '{file}'." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + str(e) + Fore.RESET)

def print_title():
    print(Fore.BLUE)
    print("                                       ____ _           _    ____ __  __ ____ ")
    print("                                      / ___| |__   __ _| |_ / ___|  \/  |  _ \ ")
    print("                                     | |   | '_ \ / _` | __| |   | |\/| | | | |")
    print("                                     | |___| | | | (_| | |_| |___| |  | | |_| |")
    print("                                      \____|_| |_|\__,_|\__|\____|_|  |_|____/ ")
    print("                                       C  O  M  P  U  T  E  R    T  A  L  K  S")
    print(Fore.RESET)
    print("                                           Type 'HELP' to see command list")

def chat(api_key, engine, max_tokens):
    response = ""
    print_title()

    while True:

        prompt = input("\nPROMPT> ")

        if prompt == "END":
            break
        elif prompt == "COPY":
            if response:
                copy(response)
            else:
                print(Fore.RED + Style.BRIGHT + "No response to copy" + Fore.RESET + Style.RESET_ALL)
        elif prompt[0:5] == "PRINT":
            if response:
                save_response(prompt[6:len(prompt)],response)
            else:
                print(Fore.RED + Style.BRIGHT + "No response to print" + Fore.RESET + Style.RESET_ALL)
        elif prompt == "HELP":
            commands()
        elif prompt == "":
            pass
        else:
            response = get_completion(engine, prompt, max_tokens)
            typewriter(response)

def main():
    parser = argparse.ArgumentParser(prog="ChatCMD", conflict_handler='resolve',
                                     epilog="REPO: https://github.com/antonioam82/ChatPy")
    parser.add_argument('-ap', '--api_key', required=True, type=str, help="Enter ChatGPT API KEY")
    parser.add_argument('-mt', '--max_tokens', type=int, default=2048, help="Enter max tokens")
    parser.add_argument('-eng', '--engine', type=str, default="text-davinci-003", help="Model to use")

    args = parser.parse_args()

    try:
        engine = setup_openai(args.api_key, args.engine)
    except Exception as e:
        parser.error(Fore.RED + Style.BRIGHT + str(e) + Fore.RESET + Style.RESET_ALL)

    chat(args.api_key, engine, args.max_tokens)

if __name__ == '__main__':
    main()


