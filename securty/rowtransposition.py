import math
import numpy as np


def encryptMessage(key,message):
    cipherText = [""] * key
    for col in range (key):
        pointer = col 
        while pointer < len(message):
            cipherText[col] += message[pointer] 
            pointer += key
        return "".join(cipherText)
    


def decryotionMessage(key,message):
    numCols = math.ceil(len(message) / key)
    numRows = key
    numShadedBoxes = (numCols * numRows) - len(message)
    plaintext =[""] * numCols
    col=0
    row=0

    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if(
            (col == numCols)
            or (col == numCols - 1)
            and (row >= numRows - numShadedBoxes)
        ):
            col = 0
            row += 1
    return "".join(plaintext)


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



message = 'HelloFromOutside'
key = 10 % (len(message) - 1)

encrypted = encryptMessage(key=key, message= message)
decrypted = decryotionMessage(key=key, message= encrypted)

print('Plain Text: ' + message)
print('Key: ' + str(key))
print('Encrpted: ' + encrypted)
print('Decrypted: ' + decrypted)

mse_val = mse(encrypted, decrypted)
psnr_val = psnr(encrypted, decrypted)

print("MSE: ", mse_val)
print("PSNR: ", psnr_val)