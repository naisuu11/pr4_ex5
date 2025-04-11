people = [("Никита", 18), ("Най-Суу", 17), ("Максим", 19), ("Николай", 20)]
sorted_people = sorted(people, key=lambda person: person[1])
print("Список отсортированных по возрасту:")
for name, age in sorted_people:
    print(f"{name}: {age}")
words = ["яблоко", "банан", "апельсин", "мандарин", "виноград", "киви"]
vowel_words = list(filter(lambda word: word[0].lower() in 'аоу', words))
print("\nСлова, начинающиеся с гласной буквы:")
print(vowel_words)