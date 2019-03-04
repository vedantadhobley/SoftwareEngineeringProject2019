import pandas as pd
import time

##### Uses book.py as object class for various books.
from book import Book

##### Creates empty book_list.
book_list = []

##### General book information.
book_title = 'Lord of the Rings'
library_path = '/Users/vedantadhobley/Desktop/SoftwareEngineeringProject2019/database/books.csv'
index_name = 'book_id'
column_name = 'title'

##### Appends book object to book_list.
book_list.append(Book(book_title, library_path, index_name, column_name))

##### Generates library_df.
# library_df = book_list[0].load_library()
# print(library_df)

##### Generates book_df.
# book_df = book_list[0].book_locate()
# print(book_df)

##### Generates book_id_list.
book_id_list = book_list[0].book_id_locate()
print(book_id_list)
