import requests

def main():
    apikey = 'RGAPI-740dbc19-ef19-4c6f-bcc4-6e8f0a3fb8d2'
    playerid = "HermesTheCat"
    region = "na1"
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + playerid + "?api_key=" + apikey
    response = requests.get(URL)
    response = response.json()
    encryptedAccountID = response['accountId']
    print(response)
    wins = matches(encryptedAccountID)
    print(wins/20)

def matches(accountId):
    apikey = 'RGAPI-740dbc19-ef19-4c6f-bcc4-6e8f0a3fb8d2'
    URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?queue=420&endindex=11&beginindex=1&api_key=" + apikey
    response = requests.get(URL)
    response = response.json()
    print(response)
    matchid = []
    matches = response['matches']
    x = 0
    while x < 21:
        matchid.append([matches[x]['gameId'], matches[x]['champion']])
        x += 1
    print(matchid)
    return winrate(matchid)

def winrate(matchid):
    apikey = 'RGAPI-740dbc19-ef19-4c6f-bcc4-6e8f0a3fb8d2'
    wins = 0
    for match in matchid:
        URL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(match[0]) + "?api_key=" + apikey
        response = requests.get(URL)
        response = response.json()
        print(response)
        try:
            participants = response['participants']
            for x in participants:
                if x['championId'] == match[1]:
                    if x['stats']['win']:
                        wins += 1 
                else:
                    print(match[1])
        except:
            print('oops sorry you were too monkey to analyze')

    return wins

##define if then statements for if winrate >, <, = .5
##make apikey an input


if __name__ == '__main__':
    main()



 
