# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
So from the previous cosine alogrithm, the final list of total scores are in a
list formation in which the top 3 (index 0,1,2) are the books that we input.
So basically taking that list and looking at index 3 we say that that is the closest match and 
put that at 100% match. Then form there we basically use that to find the other 
percentiles.
In the test case I simply used 98,90,80,65 just to see the distribution of it and see
if the code works. After doing a couple of test runs, I can figure out a better bracket 
which again depends on the score that the books are recieving. """
total=list(range(10000,200,-26))
Max=total[3]
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
print(C)