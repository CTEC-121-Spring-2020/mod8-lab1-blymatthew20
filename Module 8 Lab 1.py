"""
CTEC 121
Matthew Bly
Module 8 Lab 1
Module 8 Lab 2
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *
from dog import Dog
from msdie import MSDie
import docTest
def main():
    # mod 7 assignment review
    '''
    myDict {}
    #key - value
    #create element
    myDict['key'] = 'value'
    myDict['key'] = 'new value'
    print(myDict.keys())
    print(myDict.values())
    print(myDict.items())

    fileHandle = open('sample.txt', 'a')
    print()
    #print(fileHandle)
    readReturn = fileHandle.read
    print(type(readReturn))
    print('*',fileHandle.read(), '*')
    print()
    '''
    '''
    print()
    print(5*'All that')
    print()
    '''
    # section 1
    '''
    win = GraphWin('demo', 800, 800)
    myCirlce = Circle(Point(400,400), 200)
    myCirlce.setFill('green')
    myCirlce.draw(win)
    win.getMouse()
    '''
    # section 2
    '''
    d = Dog('Dog')
    print(d)
    print(d.getName())
    d.setName('Godzilla')
    print(d.getName())

    d.bark()
    '''
    #section 3
    '''
    die = MSDie(12)
    print('number of sides', die.getSides())
    print('Value:', die.getValue())
    die.setValue(5)
    print('Value:', die.getValue())
    die.setValue(12)
    print('Value:', die.getValue())
    die.roll()
    print('Value:', die.getValue())
    die.roll()
    print('Value:', die.getValue())
    die.roll()
    print('Value:', die.getValue())
    '''
    print()
    # print module header documentation
    print(docTest.__doc__)
    # print class docs
    print(docTest.DocTest.__doc__)
    #print method docs
    print(docTest.DocTest.method.__doc__)
    print()

main()    