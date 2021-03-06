import tensorflow as tf
import numpy as np

#TensorFlow之添加层

#添加神经层函数(输入,输入大小,输出大小,激励函数)
def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    #初始值不为0,所以+0.1
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    #没有被激活的值
    Wx_plus_b = tf.matmul(inputs,Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1,2,300)[:,np.newaxis]
#噪点
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

#定义2个参数
xs = tf.placeholder(tf.float32,[None,1]) 
ys = tf.placeholder(tf.float32,[None,1])

#输入层
l1 = add_layer(xs,1,10,activation_function = tf.nn.relu)
#输出层
prediction = add_layer(l1,10,1,activation_function = None)
#损失函数
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices = [1]))

#学习率通常小于1
#以0.1的学习率,通过loss变小,每一次的优化
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()

sess.run(init)

for i in range(1000):
    sess.run(train_step,feed_dict = {xs:x_data,ys:y_data})
    if i % 50 == 0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))







