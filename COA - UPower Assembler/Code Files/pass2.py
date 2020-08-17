# Submitted By,
# Sangeeth S V - 181CO246
# Rohith V S - 181CO243
# Jayakrishna Sukumaran - 181CO223
# J Sudarsanan - 181CO222
import re


def binary(n, m):
    x = bin(n)
    x = x[2:]
    while len(x) < m:
        x = '0'+str(x)
    return x


def form(i, flag):
    f3 = open('label.txt', 'r')
    # temp contains the line numbers of all the instructions and type of instruction along with instruction mnemonic
    temp = re.split('#|\n|(|)|,', i)
    while "" in temp:
        temp.remove("")
    while None in temp:
        temp.remove(None)
    x = int(temp[0])
    x = x-1
    while x != 0:
        x = x-1
        line = f.readline()
    line = f.readline()
    # arr contains all the things in one line of assembly code
    arr = re.split(', |\n|\s|\(|\)|,|R', line)
    while "" in arr:
        arr.remove("")
    while None in arr:
        arr.remove(None)
    f.seek(0, 0)
    f3.seek(0, 0)

    p = temp[1]
    str1 = ""
    if p != 'XL':
        if arr[1] == '4':
            flag = 0
        elif arr[1] == '3':
            flag = 1
    if p == 'XO':
        str1 = str1+temp[2]+str(binary(int(arr[1]), 5)) + \
            str(binary(int(arr[2]), 5))+str(binary(int(arr[3]), 5))+temp[3]
    elif p == 'X':
        str1 = str1+temp[2]+str(binary(int(arr[2]), 5)) + \
            str(binary(int(arr[1]), 5))+str(binary(int(arr[3]), 5))+temp[3]
    elif p == 'D':
        str1 = str1+temp[2]+str(binary(int(arr[1]), 5)) + \
            str(binary(int(arr[2]), 5))+str(binary(int(arr[3]), 14))+'00'
    elif p == 'DS':
        str1 = str1+temp[2]+str(binary(int(arr[1]), 5)) + \
            str(binary(int(arr[2]), 5))+str(binary(int(arr[3]), 14))+temp[3]
    elif p == 'XS':
        str1 = str1+temp[2]+str(binary(int(arr[1]), 5)) + \
            str(binary(int(arr[2]), 5))+str(binary(int(arr[3]), 5))+temp[3]
    elif p == 'M':
        str1 = str1+temp[2]+str(binary(int(arr[1]), 5))+str(binary(int(arr[2]), 5))+str(
            binary(int(arr[3]), 5))+str(binary(int(arr[4]), 5))+str(binary(int(arr[5]), 5))+temp[3]
    elif p == 'XL':
        str1 = str1+temp[2]+str(binary(0, 25))+temp[3]
    elif p == 'B':
        str2 = ""
        for each in f3:
            temp2 = re.split('#', each)
            if temp2[1] == arr[3]:
                str2 = str(binary(int(temp2[0]), 14))
        str1 = str1+temp[2]+str(binary(int(arr[1]), 5)) + \
            str(binary(int(arr[2]), 5))+str2+temp[3]
    elif p == 'I':
        str2 = ""
        for each in f3:
            temp2 = re.split('#', each)
            if temp2[1] == arr[1]:
                str2 = str(binary(int(temp2[0]), 24))
        str1 = str1+temp[2]+str2+temp[3]
    elif p == 'SC':
        if flag == 0:
            str1 = str1+temp[2]+str(binary(int(arr[1]), 25))+'0'
        else:
            str1 = str1+temp[2]+str(binary(int(arr[1]), 25))+'1'
    elif p == 'P':
        if temp[2] == 'li':
            str1 = str1+'001110' + \
                str(binary(int(arr[1]), 5))+'00000' + \
                str(binary(int(arr[2]), 14))+'00'
        elif temp[2] == 'subi':
            str1 = str1+'001110'+str(binary(int(arr[1]), 5))+str(
                binary(int(arr[2]), 5))+str(binary(int(arr[3]), 14))+'10'
        elif temp[2] == 'mr':
            str1 = str1+'011111'+str(binary(int(arr[2]), 5))+str(
                binary(int(arr[1]), 5))+str(binary(int(arr[2]), 5))+'01101111000'
        elif temp[2] == 'la':
            str2 = ""
            for each in f3:
                temp2 = re.split('#', each)

                if temp2[1] == arr[3]:
                    str2 = str2+str(binary(int(temp2[0]), 14))
                    break
            str1 = str1+'001110' + \
                str(binary(int(arr[1]), 5)) + \
                str(binary(int(arr[2]), 5))+str2+'01'
        elif temp[2] == 'beq':
            str2 = ""
            for each in f3:
                temp2 = re.split('#', each)
                if temp2[1] == arr[3]:
                    str2 = str(binary(int(temp2[0]), 16))
                    break
            f2.write('011111'+'00111'+str(binary(int(arr[1]), 5))+str(
                binary(int(arr[2]), 5))+'00000000000'+'\n')
            str1 = str1+'010011'+'01100'+'01010'+str2
        elif temp[2] == 'bne':
            str2 = ""
            for each in f3:
                temp2 = re.split('#', each)
                if temp2[1] == arr[3]:
                    str2 = str(binary(int(temp2[0]), 16))
                    break
            f2.write('011111'+'00111'+str(binary(int(arr[1]), 5))+str(
                binary(int(arr[2]), 5))+'00000000000'+'\n')
            f4.write(temp[0]+'#'+'011111'+'00111'+str(binary(int(arr[1]), 5)
                                                      )+str(binary(int(arr[2]), 5))+'00000000000'+'\n')
            str1 = str1+'010011'+'00100'+'00010'+str2
    # else:
        # print 'ERROR'
    f2.write(str1+'\n')
    f4.write(temp[0]+'#'+str1+'\n')
    f3.close()


# end function
f = open('Q.s', 'r')
f1 = open('ref.txt', 'r+')
f2 = open('opcode.o', 'w')
f4 = open('opcodeindex.txt', 'w')
flag = 0
for j in f1:
    flag = form(j, flag)
f.close()
f1.close()
f2.close()
f4.close()
