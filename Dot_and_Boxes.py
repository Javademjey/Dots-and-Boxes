
import numpy as np
import matplotlib.pyplot as plt


User_list_X_coor = list()
User_list_Y_coor = list()
Sys_list_X_coor = list()
Sys_list_Y_coor = list()
list_of_points = list() 


def DeterminationOfPoints(Dimns:int)->tuple:
    X = np.zeros(Dimns*Dimns)
    Y = np.zeros(Dimns*Dimns)
    i=0
    s=1
    p=1
    while i != Dimns*Dimns:
        X[i] = s
        Y[i] = p
        i+=1
        if s == Dimns:
            p += 1
            s = 0
        s+=1
    return X,Y

def UserSeparating_X_and_Y(coordinate:list)->None:    #Coordinate_of_two_dots_user:list = None   # user line
    User_list_X_coor.append(coordinate[0][0])
    User_list_X_coor.append(coordinate[1][0])
    User_list_Y_coor.append(coordinate[0][1])
    User_list_Y_coor.append(coordinate[1][1])

def SysSeparating_X_and_Y(coordinate:list)->None:     #Coordinate_of_two_dots_sys:list = None    # system line 
    Sys_list_X_coor.append(coordinate[0][0])
    Sys_list_X_coor.append(coordinate[1][0])
    Sys_list_Y_coor.append(coordinate[0][1])
    Sys_list_Y_coor.append(coordinate[1][1])


class TempBox:

    def __init__(self,index:int ,number:int=0):
        self.index = index
        self.next = None
        self.prev = None
        self.__score = 0
        self.__up:bool = False
        self.__right:bool = False
        self.__down:bool = False
        self.__left:bool = False
        self.list_of_branches = list()


class Box:

    def __init__(self ,index:int ,number:int=0):
        self.index = index
        self.number = number    # number -> up=1 or right=2 or down=3 or left=4
        self.next = None
        self.prev = None
        self.__score = 0
        self.__up:bool = False
        self.__right:bool = False
        self.__down:bool = False
        self.__left:bool = False
        self.list_of_branches = list()


