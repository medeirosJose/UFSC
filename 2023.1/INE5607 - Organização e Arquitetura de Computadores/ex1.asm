#####################################################################
# EXERCÍCIO 1
#####################################################################
.text # Define o início do Text Segment
.globl main # Define o início do código do usuário

main: # Label que define o início do código do usuário
li $s0, 10    # $s0 = x = 10
li $s1, 20    # $s1 = y = 20
li $s2, 30    # $s2 = z = 30

# x = ((x+300) – y) + z + 27 + x

#add $s0, $s1, $s2 #x = s0, y = s1, z = s

addi $t0, $s0, 300 #$t0 = x + 300

sub $t0, $t0, $s1 #st0 = st0 - s1, ou seja, st0 = (x+300) - y

add $t0, $t0, $s2 #st0 = st0 + s2, ou seja, st0 = ((x+300)-y) + z

addi $t0, $t0, 27 #st0 = st0 + 27

add $s0, $t0, $s0 #x = (((x+300)-y) + z + 27) + x



