import pyautogui
import time
# from numpy import asarray


def hitup(key):
    pyautogui.press(key)            
    return()

def location(data):
    for i in range(550,580):
        for j in range(460,470):
            if(data[i,j]<=100):
                hitup('space')
                return()
    return()





time.sleep(3)
while(True):
    imagefile= pyautogui.screenshot().convert("L")
    data= imagefile.load()
    location(data)




# imagefile= pyautogui.screenshot().convert("L")
# data= imagefile.load()
# for i in range(520,550):
#     for j in range(460,470):
#         data[i,j]=0
#         print(data[i,j])



# imagefile.show()