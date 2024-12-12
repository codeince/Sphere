from __init__ import Sphere
from json import loads, dumps

lang = 'ru'
lang_build = loads(open(f'src/langs/{lang}.json', 'r', encoding='utf-8').read())
lang_build = (lang_build if lang_build.get('lang') == 'en' else loads(dumps(lang_build, ensure_ascii=False))).get('text')

answers: dict[dict[str, list[str]]] = loads(open(f'src/langs/answer_files/answers_{lang}.json', 'r', encoding='utf-8').read())
answers = (answers if answers.get('lang') == 'en' else loads(dumps(answers, ensure_ascii=False))).get('answers')

from rich.console import Console

c = Console()
c.clear()
guesser = Sphere(lang_build, answers)



while True:
    if len(guesser) > 0:
        guesser.init_txt()
        print('\n'.join([answer.to_str(lang_build.get('answer_formatting')) for answer in guesser]), end='\n\n')
    question = input(lang_build.get('type_text'))
    if question.lower() in lang_build.get('stop_words'):
        exit()
    guesser.ask(question)
    c.clear()