import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.linear_model import LogisticRegression

# Use only normalized.csv
df = pd.read_csv("normalized.csv")

# README schema: customer_id is an identifier; churn is the target
X = df.drop(columns=["customer_id", "churn"])
y = df["churn"].astype(int)

cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
num_cols = [c for c in X.columns if c not in cat_cols]

preprocess = ColumnTransformer(
    transformers=[
        (
            "num",
            Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ]),
            num_cols,
        ),
        (
            "cat",
            Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore"))
            ]),
            cat_cols,
        ),
    ],
    remainder="drop"
)

model = LogisticRegression(
    max_iter=5000,
    class_weight="balanced",
    solver="liblinear",
    random_state=42,
)

pipe = Pipeline([
    ("preprocess", preprocess),
    ("model", model),
])

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipe.fit(X_train, y_train)
pred = pipe.predict(X_val)

acc = accuracy_score(y_val, pred)
f1 = f1_score(y_val, pred, pos_label=1)
prec = precision_score(y_val, pred, pos_label=1, zero_division=0)
rec = recall_score(y_val, pred, pos_label=1, zero_division=0)

print(f"Accuracy: {acc:.4f}")
print(f"F1: {f1:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall: {rec:.4f}")