#• Que construção de iteração é usada abaixo
#e o que faz o código?
#move $t0, $zero
#loop: sll $t1, $t0, 2
#add $t2, $a0, $t1
#sw $zero, 0($t2)
#addi $t0, $t0, 1
#slt $t3, $t0, $a1
#bne $t3, $zero, loop


.data
Vetor: .word 830224, 12041, 213141

#$a0 = endereço vetor
#$a1 = tamanho de vetor

.text
la $a0, Vetor
li $a1, 3

move $t0, $zero  
loop:
sll $t1, $t0, 2 
add $t2, $a0, $t1 
sw $zero, 0($t2) 
addi $t0, $t0, 1  
slt $t3, $t0, $a1
bne $t3, $zero, loop

#o código acima é um loop
#e é responsável por zerar o vetor inserido.