import pyscreenshot 
  
def screenshotter():
    # To capture the screen 
    image = pyscreenshot.grab()
    
    # Capture specific part of the screen 
    # im=pyscreenshot.grab(bbox=(x1,x2,y1,y2)) 
    imageBox = pyscreenshot.grab(bbox=(10, 10, 500, 500)) 
    
    # To display the captured screenshots 
    image.show() 
    imageBox.show() 
    
    # To save the screenshots 
    image.save(r"C:\Users\antonio.burevski\Desktop\PyDemo\Other\Screenshotter\test-screenshot.png") 
    imageBox.save(r"C:\Users\antonio.burevski\Desktop\PyDemo\Other\Screenshotter\test-screenshot-box.png") 

if __name__ == "__main__":
    screenshotter() 