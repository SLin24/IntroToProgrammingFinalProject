# https://www.geeksforgeeks.org/get_attribute-element-method-selenium-python/
# https://medium.com/analytics-vidhya/python-selenium-all-mouse-actions-using-actionchains-197530cf75df
# https://www.geeksforgeeks.org/python-find_element_by_id-method-in-selenium/
# https://www.tutorialspoint.com/how-to-perform-right-click-on-an-element-in-selenium-with-python
# https://cp-algorithms.com/string/aho_corasick.html#construction-of-an-automaton
# https://cp-algorithms.com/string/prefix-function.html
# https://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/
import time
from Constants import *
from Util import *


start()
periodicUpdate()
while(getCnt() < minSquaresRequired):
    reset()
    faceId.click()
    start()
    periodicUpdate()

run = 0
reachCnt = 0
while (not check()):
    print(run)
    try:
        basicMineFlag()
        basicMineClick()
        change = periodicUpdate()
        if (not change):
            reachCnt += 1
            print("REACHED")
            updateNeighborGrid()
            solvePattern(oneTwoOnePattern, oneTwoOneClickPattern, oneTwoOneFlagPattern, oneTwoOneMines)
            solvePattern(oneTwoTwoOnePattern, oneTwoTwoOneClickPattern, oneTwoTwoOneFlagPattern, oneTwoTwoOneMines)
            solvePattern(borderOnesPattern, borderOnesClickPattern, borderOnesFlagPattern, borderOnesMines)
            solvePattern(oneTwoPattern, oneTwoClickPattern, oneTwoFlagPattern, oneTwoMines)
            wait = periodicUpdate()
            if (not wait):
                while (not periodicUpdate()):
                    continue
            # if (not change):
            #     probabilityGuess()
    except:
        print("FAILED EXCEPT")
        time.sleep(100)
        print("FAILED")
        break
    run += 1
    # if (reachCnt >= 50):
    #     faceId.click()
    #     reset()
    #     reachCnt = 0




