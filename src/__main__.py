from __init__ import Sphere
from json import loads, dumps
from os import name, system

def clear(): return system('cls' if name == 'nt' else 'clear')

lang = 'ru'
lang_build = loads(open(f'{'/'.join(__file__.split('\\')[:-1])}/langs/{lang}.json', 'r', encoding='utf-8').read())
lang_build = (lang_build if lang_build.get('lang') == 'en' else loads(dumps(lang_build, ensure_ascii=False))).get('text')

answers: dict[dict[str, list[str]]] = loads(open(f'{'/'.join(__file__.split('\\')[:-1])}/langs/answer_files/answers_{lang}.json', 'r', encoding='utf-8').read())
answers = (answers if answers.get('lang') == 'en' else loads(dumps(answers, ensure_ascii=False))).get('answers')

guesser = Sphere(lang_build, answers)



while True:
    if len(guesser) > 0:
        guesser.init_txt()
        print(guesser.to_str(lang_build.get('answer_formatting')), end='\n\n')
    question = input(lang_build.get('type_text'))
    if question.lower() in lang_build.get('stop_words'):
        exit()
    guesser.ask(question)
    clear()