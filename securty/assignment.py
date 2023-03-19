import numpy as np
import math

def mse(textA, textB):
    arrA = np.array([ord(char) for char in textA])
    arrB = np.array([ord(char) for char in textB])
    # MSE = 1/n * sum(y - y') ** 2
    err = np.sum((arrA.astype("float") - arrB.astype("float")) ** 2)
    err /= float(arrA.shape[0])
    return err

def psnr(textA, textB):
    mse_val = mse(textA, textB)
    if mse_val == 0:
        return 'infinity'
    # PSNR = 20 log10( MAX / (MSE ** 0.5))
    max_pixel = 255.0
    psnr_val = 20 * math.log10(max_pixel / (mse_val ** 0.5))
    return psnr_val


# Example usage
text1 = "Hello, World!"
text2 = "Hello, World?"
mse_val = mse(text1, text2)
psnr_val = psnr(text1, text2)
print("MSE: ", mse_val)
print("PSNR: ", psnr_val)