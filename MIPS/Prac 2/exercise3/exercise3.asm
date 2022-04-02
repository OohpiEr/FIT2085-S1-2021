#Author: Er Tian Ru
#description: prints the quotient and remiander of two integers
#global variables: prompt1, prompt2, quotprompt, remprompt, newline, int1, int2, quotient, remainder


        .data
        prompt1: .asciiz "Please enter the first integer: "
        prompt2: .asciiz "Please enter the second integer: "
        quotprompt: .asciiz "The quotient is "
        remprompt: .asciiz "The remainder is "
        newline: .asciiz "\n"
        
        int1: .word 0
        int2: .word 0
        quotient: .word 0
        remainder: .word 0

        .text
main:   #print prompt1
	la $a0, prompt1
        addi $v0, $0, 4
        syscall
        
        #read int1 input
        addi $v0, $0, 5
        syscall
        sw $v0, int1
        
        #print prompt2
	la $a0, prompt2
        addi $v0, $0, 4
        syscall
        
        #read int1 input
        addi $v0, $0, 5
        syscall
        sw $v0, int2
        

        #quotient operation
        lw $t0, int1
        lw $t1, int2
        div $t0, $t1 #LO = int1 // int2
        mflo $t2
        sw $t2, quotient
               
        #remainder operation
        lw $t0, int1
        lw $t1, int2      
        div $t0, $t1 #HI = int1 % int2
        mfhi $t2
        sw $t2, remainder
        

        #print quotprompt
	la $a0, quotprompt
        addi $v0, $0, 4
        syscall
        
        #print quotient
	lw $a0, quotient
        addi $v0, $0, 1
        syscall
        
        #newline
        la $a0, newline
        addi $v0, $0, 4
	syscall 

        #print remprompt
	la $a0, remprompt
        addi $v0, $0, 4
        syscall
        
        #print remainder
	lw $a0, remainder
        addi $v0, $0, 1
        syscall
        
        #newline
        la $a0, newline
        addi $v0, $0, 4
	syscall 

        #exit
        addi $v0, $0, 10
	syscall 
