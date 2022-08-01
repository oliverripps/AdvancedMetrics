#Possessions
    #Estimates number of possessions a team has in a game/season;
    #Substitute Opponents' totals to get their number of possessions (OppPoss)
def possessions(FGA,FTA,ORB,TOV):
    return .5 * (FGA + .475 * FTA - ORB + TOV)

#Offensive and Defensive Ratings
    #Adjusts a team's scoring offense and defense for their pace of play, allows you to better compare a team like Wisconsin to a team like Duke
def OR(TmPoss,OppPoss,Pts):
    return 100 / (TmPoss + OppPoss) * Pts

def DR(TmPoss,OppPoss,OppPts):
    return 100 / (TmPoss + OppPoss) * OppPts

#Effective Field Goal Percentage
    #Adjusts a player's or team's FG% for the fact that a 3 pointer is worth 1.5 times a standard FG
def EFG(FG, 3P, FGA):
    return (FG + .5 * 3P) / FGA


#True Shooting Percentage#
    #Adjusts standard FG% to include their FT%, encompasses all ways to score (my preferred shooting % stat)
def TS(PTS,FGA,FTA):
    return PTS / (2 * (FGA + .475 * FTA))


#Free Throw Rate
    #A measure of both how often a player/team gets to the line, as well as how often they make their free throws
def FTR(FT,FGA):
    return FT / FGA

##def team(FGA, FTA, ORB, TOV, TmPoss, OppPoss,  Pts, OppPts, FG, 3P,):
##    print("Offensive Rating
##Offensive Rebounding Percentage (ORB%) = ORB / MP / (TmORB + OppDRB) * TmMP / 5
##Defensive Rebounding Percentage (DRB%) = DRB / MP / (TmDRB + OppORB) * TmMP / 5
##Total Rebounding Percentage (TRB%) = TRB / MP / (TmTRB + OppTRB) * TmMP / 5
##Measures the percentage of the available rebounds a player grabs at the offensive and defensive ends of the floor while he is in the game. TRB% measures the total rebounds he grabs of those available while he is in the game.
##
##Hollinger Assist Ratio (hAST%) = AST / (FGA + .475 * FTA + AST + TOV)
##Think of Carmelo Anthony for this statistic, it is a "ball stopper" stat. This divides the number of assists a player has by the number of offensive possessions that end in that player's hands.
##
##Pomeroy Assist Ratio (pAST%) = AST / (((MP / (TmMP / 5)) * TmFG ) - FG)
##The percentage of teammate baskets a player assisted on while he was on the court - my preferred Assists statistic
##
##Assists per Team Possession (AST/p%) = AST / ((MP / (TmMP / 5)) * TmPoss)
##Adjusts pAST% to account for pace of play; penalizes player for teammate mistakes (TOV, missed FGA)
##
##Steal Percentage (STL%) = STL / ((MP / (TmMP / 5)) * OppPoss)
##Percent of opponent possessions in which a player gets a steal
##
##Block Percentage (BLK%) = BLK / ((MP / (TmMP / 5 )) * (OppFGA - Opp3PA))
##Percent of opponents' "blockable" shots that the player blocks (removes 3 point shots, as these are generally not "blockable", somewhat arbitrary since you see these blocked and a mid range jump shot is just as unlikely to be blocked, yet is included in the sample)
##
# Turnover Percentage (TOV%) = TOV / (FGA + .475*FTA + AST + TOV)
# Percent of a player's possessions that ends in turnovers, essentially the same as the hAST% equation, but for turnovers rather than assists

def main(PTS,)