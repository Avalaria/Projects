import rdflib
import csv
import re

file_path = 'LIdioms-master/rus/russian.ttl' 

g = rdflib.Graph()
g.parse(file_path, format="turtle")

with open('idioms_clean.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Idiom', 'Language'])

    count = 0
    # Функция для проверки, есть ли в строке русские буквы
    def has_cyrillic(text):
        return bool(re.search('[а-яА-ЯёЁ]', text))

    for subj, pred, obj in g:
        # Если объект - это текст
        if isinstance(obj, rdflib.Literal):
            text = str(obj).strip()
            
                        # Проверяем: длина больше 3 символов И есть русские буквы
            if len(text) > 3 and has_cyrillic(text):
                # Оставляем только русские буквы и пробелы (удаляем всё остальное)
                text = re.sub(r'[^а-яА-ЯёЁ\s]', '', text)
                # Убираем лишние пробелы (заменяем несколько пробелов на один)
                text = " ".join(text.split())
                
                # Записываем очищенный текст
                writer.writerow([text, "rus"])
                count += 1
                
    print(f"Готово! Найдено и сохранено {count} русских строк в файл 'idioms_clean.csv'.")
