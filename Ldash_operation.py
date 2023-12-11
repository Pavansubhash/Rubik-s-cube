# Red_Front=[['R' for i in range(3)]for i in range(3)]

# Yellow_Right=[['Y' for i in range(3)]for i in range(3)]

# Blue_Down=[['B' for i in range(3)]for i in range(3)]

# Green_Left=[['G' for i in range(3)]for i in range(3)]

# White_Up=[['W' for i in range(3)]for i in range(3)]

# Orange_Back=[['O' for i in range(3)]for i in range(3)]

def L_dash_OperationFun(Front,Right,Down,Left,Up,Back):

    t1= Down[0][0]
    t2=Down[1][0]
    t3=Down[2][0]

    Down[0][0]=Back[0][0]
    Down[1][0]=Back[1][0]
    Down[2][0]=Back[2][0]

    Back[0][0]=Up[0][0]
    Back[1][0]=Up[1][0]
    Back[2][0]=Up[2][0]

    Up[0][0]=Front[0][0]
    Up[1][0]=Front[1][0]
    Up[2][0]=Front[2][0]

    Front[2][0]=t3
    Front[1][0]=t2
    Front[0][0]=t1

    temp1=Left[0][0]
    temp2=Left[1][0]
    temp3=Left[2][0]

    Left[0][0]=Left[0][2]
    Left[1][0]=Left[0][1]
    Left[2][0]=Left[0][0]

    Left[0][2]=Left[2][2]
    Left[0][1]=Left[1][2]
    Left[0][0]=Left[0][2]

    Left[2][2]=Left[2][0]
    Left[1][2]=Left[2][1]
    Left[0][2]=Left[2][2]

    Left[2][0]=temp1
    Left[2][1]=temp2
    Left[2][2]=temp3

    return Front,Right,Down,Left,Up,Back

# Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=L_dash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)




# for each in White_Up:

#     print(each)

# for each in Red_Front:

#     print(each)

# for each in Blue_Down:

#     print(each)

# for each in Orange_Back:

#     print(each)

# for each in Yellow_Right:




#     print(each)

# Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=L_dash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)




# for each in White_Up:

#     print(each)

# for each in Red_Front:

#     print(each)

# for each in Blue_Down:

#     print(each)

# for each in Orange_Back:

#     print(each)

# for each in Yellow_Right:




#     print(each)