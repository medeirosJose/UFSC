# Defina um Array Conta com 10 posições e inicialize ele com
# valores inteiros aleatórios entre 0 e 100.
# Escreva o código em assembly do MIPS que coloca no registrador
# $s0 a média das posições Conta[3] e Conta[7].

.data
Conta: .word 0, 1, 2, 100, 4, 5, 6, 50, 8, 9  # Array Conta com 10 posições

.text # Define o início do Text Segment
.globl main # Define o início do código do usuário

main:
li $t4, 2
la $s2, Conta
		# por padrão são 4 bits
lw $t0, 12($s2) # endereço 12 (4 * posição) | posição = 3
lw $t1, 28($s2) # posição 28 (4 * posição) | posição = 7
		
add $s0, $t0, $t1 #salva no $s0 a soma de $t0 + $t1

div $s0,$t4 #divide $s0 por 2
mflo $s0 #move o resultado da divisão para o registrador $s0
