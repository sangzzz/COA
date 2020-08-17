# Submitted By,
# Sangeeth S V - 181CO246
# Rohith V S - 181CO243
# Jayakrishna Sukumaran - 181CO223
# J Sudarsanan - 181CO222
import re

file = open('Q.s', 'r')
file1 = open('label.txt', 'w')
file2 = open('ref.txt', 'w')
flag = 0
c = 0
str1 = ""
str2 = ""
str3 = ""
for each in file:
    c = c+1
    if each[0] == '#':
        continue
    x = re.split(', |\n|\s|\n|"', each)
    while("" in x):
        x.remove("")
    y = len(x)
    if y == 0:
        continue
    if x[0] == '.data':
        flag = 1
    if x[0] == '.text':
        flag = 2
        # file2.write(str(c)+'\n')
        continue

    if flag == 1:
        temp = len(x[0])
        if x[0][temp-1] == ':':
            str1 = str1+str(c)+'#'
            str1 = str1+x[0][0:temp-1]+'#'
            for temp in x[1:y]:
                if temp == '.asciiz' or temp == '.word':
                    str1 = str1+temp+'#'
                else:
                    str1 = str1+temp+' '
            file1.write(str1+'\n')
            str1 = ""

    if flag == 2:
        y = len(x[0])
        if x[0][y-1] == ':':
            str1 = str1+str(c)+'#'
            str1 = str1+x[0][0:y-1]+'#'
            file1.write(str1+'\n')
            str1 = ""
            continue

        str2 = str2+str(c)+'#'
        if x[0] == 'add':
            str2 = str2+'XO'+'#'+'011111'+'#'+'01000010100'
        elif x[0] == 'addi':
            str2 = str2+'D'+'#'+'001110'
        elif x[0] == 'addis':
            str2 = str2+'D'+'#'+'001111'
        elif x[0] == 'and':
            str2 = str2+'X'+'#'+'011111'+'#'+'00000111000'
        elif x[0] == 'andi':
            str2 = str2+'D'+'#'+'011100'
        elif x[0] == 'extsw':
            str2 = str2+'X'+'#'+'011111'+'#'+'11000111000'
        elif x[0] == 'nand':
            str2 = str2+'X'+'#'+'011111'+'#'+'01110111000'
        elif x[0] == 'or':
            str2 = str2+'X'+'#'+'011111'+'#'+'01101111000'
        elif x[0] == 'ori':
            str2 = str2+'D'+'#'+'011000'
        elif x[0] == 'subf':
            str2 = str2+'XO'+'#'+'011111'+'#'+'00001010000'
        elif x[0] == 'xor':
            str2 = str2+'X'+'#'+'011111'+'#'+'00100111100'
        elif x[0] == 'xori':
            str2 = str2+'D'+'#'+'011010'
        elif x[0] == 'ld':
            str2 = str2+'DS'+'#'+'111010'+'#'+'00'
        elif x[0] == 'lwz':
            str2 = str2+'D'+'#'+'100000'
        elif x[0] == 'std':
            str2 = str2+'DS'+'#'+'111110'+'#'+'00'
        elif x[0] == 'stw':
            str2 = str2+'D'+'#'+'100100'
        elif x[0] == 'stwu':
            str2 = str2+'D'+'#'+'100101'
        elif x[0] == 'lhz':
            str2 = str2+'D'+'#'+'101000'
        elif x[0] == 'lha':
            str2 = str2+'D'+'#'+'101010'
        elif x[0] == 'sth':
            str2 = str2+'D'+'#'+'101100'
        elif x[0] == 'lbz':
            str2 = str2+'D'+'#'+'100010'
        elif x[0] == 'stb':
            str2 = str2+'D'+'#'+'100100'
        elif x[0] == 'rlwinm':
            str2 = str2+'M'+'#'+'010101'+'#'+'0'
        elif x[0] == 'sld':
            str2 = str2+'X'+'#'+'011111'+'#'+'00000110110'
        elif x[0] == 'srd':
            str2 = str2+'X'+'#'+'011111'+'#'+'10000110110'
        elif x[0] == 'srad':
            str2 = str2+'X'+'#'+'011111'+'#'+'11000110100'
        elif x[0] == 'sradi':
            str2 = str2+'XS'+'#'+'011111'+'#'+'11001110100'
        elif x[0] == 'b':
            str2 = str2+'I'+'#'+'010010'+'#'+'00'
        elif x[0] == 'ba':
            str2 = str2+'I'+'#'+'010010'+'#'+'10'
        elif x[0] == 'bl':
            str2 = str2+'I'+'#'+'010010'+'#'+'01'
        elif x[0] == 'bc':
            str2 = str2+'B'+'#'+'010011'+'#'+'00'
        elif x[0] == 'bca':
            str2 = str2+'B'+'#'+'010011'+'#'+'10'
        elif x[0] == 'bclr':
            str2 = str2+'XL'+'#'+'010011'+'#'+'1'
        elif x[0] == 'cmp':
            str2 = str2+'X'+'#'+'011111'+'#'+'00000000000'
        elif x[0] == 'cmpi':
            str2 = str2+'D'+'#'+'001101'
        elif x[0] == 'sc':
            str2 = str2+'SC'+'#'+'010001'
        else:
            str2 = str2+'P'+'#'+x[0]
        file2.write(str2+'\n')
        str2 = ""
file.close()
file1.close()
file2.close()
