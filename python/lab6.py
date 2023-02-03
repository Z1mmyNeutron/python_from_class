
def readFileInput():  
  fname = "Home _ Rowan University.html"
  fname = pickAFile() 
  fHandle = open(fname,"r") 
  content = fHandle.read()  
  fHandle.close()           
  return content         

def freqAnalysisRowan(text):
  text = readFileInput()  
  startI = text.find("<title>")  
  endI = text.find("</title>")
  print(text[startI+(len("<title>")) : endI])


  script = sum(1 for i in range(len(text)) if text.startswith("<script", i)) 
  li = sum(1 for i in range(len(text)) if text.startswith("<li", i)) 
  link = sum(1 for i in range(len(text)) if text.startswith("<link", i)) 
  img = sum(1 for i in range(len(text)) if text.startswith('<img height="1"', i)) 
  span = sum(1 for i in range(len(text)) if text.startswith("<span", i)) 

  print("The number of script tags : ",script)
  print("The number of li tags : ",li)
  print("The number of link tags: ",link)
  print("The number of img tags: ",img)
  print("The number of span tags: ",span)

text = readFileInput()
freqAnalysisRowan(text)