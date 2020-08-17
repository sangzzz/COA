.data
n1:  .asciiz "Enter 1st Number : "
n2:  .asciiz "Enter 2nd Number : "
sum: .asciiz "The Sum : "
.text
main:
  la 4, 0(n1)
  sc 4
  li 4, 0

  li 3, 0
  sc 3
  addi 5,3,0
  li 3,0

  la 4, 0(n2)
  sc 4
  li 4, 0

  li 3, 0
  sc 3
  addi 6, 3, 0
  li 3, 0

  add 8, 5, 6

  la 4, 0(sum)
  sc 4
  li 4, 0

  addi 4, 8, 0
  sc 4
  li 4, 0
