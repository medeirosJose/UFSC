# Valor = 4*(a+b+c+d)
# Usar $sx para as variáveis em ordem
# Valor vai para $v0

.text # Define o início do Text Segment
.globl main # Define o início do código do usuário
# $s0 = a, $s1 = b, $s2 = c, $s3 = d
main:
#li $s0, 1 #carrega as variáveis com valores
#li $s1, 2
#li $s2, 3
#li $s3, 4
#li $s4, 4 #registrador que contem o multipllicador

add $s0, $s0, $s1 #a = a + b
add $s0, $s0, $s2 #a = a + c
add $s0, $s0, $s3 #a = a + d

mul $v0, $s4, $s0 #v0 = 4 * a
