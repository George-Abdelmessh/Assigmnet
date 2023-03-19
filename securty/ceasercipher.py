import numpy as np
import math


def encrypt_text(plaintext,n):
    ans= ""
    for i in range (len(plaintext)):
        ch = plaintext[i]
        if ch == " ":
            ans+=""
        elif(ch.isupper()):
            ans += chr((ord(ch)+n-65)%25+65)

        else:
             ans += chr((ord(ch)+n-97)%26+97)
    return ans



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


plaintext = "hello"
n = 3
cipher = encrypt_text(plaintext,n)

print("plain text is: " + plaintext)
print("shift pattern is: " + str(n))
print("cipher text is: " + cipher)


mse_val = mse(plaintext, cipher)
psnr_val = psnr(plaintext, cipher)
print("MSE: ", mse_val)
print("PSNR: ", psnr_val)