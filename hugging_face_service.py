import joblib
import os

# Carrega o classificador e o vetor TF-IDF
model = joblib.load('models/email_classifier_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

def classify_email(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return 'Produtivo' if prediction == 1 else 'Improdutivo'

def generate_response(text, category):
    if category == 'Produtivo':
        return "Obrigado pelo seu email. Encaminharemos sua solicitação em breve."
    else:
        return "Agradecemos sua mensagem."