import os
import csv
import re
import matplotlib.pyplot as plt
import numpy as np
import xgboost as xgb
from sklearn import tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

folder_path = "/home/asma-rashidian/Documents/DrRahmaniPreProject/tfidf_results"  
# Get only CVS files in the folder
files = os.listdir(folder_path)
labels = []
vectors = []
class_map = {
    'اجتماعی اجتماعی': 0,
    'اقتصادی داخلی': 1,
    'سیاسی مجلس احزاب و تشکل ها': 2,
    'سیاسی مجلس امنیتی و دفاعی': 3,
    'سیاسی مجلس حقوقی و قضایی': 4,
    'سیاسی مجلس دولت': 5,
    'سیاسی مجلس رهبری و روسای قوا': 6,
    'سیاسی مجلس عمومی': 7,
    'صفحه نخست اقتصادی': 8,
    'صفحه نخست امنیتی و دفاعی': 9,
    'صفحه نخست بین الملل': 10,
    'صفحه نخست سیاسی': 11,
    'فرهنگی رسانه': 12,
    'فرهنگی سینما': 13,
    'فرهنگی کتاب': 14,
    'فرهنگی مذهب': 15,
    'ورزشی ورزشی': 16
}

# Iterate over the files
for file in files:
    if file.endswith(".csv"):  # Check if the file is a CSV file
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            label = re.sub(r"[()'',.csv]",'', file)
            for vector in csv_reader:
                vectors.append(vector)
                labels.append(class_map[label])

# Pad vectors with zeros to have equal length
max_len = len(max(vectors, key=len))
for i in range(len(vectors)):
    while len(vectors[i]) < max_len:
        vectors[i].append(0.0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(vectors, labels, test_size=0.2, random_state=20)

# Create the XGBoost classifier
model = xgb.XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=4)
le = LabelEncoder()
y_train = le.fit_transform(y_train)
X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)
classification_report = classification_report(y_test, y_pred)
print("XGBoost Report:")
print(classification_report)
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)