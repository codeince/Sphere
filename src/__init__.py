from json import loads, dumps
from time import time
from random import choice, seed

answers: dict[dict[str, list[str]]] = loads(open('src/answers.json', 'r', encoding='utf-8').read()).get('answers')
answers = loads(dumps(answers, ensure_ascii=False))

def capitalize(text: str) -> str:
    return text[0].upper() + text[1:]

class Answer:
    def __init__(self, question: str):
        seed(int(time()))
        self.question = capitalize(question if question.endswith('?') else f'{question}?')
        self.answer = self._generate_answer()
    
    def _generate_answer(self):
        for answers_ in answers.values():
            if True in [word in answers_.get('masks') for word in self.question.lower().split()]:
                return capitalize(choice(answers_.get('answers')))
        else:
            return capitalize(choice(answers.get('bool').get('answers')))
    
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