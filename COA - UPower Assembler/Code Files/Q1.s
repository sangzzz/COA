.data
X:  .word 5
Y:  .word 10
SUM:  .word 0
.text
main:
  la 4, 0(X)
  addi 5, 4, 0
  li 4, 0

  la 4, 0(Y)
  addi 6, 4, 0
  li 4, 0

  la 4, 0(SUM)
  add 4, 5, 6
  stw 4, 0(2)
