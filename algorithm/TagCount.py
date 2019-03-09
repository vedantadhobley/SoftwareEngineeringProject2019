myTags =['Horror','Romance','Adventure','Science'] #This is our list of know tags. Global stuff
TagCounter=[0,0,0,0] #This would be the counter for all the tags. Created new every time
testList=['Horror','Horror','Adventure','Horror','Adventure','Horror','Adventure', 'Religion','Horror','Horror',]

def UpdateCount(userList):#Function will update the counters
    for i in range(4):#Length of the list
        for j in testList:#gets the tags from the list from user
            if myTags[i]==j:#checking if the tags match
                TagCounter[i]+=1#add to the counter

UpdateCount(testList) #Simply testing it 
total=list(zip(myTags, TagCounter))#combine the counter with the tag ID for a pseudo database
print(total)

def NonZerolist(tagCount):#function that will eliminate zero count tags to speed up time later
    newlist=[] #Temp new list that holds the non zeros
    for k in range(len(tagCount)):
        tempList=tagCount[k]
        if tempList[1]!=0:#if the tag has a count then store it 
            newlist.append(tempList)
    return newlist#Gives back the new list and forgets the old list

total=NonZerolist(total)

print(total)