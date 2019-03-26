import pandas as pd
import os
#import time
os.chdir("C:\\Users\\shazi\\Desktop\\SoftwareEngineeringProject2019\\database")

def BookRetriver(bookList):
    #bookList has the goodreads number
    my_tags=pd.read_csv("book_tags.csv")
    #Stores the tags csv file in my_tags
    tagList=[] #create tag list
    for book in bookList:#go through each book in the list
        BookTag=(my_tags.loc[my_tags["goodreads_book_id"]==book, "tag_id"])
        #Retrives only the Tag_id associated with the books
        for i in BookTag:
            tagList.append(i)
    return tagList
start=time.time()
myBooks=[1,6,45,2,325,8956,56,98,15,14,13,20]  
print(BookRetriver(myBooks))  
#end=time.time()
#print(end-start)



