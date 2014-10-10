"""
URL: http://geekswipe.net/2014/10/code-python-twitter-bot-in-ten-minutes/
Author: Karthikeyan KC
Name: Funzoned Twitter Bot
Description: A Twitter bot that tweets one liners every fifteen minutes.
Comment: This bot is created for learning purposes and is full of 'novice' bugs. It might evolve soon. The process runs on my laptop from a terminal and it will be on and off at times.
Twitter: http://twitter.com/funzoned
Bitbucket: https://bitbucket.org/karthikeyankc/funzoned-twitter-bot/src/

"""

from twython import Twython, TwythonError
import time

APP_KEY = 'YOUR KEY'
APP_SECRET = 'YOUR SECRET'
OAUTH_TOKEN = 'YOUR TOKEN'
OAUTH_TOKEN_SECRET = 'YOUR SECRET TOKEN'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	with open('liners.txt', 'r+') as tweetfile:
		buff = tweetfile.readlines()

	for line in buff[:]:
		line = line.strip(r'\n') #Strips any empty line
		if len(line)<=140 and len(line)>0:
			print ("Tweeting...")
			twitter.update_status(status=line)
			with open ('liners.txt', 'w') as tweetfile:
				buff.remove(line) #Removes the tweeted line
				tweetfile.writelines(buff)
			time.sleep(900)
		else:
			with open ('liners.txt', 'w') as tweetfile:
				buff.remove(line) #Removes the line that has more than 140 characters
				tweetfile.writelines(buff)
			print ("Skipped line - Char length violation")
			continue
	print ("No more lines to tweet...") #When you see this... Well :) Go find some new tweets...


except TwythonError as e:
	print (e)