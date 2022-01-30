import numpy as np
import matplotlib.pyplot as plt
import collections

# some basic configuration

WIDTH = 10
HEIGHT = 10
COLOR = 5
MAXIMUM_REACTION =20
MOVE_COUNT = 30
CLEAR_LENGTH = 3
VIZ = 'graph'

class game:
    def __init__(self,width,height,color,move_count,clear_length=3,viz_method=None,max_reaction=100):
        self.height=height
        self.width=width
        self.move_count=move_count
        self.color=color
        self.checkpoints=[]
        self.score=0
        self.shuffle()
        self.max_reaction=max_reaction
        self.viz_method=viz_method
        # vertical pattern

    def generate_move(self,move_code):
        unit_a=[]
        unit_b=[]
        if(move_code>=self.width*(self.height-1)+self.height*(self.width-1)):
            raise ValueError('move code is higher than width*(height-1)+height*(width-1)!')
        if(move_code>self.height*(self.width-1)):
            x=move_code//(self.width-1)
            y=move_code%(self.width-1)
            unit_a=[x,y]
            unit_b=[x,y+1]
        else:
            move_code-=self.height*(self.width-1)
            y=move_code//(self.height-1)
            x=move_code%(self.height-1)
            unit_a=[x,y]
            unit_b=[x+1,y]
        self.move(unit_a,unit_b)

    def visualize(self):
        if(self.viz_method=='graph'):
            plt.imshow(self.data, cmap = 'hsv')   
            plt.show()
    
    def is_illegal_move(self,unit_a,unit_b):
        return (unit_a[0]==unit_b[0] and unit_a[1]!=unit_a[1])or(unit_a[0]!=unit_b[0] and unit_a[1]==unit_a[1])

    def get_move_code(self,unit_a,unit_b):
        if(self.is_illegal_move(unit_a,unit_b)):
            raise ValueError('input is not legal move')
        if(unit_a[0]==unit_b[0]):
            return unit_a[0]*self.width+Math.min(unit_a[1],unit_b[1])
        else:
            return (self.height-1)*self.width+unit_a[1]*self.height+Math.min(unit_a[0],unit_b[0])

    def move(self,unit_a,unit_b,real_move=True):
        if(self.is_illegal_move(unit_a,unit_b)):
            raise ValueError('input is not legal move')
        # real move means to change the actual data in self
        if(real_move):
            swap=self.data[unit_a[0]][unit_a[1]]
            self.data[unit_a[0]][unit_a[1]]=self.data[unit_b[0]][unit_b[1]]
            self.data[unit_b[0]][unit_b[1]]=swap
            self.move_count-=1
            self.update()
        # here you return a copy of self.data as a possibility
        else:
            return None

            
    def playable_check(self):
        for i in (self.width-1)*self.height+self.width*(self.height-1):
            # if the game is playable after generate_move(i)
            return True
        return False
            
        
    def matchable_check(self,data,unit):
        matchable_units=[]
        # to check whether objects around pos: unit is matchable
        # vertical match
        # horizontal match
        # return a list of matchable units
        return matchable_units

    def unit_check(self,unit,add_score=True):
        # remove mathcable elements arond unit
        # add score
        # move other element downward and add moved units to checkpoints
        return None

    def shuffle(self):
        # restart the game
        print('shuffling the game...')
        self.data=np.random.randint(self.color, size=(self.height,self.width))
        self.update(add_score=False)

    def update(self,add_score=True):
        reaction_time=0
        while(len(self.checkpoints)>0):
            unit_check(self.checkpoints.pop(),add_score)
            self.visualize()
            if(not self.playable_check()):
                print('no new move avaliable')
                self.shuffle()
            reaction_time+=1
            if(reaction_time>self.max_reaction):
                raise RuntimeError('connection overflow the maximum reaction limit')

game=game(WIDTH,HEIGHT,COLOR,MOVE_COUNT,viz_method='graph')

while(game.move_count>0):
    game.update()
    game.visualize()
    x1=int(input('x1'))
    x2=int(input('x2'))
    y1=int(input('y1'))
    y2=int(input('y2'))
    game.move([x1,y1], [x2,y2]) 
