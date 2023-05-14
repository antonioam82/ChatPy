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
                                     epilog="REPO:")
    parser.add_argument('-ap','--api_key',required=True,type=set_api_key,help="Enter API KEY")
    parser.add_argument('-mt','--max_tokens',type=int,default=2048,help="Enter max tokens")
    parser.add_argument('-eng','--engine',type=str,default="text-davinci-003",help="Model to use")

    args = parser.parse_args()

    chat(args)

def set_api_key(val):
    try:
        openai.api_key = val
    except Exception as e:
        raise argparse.ArgumentTypeError(Fore.RED+Style.BRIGHT+str(e)+Fore.RESET+Style.RESET_ALL)

def chat(args):
    pass


if __name__=='__main__':
    main()
