#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import time
from colorama import Fore, init
import openai

init()

def setup_openai(api_key, engine):
    openai.api_key = api_key
    model_lst = openai.Model.list()
    if engine not in [i['id'] for i in model_lst['data']]:
        raise ValueError(Fore.RED + f"BAD MODEL SELECTED: {engine} not valid" + Fore.RESET)
    return engine

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
        print(Fore.RED + str(e) + Fore.RESET)

def save_response(response):
    try:
        with open("response.txt", "w") as document:
            document.write(response)
        print(Fore.YELLOW + "Saved document as 'response.txt'." + Fore.RESET)
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

def chat(api_key, engine, max_tokens):
    response = ""
    print_title()
    while True:
        prompt = input("\nPROMPT> ")

        if prompt == "END":
            break
        elif prompt == "PRINT":
            if response:
                save_response(response)
            else:
                print(Fore.RED + "No response to print" + Fore.RESET)
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
        parser.error(Fore.RED + str(e) + Fore.RESET)

    chat(args.api_key, engine, args.max_tokens)

if __name__ == '__main__':
    main()

