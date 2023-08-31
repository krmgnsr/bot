import random

password = message.content[9:].strip

def sifre_uret(password):
    karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    sifre = ""
    for i in range(password):
        sifre += random.choice(karakter)

    return sifre
