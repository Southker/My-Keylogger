print('--------***********----------')
print('----------CEASER------------')
print('--------C I P H E R----------')
print('--------***********----------')

ltrs = 'abcdefghijklmnopqrstuvwxyz'

inp = input("Wann encrypt press 'E/e' or wanna decrypt press 'D/d':: ").lower()

def enc(ptxt, key):
    ciptxt = ''
    for let in ptxt:
        let = let.lower()
        if not let == ' ':
            ind = ltrs.find(let)
            if ind == -1:
                ciptxt += let
            else:
                nind = ind + key
                if nind >= 26:
                    nind -= 26
                ciptxt += ltrs[nind]
    return ciptxt

def dec(ciptxt, key):
    ptxt = ''
    for let in ciptxt:
        let = let.lower()
        if not let == ' ':
            ind = ltrs.find(let)
            if ind == -1:
                ptxt += let
            else:
                nind = ind - key
                if nind < 0:
                    nind += 26
                ptxt += ltrs[nind]
    return ptxt


if inp == 'e':
    print("******* ENCRYPTION MODE ACTIVATED *******")
    key =  int(input("CHOOSE YOUR KEY BETWEEN 1 TO 26:: "))
    txt = input('ENTER YOUR VALUE TO ENCRYPT:: ')
    ciptxt = enc(txt, key)
    print("ENCRYPTED VALUE IS:: ",ciptxt)

elif inp == 'd':
    print("******* DECRYPTION MODE ACTIVATED *******")
    key =  int(input("CHOOSE YOUR KEY BETWEEN 1 TO 26:: "))
    txt = input('ENTER YOUR VALUE TO DECRYPT:: ')
    pltxt = dec(txt, key)
    print("DECRYPTED VALUE IS:: ",pltxt)

else:
    print("*** NO MODE ACTIVATED ***")
    print('PLEASE CHOOSE "E/e" TO ENCRYPT OR "D/d" TO DECRYPT')




