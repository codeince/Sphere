from time import time
from json import loads, dumps
from string import punctuation
from random import choice, seed

lang_build = loads(open('src/langs/ru.json', 'r', encoding='utf-8').read())
lang_build = (lang_build if lang_build.get('lang') == 'en' else loads(dumps(lang_build, ensure_ascii=False))).get('text')

answers: dict[dict[str, list[str]]] = loads(open('src/langs/answer_files/answers_ru.json', 'r', encoding='utf-8').read())
answers = (answers if answers.get('lang') == 'en' else loads(dumps(answers, ensure_ascii=False))).get('answers')

def capitalize(text: str) -> str:
    return text[0].upper() + text[1:]

class Answer:
    def __init__(self, question: str):
        seed(int(time()))
        self.question = capitalize(question if question.endswith('?') else f'{question}?')
        self.answer = self._generate_answer()
    
    def _generate_answer(self):
        for answers_ in answers.values():
            if True in [word in answers_.get('masks') for word in self.question.lower().translate(str.maketrans(' ', ' ', punctuation)).split()]:
                return capitalize(choice(answers_.get('answers')))
        else:
            return capitalize(choice(answers.get('bool').get('answers')))
    
    def __str__(self) -> str:
        return lang_build.get('answer_formatting').format(question=self.question, answer=self.answer)
    
    def __dict__(self) -> dict:
        return {'question': self.question, 'answer': self.answer}
    
class Sphere(list[Answer]):
    def __init__(self):
        super().__init__()
        self.init_txt()

    def init_txt(self):
        print(lang_build.get('init_text'))

    def ask(self, question: str) -> str:
        answer = Answer(question)
        self.append(answer)
        return answer.answer
    
    def __str__(self) -> str:
        return '\n\n'.join(str(answer) for answer in self)