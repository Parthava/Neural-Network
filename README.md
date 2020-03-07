# Neural-Network

## Single layer NN 

1. It takes an input of an image of 4x4 matrix.
2. The expected output is also an image of 4x4 matrix.
3. Each value of the matrix is divided by 255 so that the value lies between 0 and 1.
4. After 10000 iterations and minimizing the errors, the machine produces the best optimized output.

Here are some of the datas:

Training Inputs
 [[0.05882353 0.21568627 0.05882353 0.21176471]
 [0.05882353 0.21568627 0.05882353 0.21176471]
 [0.05882353 0.21568627 0.05882353 0.21176471]
 [0.05882353 0.21568627 0.05882353 0.21176471]]


Expected output
 [[0.25490196 0.25490196 0.25490196 0.25490196]
 [0.1254902  0.1254902  0.1254902  0.1254902 ]
 [0.25098039 0.25098039 0.25098039 0.25098039]
 [0.1254902  0.1254902  0.1254902  0.1254902 ]]


Random starting synaptic weights:
[[-0.13622999  0.7287349   0.43908496  0.43280388]
 [ 0.58698774 -0.26563091 -0.89015776 -0.04375151]
 [-0.15918596  0.29588191  0.92125155 -0.29211519]
 [ 0.48682249 -0.91389907  0.04599759 -0.98011392]]


Predicted ouput
[[68. 68. 68. 68.]
 [ 6.  6.  6.  6.]
 [68. 68. 68. 68.]
 [ 6.  6.  6.  6.]]



