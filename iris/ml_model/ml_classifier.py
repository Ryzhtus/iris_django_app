import joblib
import sklearn


# print(iris_classifier.predict([[5.1, 3.5, 1.4, 0.2]]))
# [[5.1, 3.5, 1.4, 0.2]]


def predict(params, model_path: str) -> int:
    iris_classifier = joblib.load(model_path)
    return iris_classifier.predict(params)


def string_category(category: int) -> str:
    if category == 0:
        return 'Setosa'
    elif category == 1:
        return 'Versicolor'
    else:
        return 'Virginica'