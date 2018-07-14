import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Tensorboard简单图结构
# a = tf.constant([1.0,2.0,3.0],name = 'input1')
# b = tf.Variable(tf.random_uniform([3]),name = 'input2')
# add = tf.add_n([a,b],name = 'addOP')
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     writer = tf.summary.FileWriter("E://恶心",sess.graph)
#     print(sess.run(add))
# writer.close()

# Tensorboard命名空间：
with tf.variable_scope('input1'):
    input1 = tf.constant([1.0,2.0,3.0],name='input1')
with tf.variable_scope('input2'):
    input2 = tf.Variable(tf.random_uniform([3]),name='input2')
add = tf.add_n([input1,input2],name='addOP')
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    writer = tf.summary.FileWriter("./ex4",sess.graph)
    print(sess.run(add))
writer.close()