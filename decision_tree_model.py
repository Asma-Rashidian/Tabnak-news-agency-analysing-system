import os
import csv
import re
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import tree
import matplotlib.pyplot as plt

folder_path = "/home/asma-rashidian/Documents/DrRahmaniPreProject/tfidf_results"  
# Get only CVS files in the folder
files = os.listdir(folder_path)

labels = []
vectors = []

# Iterate over the files
for file in files:
    if file.endswith(".csv"):  # Check if the file is a CSV file
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            label = re.sub(r"[()'',.csv]",'', file)
            for vector in csv_reader:
                vectors.append(vector)
                labels.append(label)

# Pad vectors with zeros to have equal length
max_len = len(max(vectors, key=len))
for i in range(len(vectors)):
    while len(vectors[i]) < max_len:
        vectors[i].append(0.0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(vectors, labels, test_size=0.2, random_state=20)

# Train the decision tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Display the decision tree
fig, ax = plt.subplots(figsize=(12, 12))
tree.plot_tree(model, feature_names=None, class_names=None, filled=True)
plt.savefig("/home/asma-rashidian/Documents/DrRahmaniPreProject/decision_tree.png", dpi=300)
plt.show()

# Evaluate the model
y_pred = model.predict(X_test)
classification_report = classification_report(y_test, y_pred)
accuracy = model.score(X_test, y_test)

# Print the results
print("Classification Report:")
print(classification_report)
print("Accuracy:", accuracy)