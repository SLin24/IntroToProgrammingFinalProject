# Minesweeper Project



## Description

A program that assists users in solving Minesweeper

## Getting Started

### Dependencies

* Python (Latest)
* Selenium
* ChromeDriver (Latest)



### Installing

* make sure that if a new chromedriver.exe file is downloaded, move it to the folder in which you cloned the repository, but make sure it is not contained in either MazeProject or Minesweeper Project folders respectively.

### Executing program

* Simply run the code (main.py)
* It will open a window. During this time, please wait for around 10 seconds, and make sure to not alter the window (i.e. zooming, clicking, etc..., not including alt-tab or any other functions that change windows or modify other windows)
* The program will initialize for ~8 seconds
* The program will begin clicking tiles until it finds a "good" enough start (may take another 5-10 seconds)
* Watch the program run
* If the program stops inputting for more than 5 seconds, it will prompt the user to guess. (For clarification, "Awaiting User Input" will be printed in the terminal.) At these points in time, the user will be prompted to click a tile (only 1), and preferably next to a already discovered tile, to allow the program to continue solving.

## Help

Make sure ChromeDriver.exe is downloaded to the your current chrome version.
Details can be found here: https://chromedriver.chromium.org/downloads

If the program glitches, it is most likely due to the user's interference with the window (either during the wrong time for the guess while the program was still running, or when if the user performed some of the mentioned inputs above). Note that simply restarting the program will fix the issue.


## Authors

Samuel Lin
<br>
S.lin25@bcp.org

## Version History
Only 1 Version so far


## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
Sources are mentioned in the main.py file, but CP-algorithms was useful towards this project.