class BigSquare:
    
    def __init__(self ,dots:int ,squares:int):  # each square should has a number 
        self.All_Dots = dots**2                 # all of dots in board (n*n)
        self.All_Squares = squares**2           # all of boxes(squares) in board (n-1)*(n-1)
        self.dots = dots                        # inputed dots (n)
        self.squares = squares                  # inputed boxes(squares) (n-1)
        self.__head = None                      # head = 1 (first square)
        self.__headTB = None
        self.__Lines_in_location_up = list()
        self.__Lines_in_location_right = list()
        self.__Lines_in_location_down = list()
        self.__Lines_in_location_left = list()
        self.CoordinateConfiguration()

    def CoordinateConfiguration(self)->None:
        ux=1
        uy=2
        dx=dy=1
        rx=2
        ry=1
        lx=ly=1

        while True:
            
            self.__Lines_in_location_down.append([[dx,dy],[dx+1,dy]])  # down lines Coordinate
            if dx == self.squares:                                     #
                dx=0                                                   #
                dy+=1                                                  #
            dx+=1                                                      #

            self.__Lines_in_location_up.append([[ux,uy],[ux+1,uy]])    # up lines Coordinate
            if ux == self.squares:                                     #
                ux=0                                                   #
                uy+=1                                                  #
            ux+=1                                                      #

            self.__Lines_in_location_left.append([[lx,ly],[lx,ly+1]])  # left lines Coordinate
            if lx == self.squares:                                     #
                lx=0                                                   #
                ly+=1                                                  #
            lx+=1                                                      # 

            self.__Lines_in_location_right.append([[rx,ry],[rx,ry+1]])  # right lines Coordinate
            if rx == self.squares+1:                                    #
                rx=1                                                    #
                ry+=1                                                   # 
            rx+=1                                                       #

            if ry == self.dots :
                break

    def DeterminingIndexOfSquares(self, index): # Determining index for each one of the squares in board
        for i in range(2):  # Once for Box node and another time for Tempbox node
            if i == 0:  
                new_index = Box(index=index)
                if self.__head == None:
                    self.__head = new_index
                elif self.__head != None:
                    current = prev = self.__head
                    while current.next:
                        current = current.next
                        current.prev = prev
                        prev = current
                    current.next = new_index
                    new_index.prev = current
            if i == 1:
                new_index = TempBox(index=index)
                if self.__headTB == None:
                    self.__headTB = new_index
                elif self.__headTB != None:
                    current = prev = self.__headTB
                    while current.next:
                        current = current.next
                        current.prev = prev
                        prev = current
                    current.next = new_index
                    new_index.prev = current
                    
    def InsertMovesInBord(self ,turn ,index_of_square:int ,number_for_insert_line:int): # return Coordinates of two points
        if turn == 0:    
            if number_for_insert_line == 1:
                UserSeparating_X_and_Y(self.__Lines_in_location_up[index_of_square-1])
            elif number_for_insert_line == 2:
                UserSeparating_X_and_Y(self.__Lines_in_location_right[index_of_square-1])
            elif number_for_insert_line == 3:
                UserSeparating_X_and_Y(self.__Lines_in_location_down[index_of_square-1])
            elif number_for_insert_line == 4:
                UserSeparating_X_and_Y(self.__Lines_in_location_left[index_of_square-1])
        else:
            if number_for_insert_line == 1:
                SysSeparating_X_and_Y(self.__Lines_in_location_up[index_of_square])
            elif number_for_insert_line == 2:
                SysSeparating_X_and_Y(self.__Lines_in_location_right[index_of_square])
            elif number_for_insert_line == 3:
                SysSeparating_X_and_Y(self.__Lines_in_location_down[index_of_square])
            elif number_for_insert_line == 4:
                SysSeparating_X_and_Y(self.__Lines_in_location_left[index_of_square])
                
    def PrintIndexOfSquare(self):
        if self.__head == None:
           # print("List is empty")
            exit()
        temp = self.__head
        while temp:
            print(temp.index ,end=" ")
            temp = temp.next
           
    def Traverse(self ,destination:int ,Box_or_TempBox:int=0):  # location to insert
        # Traverse to find the box with given index
        if Box_or_TempBox == 0:
            temp = self.__head
            while temp.index != destination:
                temp = temp.next
            return temp
        else:
            temp = self.__headTB
            while temp.index != destination:
                temp = temp.next
            return temp

    def CreateListOfBoxes(self ,Box_or_TempBox)->list:
        if Box_or_TempBox == 0:  # Create List Of Boxes for TempBox node
            list_of_boxes = list()
            temp = self.__headTB
            while temp:
                list_of_boxes.append(temp)
                temp = temp.next
            return list_of_boxes
        else:                    # Create List Of Boxes for Box node
            list_of_boxes = list()
            temp = self.__head
            while temp:
                list_of_boxes.append(temp)
                temp = temp.next
            return list_of_boxes
        
    def CountingPoints(self ,Sys_or_User ,box:Box=None)->None: 
        if Sys_or_User == 0:           # 0 -> System
                list_of_points.append(0)
        if Sys_or_User == 1:           # 1 -> User
            if box._Box__score == 100:
                list_of_points.append(1)

    def ApplyingChangesFromBoxToTempBox(self):
        B = self.__head
        TB = self.__headTB
        while B:
            TB._TempBox__down = B._Box__down
            TB._TempBox__up = B._Box__up
            TB._TempBox__right = B._Box__right
            TB._TempBox__left = B._Box__left
            TB._TempBox__score = B._Box__score
            TB.list_of_branches = B.list_of_branches
            B = B.next
            TB = TB.next
        
    def IsEnd(self)->bool:
        temp = self.__head
        i=0
        indexes = list()
        while temp:
            if temp._Box__score !=100:
                indexes.append(temp)
                i+=1
            if i>2:
                return False
            temp = temp.next
        if len(indexes)==2:
            if indexes[0]._Box__score == 50 or indexes[1]._Box__score == 50:
                return False
        if len(indexes)==1:
            self.CountingPoints(Sys_or_User=0 ,box=indexes[0])
            return True    
        self.CountingPoints(Sys_or_User=1 ,box=indexes[0])
        self.CountingPoints(Sys_or_User=0 ,box=indexes[1])
        return True
        

