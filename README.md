
# Tabnak News Agency Analyzer 

# Python Scripts for Tabnak website link Crawling, TF-IDF Implementation on the text of each crawled link, applied(Decision Tree, Random Forest, and XGBoost ) on TF-IDF results.
 
This repository contains Python scripts for various tasks including Tabnak website link Crawling, TF-IDF Implementation on the text of each crawled link, applied(Decision Tree, Random Forest, and XGBoost ) on TF-IDF results.
 
## Prerequisites 
 
Before running the scripts, ensure that you have the following: 
 
- Python 3.x installed on your system 
- Required libraries installed (e.g., requests, BeautifulSoup, scikit-learn, xgboost, numpy, matplotlib, etc.). Install the libraries using pip:
pip install requests beautifulsoup4 scikit-learn xgboost
## Scripts 
 
1. **Link Crawler**:  link_crawler.py  
   - This script crawls the Tabnak website and extracts 100 links from the web pages. 
   - The main website is: https://www.tabnak.ir
   - Data are stored on localhost Mysql database
 
2. **TF-IDF Implementation**:  tfidf_implementation.py  
   - This script demonstrates the implementation of the Term Frequency-Inverse Document Frequency (TF-IDF) algorithm
   	on stored data in  the localhost Mysql database.
 
3. **Decision Tree**:  decision_tree.py  
   - This script implements a Decision Tree classifier using the scikit-learn library 
   	based on TF-IDF vector result.
 
4. **Random Forest**:  random_forest.py  
   - This script demonstrates the implementation of a Random Forest classifier using the scikit-learn library
      	based on the TF-IDF vector result.
 
5. **XGBoost**:  xgboost.py  
   - This script implements XGBoost, a gradient boosting framework, for classification tasks
      	based on TF-IDF vector results.
 
## Notes 
 
- Ensure to provide the required input files (e.g., corpus file, training data file, test data file) when running the respective scripts. 
- You can modify the scripts according to your specific requirements and adapt the input/output formats accordingly. 
- Feel free to explore and enhance the code based on your needs. 
 
 
## Results
- The Decision tree, Random forest, and XGBoost model achieved the following performance metrics:

	**Decision Tree Model Result**
				precision	recall	  f1-score	support
		   accuracy                                 0.85           20
                   macro avg          0.70       0.65       0.67           20
                   weighted avg       0.90       0.85       0.87           20

	**Random Forest Model Result**
				precision	recall	  f1-score	support
		   accuracy                                 0.90           20
                   macro avg          0.73       0.68       0.70           20
                   weighted avg       0.95       0.90       0.92           20

	**XGBoost Model Result**
				precision	recall	  f1-score	support
		   accuracy                                 0.40           20
                   macro avg          0.36       0.36       0.36           20
                   weighted avg       0.40       0.40       0.40           20

--- 
 
Please customize the README file further based on your specific project requirements. You may include additional sections such as installation instructions, usage examples, or license information.
