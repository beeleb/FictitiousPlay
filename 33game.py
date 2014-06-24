import matplotlib.pyplot as plt
from random import uniform, randint, choice
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class threegame:
    def __init__(self, profits):
        self.pro = profits
        self.cu_xs = [[0, 0], [0, 0]]
        """
        信念を表す。左から順に
        Player0の相手が行動1を取ると思う信念
        Player0の相手が行動2を取ると思う信念
        Player1の相手が行動1を取ると思う信念
        Player1の相手が行動2を取ると思う信念
        """
        self.x0_0s = []
        self.x0_1s = []
        self.x0_2s = []
        self.x1_0s = []
        self.x1_1s = []
        self.x1_2s = []
        """
        the example of profits:
        (((1,2),(3,4),(5,6)),
         ((7,8),(9,10),(11,12)),
        ((13,14),(15,16),(17,18)))
        """
        self.timelist =[]
    def oneplay(self, ts_length):
        self.x0_0s = []
        self.x0_1s = []
        self.x0_2s = []
        self.x1_0s = []
        self.x1_1s = []
        self.x1_2s = []
        self.timelist =[]
        pro_cal = (np.transpose(self.pro)[0],
                   np.transpose(np.transpose(self.pro)[1]))
        # transform profits for calculate
        uni = [[uniform(0, 1), uniform(0, 1)], [uniform(0, 1), uniform(0, 1)]]
        for h in range(2):
            uni[h].sort()
            self.cu_xs[h] = [uni[h][0],1-uni[h][1]]
        # プレイヤー0,1がそれぞれ「相手が行動1,2をとる」と思う初期信念を定める
        cu_es = np.empty([2,3])
        """
        the list of expected payoff when
        [(p0_do0,p0_do1,p0_do2),(p1_do0,p1_do1,p1_do2)]
        """
        for i in range(ts_length):
            self.timelist.append(i)
            self.x0_0s.append(1-self.cu_xs[0][0]-self.cu_xs[0][1])
            self.x0_1s.append(self.cu_xs[0][0])  # add x0_1(i) to x0_1s
            self.x0_2s.append(self.cu_xs[0][1])  # add x0_2(i) to x0_2s
            self.x1_0s.append(1-self.cu_xs[1][0]-self.cu_xs[1][1])
            self.x1_1s.append(self.cu_xs[1][0])  # add x1_1(i) to x1_1s
            self.x1_2s.append(self.cu_xs[1][1])  # add x1_2(i) to x1_2s
            
            exp = ((1-self.cu_xs[0][0]-self.cu_xs[0][1],
                    self.cu_xs[0][0], self.cu_xs[0][1]),
                   (1-self.cu_xs[1][0]-self.cu_xs[1][1],
                    self.cu_xs[1][0], self.cu_xs[1][1]))
            cu_es[0] = np.dot(pro_cal[0], exp[0])
            cu_es[1] = np.dot(pro_cal[1], exp[1])
            cu_as = [0, 0]
            a_choices=[[],[]]
            for j in range(2):
                for k in range(3):
                    if cu_es[j].max() == cu_es[j][k]:
                        a_choices[j].append(k)
                # 最大値をとるような行動を選択肢に含める
                cu_as[j] = random.choice(a_choices[j])
                # determine the act of player0(a0)
            for k in range(2):
                if cu_as[1-k] == 0:
                    self.cu_xs[k][0] = self.cu_xs[k][0]*(i+1)/(i+2)  # x(i+1)
                    self.cu_xs[k][1] = self.cu_xs[k][1]*(i+1)/(i+2)
                elif cu_as[1-k] == 1:
                    self.cu_xs[k][0] = (self.cu_xs[k][0]*(i+1)+1)/(i+2)
                    self.cu_xs[k][1] = self.cu_xs[k][1]*(i+1)/(i+2)
                else:
                    self.cu_xs[k][0] = self.cu_xs[k][0]*(i+1)/(i+2)
                    self.cu_xs[k][1] = (self.cu_xs[k][1]*(i+1)+1)/(i+2)

    def playplot(self, ts_length):
        self.oneplay(ts_length)
        """
        plt.plot(self.x0_1s, 'b-', label='x_0_1(t)')  # x_0_1(t) is blue line
        plt.plot(self.x0_2s, 'c-', label='x_0_2(t)')  # x_0_2(t) is cyan
        plt.plot(self.x1_1s, 'r-', label='x_1_1(t)')  # x_1_1(t) is red
        plt.plot(self.x1_2s, 'm-', label='x_1_2(t)')  # x_1_2(t) is magenta
        """
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot_wireframe(self.x0_0s,self.x0_1s,self.x0_2s, color = 'b',label='x_0(t)')
        ax.plot_wireframe(self.x1_0s,self.x1_1s,self.x1_2s, color = 'r',label='x_1(t)')
        ax.set_xlim(xmin=0, xmax=1)
        ax.set_ylim(ymin=0, ymax=1)
        ax.set_zlim(zmin=0, zmax=1)
        plt.legend()
        plt.show()

    def playsave(self, ts_length, name):  # name is str
        self.oneplay(ts_length)
        """
        plt.plot(self.x0_1s, 'b-', label='x_0_1(t)')  # x_0_1(t) is blue line
        plt.plot(self.x0_2s, 'c-', label='x_0_2(t)')  # x_0_2(t) is cyan
        plt.plot(self.x1_1s, 'r-', label='x_1_1(t)')  # x_1_1(t) is red
        plt.plot(self.x1_2s, 'm-', label='x_1_2(t)')  # x_1_2(t) is magenta
        """
        fig = plt.figure()
        ax = Axes3D(fig)
        
        """
        ax.plot_wireframe(self.timelist,self.x0_1s,self.x0_2s, color = 'b',label='x_0(t)')
        ax.plot_wireframe(self.timelist,self.x1_1s,self.x1_2s, color = 'r',label='x_1(t)')
        """
        ax.plot_wireframe(self.x0_0s,self.x0_1s,self.x0_2s, color = 'b',label='x_0(t)')
        ax.plot_wireframe(self.x1_0s,self.x1_1s,self.x1_2s, color = 'r',label='x_1(t)')
        ax.set_xlim(xmin=0, xmax=1)
        ax.set_ylim(ymin=0, ymax=1)
        ax.set_zlim(zmin=0, zmax=1)
        plt.legend()
        plt.savefig(str(name)+'.png', bbox_inches='tight', pad_inches=0)
        plt.savefig(str(name)+'.pdf', bbox_inches='tight', pad_inches=0)
        plt.close()

    def histogram(self, n, ts_length):
        last_x0_1s = []
        last_x0_2s = []
        for j in range(n):
            self.oneplay(ts_length)
            last_x0_1s.append(self.cu_xs[0][0])
            last_x0_2s.append(self.cu_xs[0][1])
        ax = plt.subplot(121)
        ax.hist(last_x0_1s, color='b', alpha=0.6, bins=5)
        ax.set_xlim(xmin=0, xmax=1)
        t = 'x0_1,''ts = '+str(ts_length)+', times = '+str(n)
        ax.set_title(t)
        ax = plt.subplot(122)
        ax.hist(last_x0_2s, color='r', alpha=0.6, bins=5)
        ax.set_xlim(xmin=0, xmax=1)
        t = 'x0_2,''ts = '+str(ts_length)+', times = '+str(n)
        ax.set_title(t)

    def histplot(self, n, ts_length):
        self.histogram(n, ts_length)
        plt.show()

    def histsave(self, n, ts_length, name):  # name is str
        self.histogram(n, ts_length)
        plt.savefig(str(name)+'.png', bbox_inches='tight', pad_inches=0)
        plt.savefig(str(name)+'.pdf', bbox_inches='tight', pad_inches=0)
        plt.close()

f=threegame((((1,0),(0,0),(0,1)),((0,1),(1,0),(0,0)),((0,0),(0,1),(1,0))))
# playplotに関してはそこそこ性能のよいはずのPCでもt=10000でカクつき、t=100000では動かなくなったのであまり増やしてはいけない