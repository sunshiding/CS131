import numpy as np


def conv_nested(image, kernel):
    """A naive implementation of convolution filter.

    This is a naive implementation of convolution using 4 nested for-loops.
    This function computes convolution of an image with a kernel and outputs
    the result that has the same shape as the input image.

    Args:
        image: numpy array of shape (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk)

    Returns:
        out: numpy array of shape (Hi, Wi)
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    ### YOUR CODE HERE

    # flip the kernel
    kernel = np.flip(kernel, 0)
    kernel = np.flip(kernel, 1)

    center_X = int(Wk / 2)
    center_Y = int(Hk / 2)

    for X in range(Wi):
        for Y in range(Hi):
            for xk in range(Wk):
                for yk in range(Hk):
                    global_x = X + xk - center_X
                    global_y = Y + yk - center_Y

                    if 0 <= global_x < Wi and 0 <= global_y < Hi:
                        out[Y, X] = out[Y, X] + image[global_y, global_x] * kernel[yk, xk]

    ### END YOUR CODE
    return out


def zero_pad(image, pad_height, pad_width):
    """ Zero-pad an image.

    Ex: a 1x1 image [[1]] with pad_height = 1, pad_width = 2 becomes:

        [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]         of shape (3, 5)

    Args:
        image: numpy array of shape (H, W)
        pad_width: width of the zero padding (left and right padding)
        pad_height: height of the zero padding (bottom and top padding)

    Returns:
        out: numpy array of shape (H+2*pad_height, W+2*pad_width)
    """

    H, W = image.shape
    out = None

    ### YOUR CODE HERE
    out = np.zeros((H + 2 * pad_height, W + 2 * pad_width))  # set a bigger zero matrix
    out[pad_height:pad_height + H, pad_width:pad_width + W] = image  # copy the image to the center part
    ### END YOUR CODE
    return out


def conv_fast(image, kernel):
    """ An efficient implementation of convolution filter.

    This function uses element-wise multiplication and np.sum()
    to efficiently compute weighted sum of neighborhood at each
    pixel.

    Hints:
        - Use the zero_pad function you implemented above
        - There should be two nested for-loops
        - You may find np.flip() and np.sum() useful

    Args:
        image: numpy array of shape (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk)

    Returns:
        out: numpy array of shape (Hi, Wi)
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    ### YOUR CODE HERE

    # flip the kernel
    kernel = np.flip(kernel, 0)
    kernel = np.flip(kernel, 1)

    pad_height = int(Hk / 2)
    pad_width = int(Wk / 2)

    imgBig = zero_pad(image, pad_height, pad_width)  # zero padding

    # X and Y are indexs for out matrix
    for X in range(Wi):
        for Y in range(Hi):
            # trans X,Y to indexs in imgBig matrix
            localX = X + pad_width
            localY = Y + pad_height
            imageArea = imgBig[localY - pad_height:localY + pad_height + 1, localX - pad_width:localX + pad_width + 1]
            out[Y, X] = np.sum(np.multiply(imageArea, kernel))
    ### END YOUR CODE

    return out


from scipy import signal


def conv_faster(image, kernel):
    """
    Args:
        image: numpy array of shape (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk)

    Returns:
        out: numpy array of shape (Hi, Wi)
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    ### YOUR CODE HERE

    # I don't know
    out = signal.convolve2d(image, kernel, boundary='symm', mode='same')

    ### END YOUR CODE

    return out


def cross_correlation(f, g):
    """ Cross-correlation of f and g

    Hint: use the conv_fast function defined above.

    Args:
        f: numpy array of shape (Hf, Wf)
        g: numpy array of shape (Hg, Wg)

    Returns:
        out: numpy array of shape (Hf, Wf)
    """

    out = None
    ### YOUR CODE HERE

    new_g = np.copy(g)

    # in case of even axis length
    if g.shape[0] % 2 is 0:
        new_g = np.zeros((g.shape[0] + 1, g.shape[1]))
        new_g[0:g.shape[0], 0:g.shape[1]] = g

    if g.shape[1] % 2 is 0:
        new_g = np.zeros((g.shape[0], g.shape[1] + 1))
        new_g[0:g.shape[0], 0:g.shape[1]] = g

    out = conv_fast(f, new_g)
    ### END YOUR CODE

    return out


def zero_mean_cross_correlation(f, g):
    """ Zero-mean cross-correlation of f and g

    Subtract the mean of g from g so that its mean becomes zero

    Args:
        f: numpy array of shape (Hf, Wf)
        g: numpy array of shape (Hg, Wg)

    Returns:
        out: numpy array of shape (Hf, Wf)
    """

    out = None
    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out


def normalized_cross_correlation(f, g):
    """ Normalized cross-correlation of f and g

    Normalize the subimage of f and the template g at each step
    before computing the weighted sum of the two.

    Args:
        f: numpy array of shape (Hf, Wf)
        g: numpy array of shape (Hg, Wg)

    Returns:
        out: numpy array of shape (Hf, Wf)
    """

    out = None
    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out
