import pyautogui
import time
import keyboard


def coordonate():
    print(pyautogui.position())
    time.sleep(0.5)

def ksp_bot():
    print("Cautam Windows Search")
    #
    #
    if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\WinSearch.png', confidence = 0.9) != None:
        #Windows Search a fost gasit
        print("Windows Search a fost gasit cu succes")
        time.sleep(0.1)
        #
        #
        print("Cream variabila pentru Windows Search")
        winSearch = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\WinSearch.png', confidence = 0.9)
        time.sleep(0.1)
        print("Variabila Windows Search Creata cu Succes")
        #
        #
        time.sleep(0.3)
        print("Apasam pe Windows Search")
        time.sleep(0.1)
        pyautogui.click(winSearch)
        time.sleep(0.1)
        print("Apasare efectuata cu succes la coordonatele:")
        coordonate()
        #
        #
        #
        time.sleep(0.1)
        print("Scriem \"Steam\"")
        time.sleep(0.1)
        pyautogui.write('steam',interval = 0.1)
        time.sleep(0.2)
        print("\"Steam\" scris cu succes")
        #
        #
        #
        time.sleep(0.1)
        print("Apasam tasta \"enter\"")
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.3)
        print("Apasare efectuata cu succes la coordonatele:")
        coordonate()
        time.sleep(2)
        #
        #
        print("Cautam \"KSP\"")
        if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSPgame.png', confidence = 0.9) != None:
            #Daca KSP a fost gasit
            #
            #
            print("Imaginea \"KSP\" a fost gasita cu succes")
            time.sleep(0.1)
            #
            #
            print("Cream variabila pentru \"KSP\"")
            ksp_Game = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSPgame.png', confidence = 0.9)
            time.sleep(0.2)
            print("Variabila creata cu succes!")
            #
            #
            time.sleep(0.2)
            print("Apasam pe KSP game")
            time.sleep(0.1)
            pyautogui.click(ksp_Game)
            time.sleep(0.1)
            print("Apasare efectuata cu succes la coordonatele:")
            coordonate()
            #
            #
            #
            time.sleep(0.1)
            print("Cautam \"Play\"")
            if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\PlayButton.png', confidence = 0.9) != None:
                #Daca KSP a fost gasit
                #
                #
                print("Imaginea \"Play\" a fost gasita cu succes")
                time.sleep(0.1)
                #
                #
                print("Cream variabila pentru \"Play\"")
                play_Button = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\PlayButton.png', confidence = 0.9)
                time.sleep(0.2)
                print("Variabila creata cu succes!")
                #
                #
                time.sleep(0.2)
                print("Apasam pe Play")
                time.sleep(0.1)
                pyautogui.click(play_Button)
                time.sleep(0.1)
                print("Apasare efectuata cu succes la coordonatele:")
                coordonate()
                #
                #
                #
                time.sleep(10)
                print("Cautam \"PlayKSP\"")
                if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\PlayKSPButton.png', confidence = 0.9) != None:
                    #Daca KSP a fost gasit
                    #
                    #
                    print("Imaginea \"PlayKSP\" a fost gasita cu succes")
                    time.sleep(0.1)
                    #
                    #
                    print("Cream variabila pentru \"Play\"")
                    playKSP_Button = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\PlayKSPButton.png', confidence = 0.9)
                    time.sleep(0.2)
                    print("Variabila creata cu succes!")
                    #
                    #
                    time.sleep(0.2)
                    print("Apasam pe Play")
                    time.sleep(0.1)
                    pyautogui.click(playKSP_Button)
                    time.sleep(0.1)
                    print("Apasare efectuata cu succes la coordonatele:")
                    coordonate()
                    #
                    #
                    #
                    time.sleep(60)
                    print("Cautam \"Start Game\"")
                    if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_StartGame.png', confidence = 0.9) != None:
                        #Daca StartGame a fost gasit
                        #
                        #
                        print("Imaginea \"Start Game\" a fost gasita cu succes")
                        time.sleep(0.1)
                        startGame = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_StartGame.png', confidence = 0.9)
                        pyautogui.click(startGame)
                        time.sleep(5)
                        if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_Resume.png', confidence = 0.6) != None:
                            resumeGame = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_Resume.png', confidence = 0.9)
                            pyautogui.click(resumeGame)
                            time.sleep(2)
                            if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_SandBox.png', confidence = 0.9) != None:
                                sandbox = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_SandBox.png', confidence = 0.9)
                                pyautogui.click(sandbox)
                                time.sleep(0.2)
                                if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_Load.png', confidence = 0.9) != None:
                                    ksp_load = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_Load.png', confidence = 0.9)
                                    pyautogui.click(ksp_load)
                                    time.sleep(30)
                                    if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_VAB.png', confidence = 0.8) != None:
                                        vab = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_VAB.png', confidence = 0.8)
                                        pyautogui.click(vab)
                                        time.sleep(10)
                                        if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_OpenShips.png', confidence = 0.9) != None:
                                            openShips = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_OpenShips.png', confidence = 0.9)
                                            pyautogui.click(openShips)
                                            time.sleep(0.5)
                                            if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_DeepSpaceSatelite.png', confidence = 0.9) != None:
                                                deepSpaceSatelite = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_DeepSpaceSatelite.png', confidence = 0.9)
                                                pyautogui.click(deepSpaceSatelite)
                                                time.sleep(1)
                                                pyautogui.click(ksp_load)
                                                time.sleep(3)
                                                if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_Launch.png', confidence = 0.9) != None:
                                                    launchButton = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_Launch.png', confidence = 0.9)
                                                    pyautogui.click(launchButton)
                                                    time.sleep(3)
                                                    if pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_SAS.png', confidence = 0.9) != None:
                                                        sas = pyautogui.locateOnScreen(r'D:\Anul II\S1\Metode Avansate de programare\Exercitii\KSPBot\Images\KSP_SAS.png', confidence = 0.9)
                                                        pyautogui.click(sas)
                                                        pyautogui.keyDowon('shift')
                                                        time.sleep(1.5)
                                                        pyautogui.keyUp('shift')
                                                        pyautogui.press('capskock')
                                                        pyautogui.press('space')
                                                        time.sleep(25)
                                                        counter = 0
                                                        while (counter < 5):
                                                            pyautogui.keyDown('d')
                                                            time.sleep(2)
                                                            pyautogui.keyUp('d')
                                                        pyautogui.keyDown('ctrl')
                                                        time.sleep(0.5)
                                                        pyautogui.keyUp('ctrl')
                                                        while (counter < 5):
                                                            pyautogui.keyDown('d')
                                                            time.sleep(2)
                                                            pyautogui.keyUp('d')

                else:
                    print("Nu s-a gasit butonul KSP Play")
            else:
                print("Nu s-a gasit buttonul de Play")
        else:
            print("Nu s-a gasit jocul KSP")
    else:
        print("nu s-a gasit butonul Winsearch")

while 1:
    ksp_bot()