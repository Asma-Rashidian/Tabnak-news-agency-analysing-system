import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
import csv 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

class TextModels ():

    def __init__(self):
        self.text_corpus = []
        self.labels = []
    
    def load_data(self):
        try :
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
            my_cursor.execute("SELECT Type FROM tab_news")
            for label in  my_cursor.fetchall():
                self.labels.append(str(label).replace("," ,''))
                self.categories.append(str(label).replace("," ,''))
            my_cursor.execute("SELECT Text FROM tab_news")
            for text in my_cursor.fetchall():
                self.text_corpus.append(str(text))
        except Exception as e:
            print("Error in connection:", e)
        finally:
            # Close the database connection
            if my_connection.is_connected():
                my_connection.close()
                my_cursor.close()
                print("MySQL connection is closed")

    def tfidf_implementation(self):
        vectorizer = TfidfVectorizer()
        self.vectors = vectorizer.fit_transform(self.text_corpus)
        self.features_names = vectorizer.get_feature_names_out()
        with open("/home/asma-rashidian/Documents/DrRahmaniPreProject/Cleaned/Models/features_name.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.features_names)
    
    def desicion_tree (self):

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.vectors, self.labels, test_size=0.4, random_state=20)

        # Train the decision tree model
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        classification_reports = classification_report(y_test, y_pred)
        accuracy = model.score(X_test, y_test)

        # Print the results
        print("Decision Tree Report:")
        print(classification_reports)

        # Display the decision tree
        fig, ax = plt.subplots(figsize=(12, 12))
        tree.plot_tree(model, feature_names=None, class_names=None, filled=True)
        plt.savefig("/home/asma-rashidian/Documents/DrRahmaniPreProject/Cleaned/Models/decision_tree.png", dpi=300)
        plt.show()

    def random_forest(self):

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.vectors, self.labels, test_size=0.3, random_state=20)

        # Train the Random Forest Classifier
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)    

        # Evaluate the model
        classification_report_str = classification_report(y_test, y_pred)
        accuracy = model.score(X_test, y_test)

        # Print the results
        print("Random Forest Report:")
        print(classification_report_str)

    def xgboost_model(self):

        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.vectors, self.labels, test_size=0.2, random_state=42)
        # Initialize the XGBoost classifier
        xgb_model = xgb.XGBClassifier()

        # Fit the model to the training data
        xgb_model.fit(X_train, y_train)

        # Make predictions on the testing data
        y_pred = xgb_model.predict(X_test)

        # Evaluate the model
        xgboost_report_str = classification_report(y_test, y_pred)
        # accuracy = model.score(X_test, y_test)
        print("XGBoost Report:")
        print(xgboost_report_str)

    def excutor (self):
        
        self.load_data()
        self.tfidf_implementation()
        inpute_num = int(input(" Press a number to execute the model: 1.Desicion Tree 2.Random Forest 3.XGBoost \n"))
        if inpute_num == 1 :
            self.desicion_tree()
        elif inpute_num == 2 :
            self.random_forest()
        elif inpute_num == 3 :
            self.xgboost_model()
        else :
            print(" You have entered wrong number....")
    


if __name__ == '__main__':
    model = TextModels()
    model.excutor()