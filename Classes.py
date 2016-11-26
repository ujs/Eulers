### Point
class Point: 
  def __init__(self, x=0, y=0): 
    self.x = x 
    self.y = y 

  def __str__(self): 
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  def __add__(self, other): 
    return Point(self.x + other.x, self.y + other.y)

  def __add__(self, other): 
    return Point(self.x + other.x, self.y + other.y)

  def __sub__(self, other): 
    return Point(self.x - other.x, self.y - other.y)
  def __mul__(self, other): 
    return self.x * other.x + self.y * other.y 



### Rectangle

class Rectangle:
    pass

box = Rectangle()
box.width = 100.0
box.height = 200.0

def findCenter(box): 
  p = Point() 
  p.x = box.corner.x + box.width/2.0 
  p.y = box.corner.y - box.height/2.0 
  return p 

def growRect(box, dwidth, dheight) : 
  import copy 
  newBox = copy.deepcopy(box) 
  newBox.width = newBox.width + dwidth 
  newBox.height = newBox.height + dheight 
  return newBox 

### Time

class Time:
    def convertToSeconds(self): 
        minutes = self.hours * 60 + self.minutes 
        seconds = minutes * 60 + self.seconds 
        return seconds 


def printTime(time):
    print (str(time.hr)+':'+str(time.min)+':'+str(time.sec))



    
    
    





    
    
