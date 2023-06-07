#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import time
import pyperclip
from colorama import Fore, Style, init
import openai

init()

def main():
    parser = argparse.ArgumentParser(prog="ChatCMD 1.1", conflict_handler='resolve',
                                     epilog="REPO: https://github.com/antonioam82/ChatPy")
    parser.add_argument('-ap', '--api_key',required=True,type=str, help="Enter ChatGPT API KEY")
    parser.add_argument('-rl', '--role',type=str,default='user',choices=['user','assistant','system'],help='Role')
    parser.add_argument('-mt', '--max_tokens', type=int, default=2048, help="Enter max tokens")
    parser.add_argument('-eng', '--engine', type=str, default="gpt-3.5-turbo", help="Model to use")
    parser.add_argument('-con', '--content',type=str, required=True,help="Content")
    

    args = parser.parse_args()

if __name__ == '__main__':
    main()
