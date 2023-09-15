import requests 
from bs4 import BeautifulSoup
import mysql.connector 
import re 
import string

# Read the links file line by line
with open('links.txt', 'r') as reader:
    links = reader.readlines()

# required datas that will be stored in mysql data base
all_data = []

# Crawling data of each page 
for id, link in enumerate(links, start=1):
    try:
        response = requests.get(link.replace('\n', ''))
        soup = BeautifulSoup(response.content, 'html.parser')
        news_type = ' '.join(re.findall('\w+', soup.find(class_="news_path").text))
        news_text = soup.find(class_='body').text.strip()
        all_data.append([id, news_type, news_text])
    except requests.exceptions.RequestException as e:
        print("An error occurred during the HTTP request:", str(e))

# Mysql database connection 
try:
    my_connection = mysql.connector.connect(
        host='localhost',
        database='tabnak_news',
        user='tabnak',
        password='*******'
    )
    my_cursor = my_connection.cursor()
    print("Successfully connected to DataBase!")

    # Insert query 
    for i in range(len(all_data)):
        my_cursor.execute('INSERT INTO tab_news VALUE (%s, %s, %s)', (all_data[i][0], all_data[i][1], all_data[i][2]))
        my_connection.commit()
    print(" Datas are stored completely!")
except Exception as e:
    print("Error in connection:", e)
finally:
    if my_connection.is_connected():
        my_connection.close()
        my_cursor.close()
        print("MySQL connection is closed")
