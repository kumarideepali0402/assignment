class LinearProbing:
    def __init__(self,size):
        self.size=size
        self.keys=[None]*size
        self.values=[None]*size

    def hashFunction(self,key):
        return hash(key)% self.size
    def put(self,key,value):
        index=self.hashFunction(key)
        while self.keys[index] is not None:
            if(self.keys[index]==key):
                self.values[index]=value
                return
            index=hash(index+1)/self.size
        
        self.keys[index]=key
        self.values[index]=value

    def get(self,key):
        index=hash(key)% self.size

        while (self.keys[index] is not None):
            if(self.keys[index]==key):
                return self.values[index]
            index=hash(index+1)/self.size
        return None
        
        
ht=LinearProbing(10)
ht.put(1,"deepali")
ht.put(2,"xqw") 
print(ht.get(1))
    
