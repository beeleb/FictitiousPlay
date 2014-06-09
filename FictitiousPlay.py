import matplotlib.pyplot as plt
from random import uniform, randint
ts_length = 200  # 時間の長さ
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

    if cu_e10 > 0:  # # プレイヤー1の行動a1を定める
        cu_a1 = 0
    elif cu_e10 == 0:
        cu_a1 = randint(0,1)  # 1or0(random)
    else:
        cu_a1 = 1
    cu_x0 = (cu_x0*(i+1)+cu_a1)/(i+2)  #x_0(i+1)
    cu_x1 = (cu_x1*(i+1)+cu_a0)/(i+2)
plt.plot(x0s, 'b-', label='x_0(t)')  # x_0(t)は青色で表した)
plt.plot(x1s, 'r-', label='x_1(t)')  # x_1(t)は赤色で表した)
plt.legend()
plt.show()