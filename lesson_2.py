import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len_pass = int(input("Сударь, соизвольте, пожалуйта, если вас не затруднит, если вам не тяжело, если у вас есть силы и время, написать длину пароля: "))
password = ""

for i in range(len_pass):
    password += random.choice(symbols)

print("Сударь, вот ваш замечательный, отличный, бесподобный, умопомрачительный, прекрасный, безупречный пароль:", password)