import time
import random

nama = input("Masukan nama: ")
print("\nHello",nama,"yuk kita main tebakannya")
time.sleep(0.5)
print("Kita mulai yaaa")
time.sleep(1)
list_word = ['rahasia','mata','hati','makanan','burung','bebek']
word = random.choice(list_word)
tebak = ""
kesempatan = 5
while kesempatan > 0 :
    print("\nHint: ada",len(word),"huruf")
    tebakan = input("Masukan tebakannya: ")
    tebak += tebakan
    gagal = 0
    for kata in word:
        if kata in tebak:
            print(kata,end="")
        else:
            print("_",end="")
            gagal += 1
    if gagal == 0:
        print("\n\nSelamat",nama,"dapat menebak",word,"dengan benar")
        main = input("Mau main lagi? (Y/N) ")
        if main == 'n' or main == 'N':
            break    
    if tebakan not in word:
        kesempatan -= 1
        print("\n\nKamu menebak kata dengan tidak benar")
        print("Kamu mempunyai " + str(kesempatan) + " kesempatan untuk dapat menebak kembali")
        if kesempatan == 0:
            print("Kamu",nama,"telah kalah dalam permainan menebak kata kali ini :(")
            main = input("Mau main lagi? (Y/N) ")
            if main == 'n' or main == 'N':
                break