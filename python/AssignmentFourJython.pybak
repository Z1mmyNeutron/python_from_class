def pickFileAndMakePicture():
  file = pickAFile()
  pictureOG = makePicture(file)
  pictureOne = picture2GrayscaleLinear(pictureOG)
  pictureOne.show()
  pictureTwo = picture2GrayscaleNonLinear(pictureOG)
  pictureTwo.show()
  
def RGB2YLinear(color):
    y = 0.2126 * color.getRed() + 0.7152 * color.getGreen() + 0.0722 * color.getBlue()
    return Color(y, y, y)

def picture2GrayscaleLinear(picture):
  copyOfPicture = duplicatePicture(picture) 
  for r in range(getHeight(copyOfPicture)):
    for w in range (getWidth(copyOfPicture)):
      pixel = getPixel(picture, w, r)
      luminance = getColor(pixel)
      luminance = RGB2YLinear(luminance)
      setColor(pixel, luminance) 
  return picture
  

def RGB2YNonLinear(color):
    y = 0.299 * color.getRed() + 0.5872 * color.getGreen() + 0.114 * color.getBlue()
    return Color(y, y, y)

def picture2GrayscaleNonLinear(picture):
  copyOfPicture = duplicatePicture(picture) 
  for r in range(getHeight(copyOfPicture)):
    for w in range (getWidth(copyOfPicture)):
      pixel = getPixel(picture, w, r)
      luminance = getColor(pixel)
      luminance = RGB2YNonLinear(luminance)
      setColor(pixel, luminance) 
  return picture
  

pickFileAndMakePicture()

