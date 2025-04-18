import requests
import re
import time
import random


celebs = [] 

with open('contestants.txt', 'r') as rf:
    lines = rf.read().split('\n')

for line in lines:
     celebs.append(line)

celebs.pop()

#print(celebs)     
#print(len(celebs))

celebCount = 0
while celebCount != 366:
    if celebCount % 10 == 0:
        time.sleep(10)

    for celeb in celebs:
        q = celeb.lower().replace(" ", "+") + "+height"

        r = requests.get(f'https://www.google.com/search?q={q}')

        sleepTime = random.randint(1,10)
        time.sleep(sleepTime)
        if r.status_code == 200:
            try:
                ft, y, inches, z = re.findall(
                    '\d+',
                    re.findall('\d+&#8242; \d+&#8243;', r.text)[0]
                )

                print(f"{celeb} is {ft}' {inches}\"")
                celebCount += 1
        
            except:
                print(f"{celeb} NA")
                celebCount += 1

        else: 
            print("Something went wrong")


'''
6&#8242; 2&#8243;
\d+&#8242; \d+&#8243;
'''
