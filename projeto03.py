import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import random

# Baixe os recursos necessários do NLTK (execute apenas uma vez)
nltk.download('punkt')
nltk.download('stopwords')

# Conjunto de dados de exemplo para perguntas e respostas
data = {
    'Olá': ['Olá! Como posso te ajudar?', 'Oi! Qual é a sua dúvida?'],
    'Como você está?': ['Estou bem, obrigado por perguntar.', 'Estou aqui para ajudar, não posso sentir emoções!'],
    'O que é inteligência artificial?': ['Inteligência artificial (IA) é a simulação de processos de inteligência humana por máquinas.', 'IA refere-se à capacidade de uma máquina pensar e aprender.'],
    'Quem criou você?': ['Fui criado por um time de desenvolvedores.', 'Sou o resultado do trabalho de muitas pessoas talentosas.'],
    'Qual o sentido da vida?': ['Essa é uma pergunta filosófica profunda!', 'O sentido da vida é algo que as pessoas tentam descobrir ao longo da existência.']
}

# Pré-processamento dos dados
def preprocess_text(text):
    stop_words = set(stopwords.words('portuguese'))
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Encontrar uma resposta para a pergunta
def get_answer(question):
    question_tokens = preprocess_text(question)
    for q, a_list in data.items():
        for a in a_list:
            if all(token in preprocess_text(a) for token in question_tokens):
                return random.choice(a_list)
    return "Desculpe, não tenho a resposta para essa pergunta."

class ChatbotApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.chat_history = TextInput(size_hint_y=0.9, readonly=True, multiline=True)
        self.question_input = TextInput(size_hint_y=0.1)
        self.question_input.bind(on_text_validate=self.ask_question)
        self.layout.add_widget(self.chat_history)
        self.layout.add_widget(self.question_input)
        return self.layout

    def ask_question(self, instance):
        question = instance.text
        answer = get_answer(question)
        self.chat_history.text += f'\nUsuário: {question}\nBot: {answer}\n'
        instance.text = ""

if __name__ == '__main__':
    ChatbotApp().run()
