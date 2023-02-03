# Final Exam Problem 3

# in:  color c (type Color)
# out: grayscale of c (type Color)
def RGB2Y(c):
  r = color.getRed(c)
  g = color.getGreen(c)
  b = color.getBlue(c)
  y = 0.299*r + 0.587*g + 0.114*b
  return makeColor(y,y,y)

# in:  picture (type Picture)
# out: pic (grayscale of picture, type Picture)     
def colorToGrayscale(picture):
  pic = duplicatePicture(picture)
  for pixel in getPixels(pic):
    setColor(pixel, RGB2Y(getColor(pixel)))
  return pic
