import pandas as pd
import time

class Book:

    ##### self variables: (* = required)
    # book_title: title of book *
    # library_path: path of book library *
    # index_name: name of dataframe index *
    # column_name: name of dataframe column to be searched *
    # library_df: book library dataframe
    # book_df: book search results dataframe
    # book_id_list: list of indices with searched book



    ##### Resource manipulation/generation:

    # Constructor.
    def __init__(self, book_title, library_path, index_name, column_name):
        self.book_title = book_title
        self.library_path = library_path
        self.index_name = index_name
        self.column_name = column_name

    # Generates library_df.
    def load_library(self):
        self.library_df = pd.read_csv(self.library_path, index_col=self.index_name)
        return self.library_df

    # Generates book_df.
    def book_locate(self):
        try:
            self.book_df = self.library_df[self.library_df[self.column_name].str.contains(self.book_title)]
            return self.book_df
        except AttributeError:
            self.load_library()
            self.book_df = self.library_df[self.library_df[self.column_name].str.contains(self.book_title)]
            return self.book_df

    # Generates book_id_list.
    def book_id_locate(self):
        try:
            self.book_id_list = self.book_df.index.values
            return self.book_id_list
        except AttributeError:
            self.book_locate()
            self.book_id_list = self.book_df.index.values
            return self.book_id_list



    ##### self variables retrieval:

    # Returns book_title.
    def get_book_title(self):
        return self.book_title

    # Returns library_path.
    def get_library_path(self):
        return self.library_path

    # Returns index_name.
    def get_index_name(self):
        return self.index_name

    # Returns column_name.
    def get_column_name(self):
        return self.column_name

    # Returns library_df.
    def get_library_df(self):
        try:
            return self.library_df
        except AttributeError:
            self.load_library()
            return self.library_df

    # Returns book_df.
    def get_book_df(self):
        try:
            return self.book_df
        except AttributeError:
            self.book_locate()
            return self.book_df

    # Returns book_id_list.
    def get_book_id_list(self):
        try:
            return book_id_list
        except AttributeError:
            self.book_id_locate()
            return self.book_id_list
