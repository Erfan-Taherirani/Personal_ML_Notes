

from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from utils import calculate_disagreement, calculate_diversity, calculate_prediction_correlations
from utils import evaluate_model_contributions

X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = [
    KNeighborsClassifier(n_neighbors=5),
    DecisionTreeClassifier(max_depth=5, random_state=42),
    LogisticRegression(max_iter=1000, random_state=42),
    RandomForestClassifier(n_estimators=100, random_state=42),
    # SVC(kernel='linear', random_state=42)
]

estimators = [
    ("knn", KNeighborsClassifier(n_neighbors=5)),
    ("dt", DecisionTreeClassifier(max_depth=5, random_state=42)),
    ("lr", LogisticRegression(max_iter=1000, random_state=42)),
    ("rf", RandomForestClassifier(n_estimators=100, random_state=42)),
    # ("svm", SVC(kernel='linear', random_state=42))
]

voting = VotingClassifier(estimators=estimators, voting='hard')
voting.fit(X_train, y_train)

# estimators = []
# for model in models:
#     estimators.append(model.fit(X_train, y_train))

# print(calculate_prediction_correlations(estimators, X_test))

# print(calculate_diversity(estimators, X_test))

print(f"Ensemble accuracy: {voting.score(X_test, y_test):.2f}")
print(f"Ensemble Model Contributions: {evaluate_model_contributions(voting, X_test, y_test)}")

