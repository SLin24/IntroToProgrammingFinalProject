from selenium import webdriver  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time  
from selenium.webdriver.common.action_chains import ActionChains
import os

# Creating an instance webdriver
c = webdriver.ChromeOptions()
#incognito parameter passed
c.add_argument("--incognito")
#set chromodriver.exe path
c.add_argument("--start-maximized")
c.add_experimental_option("excludeSwitches", ["enable-automation"])
c.add_experimental_option('useAutomationExtension', False)

parPath = os.path.dirname(os.path.dirname(__file__))
relPath = '\chromedriver.exe'
fullPath = parPath + relPath
mode = 3
names = {1: "#beginner", 2: "#intermediate", 3: "#expert"}
modeName = names.get(mode)
minSquaresRequired = 75

driver = webdriver.Chrome(options=c, executable_path=fullPath)
driver.get("https://minesweeperonline.com/" + modeName)

action = ActionChains(driver)


faceId = driver.find_element("id", "face")
getX = {1: 9, 2: 16, 3: 30}
getY = {1: 9, 2: 16, 3: 16}

dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]

x = getX.get(mode)
y = getY.get(mode)

midX = int(x//8)
midY = int(y//4)

numCnt = 26
border = 9

# maxS is limit for sum of length of all patterns
maxS = 300

# for click patterns, 1 for click, 2 for mine, 0 for nothing
oneTwoOnePattern = [
    [ 1,  2,  1],
    [-1, -1, -1]
]
# relative to bottom right corner with (a, b) being row, col
oneTwoOneClickPattern = [(0,-1)]
oneTwoOneFlagPattern = [(0, 0), (0, -2)]
# excluded mines are for values that cannot be empty
oneTwoOneMines = [(-2, -2), (-2, -1), (-2, 0)]



oneTwoTwoOnePattern = [
    [ 1,  2,  2,  1],
    [-1, -1, -1, -1]
]
oneTwoTwoOneClickPattern = [(0, 0), (0, -3)]
oneTwoTwoOneFlagPattern = [(0, -1), (0, -2)]
oneTwoTwoOneMines = [(-2, -3), (-2, -2), (-2, -1), (-2, 0)]



borderOnesPattern = [
    [1,  1],
    [-1, -1]
]
borderOnesClickPattern = [(0, 1)]
borderOnesFlagPattern = []
borderOnesMines = [(0, -2), (-1, -2), (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-1, 1)]




oneTwoPattern = [
    [1,  2],
    [-1, -1]
]
oneTwoClickPattern = []
oneTwoFlagPattern = [(0, 1)]
oneTwoMines = [(-1, -2), (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-1, 1)]





