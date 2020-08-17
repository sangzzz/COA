# Submitted By,
# Sangeeth S V - 181CO246
# Rohith V S - 181CO243
# Jayakrishna Sukumaran - 181CO223
# J Sudarsanan - 181CO222
import re
import sys
ch = int(sys.argv[1])
R = [0 for i in range(32)]
CIA = hex(0x400000)
NIA = hex(0)
SR = hex(0)
CR = '0000'
LR = hex(0)
f = open('memory.txt', 'w')
f.write('CIA\t:\t'+str(CIA)+'\n')
f.write('NIA\t:\t'+str(NIA)+'\n')
f.write('SR\t:\t'+str(SR)+'\n')
f.write('LR\t:\t'+str(LR)+'\n')
f.write('CR\t:\t'+str(CR)+'\n')
f.write('R0\t:\t'+str(R[0])+'\n')
f.write('R1\t:\t'+str(R[1])+'\n')
f.write('R2\t:\t'+str(R[2])+'\n')
f.write('R3\t:\t'+str(R[3])+'\n')
f.write('R4\t:\t'+str(R[4])+'\n')
f.write('R5\t:\t'+str(R[5])+'\n')
f.write('R6\t:\t'+str(R[6])+'\n')
f.write('R7\t:\t'+str(R[7])+'\n')
f.write('R8\t:\t'+str(R[8])+'\n')
f.write('R9\t:\t'+str(R[9])+'\n')
f.write('R10\t:\t'+str(R[10])+'\n')
f.write('R11\t:\t'+str(R[11])+'\n')
f.write('R12\t:\t'+str(R[12])+'\n')
f.write('R13\t:\t'+str(R[13])+'\n')
f.write('R14\t:\t'+str(R[14])+'\n')
f.write('R15\t:\t'+str(R[15])+'\n')
f.write('R16\t:\t'+str(R[16])+'\n')
f.write('R17\t:\t'+str(R[17])+'\n')
f.write('R18\t:\t'+str(R[18])+'\n')
f.write('R19\t:\t'+str(R[19])+'\n')
f.write('R20\t:\t'+str(R[20])+'\n')
f.write('R21\t:\t'+str(R[21])+'\n')
f.write('R22\t:\t'+str(R[22])+'\n')
f.write('R23\t:\t'+str(R[23])+'\n')
f.write('R24\t:\t'+str(R[24])+'\n')
f.write('R25\t:\t'+str(R[25])+'\n')
f.write('R26\t:\t'+str(R[26])+'\n')
f.write('R27\t:\t'+str(R[27])+'\n')
f.write('R28\t:\t'+str(R[28])+'\n')
f.write('R29\t:\t'+str(R[29])+'\n')
f.write('R30\t:\t'+str(R[30])+'\n')
f.write('R31\t:\t'+str(R[31])+'\n')
f.close()
f = open('data.txt', 'w')
f.write('.data'+'\n')
f1 = open('label.txt', 'r')
a = int('0x10000000', 16)
for each in f1:
    x = re.split('#', each)
    while "" in x:
        x.remove("")
    while None in x:
        x.remove(None)
    if len(x) <= 3:
        break
    D = {str(hex(a)): x[3]}
    f.write(str(D)+'\n')
    a = a+sys.getsizeof(x[3])
f.write('.text'+'\n')
f2 = open('ref.txt', 'r')
b = int('400000', 16)
for each in f2:
    x = re.split('#', each)
    a = int(x[0])
    i = 1
    f3 = open('Q.s', 'r')
    for y in f3:
        y = y.strip()
        if i == a:
            z = re.split(',| |\(|\)', y)
            while "" in z:
                z.remove("")
            while None in z:
                z.remove(None)

            if z[0] == 'li':
                y = 'addi '+str(z[1])+', 0, '+str(z[2])
            elif z[0] == 'mr':
                y = 'or '+str(z[1])+', '+str(z[2])+', '+str(z[2])
            elif z[0] == 'la':
                y = 'addi '+str(z[1])+', '+str(z[2])+', '+str(z[3])
            elif z[0] == 'subi':
                y = 'addi '+str(z[1])+', '+str(z[2])+', -'+str(z[3])
            elif z[0] == 'beq':
                y = 'bc '+str(12)+', '+str(10)+', '+str(z[3])
            elif z[0] == 'bne':
                y = 'bc '+str(4)+', '+str(2)+', '+str(z[3])
            D = {str(hex(b)): y}
            f.write(str(D)+'\n')
            b = b+8
        i = i+1
    f3.close()
