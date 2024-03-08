def crc8(text):
    crc = modify(text, 8)
    gx = '1'+bin(0xD5)[2:]
    new = crc[:9]
    old = crc
    return func(new, old, gx, 8)
    


def crc16_ibm(text):
    crc = modify(text, 16)
    gx = '1'+bin(0x8005)[2:]
    new = crc[:17]
    old = crc
    return func(new, old, gx, 16)



def crc32c(text):
    crc = modify(text, 32)
    gx = '1'+bin(0x814141AB)[2:]
    new = crc[:33]
    old = crc
    return func(new, old, gx, 32)



def modify(a, pow_of_poly):
    res = ''
    for i in range(len(a)):
        res = res + bin(ord(a[i]))[2:]
    return res + '0' * pow_of_poly



def func(new, old, gx, pow_of_poly):
    while len(old)>0:
        if len(new)==len(gx):
            a = ''
            for i in range(len(new)):
                a = a + str(int(new[i])^int(gx[i]))
            new = str(int(a))
            old = old[pow_of_poly+1:]
        else:
            if (len(new)+len(old))>=len(gx):
                lennew = len(new)
                new = new + old[:(len(gx)-len(new))]
                old = old[len(gx)-lennew:]
                a = ''
                for i in range(len(new)):
                    a = a + str(int(new[i])^int(gx[i]))
                new = str(int(a))
                
            else:

                return new + old
    return new

text = input("Введите нужный текст: ")
a = crc8(crc32c(crc16_ibm(crc8(crc32c(crc16_ibm(crc8(crc32c(crc16_ibm(crc8(text))))))))))
print("Захэшированный текст: " + a)