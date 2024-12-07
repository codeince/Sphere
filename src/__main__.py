from __init__ import Sphere, lang_build

from rich.console import Console

c = Console()
c.clear()
guesser = Sphere()

while True:
    if len(guesser) > 0:
        guesser.init_txt()
        print(guesser, end='\n\n')
    question = input(lang_build.get('type_text'))
    if question.lower() in lang_build.get('stop_words'):
        exit()
    guesser.ask(question)
    c.clear()