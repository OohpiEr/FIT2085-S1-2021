# a function that computes a*b/(a-b) in MIPS.

        .text

        .globl following

        # stack frame diagram for following:
        # d is at -8($fp)
        # c is at -4($fp)
        # saved fp is at ($fp) (by convention)
        # saved ra is at +4($fp) (by convention)
        # b is at +8($fp)
        # a is at +12($fp)
following:
        # saves value of $ra on stack
        addi $sp, $sp, -4
        sw $ra, ($sp)

        # saves value of $fp on stack
        addi $sp, $sp, -4
        sw $fp, ($sp)

        ### ALTERNATIVE METHOD TO THE ABOVE TWO ACTIONS
        ### addi $sp, $sp, -8
        ### sw $ra, 4($sp)
        ### sw $fp, ($sp)

        # copies $sp to $fp
        add $fp, $sp, $0

        # allocates local variables on stack
        addi $sp, $sp, -8

        # c = a-b
        lw $t0, 12($fp)         # t0 = a
        lw $t1, 8($fp)          # t1 = b
        sub $t2, $t0, $t1       #t2 = a-b 
        sw $t2, -4($fp)         # c = t2

        # d = a*b
        lw $t0, 12($fp)         # t0 = a
        lw $t1, 8($fp)          # t1 = b
        mult $t0, $t1           #a*b
        mflo $t2                #t2 = a*b
        sw $t2, -8($fp)         # d = t2


        # return d//c
        # sets $v0 to return value
        lw $t0, -4($fp)         # t0 = c
        lw $t1, -8($fp)         # t1 = d
        div $t1, $t0            # d/c
        mflo $v0                # v0 = d//c

        # clears local variables off stack
        addi $sp, $sp, 8

        # restores saved $fp off stack
        lw $fp, ($sp)
        addi $sp, $sp, +4

        # restores saved $ra off stack
        lw $ra, ($sp)
        addi $sp, $sp, +4

        # returns to caller with jr $ra
        jr $ra

