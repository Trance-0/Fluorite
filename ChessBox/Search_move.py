class piece:
	
	def __init__(self,name,symbol,move):
		self.name=name
		self.symbol=symbol
		self.move=move	
	
	def copy():
		return piece(self.name,self.symbol,self.move)
	
	def compare(self,other):
		return type(self)==type(other) and self.name==other.name and self.symbol==other.symbol and self.move==other.move
		
class puzzle:
	def __init__(self,arr,pieces):
		self.size=len(arr[0])
		self.pieces=pieces
		self.game=[]
		self.target_step=0
		for i in range(len(arr)):
			for j in range(len(arr[i])):
				self.game.append([])
				self.game[i].append(pieces[arr[i][j]])
				if pieces[arr[i][j]].symbol!="X":
					self.target_step+=1
		
	def compare(self,other):
		if self.size!=other_game.size:
			return False
		for i in range(0,size):
			for j in range(0,size):
				if self.game[i][j].compare(other.game[i][j])!=True:
					return False;
		return True
		
	def have_piece(self,x,y):
		return self.game[x][y].symbol != "X"

	def move(self,x1,y1,x2,y2):
		new_game=self.copy()
		new_game.game[x2][y2]=new_game.game[x1][y1]
		new_game.game[x1][y1]=new_game.pieces["X"]
		return new_game
			
	def is_legal_move(self,x1,y1,x2,y2):
		for i in self.game[x1][y1].move:
			if x1+i[0]==x2 and y1+i[1]==y2 and y2>=0 and y2<self.size and x2>=0 and x2<self.size:
				return True
		return False
		
	def killing_move(self,x,y):
		killing_pos=[]
		if self.have_piece(x,y):
			temp_piece=self.game[x][y]
			for i in temp_piece.move:
				if self.is_legal_move(x,y,x+i[0],y+i[1]) and self.have_piece(x+i[0],y+i[1]) :
					killing_pos.append([x+i[0],y+i[1]])
		return killing_pos
		
	def game_to_arr(self):
		result=[]
		for i in range(0,len(self.game)):
			result.append([])
			for j in self.game[i]:
				result[i].append(j.symbol)
		return result
		
	def __str__(self):
		result=""
		for i in self.game:
			for j in i:
				result+=j.symbol
			result+="\n"
		return result
		
	def copy(self):
		return puzzle(self.game_to_arr(),self.pieces)

histogame=[]
answer=[]
target_depth=6

def print_histogame():
	global histogame
	print("-------histogame-------")
	for i in histogame:
		print(i)
	print("---------end-----------")

def killing_recursive():
	global histogame,answer, target_depth
	if len(histogame)==target_depth:
			answer.append(histogame.copy())
	current_game=histogame[len(histogame)-1].copy()
	#print("depth="+str(len(histogame)))
	#print(current_game)
	for i in range(0,current_game.size):
		for j in range(0,current_game.size):
			if current_game.have_piece(i,j):
				next_move=current_game.killing_move(i,j)
				if len(next_move)>0:
					for k in next_move:
						#print("generate new move from")
						#print(current_game)
						#print("to")
						new_game=current_game.move(i,j,k[0],k[1])
						#print(new_game)
						print(str.format("testing move {},{} to {},{}",i,j,k[0],k[1]))
						histogame.append(new_game)
						#print_histogame()
						killing_recursive()
	print("Damn it.")					
	histogame.pop(len(histogame)-1)
							
def killing_DFS():
	while len(histogame)>0:
		killing_recursive()
	
king_move=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
queen_move=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1],[2,0],[0,2],[-2,0],[0,-2],[2,2],[-2,-2],[-2,2],[2,-2],[3,0],[0,3],[-3,0],[0,-3],[3,3],[-3,-3],[-3,3],[3,-3],[4,0],[0,4],[-4,0],[0,-4],[4,4],[-4,-4],[-4,4],[4,-4],[5,0],[0,5],[-5,0],[0,-5],[5,5],[-5,-5],[-5,5],[5,-5],[6,0],[0,6],[-6,0],[0,-6],[6,6],[-6,-6],[-6,6],[6,-6],[7,0],[0,7],[-7,0],[0,-7],[7,7],[-7,-7],[-7,7],[7,-7],[8,0],[0,8],[-8,0],[0,-8],[8,8],[-8,-8],[-8,8],[8,-8]]
bishop_move=[[1,1],[-1,-1],[-1,1],[1,-1],[2,2],[-2,-2],[-2,2],[2,-2],[3,3],[-3,-3],[-3,3],[3,-3],[4,4],[-4,-4],[-4,4],[4,-4],[5,5],[-5,-5],[-5,5],[5,-5],[6,6],[-6,-6],[-6,6],[6,-6],[7,7],[-7,-7],[-7,7],[7,-7],[8,8],[-8,-8],[-8,8],[8,-8]]
knight_move=[[2,3],[3,2],[-2,3],[3,-2],[-2,-3],[-3,-2],[2,-3],[-3,2]]
rook_move=[[1,0],[0,1],[-1,0],[0,-1],[2,0],[0,2],[-2,0],[0,-2],[3,0],[0,3],[-3,0],[0,-3],[4,0],[0,4],[-4,0],[0,-4],[5,0],[0,5],[-5,0],[0,-5],[6,0],[0,6],[-6,0],[0,-6],[7,0],[0,7],[-7,0],[0,-7],[8,0],[0,8],[-8,0],[0,-8]]
pawn_move=[[1,1],[1,-1],[-1,-1],[-1,1]]

king=piece("king","K",king_move)
queen=piece("queen","Q",queen_move)
bishop=piece("bishop","B",bishop_move)
knight=piece("knight","K",knight_move)
rook=piece("rook","R",rook_move)
pawn=piece("pawn","P",pawn_move)
blank=piece("blank","X",[])

pieces={king.symbol:king,queen.symbol:queen,bishop.symbol:bishop,knight.symbol:knight,rook.symbol:rook,pawn.symbol:pawn,blank.symbol:blank}

test_game=[["X","R","X","X"],
		 ["B","X","R","K"],
		 ["X","P","X","X"],
		 ["X","B","X","X"]]
histogame.append(puzzle(test_game,pieces))
killing_DFS()
for i in range(0,len(answer)):
	print("answer "+str(i+1))
	for j in answer[i]:
		print(j)

