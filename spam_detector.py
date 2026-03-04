from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# 1️⃣ Datos de ejemplo
mensajes = [
    "Gana dinero gratis ahora",
    "Hola, ¿cómo estás?",
    "Oferta exclusiva solo por hoy",
    "Reunión mañana a las 10",
    "Felicidades ganaste un premio",
    "Nos vemos el fin de semana"
]

etiquetas = ["spam", "no spam", "spam", "no spam", "spam", "no spam"]

# 2️⃣ Convertir texto en números
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(mensajes)

# 3️⃣ Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X, etiquetas, test_size=0.2, random_state=42
)

# 4️⃣ Crear modelo
modelo = MultinomialNB()

# 5️⃣ Entrenar
modelo.fit(X_train, y_train)

# 6️⃣ Probar mensaje nuevo
mensaje_nuevo = ["Ganaste dinero urgente"]
mensaje_vectorizado = vectorizador.transform(mensaje_nuevo)

prediccion = modelo.predict(mensaje_vectorizado)

print("El mensaje es:", prediccion[0])