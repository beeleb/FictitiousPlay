import matplotlib.pyplot as plt
from random import uniform, randint

class FP:

    def __init__(self, profits):
        self.pro = profits
        self.cu_x0 = 0
        self.cu_x1 = 0
        self.x0s=[]
        self.x1s=[]
  #the example of profits:((1,-1),(-1,1),(-1,1),(1,-1)) :payoff of players(left-upper,right-upper,left-lower,right-lower)

    def play(self, ts_length): 
        self.x0s=[]
        self.x1s=[]
        self.cu_x0= uniform(0,1)
        self.cu_x1= uniform(0,1)
        cu_es=[[0,0],[0,0]]  # the list of expedted payoff [(p0_do0,p0_do1),(p1_do0,p1_do1)]
        cu_as=[0,0]
        for i in range(ts_length):
            self.x0s.append(self.cu_x0)  # add x0(i) to x0s 
            self.x1s.append(self.cu_x1)  # add x1(i) to x1s
            cu_es=[[0,0],[0,0]]  # the list of expedted payoff [(p0_do0,p0_do1),(p1_do0,p1_do1)]
            cu_es[0][0] = self.pro[0][0]*self.cu_x0+self.pro[2][0]*(1-self.cu_x0)  #expected payoff of player0 by do act0
            cu_es[0][1] = self.pro[1][0]*self.cu_x0+self.pro[3][0]*(1-self.cu_x0)  #expected payoff of player0 by do act1
            cu_es[1][0] = self.pro[0][1]*self.cu_x1+self.pro[1][1]*(1-self.cu_x1)  #expected payoff of player1 by do act0
            cu_es[1][1] = self.pro[2][1]*self.cu_x1+self.pro[3][1]*(1-self.cu_x1)  #expected payoff of player1 by do act1
            if cu_es[0][0] > cu_es[0][1]:  # determine the act of player0(a0)
                cu_a0 = 0
            elif cu_es[0][0] == cu_es[0][1]:
                cu_a0 = randint(0,1)  # 1or0(random)
            else:
                cu_a0 = 1

            if cu_es[1][0] > cu_es[1][1]:  # determine the act of player0(a0)
                cu_a1 = 0
            elif cu_es[1][0] == cu_es[1][1]:
                cu_a1 = randint(0,1)  # 1or0(random)
            else:
                cu_a1 = 1
            self.cu_x0 = (self.cu_x0*(i+1)+cu_a1)/(i+2)  #x_0(i+1)
            self.cu_x1 = (self.cu_x1*(i+1)+cu_a0)/(i+2)

    def plot(self,ts_length): 
        self.play(ts_length)
        plt.plot(self.x0s, 'b-', label='x_0(t)')  # x_0(t) is written with blue line
        plt.plot(self.x1s, 'r-', label='x_1(t)')  # x_0(t) is written with red line
        plt.legend()
        plt.show()

    def histo(self,n,ts_length):
        last_x0s = []
        for j in range(n):
            self.play(ts_length)
            last_x0s.append(self.cu_x0)
        ax = plt.subplot(111)
        ax.hist(last_x0s, alpha=0.6, bins=10)
        t = 'ts = '+str(ts_length)+', times = '+str(n)
        xticks=[0.46,0.48,0.5,0.52,0.54]
        yticks=[5,10,15,20,25]
        ax.set_title(t)
        ax.set_xticks(xticks) 
        ax.set_yticks(yticks)
        plt.show()
