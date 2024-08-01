class Node:
    def __init__(self,data,right=None,left=None):
        self.data=data
        self.right=right
        self.left=left
        self.height=0
        self.balanceFactor=0

class AVL:
    def __init__(self):
        self.__nodesCount=0
        self.__root=None

    def find(self,value):
        return self.__contains(self.__root,value)
        
    def __contains(self,node,data):
        if node is None:
            return False
        if (self.__node.value==data):
            return True
        elif(node.value>data):
            return self.__contains(self.__root.right,data)
        elif(self.__root.value<data):
            return self.__contains(self.__root.left,data)
        return False
    
    def insert(self,data):
        if (data==None):
            return False
        if(self.find(data)):
            return False
        else:
            self.root=self.insert2(self.root,data)
            self.__nodesCount+=1
            return True
    
    def insert2(self,node,data):
        if node is None:
            return Node(data)
        if(node.data>data):
            node.left= self.insert2(node.left,data)
        if(node.data<data):
            node.right= self.insert2(node.right,data)
        
        self.__update(node)

        return self.__balance(node)
    def __update(self,node):
        leftHeight,rightHeight=-1,-1
        if node.left is not None:
            leftHeight=node.left.height
        if node.right is not None:
            rightHeight=node.right.height
        
        node.height=1+max(leftHeight,rightHeight)
        node.balanceFactor=rightHeight-leftHeight

    
    def __balance(self,node):
        if node.balancefactor == +2:
            if(node.right.balanceFactor > 1):
                return self.__rightRightCase(node)
            else:
                return self.__rightLeftCase(node)
        elif(node.balanceFactor == -2):
            if(node.right.balanceFactor>0):
                return self.__leftleftCase(node)
            else:
                return self.__leftRightCase(node)
        else: 
            return node
            
    def __rightRightCase(self,node):
        return self.__rotateRight(self,node)
    
    def __rightLeftCase(self,node):
        node.right=self.__rotateRight(node.right)
        return self.__rightRightCase(node)
    
    def __leftLeftCase(self,node):
        return self.__leftLeftCase(node)
    
    def __leftRightCase(self,node):
        node.left=self.__rotateLeft(node.left)
        return self.__leftLeftCase(node)
    
    def __rotateLeft(self,node):
        b=node.left
        node.left=b.right
        b.right=node

        self.__update(node)
        self.__update(b)
        return b
    
    def __rotateRight(self,node):
        b=node.right
        node.right=b.left
        b.left=node
        self.__update(node)
        self.__update(b)

        return b
    
    def remove(self,value):
        if value==None:
            return False
        if(self.find(value)==False): 
            return False
        else:
            self.root=self.__remove(self.root,value)
            self.__nodesCount-=1
            return True
        
    def __remove(self,node,value):
        if(node.data==value):
            if node.right is None and node.left is None:
                del(node)
                return None
            elif node.left is None:
                temp=node.right
                del(node)
                return temp
            elif node.right is None:
                temp=node.left
                del(node)
                return temp
            else:
                successor=node.right
                while successor is not None:
                    successor=successor.left
                node.data=successor.data
                node.right=self.__remove(node.right,successor.data)
                self.__update(node)
                return self.__balance(node)
                return node
              
        elif(node.data>value):
            node.left= self.__remove(node.left,value)
        else:
            node.right= self.__remove(node.right,value)

            
        self.__update(node)

        return self.__balance(node)





        
    


            


    
        


        


