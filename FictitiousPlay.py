import matplotlib.pyplot as plt
from random import uniform, randint

profits=[[1,-1],[-1,1],[-1,1],[1,-1]]  # payoff of players(left-upper,right-upper,left-lower,right-lower)

ts_length = 1000  # timelength
cu_x0 = uniform(0,1)  # x_0(t=0)
cu_x1 = uniform(0,1)  # x_1(t=0)
x0s = []
x1s = []
for i in range(ts_length):
    x0s.append(cu_x0)  # add x0(i) to x0s 
    x1s.append(cu_x1)  # add x1(i) to x1s
    cu_es=[[0,0],[0,0]]  # the list of expedted payoff [(p0_do0,p0_do1),(p1_do0,p1_do1)]
    cu_es[0][0] = profits[0][0]*cu_x0+profits[2][0]*(1-cu_x0)  #expected payoff of player0 by do act0
    cu_es[0][1] = profits[1][0]*cu_x0+profits[3][0]*(1-cu_x0)  #expected payoff of player0 by do act1
    cu_es[1][0] = profits[0][1]*cu_x1+profits[1][1]*(1-cu_x1)  #expected payoff of player1 by do act0
    cu_es[1][1] = profits[2][1]*cu_x1+profits[3][1]*(1-cu_x1)  #expected payoff of player1 by do act1

    
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
    cu_x0 = (cu_x0*(i+1)+cu_a1)/(i+2)  #x_0(i+1)
    cu_x1 = (cu_x1*(i+1)+cu_a0)/(i+2)
plt.plot(x0s, 'b-', label='x_0(t)')  # x_0(t) is written with blue line
plt.plot(x1s, 'r-', label='x_1(t)')  # x_0(t) is written with red line
plt.legend()
plt.show()