f2.close()
f1.close()
f.close()
c = '\n'
i = 0
fp = open('opcode.o', 'r')
for each in fp:
    i = i+1
j = 0
fp.close()
file = open('label.txt', 'r')
for each in file:
    each = re.split('#', each)
    if each[1] == 'main':
        k = int(each[0])
        break
file.close()
temp = '0x400000'
flag = 0
p = 0
if ch == 1:
    file = open('opcodeindex.txt', 'r')
    for each in file:
        each = re.split('#', each)
        if int(each[0]) <= k:
            j = j+1
            continue
        else:
            break
    start = j
    while j < i:
        NIA = int(temp, 16)+(j+1)*8
        NIA = hex(NIA)
        fp = open('opcode.o', 'r')
        k = 0
        while k < j:
            each = fp.readline()
            k = k+1
        each = fp.readline()
        op = each[0:6]
        op = int(op, 2)
        if op == 14:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:30], 2)]
            if each[30:32] == '00':
                R[r[0]] = R[r[1]]+r[2]
            elif each[30:32] == '10':
                R[r[0]] = R[r[1]]-r[2]
            else:
                f1 = open('label.txt', 'r')
                for e in f1:
                    if e[0] == str(r[2]):
                        d = re.split('#', e)
                        if d[2] == '.word':
                            xy = re.split(' |, ', d[3])
                            xy.remove('\n')
                            if len(xy) == 1:
                                R[r[0]] = int(d[3])
                            else:
                                q = 0
                                while q < p:
                                    xy.remove(xy[0])
                                    q = q+1
                                R[r[0]] = int(xy[0])
                                p = p+1
                        elif len(d) > 3:
                            R[r[0]] = d[3]
                            break
                f1.close()
        elif op == 31 and int(each[22:31], 2) == 266:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:21], 2)]
            R[r[0]] = R[r[1]]+R[r[2]]
        elif op == 31 and int(each[21:31], 2) == 444:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:21], 2)]
            R[r[1]] = R[r[0]] | R[r[2]]
        elif op == 17:
            if each[31] == '0':
                print R[4]
            elif each[31] == '1':
                R[3] = input()
        elif op == 19:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:32], 2)]
            if r[0] == 4 and r[1] == 2:
                if CR == '1000' or CR == '0100':
                    file = open('opcodeindex.txt', 'r')
                    k = 0
                    for ea in file:
                        ea = re.split('#', ea)
                        if int(ea[0]) < r[2]:
                            k = k+1
                            continue
                    j = k
                    file.close()
                    continue
            elif r[0] == 12 and r[1] == 10:
                if CR == '0010':
                    file = open('opcodeindex.txt', 'r')
                    k = 0
                    for ea in file:
                        ea = re.split('#', ea)
                        if int(ea[0]) < r[2]:
                            k = k+1
                            continue
                    j = k
                    file.close()
                    continue
            elif each[31] == '1':
                NIA = LR
                j = start
                continue
        elif op == 18 and each[30:32] == '01':
            file = open('opcodeindex.txt', 'r')
            k = 0
            for ea in file:
                ea = re.split('#', ea)
                if int(ea[0]) < r[2]:
                    k = k+1
                    continue
            start = j+1
            j = k
            LR = NIA
            file.close()
            continue
        elif op == 31 and int(each[21:32], 2) == 0:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:21], 2)]
            if r[0] == 7:
                CR = '0000'
                if R[r[1]] > R[r[2]]:
                    CR = '0100'
                elif R[r[1]] < R[r[2]]:
                    CR = '1000'
                elif R[r[1]] == R[r[2]]:
                    CR = '0010'
        elif op == 36:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:31], 2)]
            R[r[2]+r[1]] = R[r[0]]
        fp.close()
        j = j+1
        CIA = NIA
