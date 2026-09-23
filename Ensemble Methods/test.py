

from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from utils import calculate_disagreement, ensemble_diversity_matrix

# Generate some data
X, y = make_classification(
    n_samples=1000, n_features=20, n_informative=10,
    n_redundant=2, random_state=42
)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create a voting classifier
voting_classifier = VotingClassifier(
    estimators=[
        ('knn', KNeighborsClassifier(n_neighbors=5)),
        ('dt', DecisionTreeClassifier(max_depth=5)),
        # ('svc', SVC(kernel='linear', probability=True))
        ('lr', LogisticRegression(max_iter=1000)),
        ('rf', RandomForestClassifier(n_estimators=100))
    ],
    voting='soft'
)

# Train the voting classifier
voting_classifier.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = voting_classifier.predict(X_test)

# Calculate the accuracy of the voting classifier
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Calculate the disagreement between the voting classifier and the majority class
disagreement = calculate_disagreement(
    voting_classifier, 
    LogisticRegression(max_iter=1000).fit(X_train, y_train),
    X_test
)
print(f'Disagreement: {disagreement:.2f}')

diversity_matrix = ensemble_diversity_matrix(
    [
        KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train),
        DecisionTreeClassifier(max_depth=5).fit(X_train, y_train),
        # SVC(kernel='linear', probability=True).fit(X_train, y_train),
        LogisticRegression(max_iter=1000).fit(X_train, y_train),
        RandomForestClassifier(n_estimators=100).fit(X_train, y_train)
    ],
    X_test
)
print(diversity_matrix)