

#Effective Field Goal Percentage
    #Adjusts a player's or team's FG% for the fact that a 3 pointer is worth 1.5 times a standard FG
def EFG(FG, TFG, FGA):
    return (FG + .5 * TFG) / FGA


#True Shooting Percentage#
    #Adjusts standard FG% to include their FT%, encompasses all ways to score (my preferred shooting % stat)
def TS(PTS,FGA,FTA):
    if(2 * (FGA + .475 * FTA)) == 0:
        return 0.0
    return PTS / (2 * (FGA + .475 * FTA))


#Free Throw Rate
    #A measure of both how often a player/team gets to the line, as well as how often they make their free throws
def FTR(FT,FGA):
    return FT / FGA

##Hollinger Assist Ratio (hAST%) = AST / (FGA + .475 * FTA + AST + TOV)

def hasr(AST,FGA,FTA,TOV):
    return AST/ (FGA + 0.475*FTA + AST + TOV)


# Turnover Percentage (TOV%) = TOV / (FGA + .475*FTA + AST + TOV)
# Percent of a player's possessions that ends in turnovers, essentially the same as the hAST% equation, but for turnovers rather than assists

def tov(TOV, FGA, FTA, AST):
    return TOV / (FGA + 0.475*FTA + AST + TOV)

def main(PTS,FG,FGA,TFG,TFGA,FT,FTA,AST,TOV):
    Effective_Field_Goal_Percentage = EFG(FG,TFG,FGA)
    return(Effective_Field_Goal_Percentage)