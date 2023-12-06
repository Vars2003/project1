import re
import cv2
from cvzone.HandTrackingModule import HandDetector
from pyautogui import press,typewrite,hotkey,click
import speech_recognition as sr
from time import sleep
from os import system



def audiorec():
    print("Hello Krishna I am Listening")
    r = sr.Recognizer()
    # listening the speech and store in audio_text variable
    while True:
        with sr.Microphone() as source:
            audio_text = r.listen(source)
            try:
                SPtotext = r.recognize_google(audio_text)
            except:
                print("Sorry, I did not get that")
                continue

        Aakash = str(SPtotext)
        Ranjan = Aakash.lower()
        print(SPtotext)
        if Ranjan == "useless":
            break
        return Ranjan


# spotify
def spotify():
    command = "start spotify"
    system(command)
    sleep(2)
    press('Space')
    
    


# notepad
def notepad():
    system('subl')
    sleep(1)
    hotkey('ctrl','n')
    print("Hello Krishna I am Listening")
    r = sr.Recognizer()
    # listening the speech and store in audio_text variable
    while True:
        with sr.Microphone() as source:
            audio_text = r.listen(source)
            try:
                SPtotext = r.recognize_google(audio_text)
                print(SPtotext)
            except: 
                print("Sorry, I did not get that")
                continue

        Aakash = str(SPtotext)
        REC_TEXT = Aakash.lower()
        if REC_TEXT == 'line change':
            press('enter')
        elif REC_TEXT == "save it":
            hotkey('ctrl','s')
            sleep(0.5)
            press('enter')
            sleep(0.5)
            hotkey('alt','f4')
            break
        elif REC_TEXT == "useless":
            break
        else:
            typewrite(SPtotext,interval=0.05)
    # if REC_TEXT == "useless":
    #     break



# Whatsapp
def callwhat():
    press('win')
    sleep(0.5)
    typewrite('whatsapp')
    sleep(0.5)
    press('enter')
    sleep(7)
    hotkey('win', 'up')
    press('tab',presses=4,interval=0.05)
    sleep(0.5)
    typewrite('Prasnjit')
    # audi = audiorec()
    # aa.typewrite(audi)
    press('enter') # implementation of call is pending and message
    click(1725,62)
    sleep(3)
    click()
    sleep(0.5)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(detectionCon=0.8, maxHands=1)
# detector = HandDetector(detectionCon=0.7, maxHands=1)

while cap.isOpened():
    success, in_img = cap.read()
    img = cv2.flip(in_img, 1)
    img = detector.findHands(img)

    lmList, bboxInfo = detector.findPosition(img)
    if len(lmList) != 0:
        # for id, lm in enumerate(lmList):


        fingers = detector.fingersUp()

        # for spotify 1 2
        if fingers[0] == False and fingers[1] == True and fingers[2] ==True and fingers[3] == False and fingers[4] == False:
            spotify()
            for j in range(10000):
                continue


        print(fingers)

        # for Whatsapp
        if fingers[0] == False and fingers[1] == True and fingers[2] == True and fingers[3] == True and fingers[4] == True:
            callwhat()
            for j in range(10000):
                continue

        print(fingers)

       
       # for notepad 0 0 0 0 0
        if fingers[0] == False and fingers[1] == False and fingers[2] == False and fingers[3] == False and fingers[4] == False:
            notepad()
            for j in range(10000):
                continue




    cv2.imshow("Video-Feed", img)

    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

# cvzone==1.4.1
# mediapipe==0.8.7


