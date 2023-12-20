import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carregar os dados Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o classificador SVM
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

# Função para prever e calcular a precisão
def predict_and_evaluate():
    test_data = [float(entry1.get()), float(entry2.get()), float(entry3.get()), float(entry4.get())]
    prediction = svm.predict([test_data])
    messagebox.showinfo("Resultado", f"A flor é da espécie: {iris.target_names[prediction[0]]}")
    y_pred = svm.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    messagebox.showinfo("Precisão do Modelo", f"A precisão do modelo é: {accuracy}")

# Criar a interface gráfica
root = tk.Tk()
root.title("Classificação de Flores Iris")

label1 = tk.Label(root, text="Comprimento da sépala:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Largura da sépala:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Comprimento da pétala:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="Largura da pétala:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

predict_button = tk.Button(root, text="Prever", command=predict_and_evaluate)
predict_button.pack()

root.mainloop()
