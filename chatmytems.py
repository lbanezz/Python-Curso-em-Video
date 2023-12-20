import tkinter as tk
from tkinter import scrolledtext, messagebox
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import string


# Baixe os recursos necessários do NLTK (execute apenas uma vez)
nltk.download('punkt')
nltk.download('stopwords')

# Carregue um conjunto de dados de exemplo (você pode adicionar mais dados)
data = {
    'O que é inteligência artificial?': 'Inteligência artificial (IA) é a simulação de processos de inteligência humana por máquinas, especialmente sistemas de computador.',
    'O que é aprendizado de máquina?': 'Aprendizado de máquina é um campo da inteligência artificial que permite que os sistemas aprendam automaticamente e melhorem com a experiência sem serem explicitamente programados.',
    'Quais são os tipos de aprendizado de máquina?': 'Existem três tipos principais de aprendizado de máquina: supervisionado, não supervisionado e por reforço.'
    ''
}

# Pré-processamento dos dados
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Encontre a resposta para a pergunta
def get_answer(question):
    question_tokens = preprocess_text(question)
    for q, a in data.items():
        if all(token in preprocess_text(a) for token in question_tokens):
            return a
    return "Desculpe, não tenho a resposta para essa pergunta."

# Função para lidar com a pergunta e exibir a resposta
def answer_question():
    question = question_text.get("1.0", tk.END)
    answer = get_answer(question)
    answer_text.delete("1.0", tk.END)
    answer_text.insert(tk.END, answer)

# Criar a interface gráfica
root = tk.Tk()
root.title("Sistema de Perguntas e Respostas")

question_label = tk.Label(root, text="Faça sua pergunta:")
question_label.pack()

question_text = scrolledtext.ScrolledText(root, height=5)
question_text.pack()

answer_label = tk.Label(root, text="Resposta:")
answer_label.pack()

answer_text = scrolledtext.ScrolledText(root, height=10)
answer_text.pack()

answer_button = tk.Button(root, text="Obter Resposta", command=answer_question)
answer_button.pack()

root.mainloop()
