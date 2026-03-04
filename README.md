Spam Detector con Machine Learning

Este proyecto implementa un clasificador básico de mensajes spam utilizando técnicas de Procesamiento de Lenguaje Natural (NLP) y Machine Learning.

 ¿Cómo funciona?

1. Convierte texto en números usando `CountVectorizer`.
2. Divide los datos en entrenamiento y prueba.
3. Entrena un modelo `Multinomial Naive Bayes`.
4. Clasifica nuevos mensajes como:
   - SPAM
   - NO SPAM

 Tecnologías utilizadas

- Python
- scikit-learn
- CountVectorizer
- MultinomialNB

 Cómo ejecutarlo

1. Instalar dependencias:

pip install scikit-learn pandas

2. Ejecutar el programa:

python spam_detector.py

 Ejemplo

Entrada:
"Ganaste dinero urgente"

Salida:
spam

---

Proyecto educativo para aprender fundamentos de Machine Learning y clasificación de texto.
