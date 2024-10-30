import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model('mobilenetv2/')

converter.optimizations = [tf.lite.Optimize.DEFAULT]

quantized_model = converter.convert()

