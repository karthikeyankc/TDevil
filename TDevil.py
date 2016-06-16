from twython import Twython, TwythonError
import time
import sys

APP_KEY = 'YOUR KEY'
APP_SECRET = 'YOUR SECRET'
OAUTH_TOKEN = 'YOUR TOKEN'
OAUTH_TOKEN_SECRET = 'YOUR SECRET TOKEN'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def countdown(t): # in seconds
    for i in range(t,0,-1):
        print 'Tweeting again in %d seconds\r' % i,
        sys.stdout.flush()
        time.sleep(1)

try:
	with open('liners.txt', 'r+') as tweetfile:
		buff = tweetfile.readlines()

	for line in buff[:]:
		line = line.strip(r'\n') #Strips any empty line.
		if len(line)<=140 and len(line)>0:
			print ("Tweeting...")
			twitter.update_status(status=line)
			with open ('liners_tweeted_and_skipped.txt', 'a') as file:
				file.writelines(line) #Adds the line that has been tweeted.
			with open ('liners.txt', 'w') as tweetfile:
				buff.remove(line) #Removes the tweeted line from buffer.
				tweetfile.writelines(buff) #Writes buff to lines.txt.
			countdown(450)
			print
		else:
			with open ('liners_tweeted_and_skipped.txt', 'a') as file:
				file.writelines(line) #Adds the line that has been skipped.
			with open ('liners.txt', 'w') as tweetfile:
				buff.remove(line) #Removes the line that has more than 140 characters.
				tweetfile.writelines(buff) #Writes buff to lines.txt.
			print ("Skipped line - Char length violation")
			continue
	print ("No more lines to tweet...") #When you see this... Well, Go find some new tweets...


except TwythonError as e:
	print (e)