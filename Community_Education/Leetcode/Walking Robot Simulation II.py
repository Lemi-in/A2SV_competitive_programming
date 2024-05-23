class Robot(object):
    def __init__(self, width, height):
        self.direction="East"
        self.coordinate=[0,0]
        self.arr=[width-1,height-1]
        self.width=width
        self.height=height

    def step(self, num):
        total=((self.height+self.width-2)*2)
        num=num%total
        if num!=0:
           i=0
           while i<num:
                if self.direction=="East":
                    if self.coordinate[0]==self.width-1:
                        num+=1
                        self.direction="North"
                    else:self.coordinate[0]+=1

                elif self.direction=="West":
                    if self.coordinate[0]==0:
                        num+=1
                        self.direction="South"
                    else:self.coordinate[0]-=1
                elif self.direction=="North":
                    if self.coordinate[1]==self.height-1:
                        num+=1
                        self.direction="West"
                    else:self.coordinate[1]+=1
                elif self.direction=="South":
                    if self.coordinate[1]==0:
                        num+=1
                        self.direction="East"
                    else:self.coordinate[1]-=1
                i+=1      
        elif self.coordinate==[0,0]  and self.direction=="East":
            self.direction="South"
      
    def getPos(self):
        return self.coordinate

    def getDir(self):
        return self.direction


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
