import pandas as pd
import os
os.chdir("C:\\Users\\shazi\\Desktop\\Software Engine Project\\SoftwareEngineeringProject2019\\database")

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

#myBooks=[1,3] Testing 
#print(BookRetriver(myBooks)) Testing 




