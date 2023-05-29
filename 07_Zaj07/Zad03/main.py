from Test import open_file, write_file

def main():
    content = open_file("text.txt")
    print(content)

    text_to_save = "Lalalal\n123"
    write_file('lala.txt', text_to_save)

if __name__ == "__main__":
    main()