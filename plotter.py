import json   #CodeForcesGraphPlotter
import matplotlib.pyplot as plt
import requests
import string

def makegraph():
    userid=input()
    txt="https://codeforces.com/api/user.rating?handle=namitaarya2002"

    url=txt.replace("namitaarya2002",userid)
    f = requests.get(url)
    data=f.json()

    if data["status"] != "OK":
        print("Incorrect Username")
    else:
        ls1=[] 
        ls2=[]
        ls3=[]

        for i in data["result"]:
            ls1.append(i["contestId"])

        for i in data["result"]:
            ls2.append(i["oldRating"])

        for i in data["result"]:
            ls3.append(i["newRating"])

       # plt.scatter(ls3,ls1)
        plt.plot(ls3,ls1)
        plt.xlabel("RANK")
        plt.ylabel("CONTESTID")
        
def showgraph():
    plt.show()

print("Enter the number of users you wanna compare")
num=int(input())

for i in range(num):
    print("Enter username")
    makegraph()
    
showgraph()







