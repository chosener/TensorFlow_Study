import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#TensorFlow之添加层

#添加神经层函数(输入,输入大小,输出大小,激励函数)
def add_layer(inputs,in_size,out_size,activation_function=None):
    #add one more layer and return the output of this layer
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size,out_size]))
        #初始值不为0,所以+0.1
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
        #没有被激活的值
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs,Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]
#噪点
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

#定义2个参数
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32,[None,1],name='x_input') 
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')

#输入层
l1 = add_layer(xs,1,10,activation_function = tf.nn.relu)
#输出层
prediction = add_layer(l1,10,1,activation_function = None)
#损失函数
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices = [1]))

#学习率通常小于1
#以0.1的学习率,通过loss变小,每一次的优化
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
#graph收集起来.放在logs里.
#低版本时
#error:AttributeError: module 'tensorflow.python.training.training' has no attribute 'SummaryWriter'
#writer = tf.train.SummaryWriter("logs/", sess.graph)
writer = tf.summary.FileWriter("logs/",tf.get_default_graph())
#important step
sess.run(init)

