import tensorflow as tf
from numpy import *
import numpy as np

#tf.random_uniform()

#create a 4x4 矩阵
test_random_uniform = tf.random_uniform([4,4],minval = -0.5,maxval = 0.5,dtype = tf.float32)
#生成一个1x3的值都为0的矩阵
test_zeros = tf.zeros([1,3])

#最大值tf.reduce_max(input_tensor, reduction_indices=None, keep_dims=False, name=None)
#平均值tf.reduce_mean(input_tensor, reduction_indices=None, keep_dims=False, name=None)
# 'x' is [[1., 2.]
#         [3., 4.]]
x = matrix([[1.,2.],[3.,4.]])
#如果不指定第二个参数，那么就在所有的元素中取平均值 ==> 2.5
test_reduce_m0 = tf.reduce_mean(x)
#指定第二个参数为0，则第一维的元素取平均值，即每一列求平均值 ==> [2.,  3.]
test_reduce_m1 = tf.reduce_mean(x, 0)
#指定第二个参数为1，则第二维的元素取平均值，即每一行求平均值 ==> [1.5,  3.5] 
test_reduce_m2 = tf.reduce_mean(x, 1)

with tf.Session() as sess:
    print(sess.run(test_random_uniform))
    print(sess.run(test_zeros))
    print(x.shape)
    print("matrix shape : ",x.shape[0])
    print("matrix mean is : ", sess.run(test_reduce_m0))
    print("matrix mean is : ", sess.run(test_reduce_m1))
    print("matrix mean is : ", sess.run(test_reduce_m2))
    
