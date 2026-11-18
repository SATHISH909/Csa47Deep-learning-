
import math
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Create loan applicant dataset
data = {
    'Income': ['High', 'High', 'Medium', 'Low', 'Low',
               'Medium', 'High', 'Low', 'Medium', 'High'],
    'Credit_Score': ['Good', 'Bad', 'Good', 'Bad', 'Good',
                     'Bad', 'Good', 'Bad', 'Good', 'Good'],
    'Risk': ['Low', 'High', 'Low', 'High', 'Low',
             'High', 'Low', 'High', 'Low', 'Low']
}

df = pd.DataFrame(data)

print("Loan Applicant Dataset:")
print(df)

# Calculate entropy
def calculate_entropy(target):
    values = target.value_counts(normalize=True)
    entropy = 0

    for probability in values:
        entropy -= probability * math.log2(probability)

    return entropy

entropy = calculate_entropy(df['Risk'])

print("\nEntropy of Dataset:")
print(round(entropy, 4))

# Encode categorical data
encoder = LabelEncoder()

X = df[['Income', 'Credit_Score']].apply(encoder.fit_transform)
y = encoder.fit_transform(df['Risk'])

# Train Decision Tree
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X, y)

# Predict risk
predictions = model.predict(X)

print("\nActual Risk:")
print(df['Risk'].values)

print("\nPredicted Risk:")
print(encoder.fit(df['Risk']).inverse_transform(predictions))

# Analyse uncertainty
if entropy == 0:
    print("\nDataset has no uncertainty.")
else:
    print("\nDataset contains classification uncertainty.")

print("\nDecision Tree Model:")
print("Model trained successfully.")
