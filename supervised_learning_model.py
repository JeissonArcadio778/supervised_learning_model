from dataset import sample_dataset
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.linear_model import LinearRegression  # type: ignore

# Importamos el módulo de codificación para transformar los datos categóricos en numéricos
from sklearn.preprocessing import OneHotEncoder


def supervised_learning_model():
    """
    Entrena un modelo de regresión lineal con el conjunto de datos de muestra y realiza predicciones.
    :return: Predicciones del modelo.
    """
    # Codificamos las variables categóricas
    encoder = OneHotEncoder()
    encoded_data = encoder.fit_transform(
        sample_dataset[["Time of Day", "Day of the Week", "Season of the Year"]]
    ).toarray()

    # Dividimos los datos en características (X) y etiquetas (y)
    X = encoded_data
    y = sample_dataset["Number of Passengers"].values

    # Dividimos los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenamos un modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Realizamos predicciones con el modelo entrenado
    predictions = model.predict(X_test)

    # Imprimimos las predicciones
    return "Predicciones del modelo:", predictions
