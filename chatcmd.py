#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openai
import time
import os
import sys
from colorama import Fore, init, Style
import argparse

init()

def main():
    parser = argparse.ArgumentParser(prog="ChatCMD",conflict_handler='resolve',
                                     epilog="REPO: https://github.com/antonioam82/ChatPy")
    parser.add_argument('-ap','--api_key',required=True,type=str,help="Enter ChatGPT API KEY")
    parser.add_argument('-mt','--max_tokens',type=int,default=2048,help="Enter max tokens")
    parser.add_argument('-eng','--engine',type=str,default="text-davinci-003",help="Model to use")

    args = parser.parse_args()

    try:
        openai.api_key = args.api_key
        model_lst = openai.Model.list()
        model_find = False
        for i in model_lst['data']:
            if i['id'] == args.engine:
                model_find = True
                break
        if model_find == False:
            parser.error(Fore.RED+Style.BRIGHT+f"BAD MODEL SELECTED: {args.engine} not valid"+Fore.RESET+Style.RESET_ALL)
    except Exception as e:
        parser.error(Fore.RED+Style.BRIGHT+str(e)+Fore.RESET+Style.RESET_ALL)
        
        

    chat(args)

def typewriter(message):
    print(Fore.GREEN)
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
    print(Fore.RESET)

def get_completion(args,p):
    try:
        completion = openai.Completion.create(engine=args.engine,
                                              prompt = p,
                                              max_tokens=args.max_tokens)
        return str(completion.choices[0].text)
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+str(e)+Fore.RESET+Style.RESET_ALL)
        

def save_response(r):
    try:
        with open("response.txt","w") as document:
            document.write(r)
        print(Fore.YELLOW+"Saved document as 'response.txt'."+Fore.RESET)
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+str(e)+Fore.RESET+Style.RESET_ALL)

def print_title():
    print(Fore.BLUE)
    print("                                       ____ _           _    ____ __  __ ____ ")
    print("                                      / ___| |__   __ _| |_ / ___|  \/  |  _ \ ")
    print("                                     | |   | '_ \ / _` | __| |   | |\/| | | | |")
    print("                                     | |___| | | | (_| | |_| |___| |  | | |_| |")
    print("                                      \____|_| |_|\__,_|\__|\____|_|  |_|____/ ")
    print("                                       C  O  M  P  U  T  E  R    T  A  L  K  S")
    print(Fore.RESET)
    

'''def set_api_key(val):
    try:
        openai.api_key = val
    except Exception as e:
        raise argparse.ArgumentTypeError(Fore.RED+Style.BRIGHT+str(e)+Fore.RESET+Style.RESET_ALL)'''

def chat(args):
    response = ""
    print_title()
    while True:
        prompt = input("\nPROMPT> ")

        if prompt == "END":
            break
        elif prompt == "PRINT":
            if response != "":
                save_response(response)
            else:
                print(Fore.RED+Style.BRIGHT+"No response to print"+Fore.RESET+Style.RESET_ALL)
        elif prompt == "":
            pass

        else:
            response = get_completion(args,prompt)
            typewriter(response)

if __name__=='__main__':
    main()

