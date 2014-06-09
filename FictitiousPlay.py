import matplotlib.pyplot as plt
from random import uniform, randint
ts_length = 200  # ���Ԃ̒���
cu_x0 = uniform(0,1)  # x_0(t=0)
cu_x1 = uniform(0,1)  # x_1(t=0)
x0s = []
x1s = []
for i in range(ts_length):
    x0s.append(cu_x0)  # x0(i)�������Ă���, for���ɂ��0~t-1
    x1s.append(cu_x1)  # x1(i)�������Ă���
    cu_e00 = 1-2*cu_x0  #�v���C���[0���s��0����������̊��җ���
    cu_e10 = 2*cu_x1-1  #�v���C���[1���s��0����������̊��җ���
# ���̃Q�[�����ƍs��0��������ꍇ�ƍs��1��������ꍇ�̊��җ����̘a�͏��0�Ȃ̂ōs��0�̊��җ����̂ݒ�`����΂悢
    if cu_e00 > 0:  # �v���C���[0�̍s��a0���߂�
        cu_a0 = 0
    elif cu_e00 == 0:
        cu_a0 = randint(0,1)  # 1or0(random)
    else:
        cu_a0 = 1

    if cu_e10 > 0:  # # �v���C���[1�̍s��a1���߂�
        cu_a1 = 0
    elif cu_e10 == 0:
        cu_a1 = randint(0,1)  # 1or0(random)
    else:
        cu_a1 = 1
    cu_x0 = (cu_x0*(i+1)+cu_a1)/(i+2)  #x_0(i+1)
    cu_x1 = (cu_x1*(i+1)+cu_a0)/(i+2)
plt.plot(x0s, 'b-', label='x_0(t)')  # x_0(t)�͐F�ŕ\����)
plt.plot(x1s, 'r-', label='x_1(t)')  # x_1(t)�͐ԐF�ŕ\����)
plt.legend()
plt.show()