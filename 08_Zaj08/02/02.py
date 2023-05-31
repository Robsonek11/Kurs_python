# Utwórz dowolną krotkę zawierającą kilka wartości np.10.Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie.Obsłuż błąd

def main():
    tup_mixed = (1, 'dwa', [3, 4.1], 4, 'pięć', True, False,'osiem', None, 123.45 )
    num = int(input('podaj index '))
    value = input('podaj wartość ')
    try:
           tup_mixed[num] = value
           print(tup_mixed[num])
    except (IndexError, TypeError) as te:
            print(te)


if __name__ == "__main__":
    main()