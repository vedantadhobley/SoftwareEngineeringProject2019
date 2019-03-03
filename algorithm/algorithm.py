import pandas as pd

def bookLocate(book,library):
	return library[library['title'].str.contains(book)]

def book_id(book,library):
	bookLocate_df = bookLocate(book,library)
	book_id_list = bookLocate_df.index.values
	return book_id_list

# Creates DataFrame of book information from 'books.csv'. Path is specific to Vedanta Dhobley. ONLY EDIT PATH FOR TESTING.
books_df = pd.read_csv('/Users/vedantadhobley/Desktop/SoftwareEngineeringProject2019/database/books.csv', index_col='book_id')
print(books_df)

# Calls 'bookLocate(book)' and creating a new DataFrame with the rows of 'books_df' containing the string provided.
bookLocate_df = bookLocate('Hunger Games', books_df)
print(bookLocate_df)

# Creates a new CSV file containing the infomation from the DataFrame created from the 'bookLocate(book)' definition.
bookLocate_df.to_csv('test.csv')

# Creates a list of 'book_id's containing the book title provided.
book_id_list = book_id('Hunger Games', books_df)
print(book_id_list)