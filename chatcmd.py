#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openai
import time
import os
import sys
#import pyfiglet
from colorama import Fore, init, Style
import argparse

init()

def main():
    parser = argparse.ArgumentParser(prog="ChatCMD",conflict_handler='resolve',
                                     epilog="REPO:")
    parser.add_argument('-ap','--api_key',required=True,type=set_api_key,help="Enter API KEY")
    parser.add_argument('-mt','--max_tokens',type=int,default=2048,help="Enter max tokens")
    parser.add_argument('-eng','--engine',type=str,default="text-davinci-003",help="Model to use")

    args = parser.parse_args()

    chat(args)

def typewriter(message):
    print(Fore.GREEN)
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
    print(Fore.RESET)

def print_title():
    print(Fore.YELLOW)
    print("                                  ____ _           _    ____ __  __ ____ ")
    print("                                 / ___| |__   __ _| |_ / ___|  \/  |  _ \ ")
    print("                                | |   | '_ \ / _` | __| |   | |\/| | | | |")
    print("                                | |___| | | | (_| | |_| |___| |  | | |_| |")
    print("                                 \____|_| |_|\__,_|\__|\____|_|  |_|____/ ")
    print("                                  C  O  M  P  U  T  E  R    T  A  L  K  S")
    print(Fore.RESET)
    

def set_api_key(val):
    try:
        openai.api_key = val
    except Exception as e:
        raise argparse.ArgumentTypeError(Fore.RED+Style.BRIGHT+str(e)+Fore.RESET+Style.RESET_ALL)

def chat(args):
    #print(Fore.YELLOW+pyfiglet.figlet_format("ChatCMD",justify="center")+Fore.RESET)
    print_title()
    while True:
        prompt = input("\nPROMPT> ")

        if prompt == "END":
            break
        
        completion = openai.Completion.create(engine=args.engine,
                                              prompt = prompt,
                                              max_tokens=args.max_tokens)
        response = str(completion.choices[0].text)
        typewriter(response)

if __name__=='__main__':
    main()

