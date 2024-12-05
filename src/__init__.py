from time import time
from random import choice, seed

answers = [
    'да',
    'возможно',
    'возможно, стоит попробовать',
    'врят ли',
    'все зависит от обстоятельств',
    'все указывает на да',
    'это не лучший выбор',
    'это не так просто',
    'это хорошая идея',
    'это может сработать',
    'не теряй надежды',
    'не стоит на это надеяться',
    'не уверен, но есть шансы',
    'нет',
    'определенно, да',
    'определенно, нет',
    'скорее, да, чем нет',
    'скорее, нет, чем да',
    'сложно сказать, попробуй еще раз',
    'судя по всему, нет',
    'скоро узнаешь',
    'время покажет',
    'лучше не рисковать'
]

def capitalize(text: str) -> str:
    return text[0].upper() + text[1:]

class Answer:
    def __init__(self, question: str):
        seed(int(time()))
        self.question = capitalize(question if question.endswith('?') else f'{question}?')
        self.answer = self._generate_answer()
    
    def _generate_answer(self):
        return capitalize(choice(answers))
    
    def __str__(self) -> str:
        return f'Вопрос: {self.question}\nОтвет: {self.answer}'
    
class Sphere(list[Answer]):
    def __init__(self):
        super().__init__()
        self.init_txt()

    def init_txt(self):
        print('Шар Гадалка!\nЗаписывайтесь по номеру телефона 8(800)555-35-35\nЦена: 100000 рублей за запрос:)\n')

    def ask(self, question: str) -> str:
        answer = Answer(question)
        self.append(answer)
        return answer.answer
    
    def __str__(self) -> str:
        return '\n\n'.join(str(answer) for answer in self)