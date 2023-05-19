#zad4
# Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.

data = [1,2,3,4,5,6,7,8,9,10]

def show_tabliczka(num1, num2):

    if num1 > 10:
        print(num1*num2)
    return()



for row in data:
    row_num = row
    for column in data:
        column_num = column
        print(row_num*column_num, end="\t")
    print()


#zad5
# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
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

#zad6
# Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

z = days.values()
z=set(z)
tab =list(z)
print(tab)
print(list(z))


d = dict()
for j in tab:
    if j in d:
        d[j] += 1
    else:
        d[j] = 1
print(d)

#zad7
# Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

set_list=set(example_list)
print(set_list)

tuple_list =tuple(set_list)
print(min(tuple_list))
print(max(tuple_list))

#Zad8

# Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej.
# Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
france = ['Emma', 'Jade', 'Louise', 'Alice', 'Chloé', 'Lina', 'Léa', 'Rose', 'Anna', 'Mila']
spain = ['Martina', 'Julia', 'Laia', 'Lucia', 'Maria', 'Emma', 'Noa', 'Paula', 'Ona', 'Aina']
germany = ['Sophie', 'Marie', 'Maria', 'Mia', 'Sophia', 'Emma', 'Anna', 'Hannah', 'Johanna', 'Leonie']
poland = ['Anna', 'Maria', 'Katarzyna', 'Małgorzata', 'Agnieszka', 'Barbara', 'Ewa ', 'Krystyna', 'Elżbieta', 'Magdalena']
italy = ['Sofia', 'Giulia', 'Aurora', 'Alice', 'Ginevra', 'Emma', 'Giorgia', 'Greta', 'Beatrice', 'Anna']
portugese = ['Maria', 'Matilde', 'Leonor', 'Beatriz ', 'Mariana', 'Carolina', 'Ana', 'Inês', 'Sofia', 'Margarida']
hungary = ['Hanna', 'Zoé', 'Anna', 'Emma', 'Luca', 'Lena', 'Zsófia', 'Boglárka', 'Jázmin', 'Lili']
turkey = ['Elif ', 'Zeynep', 'Hiranur', 'Miray', 'Zehra', 'Ecrin', 'Azra', 'Eylül', 'Defne', 'Nehir']
danmark = ['Eva', 'Emma', 'Hanna', 'Maria', 'Ró', 'Elsa', 'Lea', 'Sofía', 'Isabella', 'Lilja']
litwa = ['Irena', 'Janina', 'Ona', 'Danutė', 'Regina', 'Aldona', 'Kristina', 'Elena', 'Marija', 'Viktorija']


list_100 =france + spain + germany + poland + italy + portugese + hungary + turkey + danmark + litwa




d = dict()
for j in list_100:
    if j in d:
        d[j] += 1
    else:
        d[j] = 1

print(d)

for klucz, wartosc in d.items():
    if wartosc > 3:

        print(klucz, '-', wartosc)





# Zad9▹ 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi,
# drukowanymi lub zaczynając od dużej litery)
tablica1 = []
tablica2 = []
tablica3 = []
tablica4 = []
tablica5 = []
for _ in range(1,5):
    item1 = input(f"Użytkowniku 1. Podaj {_} przedmiot szkolny, który chcesz dodać do listy -> ")
    tablica1.append(item1.upper())
for _ in range(1,5):
    item2 = input(f"Użytkowniku 2. Podaj {_} przedmiot szkolny, który chcesz dodać do listy -> ")
    tablica2.append(item2.upper())
for _ in range(1,5):
    item3 = input(f"Użytkowniku 3. Podaj {_} przedmiot szkolny, który chcesz dodać do listy -> ")
    tablica3.append(item3.upper())
for _ in range(1, 5):
    item4 = input(f"Użytkowniku 4. Podaj {_} przedmiot szkolny, który chcesz dodać do listy -> ")
    tablica4.append(item4.upper())
for _ in range(1, 5):
    item5 = input(f"Użytkowniku 5. Podaj {_} przedmiot szkolny, który chcesz dodać do listy -> ")
    tablica5.append(item5.upper())





tablica = tablica1 + tablica2 + tablica3 + tablica4 +tablica5


d = dict()
for j in tablica:
    if j in d:
        d[j] += 1
    else:
        d[j] = 1

print(d)


items = d.items()
print(sorted(items, key=lambda x: x[1], reverse = True))

# Zad10▹ Użytkownik podaje dowolną liczbę N. Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie
# przyporządkowany jest jej kwadrat (n : n * n).
#
# Załóżmy, że użytkownik podał N = 8
#
# Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


num = int(input('Podaj liczbę '))
d = {}
for i in range(1,num+1):
    d[i] = i *i
print(d)