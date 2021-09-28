import requests,json,time,threading,os,sys
import urllib.request, os, threading, time, random, sys
import colorama
from colorama import Fore, Style, init
#from requests_futures.sessions import FuturesSession
#from requests_futures import sessions
print (Fore.GREEN + "[11] Update")
print ("[22] Setup")
print ("[33] Spam SMS")
print ("[44] Exit")

verfly = input("Numbers :")
if verfly == '11':
	os.system("pkg update.py")
	
if verfly == '22':
	os.system("python net.py")
	
if verfly == '33':
	os.system("python verfly.py")
	
if verfly == '44':
	os.system("python exit.py")

