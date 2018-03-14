import tensorflow as tf

x = tf.constant([[2,2],[3,3]])
y = tf.constant([[8,16],[2,3]])

result = tf.pow(x,y)

with tf.Session() as sess:
    print(sess.run(result))
