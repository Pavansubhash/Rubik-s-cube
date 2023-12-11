# Red_Front=[['w' for i in range(3)]for i in range(3)]

# Yellow_Right=[['B' for i in range(3)]for i in range(3)]

# Blue_Down=[['R' for i in range(3)]for i in range(3)]

# Green_Left=[['G' for i in range(3)]for i in range(3)]

# White_Up=[['O' for i in range(3)]for i in range(3)]

# Orange_Back=[['Y' for i in range(3)]for i in range(3)]


def downShift(Front,Right,Down,Left,Up,Back):

    t1 = Front[2][0]
    t2 = Front[2][1]
    t3 = Front[2][2]

    Front[2][0] = Left[2][0]
    Front[2][1] = Left[2][1]
    Front[2][2] = Left[2][2]

    Left[2][0] = Back[0][2]
    Left[2][1] = Back[0][1]
    Left[2][2] = Back[0][0]

    Back[0][2] = Right[2][0]
    Back[0][1] = Right[2][1]
    Back[0][0] = Right[2][2]
 
    Right[2][0] = t1
    Right[2][1] = t2
    Right[2][2] = t3

    temp1=Down[0][0]
    temp2=Down[1][0]
    temp3=Down[2][0]

    Down[0][0]=Down[2][0]
    Down[1][0]=Down[2][1]
    Down[2][0]=Down[2][2]

    Down[2][0]=Down[2][2]
    Down[2][1]=Down[1][2]
    Down[2][2]=Down[0][2]

    Down[2][2]=Down[0][2]
    Down[1][2]=Down[0][1]
    Down[0][2]=Down[0][0]

    Down[0][2]=temp1
    Down[0][1]=temp2
    Down[0][0]=temp3

    return Front,Right,Down,Left,Up,Back


# Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=downShift(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)
# print("uppp")
# for each in White_Up:
#     print(each)
# print("front")
# for each in Red_Front:
#     print(each)
# print("down")
# for each in Blue_Down:
#     print(each)
# print("back")
# for each in Orange_Back:
#     print(each)
# print("right")
# for each in Yellow_Right:
#     print(each)
# print("left")
# for each in Green_Left:
#     print(each)