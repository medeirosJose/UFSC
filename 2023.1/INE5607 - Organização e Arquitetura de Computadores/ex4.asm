# Vetor[0] = Vetor[1+Vetor[2]]

# Considere que o endereço de vetor está armazenado em $s4
#	exemplo slide:
#	lw $t0, 4($s5)    -> A[1]
#	add $t1, $t0, $s0 -> A[2] recebe A[1] + i
#	sw $t1, 8($s5)    -> salva vetor A[2] no registrador $s5

#.data
#vetor: .word 0, 0, 2, 3, 4, 5, 6, 7, 8, 9 # Vetor de 10 elementos

.text 
.globl main 

main:
#la $s4, vetor # Carregar endereço de 'vetor' em $s4
lw $t0, 8($s4) 			# vetor[2]
addiu $t0, $t0, 1 		# 1 + vetor[2]
sll $t0, $t0, 2 		
add $t1, $s4, $t0		
lw $t2, 0($t1)			#vetor[1 + vetor[2]]
sw $t2, 0($s4)			#vetor[0] = vetor[1 + vetor[2]]
