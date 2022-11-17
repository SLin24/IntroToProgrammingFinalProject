# Sources
# https://www.codegrepper.com/code-examples/python/how+to+open+inspect+element+in+chrome+using+selenium
# https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder

from selenium import webdriver  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time  
import os
from time import sleep, strftime
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from Util import *



# Creating an instance webdriver
c = webdriver.ChromeOptions()
#incognito parameter passed
c.add_argument("--incognito")
#set chromodriver.exe path
c.add_argument("--start-maximized")
c.add_argument("--auto-open-devtools-for-tabs")
c.add_experimental_option("excludeSwitches", ["enable-automation"])
c.add_experimental_option('useAutomationExtension', False)

try:
    parPath = os.path.dirname(os.path.dirname(__file__))
    relPath = '\chromedriver.exe'
    fullPath = parPath + relPath

    driver = webdriver.Chrome(options=c, executable_path=fullPath)
    driver.get("https://www.mathsisfun.com/measure/mazes.html")


    # Mode works for Everything Except Roads 
    # hardButton = driver.find_element(By.XPATH, '//button[text()="Hard"]')
    # hardButton.click()

    # USER CHOOSES MODES (WORKS ON EVERYTHING EXCEPT ROADS)

    def get_download_path():
        """Returns the default downloads path for linux or windows"""
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser('~'), 'downloads')

    download_path = get_download_path()
    excelPath = download_path + '\MazeData.csv'
    # checking to make sure the excel file is downloaded
    while (not(os.path.exists(excelPath))):
        sleep(1)
        continue

    # give time for user to close inspect element window
    sleep(2)
    df = pd.read_csv(excelPath, header = None)

    w, h = df.shape[1], len(df)

    walls = [[0 for x in range(w)] for y in range(h)] 
    for i in range(h):
        for j in range(w):
            walls[i][j] = df.iloc[i, j]


    # actual maze calculating algorithm


    listMoves = getDirections(walls, w, h)

    translate = {1: Keys.ARROW_UP, 2: Keys.ARROW_DOWN, 3: Keys.ARROW_LEFT, 4: Keys.ARROW_RIGHT}
    actions = ActionChains(driver)
    for i in range(len(listMoves)):
        actions.send_keys(translate[listMoves[i]]).perform()
        sleep(0.05)

            
    sleep(3)
    driver.close()

    # delete file
    os.remove(excelPath)
except:
    # delete file
    os.remove(excelPath)