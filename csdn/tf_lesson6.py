import tensorflow as tf

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                                   [2]])

#matrix multiply
#np.dot(m1,m2)
product = tf.matmul(matrix1,matrix2)

#method 1
'''
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
'''
'''
>>> 
= RESTART: /Users/dongsai/Documents/MachineLearning/tensorflow/tf_lesson6.py =
[[12]]

'''
#method 2
#在这里面的sess自动被close掉
with tf.Session() as sess:
    result = sess.run(product)
    print(result)
