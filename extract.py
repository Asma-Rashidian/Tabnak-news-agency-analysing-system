import requests
from bs4 import BeautifulSoup
import re 
import mysql.connector
import csv


class DataCrawler ():
    def __init__(self):
        self.crawled_links = []
        self.all_crawled_data = []
        self.main_url = 'https://www.tabnak.ir'

    def link_crawler(self):
        try:
            # Make the request and get the page content
            response = requests.get(self.main_url)
            response.raise_for_status()  # Raise an exception if the request was unsuccessful
            soup = BeautifulSoup(response.content, 'html.parser')
            main_category_url = [self.main_url + cat.find('a').get("href") for cat in soup.find_all("li" , {"class":"nav_link"})][5:13]

            for url in main_category_url:
                url_response = requests.get(url)
                url_soup = BeautifulSoup(url_response.content, 'html.parser')
                for link in url_soup.find_all("a" , {"class":"picLink"}):
                    if "madre3online.ir" in link.get('href'):
                        pass
                    else:
                        self.crawled_links.append(self.main_url + link.get('href'))
                for link in url_soup.find_all("a" , {"class":"title5st_red"}):
                    if link.get('href') is None or "madre3online.ir" in link.get('href'):
                        pass
                    else :
                        self.crawled_links.append(self.main_url + link.get('href'))

            main_url1 = "https://tabnakjavan.com"
            category1 = ["https://tabnakjavan.com/fa/whatsup", "https://tabnakjavan.com/fa/culture-art" ,"https://tabnakjavan.com/fa/family" ,"https://tabnakjavan.com/fa/multimedia"]

            for cat in category1:
                cat_response = requests.get(cat)
                cat_soup = BeautifulSoup(cat_response.content, 'html.parser')
                for cat in cat_soup.find_all("div" , {"class":"special-cards col-xs-36"}):
                    self.crawled_links.append(main_url1 + cat.find('a').get("href"))
                    
            response1 = requests.get(main_url1)
            soup1 = BeautifulSoup(response1.content, 'html.parser')

            for cat in soup1.find_all("li" , {"class":"tab-list-item"}):
                self.crawled_links.append(main_url1 + cat.find('a').get("href")) 
            
            main_url2 = "https://tabnakbato.ir"
            response2 = requests.get(main_url2)
            soup2= BeautifulSoup(response2.content, 'html.parser')
            category2 = main_category_url = list(set([main_url2 + cat.find('a').get("href") for cat in soup2.find_all("li" , {"class":"nav_link"})]))

            for cat in category2:
                cat_response = requests.get(cat)
                cat_soup = BeautifulSoup(cat_response.content, 'html.parser')
                if cat_soup.find("a" , {"class":"archive_ax"}) is None:
                    pass
                else:
                    archive_link = main_url2 + cat_soup.find("a" , {"class":"archive_ax"}).get("href")
                    i = 1 
                    while i<8 :
                        archive_plink = archive_link + "?service_id=4&cat_id=&page=%d" % i
                        res_archive = requests.get(archive_plink)
                        soup_archive = BeautifulSoup(res_archive.content , 'html.parser')
                        for link in soup_archive.find_all("a" , {"class":"title_List"}):
                            self.crawled_links.append(main_url2 + link.get("href"))
                        i += 1

            self.crawled_links = list(set(self.crawled_links))
            with open("links_crwald.txt", 'w') as writer:
                for link in self.crawled_links:
                    writer.write(link + '\n')
        except requests.exceptions.RequestException as e:
            print("An error occurred during the HTTP request:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))

    def data_storing(self):
        for id , link in enumerate(self.crawled_links, start=1):
            try:
                response = requests.get(link)
                soup = BeautifulSoup(response.content, 'html.parser')
                if soup.find(class_="news_path") is None :
                    if soup.find("span" , {"class":"name-service-plus"}) is None:
                        news_type = "None"
                    else:
                        lin = soup.find("span" , {"class":"name-service-plus"})
                        start_index = lin.find('">') + 2
                        end_index = lin.find('</span>')
                        news_type = lin[start_index:end_index]
                else:
                    news_type = ' '.join(re.findall('\w+', soup.find(class_="news_path").text))

                if news_type == "None":
                    pass
                else:
                    news_text = re.sub(r'[^آ-ی ]', " ", soup.find(class_='body').text.strip()) 

                    self.all_crawled_data.append([id, news_type, news_text.replace("\u200c", "")])
            except requests.exceptions.RequestException as e:
                print("An error occurred during the HTTP request:", str(e))
        
        with open("all_crawled_data.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.all_crawled_data)

    def mysql_storage(self):
        print(len(self.all_crawled_data))
        try:
            my_connection = mysql.connector.connect(
                host='localhost',
                database='tabnak_news',
                user='tabnak',
                password='asma1379'
            )
            my_cursor = my_connection.cursor()
            print("Successfully connected to DataBase!")

            # Insert query 
            for i in range(len(self.all_crawled_data)):
                my_cursor.execute('INSERT INTO tab_news VALUE (%s, %s, %s)', (self.all_crawled_data[i][0], self.all_crawled_data[i][1], self.all_crawled_data[i][2]))
                my_connection.commit()
            print(" Datas are stored completely!")
        except Exception as e:
            print("Error in database connection:", e)
        finally:
            if my_connection.is_connected():
                my_connection.close()
                my_cursor.close()
                print("MySQL connection is closed")

    def func_executer (self):
        print(" Link crawling process has been successfully started.....")
        self.link_crawler()
        print(" All links have been successfully stored.....")
        self.data_storing()
        print(" The necessary data from every page has been successfully crawled.....")
        self.mysql_storage()

if __name__ == '__main__':
    data_crawler = DataCrawler()
    data_crawler.func_executer()