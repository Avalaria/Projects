import csv
import json
import re
from pymystem3 import Mystem

# 1. Инициализируем Mystem
mystem = Mystem()

# Имя твоего файла с идиомами, который мы недавно сделали
input_file = 'idioms_clean.csv'
output_file = 'idioms_final.json'

# Список для хранения финальных лемматизированных идиом
lemmatized_idioms = set() # Используем set, чтобы автоматически удалить дубликаты

print("Начинаем лемматизацию идиом...")

# 2. Читаем CSV файл
with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader) # Пропускаем первую строку (заголовки "Idiom;Language")
    
    for row in reader:
        if not row:
            continue
            
        idiom_raw = row[0].strip()
        
        # 3. Очистка и подготовка к Mystem
        # Приводим к нижнему регистру
        idiom_lower = idiom_raw.lower()
        
        # Удаляем всё, кроме букв и пробелов (на всякий случай, если что-то осталось)
        idiom_clean = re.sub(r'[^а-яё\s]', '', idiom_lower)
        
        # Если строка пустая после очистки — пропускаем
        if not idiom_clean:
            continue

        # 4. Лемматизация
        lemmas = mystem.lemmatize(idiom_clean)
        
        # Склеиваем обратно в строку, убирая пустые элементы (пробелы, переносы)
        idiom_lemmatized = " ".join([word for word in lemmas if word.strip()])
        
        if idiom_lemmatized:
            lemmatized_idioms.add(idiom_lemmatized)

# 5. Сохраняем результат в JSON
with open(output_file, 'w', encoding='utf-8') as f:
    # Преобразуем set обратно в list для сохранения
    json.dump(list(lemmatized_idioms), f, ensure_ascii=False, indent=4)

print(f"Готово! Обработано и сохранено {len(lemmatized_idioms)} уникальных идиом в файл {output_file}")