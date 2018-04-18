import tweepy
import json
from secrets import *

def postNextMatches():
    "Posts every team's next match"
    for league in jsonLeague:
        for team in jsonTeams:
            next_match = jsonTeams[team]['nextMatch']  # Helper
            if next_match['status'] is 'home':
                opponent = next_match['against']
                day = next_match['date']
                place = next_match['stadium']

                tweet_text = f'{team.capitalize()} plays against {opponent} on {day} at {place}'
                api.update_status(text=tweet_text)


# File is executed once per week by Heroku Scheduler
if __name__ == '__main__':
    # Constructs Twitter API instance
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    # Import Team Info.
    with open('teamData.json') as teams:
        jsonTeams = json.load(teams)

    # Import League Info.
    with open('leagueData.json') as leagues:
        jsonLeague = json.load(leagues)

    postNextMatches()
