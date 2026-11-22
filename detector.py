import json

# Загружаем наши лемматизированные идиомы
with open('idioms_final.json', 'r', encoding='utf-8') as f:
    idioms = json.load(f)

# Для удобства разобьем каждую идиому на список слов
# Например, "из кожа вон лезть" -> ["из", "кожа", "вон", "лезть"]
idioms_split = [idiom.split() for idiom in idioms]

def find_idioms_in_text(text_lemmas, window_size=6):
    """
    text_lemmas: список лемм (например, ['он', 'съесть', 'собака', 'на', 'этот', 'дело'])
    window_size: максимальное расстояние между первым и последним словом идиомы
    """
    found = []
    
    # Проходим по тексту скользящим окном
    for i in range(len(text_lemmas)):
        # Берем кусочек текста (окно) начиная с текущего слова
        window = text_lemmas[i : i + window_size]
        
        # Проверяем каждую идиому
        for idiom_parts in idioms_split:
            # Если все слова идиомы есть внутри нашего окна...
            if all(word in window for word in idiom_parts):
                # ...и они идут в правильном порядке
                # (это упрощенная проверка, чтобы не было совсем уж ложных срабатываний)
                indices = [window.index(word) for word in idiom_parts if word in window]
                if indices == sorted(indices): 
                    idiom_str = " ".join(idiom_parts)
                    if idiom_str not in found:
                        found.append(idiom_str)
                        
    return found

# --- ТЕСТИРУЕМ ---
# Пример текста от Кости (список лемм)
test_text = ["он", "съесть", "на", "этот", "собака", "зубы", "и", "бить", "баклуша"]

result = find_idioms_in_text(test_text, window_size=6)
print("Найденные идиомы:", result)