import B_operation
import Bdash_operation
import D_operation
import Ddash_operation
import F_operation
import Fdash_operation
import L_opeation
import Ldash_operation
import R_operation
import Rdash_operation
import Udash_operation
import U_operation







Red_Front=[['W' for i in range(3)]for i in range(3)]        # Front Side
Yellow_Right=[['R' for i in range(3)]for i in range(3)]     # rigt side
Blue_Down=[['G' for i in range(3)]for i in range(3)]        # down side
Green_Left=[['O' for i in range(3)]for i in range(3)]       # left side
White_Up=[['B' for i in range(3)]for i in range(3)]         # up side
Orange_Back=[['Y' for i in range(3)]for i in range(3)]      # back side





# patt ="RLUPFB"

# for i in range(len(string)):

#     if string[i] in patt:

#         if i < (len(string)-1) and string[i+1]=="'":

#             if string == "R":



# stringInput="R'L'UPRFD'"
# patt = "RLUFBD'"




# for i in range(len(stringInput)):
#     if stringInput[i] in patt:

        

#         if i < (len(stringInput)-1) and stringInput[i+1]=="'":
            
#             if stringInput[i] == "R":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Rdash_operation.Rdash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)#R' function
#             if stringInput[i]  == "L":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Ldash_operation.L_dash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)#L' function
#             if stringInput[i]  == "U":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Udash_operation.up_dash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)
#             if stringInput[i] == "F":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Fdash_operation.FrontAnti_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #F' function
#             if stringInput[i]  == "B":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Bdash_operation.Bdash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #B' functon
#             if stringInput[i]  == "D":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Ddash_operation.down_dash_operationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #B' functon


#         elif(i != "'"):
#             print(i)
#             if stringInput[i]  == "R":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=R_operation.R_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #R function
#             if stringInput[i]  == "L":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=L_opeation.L_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #L function
#             if stringInput[i]  == "U":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=U_operation.up_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #U function
#             if stringInput[i] == "F":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=F_operation.Front_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #F function
#             if stringInput[i]  == "B":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=B_operation.B_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #B functo
#             if stringInput[i]  == "D":
#                 Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=D_operation.downShift(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #B' functon
#     else:
#         print("Your input is wrong!!! please enetr a correct Input!!!")            

# for each in White_Up:
#     print(each)
# print("---------------------------")
# for each in Red_Front:
#     print(each)
# print("---------------------------")
# for each in Blue_Down:
#     print(each)
# print("---------------------------")
# for each in Orange_Back:
#     print(each)
# print("---------------------------")
# for each in Yellow_Right:
#     print(each)
# print("---------------------------")
# for each in Green_Left:
#     print(each)


#################################
############################


while True:

    # stringInput="R'L'UPRFD'"      # for testing purpose
    stringInput = input("Enter the Rotation : ").upper()
    if stringInput.lower() == "end":    # to end the game
        break
    pattern = "RLUFBD'"     # given input should contain this letters and symbols only

    flag = True    # When this is true then only cube faces will be shown
    for i in range(len(stringInput)):
        if stringInput[i] in pattern:   # validation to check input is right
            if i < (len(stringInput)-1) and stringInput[i+1]=="'":  # All the dash letter will go inside here
                
                if stringInput[i] == "R":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Rdash_operation.Rdash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)#R' function
                if stringInput[i]  == "L":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Ldash_operation.L_dash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)#L' function
                if stringInput[i]  == "U":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Udash_operation.up_dash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back)
                if stringInput[i] == "F":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Fdash_operation.FrontAnti_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #F' function
                if stringInput[i]  == "B":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Bdash_operation.Bdash_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #B' functon
                if stringInput[i]  == "D":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=Ddash_operation.down_dash_operationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #B' functon


            elif(i != "'"):     # Without Dash Letter will go inside this block
                
                if stringInput[i]  == "R":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=R_operation.R_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #R function
                if stringInput[i]  == "L":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=L_opeation.L_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #L function
                if stringInput[i]  == "U":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=U_operation.up_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #U function
                if stringInput[i] == "F":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=F_operation.Front_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #F function
                if stringInput[i]  == "B":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=B_operation.B_OperationFun(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #B functo
                if stringInput[i]  == "D":
                    Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back=D_operation.downShift(Red_Front,Yellow_Right,Blue_Down,Green_Left,White_Up,Orange_Back) #B' functon
        
            flag = True

        else:
            
            # If user input is wrong 
            print("Your input is wrong!!! please enetr a correct Input!!!")
            print("Enter either R L U F B D R' L' U' F' B' D' only! ")
            flag = False


        
    # If flag is true that means no error, we can print the cube sides
    if flag:
        print("Front:")
        for each in Red_Front:

            print(each)
        print("---------------------------")

        print(" Left:")
        for each in Green_Left:
            
            print(each)
        print("---------------------------")

        print(" Right:")
        for each in Yellow_Right:
           
            print(each)
        print("---------------------------")

        print("up side:")
        for each in White_Up:
            print(each)

        print("---------------------------")

        
        print(" Down:")
        for each in Blue_Down:
            
            print(each)
        print("---------------------------")
        print(" Back:")
        for each in reversed(Orange_Back):
            print(each)
        print("---------------------------")