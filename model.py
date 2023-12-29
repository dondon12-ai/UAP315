import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Data
data = pd.read_csv('income.csv')  # Ganti 'nama_file.csv' dengan nama file yang sesuai

# Preprocessing Data
data = data.dropna()


le = LabelEncoder()
categorical_cols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country']

for col in categorical_cols:
    data[col] = le.fit_transform(data[col])

data = data.drop(['fnlwgt', 'education', 'relationship', 'native-country','race','educational-num'], axis=1)



X = data.drop('income_>50K', axis=1)
y = data['income_>50K']

print(data.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training Model
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)
pickle.dump(rf_classifier, open("model.pkl", "wb"))