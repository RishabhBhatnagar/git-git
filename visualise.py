from keras.models import load_model, Model
from ml_nn import *
from ml_nn import Constants
from keras.utils.vis_utils import plot_model


def generate_encapsulate_model_with_output_layer_names(model, output_layer_names):
    enc_model = Model(
        inputs=model.input,
        outputs=list(map(
            lambda oln: model.get_layer(oln).output,
            output_layer_names
        ))
    )
    return enc_model

def deprecated_main():
    # I don't know what i did here.
    lstm_model_name = Constants.lstm_model_name
    gensim_model_name = Constants.gensim_model_name
    print()
    lstm_model = load_model(lstm_model_name)
    output_layer_names = [layer.name for layer in lstm_model.layers]
    enc_model = generate_encapsulate_model_with_output_layer_names(
        lstm_model, 
        output_layer_names
    )
    enc_model.save("./enc_keras_model.h5")
    print(predict_single_essay("hello i am rishabh bhatnagar, this is computer engineering course", Constants.gensim_model_name, Constants.lstm_model_name, lstm_model=enc_model))


from matplotlib import pyplot as plt


if __name__ == '__main__':
    # assumption: the model is already trained.
    lstm_model = load_model(Constants.lstm_model_name)

    # this will print the overview of the model to a png file.
    plot_model(lstm_model, to_file='model_visualise.png')   
    deprecated_main()


