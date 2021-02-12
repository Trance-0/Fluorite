'''
    2048小游戏
'''
import pygame,sys,random,numpy
 
class MyGame(object):
 
    '''
       1.初始化函数
    '''
    def __init__(self):
        # 窗体
        self.screen = pygame.display.set_mode((460, 620),0,0)
        # 背景图
        self.back = pygame.image.load("2048.png")
        # 4行4列
        self.Size = 4
        # 每个块的长宽
        self.Block_WH = 100
        # 两个块之间的间隙
        self.Block_Space = 10
        # 初始化矩阵4*4的0矩阵
        self.matrix = numpy.zeros([self.Size,self.Size])
        # 设置计分器
        self.Score = 0
        # 数块颜色字典
        self.Block_Color = {
            0:(205,193,180),
            2:(255,255,220),
            4:(255,255,130),
            8:(255,255,0),
            16:(255,220,128),
            32:(255,220,0),
            64:(255,190,0),
            128:(255,160,0),
            256:(255,130,0),
            512:(255,100,0),
            1024:(255,70,0),
            2048:(255,40,0),
            4096:(255,10,0),
        }
        # 二维列表zerolist
        self.zerolist = []
        # 游戏结束标志
        self.flag = False
 
    '''
        5.初始化矩阵
    '''
    def initData(self,matrix = None,zerolist = None):
        # 若矩阵为空，则拷贝初始化矩阵
        if matrix is None:
            matrix = self.matrix.copy()
        # 若zerolist为空，则随机返回(x,y)位置，否则返回任意一个0元素位置
        a,b = self.getRandomLocal(zerolist)
        n = self.getNewNum()
        matrix[a][b] = n
        # 返回初始化任意位置为2或者4的矩阵
        return matrix
 
    # 5.1 获取要生成数字方块的位置
    def getRandomLocal(self,zerolist = None):
        # 5.1.1 若为空，随机生成某行某列
        if zerolist == None:
            a = random.randint(0,self.Size-1)
            b = random.randint(0,self.Size-1)
        # 5.1.2 若不为空，则从zerolist中随机抽取一个数字为0的列表坐标
        else:
            a,b = random.sample(zerolist,1)[0]
        return a,b
 
    # 5.2 随机返回新数字2或4
    def getNewNum(self):
        # 5.2.1 生成0和1之间的随机浮点数
        n = random.random()
        if n > 0.8:
            n = 4
        else:
            n = 2
        return n
 
 
    '''
       2.业务执行模块
    '''
    def action(self):
        # 2.1 循环所有监听时间
        for event in pygame.event.get():
            # 2.2 判断退出
            if event.type == pygame.QUIT:
                sys.exit()
            # 2.3 判断键盘监听
            elif event.type == pygame.KEYDOWN:
                # 2.4 判断按键,当游戏结束时，不可再按
                if event.key == pygame.K_UP and self.flag == False:
                    self.matrix = self.upAction()
                elif event.key == pygame.K_DOWN and self.flag == False:
                    self.matrix = self.downAction()
                elif event.key == pygame.K_LEFT and self.flag == False:
                    self.matrix = self.leftAction()
                elif event.key == pygame.K_RIGHT and self.flag == False:
                    self.matrix = self.rightAction()
            # 2.8 判断鼠标监听
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 2.8.1 获取鼠标按下的位置
                mouseX,mouseY = pygame.mouse.get_pos()
                # 2.8.3 重新开始游戏
                if 335 < mouseX < 430 and 95 < mouseY < 125:
                    # 2.8.4 重新初始化矩阵、分数、结束标志
                    self.matrix = numpy.zeros([self.Size,self.Size])
                    self.matrix = myGame.initData()
                    self.Score = 0
                    self.flag = False
            # 2.9 判断游戏是否结束
            # 2.9.1 当方块中的数字最大为2048时，游戏成功
            if self.matrix.max() == 256:
                self.flag = True
            # 2.9.2 当方块中的数字都填满时，且移动方块后界面不会修改，则游戏失败
            elif self.matrix.min() != 0:
                self.flag = self.gameOver()
 
    # 2.4.1 向上操作
    def upAction(self):
        print(self.matrix)
        matrix = self.matrix.T
        print(matrix)
        newmatrix = self.toSequence(matrix)
        print(newmatrix)
        return newmatrix.T
 
    # 2.4.2 向下操作
    def downAction(self):
        # print(self.matrix)
        matrix = self.matrix[::-1].T
        # print(matrix)
        newmatrix = self.toSequence(matrix)
        # print(newmatrix)
        return newmatrix.T[::-1]
 
    # 2.4.3 向左操作
    def leftAction(self):
        # print(self.matrix)
        newmatrix = self.toSequence(self.matrix)
        # print(newmatrix)
        return newmatrix
 
    # 2.4.4 向右操作
    def rightAction(self):
        # print(self.matrix)
        matrix = self.matrix[:,::-1]
        # print(matrix)
        newmatrix = self.toSequence(matrix)
        # print(newmatrix)
        return newmatrix[:,::-1]
 
    # 2.5 矩阵处理
    def toSequence(self,matrix):
        # 2.5.1 获得矩阵的行，列
        row,col = matrix.shape
        # 2.5.2 遍历矩阵
        for i in range(row):
            # 2.5.3 分别将每行矩阵中的0元素删除，从而实现了数字的移动
            newList = self.removeZero(list(matrix[i]))
            matrix[i] = newList
            # 2.5.4 在zerolist中添加0元素的位置，计算0的个数
            for k in range(self.Size-1,self.Size-newList.count(0)-1,-1):
                self.zerolist.append((i,k))
        # 2.5.5 矩阵中有最小值0，才可以在0位置处添加随机数
        if matrix.min() == 0:
            self.initData(matrix,self.zerolist)
            # 列表清空
            self.zerolist = []
        return matrix
 
    # 2.6 删除0
    def removeZero(self,rowlist):
        while True:
            # 2.6.1 拷贝一份list
            mid = rowlist[:]
            try:
                # 2.6.2 移除一个0，在最后加上一个0
                rowlist.remove(0)
                rowlist.append(0)
            except:
                pass
            # 2.6.3 若列表中没有0，退出循环
            if rowlist == mid:
                break
        # 2.6.4 返回新列表，数据要进行修改，调用combineList()函数
        return self.combineList(rowlist)
 
    # 2.7 列表数字调整，相同相加
    def combineList(self,rowlist):
        start_num = 0
        end_num = self.Size-rowlist.count(0)-1
        # 2.7.1 循环依次比较列表中非0位置的数字
        while start_num < end_num:
            if rowlist[start_num] == rowlist[start_num+1]:
                # 2.7.2 分数相同相加
                rowlist[start_num] *= 2
                # 2.7.3 每次返回累加的分数
                self.Score += int(rowlist[start_num])
                # 2.7.4 数字前移，末尾加0
                rowlist[start_num+1:] = rowlist[start_num+2:]
                rowlist.append(0)
            start_num += 1
        return rowlist
 
    # 2.9 游戏结束判断
    def gameOver(self):
        testmatrix = self.matrix.copy()
        a,b = testmatrix.shape
        for i in range(a):
            for j in range(b-1):
                # 2.9.1 如果每行存在相邻两个数相同，则游戏没有结束
                if testmatrix[i][j] == testmatrix[i][j+1]:
                    print('游戏没有结束')
                    return False
        for i in range(b):
            for j in range(a-1):
                # 2.9.1 如果每列存在相邻两个数相同，则游戏没有结束
                if testmatrix[j][i] == testmatrix[j+1][i]:
                    print('游戏没有结束')
                    return False
        print('游戏结束')
        return True
 
    '''
        3.图形图像绘制模块
    '''
    def paint(self):
        # 3.1 绘制背景图上部分
        self.screen.blit(self.back,(0,0))
        # 3.1.1 初始化字体样式
        pygame.font.init()
        # 3.1.2 设置系统字体样式 华文行楷
        font = pygame.font.SysFont("stxingkai",40)
        # 3.1.3 添加分数居中显示
        fontW,fontH = font.size(str(self.Score))
        self.screen.blit(font.render("%d"%self.Score,True,(238,253,60)),((460-fontW)/2+152,45))
        # 3.2 绘制背景图下部分
        # 3.2.1 获取矩阵行数和列数
        a,b = self.matrix.shape
        # 3.2.2 循环遍历，依次绘图
        for i in range(a):
            for j in range(b):
                # 3.2.3 确定方块的初始位置
                w = j * self.Block_WH + (j + 1) * self.Block_Space
                h = i * self.Block_WH + (i + 1) * self.Block_Space
                # 3.2.4 画出方块   参数：位置，颜色,绘图的起始位置,矩形长宽
                pygame.draw.rect(self.screen,self.Block_Color[int(self.matrix[i][j])],(w+5,h+155,100,100))
                # 3.2.5 若初始化方块内有数字，修改方块背景颜色，并添加数字
                if self.matrix[i][j] != 0:
                    # 3.2.6 设置使用系统字体 华文行楷
                    font = pygame.font.SysFont("stxingkai",80)
                    # 3.2.7 矩阵元素为浮点型===>int()===>str()
                    #        获取数字的字体大小来确定绘图位置
                    fw,fh = font.size(str(int(self.matrix[i][j])))
                    self.screen.blit(font.render(str(int(self.matrix[i][j])),True,(4,145,249)), \
                                     (w+(100-fw)/2+5,h+(110-fh)/2+155))
        # 3.3 游戏结束判断
        if self.flag:
            # 3.3.1 初始化字体样式
            pygame.font.init()
            # 3.3.2 设置系统字体样式 宋体
            font = pygame.font.SysFont("simsunnsimsun",40)
            # 3.3.3 绘图
            Str = "游戏结束"
            self.screen.blit(font.render("%s" % Str,True,(251,15,2)),(170,360))
 
 
    '''
        4.主函数
    '''
    def menu(self):
        # 4.1 设置窗口标题
        pygame.display.set_caption("2048小游戏")
        # 4.7 初始化矩阵
        self.matrix = myGame.initData()
        # 4.2 死循环
        while True:
            # 4.6 背景颜色填充
            self.screen.fill((250,248,240))
            # 4.3 业务执行模块
            self.action()
            # 4.4 图形图像绘制模块
            self.paint()
            # 4.5 刷新屏幕
            pygame.display.update()
 
 
if __name__ == '__main__':
    myGame = MyGame()
    myGame.menu()