class Square(BigSquare):

    def __init__(self ,dots ,squares ):
        BigSquare.__init__(self ,dots ,squares)
        self.number = None
        self.index = None
            
    def InputFunc(self)->None:
        i=0
        while i!=1:
            self.index = int(input("Index of square: "))
            self.number = int(input("Which line(enter the number):\n1.Up\n2.Right\n3.Down\n4.Left\n"))
            if self.index>=1 and self.index<=self.All_Squares and self.number>=1 and self.number<=4:
                if self.Validation2(self.index ,self.number):
                    self.__InsertForYourself()
                    self.__InsertForNeighbor()
                    self.ApplyingChangesFromBoxToTempBox()
                    return
                else:
                    print("Already selected!")
                    i=0
            else:
                print("Wrong index!! Try again.")
                i=0

    def __InsertForYourself(self):
        box = self.Traverse(destination=self.index)
        if self.number == 1:
            box._Box__up = True
            box._Box__score += 25
            self.InsertMovesInBord(0 ,self.index ,self.number)
            self.CountingPoints(Sys_or_User=1 ,box=box)
            return
        elif self.number == 2:
            box._Box__right = True
            box._Box__score += 25
            self.InsertMovesInBord(0 ,self.index ,self.number)
            self.CountingPoints(Sys_or_User=1 ,box=box)
            return
        elif self.number == 3:
            box._Box__down = True
            box._Box__score += 25
            self.InsertMovesInBord(0 ,self.index ,self.number)
            self.CountingPoints(Sys_or_User=1 ,box=box)
            return
        elif self.number == 4:
            box._Box__left = True
            box._Box__score += 25
            self.InsertMovesInBord(0 ,self.index ,self.number)
            self.CountingPoints(Sys_or_User=1 ,box=box)
            return
        
    def __InsertForNeighbor(self):
        if self.Validation1():
            if self.number == 1:
                box = self.Traverse(self.index+self.squares)
                box._Box__down = True
                box._Box__score += 25
                self.CountingPoints(Sys_or_User=1 ,box=box)
            elif self.number == 2:
                box = self.Traverse(self.index+1)
                box._Box__left = True
                box._Box__score += 25
                self.CountingPoints(Sys_or_User=1 ,box=box)
            elif self.number == 3:
                box = self.Traverse(self.index-self.squares)
                box._Box__up = True
                box._Box__score += 25
                self.CountingPoints(Sys_or_User=1 ,box=box)
            elif self.number == 4:
                box = self.Traverse(self.index-1)
                box._Box__right = True
                box._Box__score += 25
                self.CountingPoints(Sys_or_User=1 ,box=box)
        else:
            # No neighbor to insert for
            return
    
    def Validation1(self)->bool: # 1.special modes 2.normal modes
        for counter in range(1 ,self.All_Squares+1):
            if self.index == counter and counter >= 1 and counter <=  self.squares and self.number == 3:     # down row -> there isn't down neighbor
                return False
            elif (counter-1)*self.squares +1 == self.index and self.number == 4:   # left column -> there isn't left neighbor and either up neighbor in upest and down neighbor in downest 
                return False
            elif counter*self.squares == self.index and self.number == 2:          # right column -> there isn't down neighbor and either up neighbor in upest and down neighbor in downest
                return False
            elif self.squares*(self.squares-1) +1 <= self.index and self.squares*(self.squares-1) +(self.squares) >= self.index and self.number == 1:
                return False                                                       # up row
        return True
    
    def Validation2(self ,index ,direct)->bool:
        box =self.Traverse(destination=index)
        if box._Box__score == 100:
            return False
        else:
            if direct == 1 and box._Box__up ==True:
                return False
            elif direct == 2 and box._Box__right ==True:
                return False
            elif direct == 3 and box._Box__down ==True:
                return False
            elif direct == 4 and box._Box__left ==True:
                return False
            else:
                return True



