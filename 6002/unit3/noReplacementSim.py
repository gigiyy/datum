import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    def drawThreeFrom(L):
        ret = []
        for _ in range(3):
            idx = random.randrange(0, len(L))
            ball = L[idx]
            ret.append(ball)
            L.remove(ball)
        return ret

    sameColor = 0
    for _ in range(numTrials):
        balls = ["red"] * 3 + ["green"] * 3
        random.shuffle(balls)
        drawn = drawThreeFrom(balls)
        if drawn.count(drawn[0]) == 3:
            sameColor += 1
    return sameColor / numTrials

if __name__ == "__main__":
    print(noReplacementSimulation(100000))


