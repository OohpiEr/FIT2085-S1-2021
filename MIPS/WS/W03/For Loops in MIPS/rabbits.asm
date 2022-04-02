        .data

previous:.word -1
current:.word 1
size:   .word 0
i:      .word 0

input:  .asciiz "Input size: "
space:  .asciiz " "
newline:.asciiz "\n"

        .text

        #size = int(input("Input size: "))
        #ask for size`
        addi $v0, $0, 4
        la $a0, input
        syscall

        #read int
        addi $v0, $0, 5
        syscall
        sw $v0, size

        #Complete the missing lines below
        #i = 0
        sw $0, i

whilerabbits:
        #while i < size:
        lw $t0, i
        lw $t1, size
        slt $t0, $t0, $t1		#is i < size?
	beq $t0, $0, endwhilerabbits	#if i >= size, branch to end of loop

        #do while
        #current = current + previous
        lw $t0, current
        lw $t1, previous
        add $t0, $t0, $t1
        sw $t0, current

        #previous = current - previous
        lw $t0, current
        lw $t1, previous
        sub $t1, $t0, $t1
        sw $t1, previous

        #print(current, end=' ')
        addi $v0, $0, 1
        lw $a0, current
        syscall
        #print space
        add $v0, $0, 4
        la $a0, space
        syscall

        #i += 1
	lw $t0, i
	addi $t0, $t0, 1
	sw $t0, i

        #jump back
	j whilerabbits

endwhilerabbits:

        #print newline
        add $v0, $0, 4
        la $a0, newline
        syscall

        addi $v0, $0, 10
        syscall

