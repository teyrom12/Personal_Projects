import pyautogui
import time
import keyboard
import webbrowser
pozitie_initial_x=512
pozitie_initiala_y=390
pos_fin_x=1656
pos_fin_y=780
dif_x=889-pozitie_initial_x
dif_y=pos_fin_y-pozitie_initiala_y
curent_x=pozitie_initial_x
curent_x=512
curent_y=390
def autoviwe(curent_x,pos_fin_x,pozitie_initial_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y):
    time.sleep(1)
    while not keyboard.is_pressed('esc'):
        time.sleep(2)
        if curent_x<=pos_fin_x :
            pyautogui.click(curent_x,curent_y)
            print(1,curent_x,curent_y)
            curent_x=curent_x+dif_x
            time.sleep(5)
            if pyautogui.locateOnScreen(r'C:\Users\TeyRo\Desktop\Chrome\Screenshot 2022-11-10 144312.png' , confidence=0.7)!= None:
                #camp_google=pyautogui.locateOnScreen(r'C:\Users\beni\Desktop\python\back.png' , confidence=0.7)
                pyautogui.click(pyautogui.locateOnScreen(r'C:\Users\TeyRo\Desktop\Chrome\Screenshot 2022-11-10 144312.png' , confidence=0.7))
        else:
            curent_x=pozitie_initial_x
            time.sleep(2)
            pyautogui.move(curent_x,curent_y)
            pyautogui.scroll(-200)
            time.sleep(4)   
webbrowser.open("https://www.youtube.com/")
time.sleep(5)           
autoviwe(curent_x,pos_fin_x,pozitie_initial_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y)
