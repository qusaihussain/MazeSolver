'''
Created on Sep 27, 2016

@author: QusaiHussain
'''
import urllib
import urllib2
import json

    
def solvingAlg(mainMaze, x, y):
    if (x==endX and y==endY):
        return True
    elif mainMaze[x][y] == True:
        return False
    elif mainMaze[x][y] == 'visited':
        return False
    

    mainMaze[x][y] = 'visited'
    
    if (solvingAlg(mainMaze, x+1, y) and len(mainMaze)-1 > x) or (solvingAlg(mainMaze, x-1, y) and x > 0) or (solvingAlg(mainMaze, x, y+1) and len(mainMaze)-1 > y) or (solvingAlg(mainMaze, x, y-1) and y > 0):
        return True
    
    global mazeList
    mazeList = mainMaze
    
    return False

def mazeListPrinter(mainMaze, x,y):
    solvingAlg(mainMaze, x,y)
    mazeListUpdated = mazeList
    
    for i in range(len(mazeListUpdated)):
        newline = ""
        for k in range(len(mazeListUpdated)):
            if (i==startX and k==startY):
                newline += "|" + "s"
            elif (i==endX and k==endY):
                newline += "|" + "f"
            elif (mazeListUpdated[i][k] == True):
                newline += "|" + u'\u2588'
            elif (mazeListUpdated[i][k] == False):
                newline += "|" + "_"
            elif (mazeListUpdated[i][k] == 'visited'):
                newline += "|" + "*"
        print newline
    
    
if __name__ == '__main__':
    url = "https://s3-us-west-1.amazonaws.com/circleup-challenge/maze.json"
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    jsondata = json.load(f)
    
    maze = jsondata['maze']
    startX = jsondata['start']['x']
    startY = jsondata['start']['y']
    endX = jsondata['end']['x']
    endY = jsondata['end']['y']

    mazeListPrinter(maze,startX,startY)
    
    
    
    
    