file = pickAFile()
picture = makePicture(file)

def mirrorPictureDiagonal(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  
  sqWidth = width
  if height < width:
    sqWidth = height
  for x in range(0, getHeight(picture)):
    for y in range(0, getWidth(picture)):
      pixelA = getPixel(picture, x, y)
      pixelB = getPixel(picture, y, x)
      colorA = getColor(getPixel(picture, pixelA))
      setColor(pixelB, colorA)     
      
      
      
      
  #for indexI in range(0, getHeight(picture)):
  #  for indexJ in range(0, getWidth(picture)-indexI):
  #    nextColor = getColor(getPixelAt(picture, indexJ, indexI))
  #    y = getHeight(picture)-indexI-1
  #    x = getWidth(picture)-indexJ-1
  #    ogPixel = getPixelAt(picture,y,x)
  #  setColor(ogPixel, newColor)
      
mirrorPictureDiagonal(picture)
explore(picture)