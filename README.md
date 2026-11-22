# О чем проект в целом?
Я пишу ВКР на тему: "Технология автоматизированной разметки фразеологизмов в сбалансированном лингвистическом корпусе". Поэтому моя цель на ближайший год - узнать, что и как люди уже умеют делать в этой сфере и что можно привнести в разработанный в МГЛУ корпусный менеджер.

# Про файлы
1. **LIdioms-master**
Папка с датасетом. Люди уже составили список фразеологизмов, нашли по ссылке: https://github.com/dice-group/LIdioms/ (Дата обращения: 3 ноя 2026).

2. **`convert.py`**
*   **Задача:** Извлечь данные из «сырого» графа знаний LIdioms (файлы `.ttl`) и конвертировать их в удобный табличный формат (CSV). 
*   **Что делает:** Читает RDF-файл, отфильтровывает мусор и английские переводы, оставляя только русские идиомы, очищает их от знаков ударения и сохраняет в файл `idioms_clean.csv`.

3. **`prepare_idioms.py`**
*   **Задача:** Подготовить словарь идиом к сравнению с текстами, которые придет от Кости.
*   **Что делает:** Берет CSV-файл с идиомами, приводит их к нижнему регистру, прогоняет через морфологический анализатор `pymystem3` (лемматизирует) и сохраняет результат в виде чистого JSON-списка (`idioms_final.json`), удаляя дубликаты.

4. **`detector.py` (не проверен)**
*   **Задача:** Найти фразеологизмы в массиве текстов.
*   **Что делает:** Загружает готовый словарь `idioms_final.json` и тексты статей (состоящие из лемм). Использует метод «скользящего окна» (по 5–7 слов), чтобы найти идиомы внутри предложений, проверить правильный порядок слов и избежать ложных срабатываний (когда слова из идиомы случайно оказались в разных частях статьи).

# Источники
LIdioms-master
@InProceedings{Moussallem18_LREC,
  author = {Diego Moussallem ,Mohamed Ahmed Sherif ,Diego Esteves ,Marcos Zampieri and Axel-Cyrille Ngonga Ngomo},
  title = {LIdioms: A Multilingual Linked Idioms Data Set},
  booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year = {2018},
  month = {may},
  date = {7-12},
  location = {Miyazaki, Japan},
  editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and Hélène Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},
  publisher = {European Language Resources Association (ELRA)},
  address = {Paris, France},
  isbn = {979-10-95546-00-9},
  language = {english}
  }
