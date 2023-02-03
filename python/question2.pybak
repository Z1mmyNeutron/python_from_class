
def rotatePicture180(picture):
  pixels = getPixels(picture)
  width = getWidth(picture)
  height = getHeight(picture)
  newPicture = makeEmptyPicture(width, height)
  for x in range(width):
    for y in range(height):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(newPicture, (width-x-1), (height-y-1)), color)
  show(newPicture)
  return newPicture
  
  
file = pickAFile()
picture = makePicture(file)
rotatePicture180(picture)