elif ch == 0:
    print 'Simulating Step By Step'
    print 'Enter 0 to stop simulation'
    c = '1'
    file = open('opcodeindex.txt', 'r')
    for each in file:
        each = re.split('#', each)
        if int(each[0]) <= k:
            j = j+1
            continue
        else:
            break
    start = j
    while j < i:
        NIA = int(temp, 16)+(j+1)*8
        NIA = hex(NIA)
        c = input()
        if c == '0':
            break
        fp = open('opcode.o', 'r')
        k = 0
        while k < j:
            each = fp.readline()
            k = k+1
        each = fp.readline()
        op = each[0:6]
        op = int(op, 2)
        if op == 14:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:30], 2)]
            if each[30:32] == '00':
                R[r[0]] = R[r[1]]+r[2]
            elif each[30:32] == '10':
                R[r[0]] = R[r[1]]-r[2]
            else:
                f1 = open('label.txt', 'r')
                for e in f1:
                    if e[0] == str(r[2]):
                        d = re.split('#', e)
                        if d[2] == '.word':
                            xy = re.split(' |, ', d[3])
                            xy.remove('\n')
                            if len(xy) == 1:
                                R[r[0]] = int(d[3])
                            else:
                                q = 0
                                while q < p:
                                    xy.remove(xy[0])
                                    q = q+1
                                R[r[0]] = int(xy[0])
                                p = p+1
                        elif len(d) > 3:
                            R[r[0]] = d[3]
                            break
                f1.close()
        elif op == 31 and int(each[22:31], 2) == 266:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:21], 2)]
            R[r[0]] = R[r[1]]+R[r[2]]
        elif op == 31 and int(each[21:31], 2) == 444:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:21], 2)]
            R[r[1]] = R[r[0]] | R[r[2]]
        elif op == 17:
            if each[31] == '0':
                print R[4]
            elif each[31] == '1':
                R[3] = input()
        elif op == 19:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:32], 2)]
            if r[0] == 4 and r[1] == 2:
                if CR == '1000' or CR == '0100':
                    file = open('opcodeindex.txt', 'r')
                    k = 0
                    for ea in file:
                        ea = re.split('#', ea)
                        if int(ea[0]) < r[2]:
                            k = k+1
                            continue
                    j = k
                    file.close()
                    continue
            elif r[0] == 12 and r[1] == 10:
                if CR == '0010':
                    file = open('opcodeindex.txt', 'r')
                    k = 0
                    for ea in file:
                        ea = re.split('#', ea)
                        if int(ea[0]) < r[2]:
                            k = k+1
                            continue
                    j = k
                    file.close()
                    continue
            elif each[31] == '1':
                NIA = LR
                j = start
                continue
        elif op == 18 and each[30:32] == '01':
            file = open('opcodeindex.txt', 'r')
            k = 0
            for ea in file:
                ea = re.split('#', ea)
                if int(ea[0]) < r[2]:
                    k = k+1
                    continue
            start = j+1
            j = k
            LR = NIA
            file.close()
            continue
        elif op == 31 and int(each[21:32], 2) == 0:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:21], 2)]
            if r[0] == 7:
                CR = '0000'
                if R[r[1]] > R[r[2]]:
                    CR = '0100'
                elif R[r[1]] < R[r[2]]:
                    CR = '1000'
                elif R[r[1]] == R[r[2]]:
                    CR = '0010'
        elif op == 36:
            r = [int(each[6:11], 2), int(each[11:16], 2), int(each[16:31], 2)]
            R[r[2]+r[1]] = R[r[0]]
        f = open('memory.txt', 'w')
        f.write('CIA\t:\t'+str(CIA)+'\n')
        f.write('NIA\t:\t'+str(NIA)+'\n')
        f.write('SR\t:\t'+str(SR)+'\n')
        f.write('LR\t:\t'+str(LR)+'\n')
        f.write('CR\t:\t'+str(CR)+'\n')
        f.write('R0\t:\t'+str(R[0])+'\n')
        f.write('R1\t:\t'+str(R[1])+'\n')
        f.write('R2\t:\t'+str(R[2])+'\n')
        f.write('R3\t:\t'+str(R[3])+'\n')
        f.write('R4\t:\t'+str(R[4])+'\n')
        f.write('R5\t:\t'+str(R[5])+'\n')
        f.write('R6\t:\t'+str(R[6])+'\n')
        f.write('R7\t:\t'+str(R[7])+'\n')
        f.write('R8\t:\t'+str(R[8])+'\n')
        f.write('R9\t:\t'+str(R[9])+'\n')
        f.write('R10\t:\t'+str(R[10])+'\n')
        f.write('R11\t:\t'+str(R[11])+'\n')
        f.write('R12\t:\t'+str(R[12])+'\n')
        f.write('R13\t:\t'+str(R[13])+'\n')
        f.write('R14\t:\t'+str(R[14])+'\n')
        f.write('R15\t:\t'+str(R[15])+'\n')
        f.write('R16\t:\t'+str(R[16])+'\n')
        f.write('R17\t:\t'+str(R[17])+'\n')
        f.write('R18\t:\t'+str(R[18])+'\n')
        f.write('R19\t:\t'+str(R[19])+'\n')
        f.write('R20\t:\t'+str(R[20])+'\n')
        f.write('R21\t:\t'+str(R[21])+'\n')
        f.write('R22\t:\t'+str(R[22])+'\n')
        f.write('R23\t:\t'+str(R[23])+'\n')
        f.write('R24\t:\t'+str(R[24])+'\n')
        f.write('R25\t:\t'+str(R[25])+'\n')
        f.write('R26\t:\t'+str(R[26])+'\n')
        f.write('R27\t:\t'+str(R[27])+'\n')
        f.write('R28\t:\t'+str(R[28])+'\n')
        f.write('R29\t:\t'+str(R[29])+'\n')
        f.write('R30\t:\t'+str(R[30])+'\n')
        f.write('R31\t:\t'+str(R[31])+'\n')
        f.close()
        fp.close()
        CIA = NIA
        j = j+1

