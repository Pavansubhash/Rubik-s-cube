# Red_Front=[['R' for i in range(3)]for i in range(3)]

# Yellow_Right=[['Y' for i in range(3)]for i in range(3)]

# Blue_Down=[['B' for i in range(3)]for i in range(3)]

# Green_Left=[[1,2,3],[4,5,6],[7,8,9]]

# White_Up=[['W' for i in range(3)]for i in range(3)]

# Orange_Back=[['O' for i in range(3)]for i in range(3)]






def L_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back):

    t1=Blue_Down[0][0]
    t2=Blue_Down[1][0]
    t3=Blue_Down[2][0]

    Blue_Down[0][0]=Red_Front[0][0]
    Blue_Down[1][0]=Red_Front[1][0]
    Blue_Down[2][0]=Red_Front[2][0]

    Red_Front[0][0]=White_Up[0][0]
    Red_Front[1][0]=White_Up[1][0]
    Red_Front[2][0]=White_Up[2][0]

    White_Up[0][0]=Orange_Back[0][0]
    White_Up[1][0]=Orange_Back[1][0]
    White_Up[2][0]=Orange_Back[2][0]
    
    Orange_Back[0][0]=t1
    Orange_Back[1][0]=t2
    Orange_Back[2][0]=t3

    temp1=Green_Left[0][0]
    temp2=Green_Left[1][0]
    temp3=Green_Left[2][0]

    Green_Left[0][0]=Green_Left[2][0]
    Green_Left[1][0]=Green_Left[2][1]
    Green_Left[2][0]=Green_Left[2][2]

    Green_Left[2][0]=Green_Left[2][2]
    Green_Left[2][1]=Green_Left[1][2]
    Green_Left[2][2]=Green_Left[0][2]

    Green_Left[2][2]=Green_Left[0][2]
    Green_Left[1][2]=Green_Left[0][1]
    Green_Left[0][2]=Green_Left[0][0]

    Green_Left[0][2]=temp3
    Green_Left[0][1]=temp2
    Green_Left[0][0]=temp1

    return Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back




# Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=L_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)




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




# for each in Green_Left:

#     print(each)

