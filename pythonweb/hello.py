import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
num_points=100
vectors_set=[]
for i in range(num_points):
    x1=np.random.normal(0.0,5.5)   #横坐标，进行随机高斯处理化，以0为均值，以0.55为标准差
    y1=x1*2+10+np.random.normal(0.0,3)   #纵坐标，数据点在y1=x1*2+5上小范围浮动上下3
    vectors_set.append([x1,y1])
    x_data=[v[0] for v in vectors_set]
    y_data=[v[1] for v in vectors_set]
    plt.scatter(x_data,y_data,c='r')
    plt.show()

W = tf.Variable(tf.random_uniform([1], -10.0, 10.0), name='W')  # 生成1维的W矩阵，取值是[-10,1]之间的随机数
b = tf.Variable(tf.zeros([1]), name='b') # 生成1维的b矩阵，初始值是0
y = W * x_data + b     # 经过计算得出预估值y
loss = tf.reduce_mean(tf.square(y - y_data), name='loss') # 以预估值y和实际值y_data之间的均方误差作为损失
optimizer = tf.train.GradientDescentOptimizer(15) # 采用梯度下降法来优化参数  学习率为2
train = optimizer.minimize(loss, name='train')  # 训练的过程就是最小化这个误差值
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print ("W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss))  # 初始化的W和b是多少
for step in range(20):   # 执行20次训练
  sess.run(train)
  print ("W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss)) # 输出训练好的W和b