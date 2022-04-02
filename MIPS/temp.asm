        .data
x:      .word 0
y:      .word 2
z:      .word 4

        .text
        lw $t0, y
        lw $t1, z
        mult $t0 , $t1
        mflo $t1
        sw $t1, x

        lw $t0, x
        addi $t1, $0, 4
        div $t0, $t1
        mflo $t1
        sw $t1, x

        lw $t1, x
        addi $v0, $0, 1
        syscall