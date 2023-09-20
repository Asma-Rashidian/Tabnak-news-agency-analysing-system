
# Tabnak News Agency Analyzer 

## Python Scripts are designed for  Tabnak website link Crawling, TF-IDF Implementation on the text of each crawled link, and applying Decision Tree, Random Forest, and XGBoost models on TF-IDF results.
 
This repository contains Python scripts for various tasks including Tabnak website link Crawling, TF-IDF Implementation on the text of each crawled link, applied(Decision Tree, Random Forest, and XGBoost ) on TF-IDF results.
 
## Prerequisites 
 
Before running the scripts, ensure that you have the following: 
 
- Python 3.x installed on your system 
- Required libraries installed (e.g., requests, BeautifulSoup, scikit-learn, xgboost, numpy, matplotlib, etc.). Install the libraries using pip:
pip install requests beautifulsoup4 scikit-learn xgboost
## Scripts 
1. **Data and Link Crawler** : extract.py
	
 	1. The code starts by importing the necessary libraries: requests, BeautifulSoup, re, mysql.connector, and csv. 
 
	
 	2. It defines a class called DataCrawler with the following attributes: 
	   - crawled_links: a list to store all the crawled links 
	   - all_crawled_data: a list to store all the crawled data 
	   - main_url: the main URL of the website to be crawled 
	 
	
 	3. The class has several methods: 
	   - link_crawler: This method is responsible for crawling the links from different categories of the main website and other websites. It uses the requests library to make HTTP requests and BeautifulSoup library to parse the HTML content of the web pages. It extracts the links and stores them in the crawled_links list. 

2.**Apply Models** : models.py
	
 	1. The code imports necessary libraries such as MySQL Connector, TfidfVectorizer, DecisionTreeClassifier, train_test_split, RandomForestClassifier, classification_report, matplotlib, etc. 
	
 	2. The "TextModels" class is defined with the following methods: 
	   a. __init__(): Initializes the class with empty text_corpus and labels lists. 
	   b. load_data(): Connects to a MySQL database and retrieves the text corpus and labels from the "tab_news" table. It then appends each text and label to the corresponding list. 
	   c. tfidf_implementation(): Implements tf-idf vectorization on the text corpus using TfidfVectorizer. It then saves the feature names to a CSV file. 
	   d. decision_tree(): Splits the data into training and testing sets, trains a decision tree classifier on the training set, makes predictions on the testing set, and evaluates the model. It then prints the classification report and displays the decision tree using matplotlib. 
	   e. random_forest(): Splits the data into training and testing sets, trains a random forest classifier on the training set, makes predictions on the testing set, and evaluates the model. It then prints the classification report. 
	   f. xgboost_model(): Splits the data into training and testing sets, trains an XGBoost classifier on the training set, makes predictions on the testing set, and evaluates the model. It then prints the classification report. 
	   g. excutor(): Calls the load_data() and tfidf_implementation() methods, prompts the user to choose a machine learning model to execute, and calls the corresponding method. 
	
 	3. The code checks if the current module is the main program and creates an instance of the "TextModels" class. It then calls the excutor() method to run the program.
## Notes 
 
- Ensure to provide the required input files (e.g., corpus file, training data file, test data file) when running the respective scripts. 
- You can modify the scripts according to your specific requirements and adapt the input/output formats accordingly. 
- Feel free to explore and enhance the code based on your needs. 
 
 
## Results
- The Decision tree, Random forest, and XGBoost model achieved the following performance metrics:

	**Decision Tree Model Result**
  
  					precision	recall	  f1-score	support
		
			     accuracy                                 0.39           344
  
                   macro avg          0.12       0.14       0.12           344
  
                   weighted avg       0.33       0.39       0.35           344
  

	**Random Forest Model Result**
  
					precision	recall	  f1-score	support
  
		  	     accuracy                                 0.48           344
  
                   macro avg          0.18       0.19       0.16           344
  
                   weighted avg       0.37       0.48       0.36           344

	**XGBoost Model Result**
  
					precision	recall	  f1-score	support
  
			     accuracy                                 0.54           344
  
                   macro avg          0.21       0.24       0.22           344
  
                   weighted avg       0.45       0.54       0.48           344
  

--- 
 
Please customize the README file further based on your specific project requirements. You may include additional sections such as installation instructions, usage examples, or license information.
