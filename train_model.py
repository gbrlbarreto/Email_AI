import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Carregar dataset rotulado, ignorando linhas sem label
df = pd.read_csv("emails_rotulados_balanceado.csv", encoding="latin1")
df = df.dropna(subset=["label"])
df["label"] = df["label"].astype(int)

print("Distribuição dos rótulos:\n", df['label'].value_counts())

emails = df["email"].tolist()
labels = df["label"].tolist()

X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred, labels=[0,1], target_names=["Improdutivo", "Produtivo"]))

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/email_classifier_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("Modelo treinado e salvo com sucesso.")
