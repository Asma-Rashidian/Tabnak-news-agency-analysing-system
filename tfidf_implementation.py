import mysql.connector
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd 
import csv
import numpy as np 

# Create an empty dictionary to store the data
data_dictionary = {}
keys = []

try:
    # Connect to the database
    my_connection = mysql.connector.connect(
        host='localhost',
        database='tabnak_news',
        user='tabnak',
        password='asma1379'
    )
    my_cursor = my_connection.cursor()
    print("Successfully connected to the database!")
    
    # Retrieve distinct types from the table
    my_cursor.execute("SELECT DISTINCT Type FROM tab_news")
    keys = my_cursor.fetchall()
    
    # Process each type
    for i in range(len(keys)):
        # Retrieve texts for the current type
        my_cursor.execute("SELECT Text FROM tab_news WHERE Type = %s", (keys[i]))
        texts = [re.sub(r"u200c|\\|/|nnnn|nxa0n|«|»|[()'.,:/_\-a-zA-Z0-9،؛]|[\s+]", " ", str(tex)) for tex in my_cursor.fetchall()]
        
        # Tokenize the texts
        tokenized_text = []
        for text in texts:
            t = [word for word in text.split(" ") if word != ""]
            tokenized_text.append(t)
        
        # Add the tokenized texts to the dictionary
        data_dictionary[keys[i]] = tokenized_text
        print("For type: %s, %d text is added" % (keys[i], len(tokenized_text)))
        
except Exception as e:
    print("Error in connection:", e)
    
finally:
    # Close the database connection
    if my_connection.is_connected():
        my_connection.close()
        my_cursor.close()
        print("MySQL connection is closed")


def calculate_tfidf(document, word):
    """
    Calculate the TF-IDF score for a given word in a document.
    """
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([document])
    feature_names = tfidf_vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()[0]
    tfidf_scores = dict(zip(feature_names, tfidf_scores))
    return tfidf_scores.get(word, 0.0)


def tfidf_implementation(key, values):
    """
    Calculate the TF-IDF scores for a given key and its corresponding values.
    """
    def get_union(values):
        """
        Get the union of all values.
        """
        union_set = set()
        for lst in values:
            union_set.update(lst)
        return list(union_set)
    
    union = get_union(values)
    total_tfidf_type = []
    
    for value in values:
        tfidf_scores = []
        
        if isinstance(value, str):
            value = value.lower()
        else:
            # Handle the case if the value is not a string (e.g., list, tuple, etc.)
            value = str(value).lower()
        
        for word in union:
            tfidf_score = calculate_tfidf(value, word)
            tfidf_scores.append(tfidf_score)
        
        total_tfidf_type.append(tfidf_scores)
    
    return total_tfidf_type, union

tfidf_vectorizing_result = {}

for key in keys:
    tfidf_result, union = tfidf_implementation(key, data_dictionary[key])
    tfidf_vectorizing_result[key] = tfidf_result
    
    # Open the file in write mode
    with open("/home/asma-rashidian/Documents/DrRahmaniPreProject/union_results/%s.txt" % str(key), 'w') as file:
        file.write(','.join(union))
    
    with open("/home/asma-rashidian/Documents/DrRahmaniPreProject/tfidf_results/%s.csv" % str(key), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tfidf_result)