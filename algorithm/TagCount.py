import time
start = time.time()

import pandas as pd
import os
os.chdir("C:\\Users\\shazi\\Desktop\\Software Engine Project\\SoftwareEngineeringProject2019\\database")
myTags=pd.read_csv("tags.csv")
myTags=(myTags["tag_name"])
#print(myTags) ##Test line
tag_list=[]
for tag in myTags:
    tag_list.append(tag)
#print(tag_list) ##Test Line

TagCounter=[0]*len(myTags) #This would be the counter for all the tags. Created new every time
testList=['Horror','childrens-classics','erica-jong','Horror','Adventure','Horror','Adventure', 'Religion','Horror','Horror',]

def UpdateCount(userList):#Function will update the counters
    for i in range(len(myTags)):#Length of the list
        for j in testList:#gets the tags from the list from user
            if myTags[i]==j:#checking if the tags match
                TagCounter[i]+=1#add to the counter

UpdateCount(testList) ## Testing Line
total=list(zip(myTags, TagCounter))#combine the counter with the tag ID for a pseudo database
#print(total) ##Test Line

def NonZerolist(tagCount):#function that will eliminate zero count tags to speed up time later
    newlist=[] #Temp new list that holds the non zeros
    for k in range(len(tagCount)):
        tempList=tagCount[k]
        if tempList[1]!=0:#if the tag has a count then store it 
            newlist.append(tempList)
    return newlist#Gives back the new list and forgets the old list

total=NonZerolist(total)

print(total) ##Test line
end = time.time()
print(end - start)
###The only issue with this implimentation
#right now would have to be the it is brute force
#the run time is too long
#figure out a way to make the run time shorter