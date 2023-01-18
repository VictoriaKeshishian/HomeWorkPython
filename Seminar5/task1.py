# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв""

text = 'Высокий уровень вовлечабв представителей целевой аудитории является четкабв дабввлений прогрессивного развития'
print(text)
list_text = text.split(sep = ' ')
find_txt = "абв"
result = list(filter(lambda x: True if find_txt not in x else False, list_text))
print(result)