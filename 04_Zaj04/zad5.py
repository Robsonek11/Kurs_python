poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""


poem = poem.lower().replace(",", "").split()
print(poem)
counting_words={}
for word in poem:
    if word in counting_words:
        counting_words[word] += 1
    else:
        counting_words[word] = 1
print(counting_words)

for word, counter in counting_words.items():
    print('*', word,"-", counter)