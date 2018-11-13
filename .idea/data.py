import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ratings = pd.read_csv("./data/BX-Book-Ratings.csv", sep=";",
                         encoding="ISO-8859-1")

books = pd.read_csv("./data/BX-Books.csv", sep=";",
                       encoding="ISO-8859-1", error_bad_lines=False)

users = pd.read_csv("./data/BX-Users.csv", sep=";",
                         encoding="ISO-8859-1")

users.columns = users.columns.str.lower().str.replace('-', '_')
books.columns = books.columns.str.lower().str.replace('-', '_')
ratings.columns = ratings.columns.str.lower().str.replace('-', '_')

# Users
users_clean = users.loc[(users.age > 10) & (users.age < 100) | (pd.isnull(users.age))]

users_clean = users_clean.assign(age = users_clean.age.fillna(users_clean.age.mean()))

split_location = users_clean.location.str.split(",", 2, expand=True)
split_location.columns = ["city", "state", "country"]
users_clean = pd.concat([users_clean, split_location], axis=1).drop("location", axis=1)
users_clean.country.replace("", np.nan, inplace=True)

# Books
books.drop(columns=["image_url_s", "image_url_m", "image_url_l"], inplace=True)
books.year_of_publication = pd.to_numeric(books.year_of_publication, errors="coerce")

# replacing all years of publication that are 0 with NaN
books.year_of_publication.replace(0, np.nan, inplace=True)

# counting number of books with year of publication as null
books.year_of_publication.isnull().sum().sum()

# books with publication dates beyond 2018 seem to be erroneous. Also books with NaN publication dates could cause and issue.
books = books[books.year_of_publication < 2018]

# correcting publisher names and assigning the name 'Other' to those with missing publisher names
books.publisher = books.publisher.str.replace("&amp;", "&")

books.publisher.replace(np.nan, "Other", inplace=True)

# replacing the NaN in for book_author with Unknown
books.book_author.replace(np.nan, "Unknown", inplace=True)

# Ratings is clean

# removing the rows with an implicit book_rating of 0
ratings = ratings[ratings.book_rating != 0]

users_clean.to_csv("./data/clean/users_clean.csv", sep=",", encoding="utf-8")
books.to_csv("./data/clean/books_clean.csv", sep=",", encoding="utf-8")
ratings.to_csv("./data/clean/ratings_clean.csv", sep=",", encoding="utf-8")