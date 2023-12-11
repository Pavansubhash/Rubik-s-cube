# Front=[['w' for i in range(3)]for i in range(3)]

# Right=[['B' for i in range(3)]for i in range(3)]

# Down=[['R' for i in range(3)]for i in range(3)]

# Left=[['G' for i in range(3)]for i in range(3)]

# Up=[['O' for i in range(3)]for i in range(3)]

# Back=[['Y' for i in range(3)]for i in range(3)]

def Bdash_OperationFun(Front,Right,Down,Left,Up,Back):

    t1=Up[0][0]
    t2=Up[0][1]
    t3=Up[0][2]


    Up[0][0]=Left[2][0]
    Up[0][1]=Left[1][0]
    Up[0][2]=Left[0][0]

    Left[0][0]=Down[2][0]
    Left[1][0]=Down[2][1]
    Left[2][0]=Down[2][2]

    Down[2][0]=Right[2][2]
    Down[2][1]=Right[1][2]
    Down[2][2]=Right[0][2]

    Right[2][2]=t3
    Right[1][2]=t2
    Right[0][2]=t1

    # t1=Up[0][0]
    # t2=Up[0][1]
    # t3=Up[0][2]

    # Up[0][0]=Right[0][2]
    # Up[0][1]=Right[1][2]
    # Up[0][2]=Right[2][2]

    # Right[0][2]=Down[2][2]
    # Right[1][2]=Down[2][1]
    # Right[2][2]=Down[2][0]

    # Down[2][2]=Left[2][0]
    # Down[2][1]=Left[1][0]
    # Down[2][0]=Left[0][0]

    # Left[2][0]=t1
    # Left[1][0]=t2
    # Left[0][0]=t3

    temp1=Back[0][2]
    temp2=Back[0][1]
    temp3=Back[0][0]

    Back[0][0]=Back[0][2]
    Back[0][1]=Back[1][2]
    Back[0][2]=Back[2][2]

    Back[0][2]=Back[2][2]
    Back[1][2]=Back[2][1]
    Back[2][2]=Back[2][0]

    Back[2][2]=Back[2][0]
    Back[2][1]=Back[1][0]
    Back[2][0]=Back[0][0]

    Back[2][0]=temp3
    Back[1][0]=temp2
    Back[0][0]=temp1


    return Front,Right,Down,Left,Up,Back
# Front,Right,Down,Left,Up,Back=Bdash_OperationFun(Front,Right,Down,Left,Up,Back)
# print("up")
# for each in Up:
#     print(each)
# print("front")
# for each in Front:
#     print(each)
# print("down")
# for each in Down:
#     print(each)
# print("back")
# for each in Back:
#     print(each)
# print("right")
# for each in Right:
#     print(each)
# print("left")
# for each in Left:
#     print(each)

