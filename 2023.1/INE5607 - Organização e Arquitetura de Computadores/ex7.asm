
#Faça o papel do compilador para o seguinte código
#	– for ( i = 0 ; i < y ; i ++ ) x *= z;
#	• Considere que existe uma pseudoinstrução mult
#	que é composta de várias instruções mais simples
#	– mult $t0, $t1, $t2 -> $t0 = $t1 * $t2

.data
i: .word 0 #i == 0
y: .word 4
x: .word 6
z: .word 2

.text
main:
#é possível não utilizar a .data e usar os li para carregar os
#endereços diretamente
    la $t0, i
    la $t1, y
    la $t2, x
    la $t3, z

    lw $s0, 0($t0)
    lw $s1, 0($t1)
    lw $s2, 0($t2)
    lw $s3, 0($t3)

for:
    bge $s0, $s1, end_for   
    mult $s2, $s3           
    mflo $s2                
    addi $s0, $s0, 1        
    j for                    

end_for:
    sw $s2, 0($t2)       #dados os valores, esperasse resultar em 96
    			 #no caso, 60 em hex.   
