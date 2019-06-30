from graphics import *
def getInputs():
    size = 0
    colour= ["","",""]
    validColours = ["red","green","blue","magneta","orange","pink"]
    validSizes = [5,7,9]
    
    #Loop to check size is valid
    while size not in validSizes:
        size = eval(input("Input the size of the patchwork? 5 7 or 9:" ))
        if size not in validSizes:
            print("That isn't a valid answer")
    print("Next is colour, the valid colours are red, green,blue,magneta,orange and pink")
    
    #Loop to check colours are valid
    while colour[0] not in validColours:
        colour[0] = input("Input the first colour: ")
        if colour[0] not in validColours: 
            print("invalid colour")
    #Loop to check 2nd colour is valid
    while colour[1] not in validColours or colour[1] == colour[0]:
        colour[1] = input("Input the second colour: ")
        if colour[1]  not in validColours:
            print("invalid colour")
        if colour[1] == colour[0]:
            print("Choose another colour")
    #Loop to check 3rd colour is valid
    while colour[2] not in validColours or colour[2] == colour[1] or colour[2] == colour[0]:
        colour[2] = input("Input the third colour: ")
        if colour[2] not in validColours:
            print("invalid colour")
        if colour[2] == colour[1] or colour[2] == colour[0]:
            print("choose another colour")
    return size,colour[0],colour[1],colour[2]
    
def main():
    startx = 0 
    starty = 0
    size,colour1,colour2,colour3 = getInputs()
    drawPatchTwo(size,colour1)
    
def drawPatchTwo(size,colour1,colour2,colour3):
    d = 0 #Used in loop
    maxSize = size*100 - 100 #This variable is the absolute bottom, the bottom of the window varies on size of it
    comP= 20 #This ads to the vars to help make the pattern
    win = GraphWin("894039",100*size,100*size)
    startx = [0,200,400,200,200,400,400,400,400,400]
    starty = [maxSize,maxSize,maxSize,maxSize-100,maxSize-200,maxSize-100,maxSize-200,maxSize-300,maxSize-400]
    colour = [colour2,colour2,colour2,colour1,colour2,colour2,colour2,colour2,colour2,colour2]
    if size == 7:
        colour[5] = colour1
        colour[6] = colour1
        colour[7] = colour1
        
    for d in range(len(starty)):
        y1 = starty[d] + 10
        x1 = startx[d] + 0
        x2 = startx[d] + 90
        y2 = starty[d] + 20
        x3 = startx[d] + 90
        y3 = starty[d] + 100
        x4 = startx[d] + 80
        for i in range(5):
            rect =  Rectangle(Point(x1,y1),Point(x2,y2))
            rect2 =  Rectangle(Point(x3,y1),Point(x4,y3))
            rect.setFill(colour[d])
            rect.setOutline(colour[d])
            rect2.setFill(colour[d])
            rect2.setOutline(colour[d])
            rect.draw(win) #right to left rectangles
            rect2.draw(win) #down rectangles
            x2 = x2 - comP
            y1 = y1 + comP
            y2 = y2 + comP
            x3  = x3 - comP
            x4 = x4 - comP
drawPatchTwo(7,"red","blue","green")



