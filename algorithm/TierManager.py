# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
So from the previous cosine alogrithm, the final list of total scores are in a
list formation in% match. Then form there we basically use that to find the other 
percentiles.
In the test case I simply used 98,90,80,65 just to see the distribution of it and see
if the code works. After doing a couple of test runs, I can figure out a better bracket 
which again dep which the top 3 (index 0,1,2) are the books that we input.
So basically taking that list and looking at index 3 we say that that is the closest match and 
put that at 100ends on the score that the books are recieving. """

import random
total = random.sample(range(25000), 100)
total.sort(reverse=True)
print(total[3:53])
'''Max=total[3]
S=[]
A=[]
B=[]
C=[]
count= 3
while count<53 and total[count]>=Max*.65: #Check if the value is higher that 50% mark
    if total[count]>=Max*.80:
        while count<53 and total[count]>=Max*.80:#check if the value is higher than the 80% mark
            if total[count]>=Max*.90:
                while count<53 and total[count]>=Max*.90:#check if the value is higher than 90% mark
                    if total[count]>=Max*.98:
                        while count<53 and total[count]>=Max*.98:#check for above 98% mark
                            S.append(total[count])
                            count+=1
                    else:
                        A.append(total[count])
                        count+=1
            else:
                B.append(total[count])
                count+=1
    else:
        C.append(total[count])
        count+=1
print(S)
print(A)
print(B)
print(C)'''

def TierCreater(myValues):
    diff= myValues[3]-myValues[52]
    Lower= myValues[52]
    s=Lower+(diff*.95)
    a= Lower+(diff*.85)
    b= Lower+(diff*.6)
    c=Lower
    """The top portion is basically so that the tier 
    brackets work with any set of data. This means it doesn't matter how
    diverse the numbers are, every tier will have values, and it 
    will be in a bell curve model"""
    S=[]
    A=[]
    B=[]
    C=[]
    count= 3
    while count<53 and myValues[count]>=c:
        if myValues[count]>=b:
            while count<53 and myValues[count]>=b:
                if myValues[count]>=a:
                    while count<53 and myValues[count]>=a:
                        if myValues[count]>=s:
                            while count<53 and myValues[count]>=s:
                                S.append(myValues[count])
                                count+=1
                        else:
                            A.append(myValues[count])
                            count+=1
                else:
                    B.append(myValues[count])
                    count+=1
        else: 
            C.append(myValues[count])
            count+=1
    return S, A, B, C
print(TierCreater(total))