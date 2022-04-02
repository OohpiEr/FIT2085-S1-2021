#if-then-else to guess a number.

        .data
secret: .word 42
guess:  .word 0
diff:   .word 0

ask:    .asciiz "Enter guess: "
high:   .asciiz "Too high"
good:   .asciiz "Good guess!"
low:    .asciiz "Too low"

        .text

        #guess = int(input("Enter guess: "))
        #ask for guess
        addi $v0, $0, 4
        la $a0, ask
        syscall

        #read int
        addi $v0, $0, 5
        syscall
        sw $v0, guess

        #diff = secret - guess
        lw $t0, secret
        lw $t1, guess
        sub $t2, $t0, $t1
        sw $t2, diff

        #if diff < 0:
        lw $t0, diff		#load diff into $t0
        slt $t0, $t0, $0		#is diff < 0?
	beq $t0, $0, elifdiff 	#branch if diff is not < 0

        #print("Too high")
        addi $v0, $0, 4
        la $a0, high
        syscall
        j endifguess

elifdiff:
        #elif diff == 0:
        lw $t0, diff		#load diff into $t0
	bne $t0, $0, elsediff	#branch to else when diff != 0

        #print("Good guess!")
        addi $v0, $0, 4
        la $a0, good
        syscall
        j endifguess

elsediff: 
        #print("Too low")
        addi $v0, $0, 4
        la $a0, low
        syscall
        j endifguess

endifguess:
        #exit
        addi $v0, $0, 10
        syscall
