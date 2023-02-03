def signsOfLife():
  print 'signs of life'
  
  

def mirrorPoint(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  for x in range(0, 2 * width):
   addLine(picture, x, 0, x-width, height)       
   for y in range(0, 2 * height):
     addLine(picture, 0, y, width, y - height)   
  show(picture)
  print picture
                              
  show(picture)
  print picture
  
def drawLines(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  space = 10
  for x in range(0, 2 * width, space):
   addLine(picture, x, 0, x-width, height)       
  show(picture)
  print picture
file = pickAFile()
picture = makePicture(file)
drawLines(picture)

file = pickAFile()
picture = makePicture(file)
mirrorPoint(picture)

  