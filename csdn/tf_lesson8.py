import tensorflow as tf

#dtype is float32
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)


'''
output = tf.mul(input1,input2)

Traceback (most recent call last):
  File "/Users/dongsai/Documents/MachineLearning/tensorflow/tf_lesson8.py", line 7, in <module>
    output = tf.mul(input1,input2)
AttributeError: module 'tensorflow' has no attribute 'mul'

旧版本用tf.mul()
'''
output = tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict = {input1: [7.],input2:[2.]}))