class Tree(BigSquare):

    def __init__(self, selfBS):
        if selfBS.IsEnd():
            return
        self.index = None   # insert in board
        self.direct = None  # insert in board
        self.original_root = list()
        self.root = list()
        self.CreateListOfRoots(selfBS)
        accepted_predict = self.CreateBranchesOfEachRoot(selfBS)
        self.InsertSystemMove(selfBS ,accepted_predict)
        selfBS.ApplyingChangesFromBoxToTempBox()

    def CreateListOfRoots(self ,selfBS):
        self.root = selfBS.CreateListOfBoxes(0)
        
    def CreateBranchesOfEachRoot(self ,selfBS):   # predecting moves 
        
        #first state
        boxes_list1 = self.root
        ret_list1 = self.StatePrediction(selfBS ,boxes_list1 ,Box_or_TempBox=1) #  predict a guss for sys -> level 1  , Box_or_TempBox -> Box = 0 , TempBox = 1
        self.root[ret_list1[1]].list_of_branches = ret_list1[0]  # ret_list[0] = boxes_list , ret_list[1] = boxindex  
        boxes_list2 = self.root[ret_list1[1]].list_of_branches   

        #second state
        ret_list2 = self.StatePrediction(selfBS ,boxes_list2 ,Box_or_TempBox=1) # predict a guss for user -> level 2
        boxes_list2[ret_list2[1]].list_of_branches = ret_list2[0]  
        boxes_list3 = boxes_list2[ret_list2[1]].list_of_branches
         
        #third state
        ret_list3 = self.StatePrediction(selfBS ,boxes_list3 ,Box_or_TempBox=1) # predict a guss for sys -> level 3
        boxes_list3[ret_list3[1]].list_of_branches = ret_list3[0]  
        

        self.original_root = selfBS.CreateListOfBoxes(1)                        # if predict has a good result --> apply the result in Box
        final_ret = self.StatePrediction(selfBS ,self.original_root ,Box_or_TempBox=0)
        selfBS.InsertMovesInBord(1,final_ret[1] ,final_ret[2])
        if final_ret[3] == 1:
            selfBS.CountingPoints(0)
        
        return final_ret[0]

    def StatePrediction(self ,selfBS ,boxes_list ,Box_or_TempBox:int)->list:
        max_score = max_score_temp =0
        boxindex = boxindex_temp =0
        box =box_temp = None
        Point_confirmation = 0
        ac =0   # if ac =1 -> TempBox , if ac =0 -> Box

        if Box_or_TempBox == 1:
            for item in boxes_list:
                if item._TempBox__score > max_score and item._TempBox__score <100:
                    box = item
                    max_score = item._TempBox__score
                    boxindex = item.index-1
                if item._TempBox__score == 75:
                    box =item
                    max_score = item._TempBox__score
                    boxindex = item.index-1
                    break
                if item._TempBox__score == 25:
                    box_temp =item
                    max_score_temp = item._TempBox__score
                    boxindex_temp = item.index-1
            if box_temp != None and box._TempBox__score !=75 :
                box = box_temp
                boxindex= boxindex_temp
                max_score = max_score_temp
            if box ==None:
                for item in boxes_list:
                    if item._TempBox__score!=100:
                        box=item
            
            self.direct = self.SmartChoiceForLines(selfBS ,box ,1)               
            self.InsertForNeighbor(selfBS ,boxes_list ,self.direct ,boxindex ,Box_or_TempBox)
            ac=1
        
        else:
            for item in boxes_list:
                if item._Box__score > max_score and item._Box__score <100:
                    box = item
                    max_score = item._Box__score
                    boxindex = item.index-1
                if item._Box__score == 75:
                    box =item
                    max_score = item._Box__score
                    boxindex = item.index-1
                    break
                if item._Box__score == 25:
                    box_temp =item
                    max_score_temp = item._Box__score
                    boxindex_temp = item.index-1
            if box_temp != None and box._Box__score !=75 :
                box = box_temp
                boxindex= boxindex_temp
                max_score = max_score_temp
            if box ==None:
                for item in boxes_list:
                    if item._Box__score!=100:
                        box=item

            self.direct = self.SmartChoiceForLines(selfBS ,box ,0)               
            self.InsertForNeighbor(selfBS ,boxes_list ,self.direct ,boxindex ,Box_or_TempBox)

        if ac==1:
            if box._TempBox__score == 100:
                Point_confirmation=1
        else:
            if box._Box__score == 100:
                Point_confirmation=1
        
       # print(box.index ,self.direct)
        boxes_list[boxindex] = box
        return [boxes_list ,boxindex ,self.direct ,Point_confirmation]
        
    def InsertForNeighbor(self ,selfBS ,templist ,direct ,index ,Box_or_TempBox:int):
        if self.Validation(selfBS ,direct ,index+1):
            if Box_or_TempBox == 1:
                if direct == 1:
                    templist[index+selfBS.squares]._TempBox__down = True
                    templist[index+selfBS.squares]._TempBox__score += 25
                elif direct == 2:
                    templist[index+1]._TempBox__left = True
                    templist[index+1]._TempBox__score += 25
                elif direct == 3:
                    templist[index-selfBS.squares]._TempBox__up = True
                    templist[index-selfBS.squares]._TempBox__score += 25
                elif direct == 4:
                    templist[index-1]._TempBox__right = True
                    templist[index-1]._TempBox__score += 25
            else:
                if direct == 1:
                    templist[index+selfBS.squares]._Box__down = True
                    templist[index+selfBS.squares]._Box__score += 25
                elif direct == 2:
                    templist[index+1]._Box__left = True
                    templist[index+1]._Box__score += 25
                elif direct == 3:
                    templist[index-selfBS.squares]._Box__up = True
                    templist[index-selfBS.squares]._Box__score += 25
                elif direct == 4:
                    templist[index-1]._Box__right = True
                    templist[index-1]._Box__score += 25
        else:
            # No neighbor to insert for
            return

    def Validation(self ,selfBS, direct ,index)->bool: # 1.special modes 2.normal modes
        for counter in range(1 ,selfBS.All_Squares+1):
            if index == counter and counter >= 1 and counter <=  selfBS.squares and direct == 3:     # down row -> there isn't down neighbor
                return False
            elif (counter-1)*selfBS.squares +1 == index and direct == 4:   # left column -> there isn't left neighbor and either up neighbor in upest and down neighbor in downest 
                return False
            elif counter*selfBS.squares == index and direct == 2:          # right column -> there isn't down neighbor and either up neighbor in upest and down neighbor in downest
                return False
            elif selfBS.squares*(selfBS.squares-1) +1 <= index and selfBS.squares*(selfBS.squares-1) +(selfBS.squares) >= index and direct == 1:
                return False                                                       # up row
        return True

    def InsertSystemMove(self ,selfBS ,boxes_list):
        temp = selfBS._BigSquare__head
        selfBS.__head = boxes_list[0]
        for box in boxes_list[1:]:
            temp = temp.next
            temp = box

    def SmartChoiceForLines(self ,selfBS ,box ,Box_or_TempBox)->list:
        x =list([0])
        
        if Box_or_TempBox == 0:    
            if box._Box__score == 75:
                if box._Box__right == False:
                    x.append(2)
                elif box._Box__left == False:
                    x.append(4)
                elif box._Box__down == False:
                    x.append(3)
                elif box._Box__up == False:
                    x.append(1)
           
            else:
                temporary = list()
                if box._Box__right == False:
                    if self.Validation(selfBS ,2 ,box.index):    
                        temporary.append([box.next,2])
                if box._Box__left == False:
                    if self.Validation(selfBS ,4 ,box.index):
                        temporary.append([box.prev,4])
                if box._Box__up == False:
                    if box.index+selfBS.squares <= selfBS.All_Squares:
                        x = selfBS.Traverse(destination=box.index+selfBS.squares)
                        temporary.append([x,1]) 
                if box._Box__down == False:    
                    if box.index-selfBS.squares >=1:
                        x = selfBS.Traverse(destination=box.index-selfBS.squares)
                        temporary.append([x,3])
                
                if len(temporary)==0:    # extra condition that never become True
                    if box._Box__up:                                                                        # random insert directs
                        if box._Box__right:                                                                 #
                            if box._Box__down:                                                              #
                                box._Box__left = True                                                       #
                                x.append(4)                                                                 #
                                x.append(4)                                                                 #      
                            else:                                                                           #
                                box._Box__down = True                                                       #
                                x.append(3)                                                                 #
                                x.append(3)                                                                 #
                        else:                                                                               #
                            box._Box__right = True                                                          #
                            x.append(2)                                                                     #
                            x.append(2)                                                                     #
                    else:                                                                                   #
                        box._Box__up = True                                                                 #
                        x.append(1)                                                                         #        
                        x.append(1)                                                                         #
                    box._Box__score +=25 

                else:
                    x = temporary[0]
                    for i in temporary:
                        if i[0]._Box__score == 0 or i[0]._Box__score == 25 or i[0]._Box__score == 75:
                            if x[0]._Box__score != 75:
                                x = i

            if x[1] == 1:
                box._Box__up =True
                box._Box__score +=25
            elif x[1] == 2:
                box._Box__right =True
                box._Box__score +=25
            elif x[1] == 4:
                box._Box__left =True
                box._Box__score +=25
            elif x[1] == 3:
                box._Box__down =True
                box._Box__score +=25
    
        else:
            if box._TempBox__up:                                                                    # random insert directs
                if box._TempBox__right:                                                             #
                    if box._TempBox__down:                                                          #
                        box._TempBox__left = True                                                   #
                        x.append(4)                                                                 #
                        x.append(4)                                                                 #      
                    else:                                                                           #
                        box._TempBox__down = True                                                   #
                        x.append(3)                                                                 #
                        x.append(3)                                                                 #
                else:                                                                               #
                    box._TempBox__right = True                                                      #
                    x.append(2)                                                                     #
                    x.append(2)                                                                     #
            else:                                                                                   #
                box._TempBox__up = True                                                             #
                x.append(1)                                                                         #        
                x.append(1)                                                                         #
            box._TempBox__score +=25 

        return x[1]
        
         


