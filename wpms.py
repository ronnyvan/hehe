import random
import time
import pyautogui


time.sleep(2)
text = open("./text.txt", 'r') 
for line in text:
    words = line.split()
    for word in words:
        #the lower the interval the shorter the duration between each keystroke
        # -> faster time to type that word
        # range 0.10 to 0.60 replicates above average typespeed ~50-60 wpm
        # increase the upper bound to type slower
        # you can increase the lower bound if you want

        pyautogui.typewrite(word, interval=round(random.uniform(0.1, 0.6), 2))
        #randomized time between each word
        time.sleep(len(word)*0.1)
        pyautogui.press('space')
        
        if random.randint(1, 100) == 1:
            randInterval = random.randint(50, 150)
            print(f"pause for {randInterval}")
            time.sleep(randInterval)



# keyboard.type("wsg gang")

# text = open("./text.txt")
# for each_line in text:
#     keyboard.type(each_line)
