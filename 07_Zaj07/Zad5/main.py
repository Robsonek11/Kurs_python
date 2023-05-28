from areas import square, triangle, rectangle, circle
def get_user_rooms():
    while True:
        rooms = {
            "square": [],
            "circle": [],
            'rectangle': []
        }
        options = """ Dostępne kszztałty pokoi
        1 - kwadrat
        2 -koło
        3- prostokąt      
        
        """
        print(options)
        room_type =int(input('jaki typ pokoju chcesz dodać(1,2,3,'))
        if room_type =='1':
            a=float(input  )
def main():


    total = 0
    rooms = get_user_rooms()
    for shape, space in rooms.items():
        if shape == "square":
            for wall in space:
                total += square(wall)
        if shape == "circle":
            for radius in space:
                total += circle(radius)
        if shape == "retangle":
            for wall in space:
                a,b = wall
                total += rectangle(a, b)

    print(total)
if __name__=='__main__':
    main()