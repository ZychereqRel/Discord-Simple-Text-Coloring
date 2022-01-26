import clipboard
import os
import sys
from colorama import Fore, init


init(convert=True)

intro = f"""                                                                       
{Fore.CYAN}                                                                   _                   
{Fore.CYAN}                                                                  (_)              
{Fore.CYAN}                                          _ __ ___    __ _   __ _  _   ___  
{Fore.CYAN}                                         | '_ ` _ \  / _` | / _` || | / __| 
{Fore.CYAN}                                         | | | | | || (_| || (_| || || (__ 
{Fore.CYAN}                                         |_| |_| |_| \__,_| \__, ||_| \___|
{Fore.CYAN}                                                             __/ |                                           
{Fore.CYAN}                                                            |___/      
                                                        {Fore.WHITE}zyc{Fore.RED}her    {Fore.RESET}   
                                            
                                                [{Fore.RED}>{Fore.RESET}]{Fore.CYAN}1{Fore.RESET} color changer
                                                [{Fore.RED}>{Fore.RESET}]{Fore.CYAN}2{Fore.RESET} formatting list
                                               
                                            
"""
def changer():

    
    text = input("text:\n")
    formatting = input("formatting:\n")
    color = input("color:\n")
    
    gay = f"```ansi\n [{formatting};{color}m" + text + "\n```"
    clipboard.copy(gay)

    print('check your clipboard!')
    os.system('cls')
    startMenu()
    

    startMenu()
formatting = ["Formatting",F"{Fore.CYAN}0: Normal",F"{Fore.CYAN}1: Bold",F"{Fore.CYAN}4: Underline",f"{Fore.RESET} "]
colorList = ["Colors","30: Gray", F"{Fore.RED}31: Red", F"{Fore.GREEN}32: Green", F"{Fore.YELLOW}33: Yellow",F"{Fore.BLUE}34: Blue", F"{Fore.MAGENTA}35: Pink", F"{Fore.CYAN}36: Cyan", F"{Fore.WHITE}37: White", " ", F"{Fore.RED}Click Enter to exit"]
def list():
  for i in formatting:
      print(i)

  for i in colorList:
      print(i)

      

    
def startMenu():
    print(intro)
    print(f'[{Fore.RED}>{Fore.RESET}] Your choice', end=''); choice = str(input('  :  '))
    if choice == '1':
       os.system('cls')
       changer()
    if choice == '2':
        os.system('cls')
        list()
        input()
        os.system('cls')
        startMenu()
        
    


if __name__ == '__main__':
    startMenu()