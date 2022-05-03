from python_translator import Translator

print('\n TRANSLATOR \n')
prompt = '> '
translator = Translator()

while True:

    text = input(prompt)
    
    if text == 'q':
        break
    
    elif text == 'p':

        portuguese_text = input(prompt)

        result = translator.translate(portuguese_text, 'english', 'portuguese')
        print(f'\n{result}\n')
        continue

    elif text == 'e':

        english_text = input(prompt)

        result = translator.translate(english_text, 'portuguese', 'english')
        print(f'\n{result}\n')
        continue
