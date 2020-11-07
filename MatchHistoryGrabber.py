import requests
import json
 
def main():
    apikey = 'RGAPI-9299b298-5fdd-4d1d-9962-0f5e9c00e5da'
    playerid = "Red Sly Fox"
    region = "na1"
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + playerid + "?api_key=" + apikey
    response = requests.get(URL)
    response = response.json()
    print(response)

def matches():
    apikey = 'RGAPI-9299b298-5fdd-4d1d-9962-0f5e9c00e5da'
    encryptedAccountID = 'accountid'
    URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/3A8CV3VkKPSlhVnee-WROo_4zVANB-ka34KMa2UZpTTR5fY?queue=420&api_key=RGAPI-9299b298-5fdd-4d1d-9962-0f5e9c00e5da"
    queue = 420
    endindex = 20
    response = requests.get(URL)
    response = response.json()
    return (response)
###
#def matchhistory(matches):
#    matchhistory = json.loads(matches)
#    wins = {}
#    for (match in matchhistory):
#        wins[matchhistory[matchid]]= #the win loss variable
###
if __name__ == '__main__':
    main()
    ms = matches()
    #matchhistory(ms)
 
