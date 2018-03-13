import tensorflow as tf
import numpy as np

#create data
x_data  = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

###create tensorflow structure start ###
#为大写,因为可能为矩阵
#用一个随机数列生成.1列,-1到1的范围
Weights = tf.Variable(tf.random_uniform([1],-1.0,1))
#初始值为0,一步步学习到0.1及0.3
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases
#预测的y与真实值的差别,刚开始loss会很大
loss = tf.reduce_mean(tf.square(y - y_data))
#优化器,0.5为学习效率.
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
#前面只是建立结构,现在初始化一下
init = tf.initialize_all_variables()
###create tensorflow structure end ###

#结构激活
sess = tf.Session()
#这里激活,开始飞起来
sess.run(init)     #very important

for step in range(201):
    #开始训练
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(Weights),sess.run(biases))
