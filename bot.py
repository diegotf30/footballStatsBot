import tweepy
import time
from footballData import *
from secrets import *

##############################################################################
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#API instance
api = tweepy.API(auth)

##############################################################################

#Current supported teams by the bot
supportedTeams = ['Tigres']

#Current supported leagues by the bot
supportedLeagues = ['ligaMx']


#Post weekly the supported teams next match
def postNextMatches():
	#List for avoiding the repetition of a match
	secondaryTeams = []
	for league in supportedLeagues:
		for team in supportedTeams:
			if (time.localtime().tm_wday == 1 and data['leagues'][league]['teams'][team]['nextMatch']['status'] == 'home'):

				api.update_status('{} plays against {} on {} at {}'.format(team.capitalize(), 
					data['leagues'][league]['teams'][team]['nextMatch']['against'], 
					data['leagues'][league]['teams'][team]['nextMatch']['date'], 
					data['leagues'][league]['teams'][team]['nextMatch']['stadium']))

				secondaryTeams.append(teams[team]['nextMatch']['against'])




###############################################################################
#Main
postNextMatches()
print(data['leagues']['ligaMx']['teams'][0])











		






