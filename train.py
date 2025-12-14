from features import load_dataset
from utils import normalize
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import numpy as np

X, y = load_dataset()
X = normalize(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

mlp = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation="logistic",
    solver="sgd",
    learning_rate_init=0.2,
    momentum=0.9,
    max_iter=500
)

mlp.fit(X_train, y_train)

print("Eğitim doğruluğu:", mlp.score(X_train, y_train))
print("Test doğruluğu:", mlp.score(X_test, y_test))

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


print(len(y_test))
print(np.bincount(y_test))


y_pred = mlp.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=["EVET", "HAYIR"])

disp.plot()
plt.title("Confusion Matrix (Test)")
plt.show()