def Start():

    square:int = int(input("How many squares should the game board have?\nIf you enter 3, it means 9 squares or 4 means 16 squares: "))
    dots = square+1
    squares = square
    all_squares = squares**2

    BS = Square(dots=dots ,squares=squares)
    i=1
    while i <= all_squares:
        BS.DeterminingIndexOfSquares(i)
        i+=1


    Dimns = dots   #int(input("Dimensions n*n: "))
    X,Y = DeterminationOfPoints(Dimns)

    z =1
    while True:

        if z ==1:     # User turn
            BS.InputFunc()
            z =0
        else:     # System turn
            Tree(BS)
            z =1

        Sys = User =0
        for i in list_of_points:
            if i ==0:
                Sys+=1
            else:
                User+=1

        #print(User_list_X_coor,User_list_Y_coor)
        #print(Sys_list_X_coor,Sys_list_Y_coor,"\n")
        #print(User," ",Sys)
        if z==1:
            print(f'User: {User}\nSystem: {Sys}')

        if Sys+User == all_squares:
            if Sys>User:
                print("hahahaha You lose!!!\U0001F60E\U0001F60E\U0001F923\U0001F923")
                exit()
            elif Sys<User:
                print("Unfortunately You Won. Congratulations!\U0001F629")
                exit()
            else:
                print("The game has no winner. Good game")
                exit()


        if squares <=4:
            font =14
        else:
            font =10
        xx =yy =1.5
        for i in range(1 ,all_squares+1):
            if xx >dots:
                xx= 1.5
                yy+=1
            plt.text(xx ,yy ,i ,fontsize = font)
            xx+=1

        plt.scatter(X ,Y)
        for i in range(0 ,len(User_list_X_coor),2):
            plt.plot(User_list_X_coor[i:i+2] ,User_list_Y_coor[i:i+2] ,'b')
        for i in range(0 ,len(User_list_X_coor),2):    
            plt.plot(Sys_list_X_coor[i:i+2] ,Sys_list_Y_coor[i:i+2] ,'r')
        plt.show()

        
  
#if __name__ == "main":
Start()
