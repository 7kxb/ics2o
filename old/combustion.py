compound = input()
length = len(compound)
c = 0
h = 0
o = 0
pointer = 0
last = ''
while pointer < length:
    if compound[pointer] == 'C':
        if pointer+1 == length:
            c += 1
        if last == 'c':
            c += 1
        if last == 'h':
            h += 1
        if last == 'o':
            o += 1
        last = 'c'
    if compound[pointer] == 'H':
        if pointer+1 == length:
            h += 1
        if last == 'c':
            c += 1
        if last == 'h':
            h += 1
        if last == 'o':
            o += 1
        last = 'h'
    if compound[pointer] == 'O':
        if pointer+1 == length:
            o += 1
        if last == 'c':
            c += 1
        if last == 'h':
            h += 1
        if last == 'o':
            o += 1
        last = 'o'
    if compound[pointer].isdigit():
        coefficient = int(compound[pointer])
        if last == 'c':
            c += coefficient
        if last == 'h':
            h += coefficient
        if last == 'o':
            o += coefficient
        last = ''
    pointer += 1
if h%2 == 1:
    a1 = 2
    c *= 2
    c3 = c
    h *= 2
    d4 = int(h/2)
    o *= 2
else:
    a1 = 1
    d4 = int(h/2)
    c3 = c
op = (c3*2)+d4
if o%2 == 0 and op%2 == 0:
    b2 = int(op/2) - int(o/2)
else:
    a1 *= 2
    c3 *= 2
    d4 *= 2
    c *= 2 
    h *= 2 
    o *= 2
    op = (c3*2)+d4
    b2 = int(op/2) - int(o/2)
if c == 0 or h == 0:
    print('Impossible')
elif a1 == 0 or b2 == 0 or c3 == 0 or d4 == 0:
    print('Impossible')
else:
    print(str(a1)+compound+' + '+str(b2)+'O2'+' -> '+str(c3)+'CO2'+' + '+str(d4)+'H20')