f = open('memory.txt', 'w')
f.write('CIA\t:\t'+str(CIA)+'\n')
f.write('NIA\t:\t'+str(NIA)+'\n')
f.write('SR\t:\t'+str(SR)+'\n')
f.write('LR\t:\t'+str(LR)+'\n')
f.write('CR\t:\t'+str(CR)+'\n')
f.write('R0\t:\t'+str(R[0])+'\n')
f.write('R1\t:\t'+str(R[1])+'\n')
f.write('R2\t:\t'+str(R[2])+'\n')
f.write('R3\t:\t'+str(R[3])+'\n')
f.write('R4\t:\t'+str(R[4])+'\n')
f.write('R5\t:\t'+str(R[5])+'\n')
f.write('R6\t:\t'+str(R[6])+'\n')
f.write('R7\t:\t'+str(R[7])+'\n')
f.write('R8\t:\t'+str(R[8])+'\n')
f.write('R9\t:\t'+str(R[9])+'\n')
f.write('R10\t:\t'+str(R[10])+'\n')
f.write('R11\t:\t'+str(R[11])+'\n')
f.write('R12\t:\t'+str(R[12])+'\n')
f.write('R13\t:\t'+str(R[13])+'\n')
f.write('R14\t:\t'+str(R[14])+'\n')
f.write('R15\t:\t'+str(R[15])+'\n')
f.write('R16\t:\t'+str(R[16])+'\n')
f.write('R17\t:\t'+str(R[17])+'\n')
f.write('R18\t:\t'+str(R[18])+'\n')
f.write('R19\t:\t'+str(R[19])+'\n')
f.write('R20\t:\t'+str(R[20])+'\n')
f.write('R21\t:\t'+str(R[21])+'\n')
f.write('R22\t:\t'+str(R[22])+'\n')
f.write('R23\t:\t'+str(R[23])+'\n')
f.write('R24\t:\t'+str(R[24])+'\n')
f.write('R25\t:\t'+str(R[25])+'\n')
f.write('R26\t:\t'+str(R[26])+'\n')
f.write('R27\t:\t'+str(R[27])+'\n')
f.write('R28\t:\t'+str(R[28])+'\n')
f.write('R29\t:\t'+str(R[29])+'\n')
f.write('R30\t:\t'+str(R[30])+'\n')
f.write('R31\t:\t'+str(R[31])+'\n')
f.close()

# 68
