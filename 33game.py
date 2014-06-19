import matplotlib.pyplot as plt
from random import uniform, randint
import numpy as np

class threegame:
    def __init__(self, profits):
        self.pro = profits
        self.cu_xs = [[0,0],[0,0]] 
        #左からプレイヤー0の相手が行動1を取ると思う信念/0の相手が2を取ると思う信念/1の相手が1という信念/
        self.x0_1s=[]
        self.x0_2s=[]
        self.x1_1s=[]
        self.x1_2s=[]
  #the example of profits:(((1,2),(3,4),(5,6)),
  #                        ((7,8),(9,10),(11,12)),
  #                      ((13,14),(15,16),(17,18)))

    def oneplay(self, ts_length):
        pro_cal = (np.transpose(self.pro)[0],np.transpose(np.transpose(self.pro)[1]))  # transform profits for calculate
        uni= [(uniform(0,1),uniform(0,1)),(uniform(0,1),uniform(0,1))] 
        for h in range(2):
            if uni[h][0] > uni[h][1]:
                self.cu_xs[h]=[uni[h][1],uni[h][0]-uni[h][1]]
            else:
                self.cu_xs[h]=[uni[h][0],uni[h][1]-uni[h][0]]
        #プレイヤー0,1がそれぞれ「相手が行動1,2をとる」と思う初期信念を定める
        cu_es=[[0,0,0],[0,0,0]]  # the list of expected payoff [(p0_do0,p0_do1,p0_do2),(p1_do0,p1_do1,p1_do2)]
        for i in range(ts_length):
            self.x0_1s.append(self.cu_xs[0][0])  # add x0_1(i) to x0_1s 
            self.x0_2s.append(self.cu_xs[0][1])
            self.x1_1s.append(self.cu_xs[1][0])  # add x1_1(i) to x1_1s
            self.x1_2s.append(self.cu_xs[1][1])
            exp = ((1-self.cu_xs[0][0]-self.cu_xs[0][1],self.cu_xs[0][0],self.cu_xs[0][1]),
                   (1-self.cu_xs[1][0]-self.cu_xs[1][1],self.cu_xs[1][0],self.cu_xs[1][1]))
            cu_es[0]=np.dot(pro_cal[0],exp[0])
            cu_es[1]=np.dot(pro_cal[1],exp[1])
            cu_as=[0,0]
            for j in range(2):
                if cu_es[j][0] > cu_es[j][1] and cu_es[j][0] > cu_es[j][1]:  # determine the act of player0(a0)
                    cu_as[j] = 0
                elif cu_es[j][1] > cu_es[j][0] and cu_es[j][1] > cu_es[j][2]:
                    cu_as[j] = 1
                elif cu_es[j][2] > cu_es[j][0] and cu_es[j][2] > cu_es[j][1]:
                    cu_as[j] = 2
                elif cu_es[j][0] == cu_es[j][1] > cu_es[j][2]:
                    cu_as[j] = randint(0,1)  # 1or0(random)
                elif cu_es[j][1] == cu_es[j][2] > cu_es[j][0]:
                    cu_as[j] = randint(0,1)+1  # 2or1(random)
                elif cu_es[j][2] == cu_es[j][0] > cu_es[j][1]:
                    cu_as[j] = randint(0,1)*2  # 2or0(random)
                else:
                    cu_as[j] = randint(0,1,2) #0or1or2(random)
            for k in range(2):  
                if cu_as[1-k] == 0:
                    self.cu_xs[k][0] = self.cu_xs[k][0]*(i+1)/(i+2)  #x(i+1)
                    self.cu_xs[k][1] = self.cu_xs[k][1]*(i+1)/(i+2)
                elif cu_as[1-k] ==1:
                    self.cu_xs[k][0] = (self.cu_xs[k][0]*(i+1)+1)/(i+2)
                    self.cu_xs[k][1] = self.cu_xs[k][1]*(i+1)/(i+2)
                else:
                    self.cu_xs[k][0] = self.cu_xs[k][0]*(i+1)/(i+2)
                    self.cu_xs[k][1] = (self.cu_xs[k][1]*(i+1)+1)/(i+2)
                 
    def playplot(self,ts_length): 
        self.oneplay(ts_length)
        plt.plot(self.x0_1s, 'b-', label='x_0_1(t)')  # x_0(t) is written with blue line
        plt.plot(self.x0_2s, 'g-', label='x_0_2(t)')
        plt.plot(self.x1_1s, 'r-', label='x_1_1(t)')  # x_0(t) is written with red line
        plt.plot(self.x1_2s, 'k-', label='x_1_2(t)') 
        plt.legend()
        plt.show()

    def histogram(self,n,ts_length):
        last_x0_1s = []
        last_x0_2s = []
        for j in range(n):
            self.oneplay(ts_length)
            last_x0_1s.append(self.cu_xs[0][0])
            last_x0_2s.append(self.cu_xs[0][1])
        ax = plt.subplot(121)
        ax.hist(last_x0_1s, alpha=0.6, bins=5)
        ax.set_xlim(xmin=0, xmax=1)
        t = 'x0_1,''ts = '+str(ts_length)+', times = '+str(n)
        ax.set_title(t)
        ax = plt.subplot(122)
        ax.hist(last_x0_2s, alpha=0.6, bins=5)
        ax.set_xlim(xmin=0, xmax=1)
        t = 'x0_2,''ts = '+str(ts_length)+', times = '+str(n)
        ax.set_title(t)
        
    def histplot(self,n,ts_length):
        self.histogram(n,ts_length)
        plt.show()
