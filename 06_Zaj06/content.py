with open('Pan_Tadeusz.txt') as fileopen:
    # while True:

        # current_line =fopen.readline()
        # # print(fopen.readline())
    content_list = fileopen.readlines()
    print(content_list)
    for line in content_list:
        print(line)

