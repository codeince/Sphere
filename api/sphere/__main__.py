from sphere.__init__ import Sphere
from json import loads, dumps
from os import name, system
from string import digits
from os import path

def clear(): return system('cls' if name == 'nt' else 'clear')
def cur_dir(): return path.abspath(path.dirname(__file__))

resource_pack = 'sphere'
lang = 'ru'
lang_build = loads(open(f'{cur_dir()}/resources/{resource_pack}/langs/{lang}.json', 'r', encoding='utf-8').read())
lang_build: dict[str, str] = (lang_build if lang_build.get('lang') == 'en' else loads(dumps(lang_build, ensure_ascii=False))).get('text')

answers: dict[dict[str, list[str]]] = loads(open(f'{cur_dir()}/resources/{resource_pack}/langs/answer_files/answers_{lang}.json', 'r', encoding='utf-8').read())
answers = (answers if answers.get('lang') == 'en' else loads(dumps(answers, ensure_ascii=False))).get('answers')

if __name__=="__main__":
    seed = input(lang_build.get("custom_model_text"))
    try:
        seed = int(''.join([symbol for symbol in seed if symbol in digits]))
    except:
        seed = None
    clear()


    guesser = Sphere(lang_build, answers, seed)



    while True:
        if len(guesser) > 0:
            guesser.init_txt()
            print(guesser.to_str(lang_build.get('answer_formatting')), end='\n\n')
        question = input(lang_build.get('type_text'))
        if question.lower() in lang_build.get('stop_words'):
            exit()
        guesser.ask(question)
        clear()