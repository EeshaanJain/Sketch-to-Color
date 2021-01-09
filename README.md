# Sketch-to-Color
We will be creating a cGAN model to return colored images from just sketches without knowing the ground truth. The original code is present in sketch_to_color.ipynb, and the latest checkpoint is present in checkpts/ 

A demonstration of the model is in videos/

[To be added] : I will soon add a sketch_to_color.py file which you could run from the terminal and link a sketch to get the colored output.

Resources : 
1. This project is an implementation of the architecture described in the paper : [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/pdf/1611.07004.pdf)
2. The following article is followed for implementing the project : [Learning to Build a Model for Sketch-to-Color Image Generation using Conditional GANs](https://towardsdatascience.com/generative-adversarial-networks-gans-89ef35a60b69)
3. The model has been trained on this dataset : [Anime Sketch Colorization Pair](https://www.kaggle.com/ktaebum/anime-sketch-colorization-pair) which has around 14k sketches with ground truth.
