import constants as c
from pre_process import data_catalog
import numpy as np
from models import convolutional_model, recurrent_model
from utils import get_last_checkpoint_if_any
import tensorflow as tf
from keras.layers.core import Dense
from keras.models import Model
import utils
import os



guess_dir = c.GUESS_DIR
num_neg = c.TEST_NEGATIVE_No



def clipped_audio(x, num_frames=c.NUM_FRAMES):
    if x.shape[0] > num_frames + 20:
        bias = np.random.randint(20, x.shape[0] - num_frames)
        clipped_x = x[bias: num_frames + bias]
    elif x.shape[0] > num_frames:
        bias = np.random.randint(0, x.shape[0] - num_frames)
        clipped_x = x[bias: num_frames + bias]
    else:
        clipped_x = x
    return clipped_x

def get_test(guess_dir):
    global num_neg
    libri = data_catalog(guess_dir)
    num_neg, num_triplets = 141, 2
    test_batch = None
    filename = libri['filename'].values[0]
    x = np.load(filename)
    new_x = []
    new_x.append(clipped_audio(x))
    x = np.array(new_x)
    return x

def pred(x):
    batch_size = c.BATCH_SIZE * c.TRIPLET_PER_BATCH
    train_path = c.TEST_DIR

    id_to_labels = c.DICT
    
    no_of_speakers = 142

    b = x[0]
    num_frames = b.shape[0]
    base_model = convolutional_model(input_shape=x.shape[1:], batch_size=batch_size, num_frames=num_frames)

    y = base_model.output
    y = Dense(no_of_speakers, activation='softmax',name='softmax_layer')(y)

    model = Model(base_model.input, y)


    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    last_checkpoint = utils.get_last_checkpoint_if_any(c.PRE_CHECKPOINT_FOLDER)
    if last_checkpoint is not None:
        model.load_weights(last_checkpoint)
        grad_steps = int(last_checkpoint.split('_')[-2])

    index = np.argmax(model.predict_on_batch(x))
    
    return id_to_labels[index], index
        
def delete():
	os.remove('guess/npy/unknown-common-1.npy')
	os.remove('guess/wav/unknown-common-1.wav')
    
if __name__ == '__main__':
    x = get_test(guess_dir)
    pred(x)
    delete()
