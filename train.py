import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
    HistGradientBoostingClassifier,
    VotingClassifier,
    BaggingClassifier,
)
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import (
    LinearDiscriminantAnalysis,
    QuadraticDiscriminantAnalysis,
)

df = pd.read_csv("/home/w/AI_move/tank_data.csv")

X = df.drop(columns=("hit"))
y = df["hit"]
# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Các model cần thử
models = {
    "Logistic Regression": make_pipeline(
        StandardScaler(), LogisticRegression(max_iter=1000)
    ),
    "KNN": make_pipeline(StandardScaler(), KNeighborsClassifier()),
    "SVM": make_pipeline(StandardScaler(), SVC()),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Extra Trees": ExtraTreesClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "AdaBoost": AdaBoostClassifier(),
    "Hist Gradient Boosting": HistGradientBoostingClassifier(),
    "Bagging": BaggingClassifier(),
    "Naive Bayes": GaussianNB(),
    "Neural Network (MLP)": make_pipeline(
        StandardScaler(), MLPClassifier(max_iter=2000)
    ),
    "SGD Classifier": make_pipeline(StandardScaler(), SGDClassifier()),
    "LDA": LinearDiscriminantAnalysis(),
    "QDA": QuadraticDiscriminantAnalysis(),
}

# Huấn luyện và đánh giá
results = []

for name, model in models.items():
    try:
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)

        results.append((name, accuracy))

    except Exception as e:
        print(f"{name} failed: {e}")

# In kết quả từ accuracy cao xuống thấp
results.sort(key=lambda item: item[1], reverse=True)

print("\n===== MODEL ACCURACY =====")

for name, accuracy in results:
    print(f"{name:25s}: {accuracy:.4f} ({accuracy * 100:.2f}%)")
