import pandas as pd

def bookLocate(book):
	return books_df[books_df['title'].str.match(book)]

# Creating DataFrame of book information from 'books.csv'. Path is specific to Vedanta Dhobley. ONLY EDIT PATH FOR TESTING.
books_df = pd.read_csv('/Users/vedantadhobley/Desktop/SoftwareEngineeringProject2019/database/books.csv', index_col='book_id')
print(books_df)

# Calling 'bookLocate(book)' and creating a new DataFrame with the rows of 'books_df' containing the string provided.
bookLocate_df = bookLocate('Harry Potter')
print(bookLocate_df)

# Creating a new CSV file containing the infomation from the DataFrame created from the 'bookLocate(book)' definition.
bookLocate_df.to_csv('harry_potter.csv')