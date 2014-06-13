import matplotlib.pyplot as plt
from random import uniform, randint
profits=((1,-1),(-1,1),(-1,1),(1,-1))# payoff of players(left-upper,right-upper,left-lower,right-lower)
ts_length = 1000 # timelength
cu_xs = [uniform(0,1),uniform(0,1)]  # x_0(t=0),x_1(t=0)
x0s = []
x1s = []
cu_es=[[0,0],[0,0]]  # the list of expedted payoff [(p0_do0,p0_do1),(p1_do0,p1_do1)]
cu_as=[0,0]
for i in range(ts_length):
    x0s.append(cu_xs[0])  # add x0(i) to x0s 
    x1s.append(cu_xs[1])  # add x1(i) to x1s
    for j in range(len(cu_es)):  # j:number of player
        for k in range(len(cu_es[0])):  # k:number of act
            cu_es[j][k] = profits[k*(1+j)][j]*cu_xs[j]+profits[k*(1+j)+2-j][j]*(1-cu_xs[j])  #expected payoff of player0 by doing act0
        if cu_es[j][0] > cu_es[j][1]:  # determine the act of player0(a0)
            cu_as[j] = 0
        elif cu_es[j][0] == cu_es[j][1]:
            cu_as[j] = randint(0,1)  # 1or0(random)
        else:
            cu_as[j] = 1
        cu_xs[j] = (cu_xs[j]*(i+1)+cu_as[1-j])/(i+2)  #x_j(i+1)
plt.plot(x0s, 'b-', label='x_0(t)')  # x_0(t) is written with blue line
plt.plot(x1s, 'r-', label='x_1(t)')  # x_0(t) is written with red line
plt.legend()
plt.show()
