# a main function that calls the external function "following"
        .data

prompt: .asciiz "Enter integer: "
newline:.asciiz "\n"

        .text

        # stack frame diagram for main:
        # y is at -8($fp)
        # x is at -4($fp)
main:
        # copies $sp to $fp
        add $fp, $sp, $0

        # allocates local variables on stack
        addi $sp, $sp, -8

        # x = int(input("Enter integer: "))
        # ask for int
        addi $v0, $0, 4
        la $a0, prompt
        syscall

        # read int
        addi $v0, $0, 5
        syscall
        sw $v0, -4($fp)         # save read int into x

        # y = int(input("Enter integer: "))
        # ask for int
        addi $v0, $0, 4
        la $a0, prompt
        syscall

        # read int
        addi $v0, $0, 5
        syscall
        sw $v0, -8($fp)         # save read int into y

        # print(following(x, y))
        # 1st step: $a0 = following(x, y)

        # passes arguments on stack
        # pass x into arg a
        addi $sp, $sp, -4
        lw $t0, -4($fp)         # load x into $t0
        sw $t0, ($sp)           # save x into arg1 (a)
        # pass y into arg b
        addi $sp, $sp, -4
        lw $t0, -8($fp)         # load y into $t0
        sw $t0, ($sp)           # save y into arg2 (b)

        ### ALTERNATIVE METHOD TO THE ABOVE ACTIONS (passes arguments on stack)
        ### addi $sp, $sp, -8
        ### lw $t0, -4($fp)
        ### sw $t0, 4($sp)
        ### lw $t0, -8($fp)
        ### sw $t0, ($sp)

        # calls function using jal fnlabel
        jal following

        # clears arguments off stack
        addi $sp, $sp, 8

        # uses return value in $v0
        add $a0, $v0, $0

        # 2nd step: print $a0
        addi $v0, $0, 1
        syscall
        #print newline
        la $a0, newline
        add $v0, $0, 4
        syscall

        #exit
        addi $v0, $0, 10
        syscall
