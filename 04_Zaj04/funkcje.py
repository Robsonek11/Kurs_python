def my_mood(answer):
    print('My mood today:')
    print(answer)


resp = input("how are you?")
my_mood(resp)

def my_mood2(answer):
    return answer *2


resp = input("how are you?")
twiced = my_mood2(resp)
print('my mood is like', twiced)