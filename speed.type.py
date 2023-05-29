import random
import time


paragraphs = [
    "Через час отсюда в чистый переулок вытечет по человеку ваш обрюзгший жир, а я вам открыл столько стихов шкатулок, "
    "я бесценных слов мот и транжир.",
    "Я сразу смазал карту будня, плеснувши краску из стакана я показал на блюде студня косые скулы океана.  "
    "На чешуе жестяной рыбы прочел я зовы новых губ.",
    "Послушайте! Ведь, если звезды зажигают  значит - это кому-нибудь нужно? Значит - кто-то хочет, чтобы они были? "
    " Значит - кто-то называет эти плевочки",
    "Ночь, улица, фонарь, аптека, Бессмысленный и тусклый свет. Живи еще хоть четверть века - Все будет так. Исхода  "
    "нет. Умрешь - начнешь опять сначала",
]


paragraph = random.choice(paragraphs)
words = paragraph.split()

start_time = time.time()

char_count = 0
error_count = 0

for word in words:
    print(word, end=" ")
    char_count += len(word) + 1

    user_input = input()

    while user_input != word:
        print("Ошибка! Попробуйте еще раз.")
        user_input = input()
        error_count += 1

    if user_input == word:
        continue

# останавливаем отсчет времени
end_time = time.time()

elapsed_time = end_time - start_time

with open("результаты.txt", "a", encoding="utf-8") as f:
    f.write(f'Колличество символов: {char_count} | Колличество ошибок: {error_count} | Время: {round(elapsed_time)} | '
            + '\n')

with open("результаты.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

# создаем список результатов
results = []
for line in data:
    parts = line.split("|")
    char_count = int(parts[0].split(":")[1].strip())
    error_count = int(parts[1].split(":")[1].strip())
    time = int(parts[2].split(":")[1].strip())
    results.append((char_count, error_count, time))

# сортируем результаты по времени выполнения теста
results.sort(key=lambda x: x[2])

# находим место пользователя в списке результатов
place = results.index((char_count, error_count, round(elapsed_time))) + 1
print(f'Вы ввели: {char_count} символов за : {round(elapsed_time)} секунд')
print(f'Вы допустили: {error_count} ошибок')
print(f'Вы заняли {place} место в рейтинге')
