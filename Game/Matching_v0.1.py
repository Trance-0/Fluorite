import numpy as np
import matplotlib.pyplot as plt
import collections

# some basic configuration

WIDTH = 5
HEIGHT = 5
COLOR = 4
MAXIMUM_REACTION =20
MOVE_COUNT = 30
CLEAR_LENGTH = 3
VIZ = 'graph'

class game:
    # First, this game would calculate all the possible move at init
    # while in game
    # if the move code matched the possible future graph, then move the game to possbile future and calculate the game again
    def __init__(self,width,height,color,move_count,clear_length=3,viz_method=None,max_reaction=100):
        self.height=height
        self.width=width
        self.move_count=move_count
        self.color=color
        self.clear_length=clear_length
        self.checkpoints=[]
        self.score=0
        self.shuffle()
        self.max_reaction=max_reaction
        self.viz_method=viz_method
        self.update(add_score=False)
        # vertical pattern

    def get_move(self,move_code):
        # generate move from move code
        unit_a=[]
        unit_b=[]
        # test if the move code is legal
        if(move_code>=self.width*(self.height-1)+self.height*(self.width-1)):
            raise ValueError('move code is higher than width*(height-1)+height*(width-1)!')
        # convert move code to real move
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
        return unit_a,unit_b
    
    def get_move_code(self,unit_a,unit_b):
        if(self.is_illegal_move(unit_a,unit_b)):
            raise ValueError('input is not legal move')
        if(unit_a[0]==unit_b[0]):
            return unit_a[0]*self.width+Math.min(unit_a[1],unit_b[1])
        else:
            return (self.height-1)*self.width+unit_a[1]*self.height+Math.min(unit_a[0],unit_b[0])


    def visualize(self):
        if(self.viz_method=='graph'):
            plt.imshow(self.data, cmap = 'hsv')   
            plt.show()
    
    def is_illegal_move(self,graph,unit_a,unit_b):
        return (unit_a[0]==unit_b[0] and unit_a[1]!=unit_a[1])or(unit_a[0]!=unit_b[0] and unit_a[1]==unit_a[1]) and unit_a[0]>=0 and unit_a[1]<graph.shape()[0] and unit_b[0]>=0 and unit_b[1]<graph.shape()[1]

    
    def move(self,graph,unit_a,unit_b):
        if(self.is_illegal_move(graph,unit_a,unit_b)):
            raise ValueError('input is not legal move')
        # real move means to change the actual data in self
        swap=graph[unit_a[0]][unit_a[1]]
        graph[unit_a[0]][unit_a[1]]=graph[unit_b[0]][unit_b[1]]
        graph[unit_b[0]][unit_b[1]]=swap
        return graph
            
    def playable_check(self):
        for i in (self.width-1)*self.height+self.width*(self.height-1):
            # if the game is playable after generate_move(i)
            pos_graph=self.move(self.get_move(self,i))
            

            

    def unit_check(self,graph,unit):
        current_color=graph[unit[0],unit[1]]
        vertical_match=np.array([[]])
        for i in range(1,unit[0]):
            if(graph[unit[0]-i,unit[1]]==current_color):
                np.append(vertical_match, [unit[0]-i,unit[1]])
            else:
                break
        for i in range(unit[0],graph.shape()[0]):
            if(graph[i,unit[1]]==current_color):
                np.append(vertical_match, [i,unit[1]])
            else:
                break
        horizontal_match=np.array([[]])
        for i in range(1,unit[1]):
            if(graph[unit[0],unit[1]-i]==current_color):
                np.append(horizontal_match, [unit[0],unit[1]-i])
            else:
                break
        for i in range(1,unit[0]):
            if(graph[unit[0],i]==current_color):
                np.append(horizontal_match, [unit[0],i])
            else:
                break
        return horizontal_match,vertical_match
        
    
    def fall(self,graph,horizontal_match,vertical_match):
        score=0
        # for this version, we ignore the possibility that vertical match and horizontal match are both greater than desired match
        if(vertical_match.shape()[0]>self.clear_length):
            for i in vertical_match:
                score+=1
                for j in range(0,i[1]-1):
                    graph[i[0],i[1]-j]=graph[i[0],i[1]-j+1]
                    self.checkpoints.append([i[0],i[1]-j])
                graph[i[0],0]=np.random.randint(self.color)
        elif(horizontal_match.shape()[0]>self.clear_length):
            for i in horizontal_match:
                score+=1
                for j in range(0,i[1]-1):
                    graph[i[0],i[1]-j]=graph[i[0],i[1]-j+1]
                    self.checkpoints.append([i[0],i[1]-j])
                graph[i[0],0]=np.random.randint(self.color)
        # move other element downward and add moved units to checkpoint
        return score, graph

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
            self.playable_check()
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
