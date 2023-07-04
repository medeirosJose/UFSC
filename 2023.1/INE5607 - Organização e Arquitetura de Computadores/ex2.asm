#s = (a & b) | (!a & c)
#s = (a E b) OU (não a E c)

# $s0 = s | $s1 = a | $s2 = b | $s3 = c 
# $t0 | $t1 | $t2 #registradores temporarios

.text # Define o início do Text Segment
.globl main # Define o início do código do usuário
#li $s1,1 
#li $s2,1
#li $s3,0
main: # Label que define o início do código do usuário

and $t1, $s1, $s2

nor $t3, $s1, $zero

and $t2, $t3, $s3

or $s0, $t1, $t2
