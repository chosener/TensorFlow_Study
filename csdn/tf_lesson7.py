import tensorflow as tf

state = tf.Variable(0,name='counter')
print(state.name)
#counter:0

one = tf.constant(1)

new_value = tf.add(state,one)
#当前new_value
update = tf.assign(state,new_value)

#must have if define variable
init = tf.initialize_all_variables()

with tf.Session() as sess:
    #初始化
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
