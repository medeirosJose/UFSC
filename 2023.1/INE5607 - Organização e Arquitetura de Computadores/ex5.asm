#Considere a seguinte situação:
#$t8 = 0x00BADBED
#$t9 = 0xAFADA007

#Qual seria o valor de $s6 após a
#execução das instruções abaixo?
#sll $t1, $t8, 4
#and $t1, $t1, $t9
#ori $s6, $t1, 20

.text 
.globl main # Define o início do código do usuário

main:
li $t8, 0x00BADBED
li $t9, 0xAFADA007
				#começo em 0x00BADBED
sll $t1, $t8, 16 #shift left resulta em 0x0bada000
sll $t2, $t8, 4 #empurra 1 em hexa para o lado
and $t1, $t1, $t9
ori $s6, $t1, 20 #resultará em 0x0bada014
