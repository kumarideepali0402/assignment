class Entry:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.hash=hash(key)
    def __str__(self):
        return str(self.key) +":"+(self.value)

class HT:
    def __init__(self,size,cap):
        self.__size=0
        self.__cap=5
        self.__data=[[] for i in range(self.__cap)]
        

    def size(self):
        return self.__size
    def isEmpty(self):
        return self.__size==0
    def resize(self):
        new_cap=2*self.__cap
        new_data=[[] for i in range(new_cap)]
        for i in range(self.__cap):
            for e in (self.__data[i]):
                new_hash=hash(e.key)%new_cap
                new_data[new_hash].append(Entry(e.key,e.value,e.hash))
        del self.__data
        self.__data==new_data
        self.__cap=new_cap

    
    def insert(self,key,value):
        # find index to store the key (0,cap-1)
# check if key is already present in index or not if yes update the value else append it
        # if((self.__size/self.__cap)>=self.__max_threshold):
        #     self.resize()
        e=Entry(key,value)
        is_present=False
        index=e.hash%self.__cap
        for i in range(len(self.__data[index])):
            if(self.__data[index][i].key==key):
                self.__data[index][i]=e
                is_present=True
                break
            if(not is_present):
                self.__data[index].append(e)
                self.__size+=1
    def print(self):
        for i in range (self.__cap):
            print("bucket:" +str(i)+":")
            for e in self.data[i]:
                print(e,sep='->')
        print("----------------")


    def get(self,key):
        hv=hash(key)%self.__cap
        for i in range(len(self.__data[hv])):
            if(self.__data[hv][i].key==key): 
                return self.__data[hv][i].value
            else:
                return None
        
    def remove(self,key):
        hv=hash(key)%self.__cap
        l=len(self.__data[hv])
        
        for i in range (l):
            if (self.__data[hv][i].key==key):
                # temp=self.__data[hv][l-1]
                # self.__data[hv][l-1]=self.__data[hv][i]
                # self.__data[hv][key]=temp
                # self.__data[hv].pop()
                del self.__data[hv][i]
                self.__size-=1
                break


                



a=HT(4,6)
a.insert(2,"deepali")
a.insert(1,"Najma")
a.insert(3,"Keerthana")
print(a.size())  
print(a.get(2))
a.remove(1)
print(a.get(2))
print(a.size())  
