import matplotlib.pyplot as plt
from random import uniform, randint

profit_0=(1,-1,-1,1)  # payoff of player0(left-upper,right-upper,left-lower,right-lower)
profit_1=(-1,1,1,-1)  # payoff of player1(left-upper,right-upper,left-lower,right-lower)


ts_length = 1000  # timelength
cu_x0 = uniform(0,1)  # x_0(t=0)
cu_x1 = uniform(0,1)  # x_1(t=0)
x0s = []
x1s = []
for i in range(ts_length):
    x0s.append(cu_x0)  # add x0(i) to x0s 
    x1s.append(cu_x1)  # add x1(i) to x1s
    cu_e00 = profit_0[0]*cu_x0+profit_0[2]*(1-cu_x0)  #expected payoff of player0 by do act0
    cu_e01 = profit_0[1]*cu_x0+profit_0[3]*(1-cu_x0)  #expected payoff of player0 by do act1
    cu_e10 = profit_1[0]*cu_x1+profit_1[1]*(1-cu_x1)  #expected payoff of player1 by do act0
    cu_e11 = profit_1[2]*cu_x1+profit_1[3]*(1-cu_x1)  #expected payoff of player1 by do act1

    if cu_e00 > cu_e01:  # determine the act of player0(a0)
        cu_a0 = 0
    elif cu_e00 == cu_e01:
        cu_a0 = randint(0,1)  # 1or0(random)
    else:
        cu_a0 = 1

    if cu_e10 > cu_e11:  # determine the act of player0(a0)
        cu_a1 = 0
    elif cu_e10 == cu_e11:
        cu_a1 = randint(0,1)  # 1or0(random)
    else:
        cu_a1 = 1
    cu_x0 = (cu_x0*(i+1)+cu_a1)/(i+2)  #x_0(i+1)
    cu_x1 = (cu_x1*(i+1)+cu_a0)/(i+2)
plt.plot(x0s, 'b-', label='x_0(t)')  # x_0(t) is written with blue line
plt.plot(x1s, 'r-', label='x_1(t)')  # x_0(t) is written with red line
plt.legend()
plt.show()
