import tensorflow as tf


def load(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_png(image)
    image = tf.cast(image, tf.float32)

    return image


def resize_image(image, height=256, width=256):
    image = tf.image.resize(image, [height, width],
                            method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

    return image


def normalize(image):
    image = (image/127.5) - 1

    return image


def test_image(image_path):
    image = load(image_path)
    image = resize_image(image, height=256, width=256)
    image = normalize(image)

    return image
