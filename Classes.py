class Point:
    pass
blank = Point()

blank.x = 3.0
blank.y = 4.0

p1 = Point()
p2 = Point()
p1.x = 3
p1.y = 4
p2.x = 3
p2.y = 4

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



