# LCPRNG and LSFR written by Hosung Lee
# BBS written by Sean Kullmann

def lcprng(x0, modulus, multiplier, offset):
    print("Performing LCPRNG")
    xn = x0
    v = []
    i = 0
    while xn != x0 or i == 0:
        print(xn, end=" ")
        xn = xn * multiplier + offset
        xn = xn % modulus
        if xn in v:
            print(f"\nno cycle")
            break
        v.append(xn)
        i += 1

def shift(bits):
    bits = list(bits)
    bits[1:len(bits)] = bits[0:len(bits)-1]
    bits[0] = 0
    return "".join(map(str,bits))

def xor(a, b):
    if a == b:
        return "0"
    return "1"

def xorE(bits, taps):
    res = xor(bits[taps[0]], bits[taps[1]])
    for i in range(len(taps)):
        if i < 2:
            continue
        res = xor(res, bits[taps[i]])
    return res

def lfsrutil(bits, taps):
    bits = list(bits)
    bits[0] = xor(bits[1], bits[-1])
    bits = shift(bits)
    return bits

def lfsutilv2(bits, taps):
    taps = list(map(lambda x: len(taps)-x, taps))
    bits = list(bits)
    for i in range(0,len(taps)-1):
        xor_res = xorE(bits[1:len(bits)], taps)
    bits[0] = xor_res
    bits = shift(bits)
    return bits

def lfsr(bits, taps):
    print("Performing LFSR")
    s0 = "0"+bits
    sn = s0
    i = 0
    while sn != s0 or i == 0:
        print(sn[1:len(sn)])
        if len(taps) == 2:
            sn = lfsrutil(sn, taps)
        else:
            sn = lfsutilv2(sn, taps)
        i += 1

def bbs(n, s):
  print("Performing BBS")
  i = 0
  counter = 12
  temp = 0
  output = ""
  while counter != 0:
    if checkEven(s):
      output += "0"
    else:
      output += "1"
    temp = s ** 2
    s = temp % n
    counter -= 1
  print(output)

def checkEven(number):
  if (number % 2 == 0):
    return True
  else:
    return False

# lcprng(0, 7, 3, 5)
# def bruteForceAB():
#   a = 0
#   b = 1
#   while a != 10:
#     lcprng(0, 9, a, b)
#     a += 1

# bruteForceAB()
#lcprng(0, 9, 9, 1)
#lcprng(0, 16, 6, 5)

#lcprng(0, 13, 6, 7)
lcprng(0, 9, 5, 1)

# bits = "0001"
# lfsr("0001", [0, 3])

# bbs(11, 5)