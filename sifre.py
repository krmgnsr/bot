import random


def sifre_uret(password):
    karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    sifre = ""
    for i in range(password):
        sifre += random.choice(karakter)

    return sifre
