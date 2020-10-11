import os.path
from typing import List


# Create class to use functions in main.py
class Scenreader:

    # Filter through full cache by checking for ;824270|;824270|; which proceeds each scenario
    # Then take substring between last and first ; and add it as scenario
    # startindex and endindex check that u dont reiterate infinitely, by starting the next search at the end of the last
    def createscenlist(self, cache):
        scenarios: List[str] = []
        if not os.path.exists('scenarios.txt'):
            startindex = 0
            while cache.find(";824270|;824270|;", startindex) != -1:
                lowest = cache.find(";824270|;824270|;", startindex)
                startindex = lowest + len(";824270|;824270|;")
                endindex = int(cache.find("|", startindex))
                tempscen = str(cache[int(startindex): endindex])
                scenarios.append(tempscen)
            # Write all scenarios into a .txt, if it does not exist yet
            with open('scenarios.txt', 'w') as f:
                for item in scenarios:
                    f.write("%s\n" % item)
            f.close()
        else:
            f = open('scenarios.txt', "r")
            text = f.read()
            scenarios = text.splitlines()
            f.close()
        return scenarios

    # Write the path the user input into the path.txt file in the application folder
    def createpath(self, path):
        f = open("path.txt", "w")
        f.write(path)
        f.close()
        return path

    # Check if path.txt is there, if not call createpath and create it
    def getpath(self):
        pather = os.path
        if pather.exists('path.txt'):  # Check if the file exists
            f = open("path.txt", "r")  # If yes save the path in the file to scenariopath
            scenariopath = f.read()
            f.close()
            return scenariopath
        else:
            #  If it doesnt exist ask the user to input it then call createpath
            userinput = input(
                "Input the path to your SteamWorkshop.cache, in most cases it is: \n C:\Program Files ("
                "x86)\Steam\steamapps\common\FPSAimTrainer\FPSAimTrainer\Saved\SaveGames\SteamWorkshop.cache \n")
            assert os.path.exists(userinput), "Could not find the file, please restart the program"  # Check if path
            # exists, error if it does not
            return self.createpath(self, userinput)

    # Open the cache with the specified path, get path from the path.txt, return scenarios
    def opencache(self, path):
        f = open(path, "r")
        scenariosunedited = str(f.read())
        return scenariosunedited
