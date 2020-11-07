
# this file contains methods to call upon riot api 




#gets summoner name from input in GUI
def getMatches(summonerName){
    #accesses riot api and retrieves 20? most recent matches
    list matches
    #here get the matches and put them in list (or some other structure :))
    return matches
}


#calculate
#what should I be passing -- a list of most recent matches
def calcWinRate(matchesList):
    #take # of matches in match list, retrieve win/loss for each
    # to make it quick and dirty -- just have ints and increment as traverse list
    #if we want to do red side/blue side, maybe have a map or some other structure that ties match ID to info about it
    ##
    int wins, losses
    double winRate = wins/losses
    return winRate