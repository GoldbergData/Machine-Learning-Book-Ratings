import numpy as np
import pandas as pd

ratings_df = pd.read_csv("./data/BX-Book-Ratings.csv", sep=";",
                         encoding="ISO-8859-1")

books_df = pd.read_csv("./data/BX-Books.csv", sep=";",
                       encoding="ISO-8859-1", error_bad_lines=False)

users_df = pd.read_csv("./data/BX-Users.csv", sep=";",
                         encoding="ISO-8859-1")


