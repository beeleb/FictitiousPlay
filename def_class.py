import matplotlib.pyplot as plt
from random import uniform, randint
import numpy as np


class FP:

    def __init__(self, profits):
        self.pro = profits
        self.cu_xs = [0, 0]
        self.x0s = []
        self.x1s = []
    # the example of profits:
    # (((1,-1),(-1,1)),
    # ((-1,1),(1,-1)))

    def oneplay(self, ts_length):
        pro_cal = (np.transpose(self.pro)[0],
                   np.transpose(np.transpose(self.pro)[1]))
        # transform profits for calculate
        self.x0s = []
        self.x1s = []
        self.cu_xs = [uniform(0, 1), uniform(0, 1)]
        # プレイヤー0,1がそれぞれ「相手が行動1をとる」と思う信念
        cu_es = [[0, 0], [0, 0]]
        # the list of expedted payoff [(p0_do0,p0_do1),(p1_do0,p1_do1)]
        for i in range(ts_length):
            self.x0s.append(self.cu_xs[0])  # add x0(i) to x0s
            self.x1s.append(self.cu_xs[1])  # add x1(i) to x1s
            exp = ((1-self.cu_xs[0], self.cu_xs[0]),
                   (1-self.cu_xs[1], self.cu_xs[1]))
            cu_es[0] = np.dot(pro_cal[0], exp[0])
            cu_es[1] = np.dot(pro_cal[1], exp[1])
            cu_as = [0, 0]
            for j in range(2):
                if cu_es[j][0] > cu_es[j][1]:
                    cu_as[j] = 0
                elif cu_es[j][0] == cu_es[j][1]:
                    cu_as[j] = randint(0, 1)  # 1or0(random)
                else:
                    cu_as[j] = 1
            # determine the act of player0(a0)
            for k in range(2):
                self.cu_xs[k] = (self.cu_xs[k]*(i+1)+cu_as[1-k])/(i+2)
                # x(i) to x(i+1)
                # cu_as[1-i]という記述はプレイヤー数が2の時にしか使えない
            # 上のfor文に入れるとt=iでプレイヤー0はa_1(i-1)を,
            # プレイヤー1はa_0(i)を足すことになるので
            # 両者がともにa(i)を足すよう分けた

    def playplot(self, ts_length):
        self.oneplay(ts_length)
        plt.plot(self.x0s, 'b-', label='x_0(t)')  # blue line means x_0(t)
        plt.plot(self.x1s, 'r-', label='x_1(t)')  # red line means x_1(t)
        plt.legend()
        plt.show()

    def playsave(self, ts_length, name):  # name is str
        self.oneplay(ts_length)
        plt.plot(self.x0s, 'b-', label='x_0(t)')  # blue line means x_0(t)
        plt.plot(self.x1s, 'r-', label='x_1(t)')  # red line means x_1(t)
        plt.legend()
        plt.savefig(str(name)+'.png', bbox_inches='tight', pad_inches=0)
        plt.savefig(str(name)+'.pdf', bbox_inches='tight', pad_inches=0)
        plt.close()

    def histogram(self, n, ts_length):
        last_x0s = []
        for j in range(n):
            self.oneplay(ts_length)
            last_x0s.append(self.cu_xs[0])
        ax = plt.subplot(111)
        ax.hist(last_x0s, alpha=0.6, bins=5)
        ax.set_xlim(xmin=0, xmax=1)
        t = 'ts = '+str(ts_length)+', times = '+str(n)
        ax.set_title(t)

    def histplot(self, n, ts_length):
        self.histogram(n, ts_length)
        plt.show()

    def histsave(self, n, ts_length, name):  # name is str
        self.histogram(n, ts_length)
        plt.savefig(str(name)+'.png', bbox_inches='tight', pad_inches=0)
        plt.savefig(str(name)+'.pdf', bbox_inches='tight', pad_inches=0)
        plt.close()
