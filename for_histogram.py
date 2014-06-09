import matplotlib.pyplot as plt
from random import uniform, randint
import numpy as np
from scipy.stats import norm
last_x0s = []
n = 100 #繰り返し回数
ts_length = 1000  # 時間の長さ
xticks=[0.4,0.45,0.5,0.55,0.6]
yticks=[5,10,15,20,25,30]
for j in range(n):
    cu_x0 = uniform(0,1)  # x_0(t=0)
    cu_x1 = uniform(0,1)  # x_1(t=0)
    x0s = []
    x1s = []
    for i in range(ts_length):
        x0s.append(cu_x0)  # x0(i)を加えている, for文により0~t-1
        x1s.append(cu_x1)  # x1(i)を加えている
        cu_e00 = 1-2*cu_x0  #プレイヤー0が行動0を取った時の期待利得
        cu_e10 = 2*cu_x1-1  #プレイヤー1が行動0を取った時の期待利得
# このゲームだと行動0を取った場合と行動1を取った場合の期待利得の和は常に0なので行動0の期待利得のみ定義すればよい
        if cu_e00 > 0:  # プレイヤー0の行動a0を定める
            cu_a0 = 0
        elif cu_e00 == 0:
            cu_a0 = randint(0,1)  # 1or0(random)
        else:
            cu_a0 = 1

        if cu_e10 > 0:  # プレイヤー1の行動a1を定める
            cu_a1 = 0
        elif cu_e10 == 0:
            cu_a1 = randint(0,1)  # 1or0(random)
        else:
            cu_a1 = 1
        cu_x0 = (cu_x0*(i+1)+cu_a1)/(i+2)  #x_0(i+1)
        cu_x1 = (cu_x1*(i+1)+cu_a0)/(i+2)
    last_x0s.append(cu_x0)


fig, axes = plt.subplots(figsize=(12, 12))
axes.hist(last_x0s, alpha=0.6, bins=20)
t = 'ts = '+str(ts_length)+', times = '+str(n)
axes.set_title(t)
axes.set_xticks(xticks) 
axes.set_yticks(yticks)
plt.show()