#Author: Er Tian Ru
#description: reads in two positive integers, and prints the (almost) Pythagorean triple
#global variables: prompt1, prompt2, outputprompt, space, newline, intn, intm, inta, intb, intc      
        
        .data
	prompt1: .asciiz "Please enter integer n: "
        prompt2: .asciiz "Please enter integer m: "
        outputprompt: .asciiz "The almost pythagorean triple is "
        space: .asciiz " "
        newline: .asciiz "\n"
        
        intn: .word 0
        intm: .word 0
        inta: .word 0
        intb: .word 0
        intc: .word 0

        .text
main:   #print prompt1
	la $a0, prompt1
        addi $v0, $0, 4
        syscall
        
        #read intn input
        addi $v0, $0, 5
        syscall
        sw $v0, intn
        
        
        #print prompt2
	la $a0, prompt2
        addi $v0, $0, 4
        syscall
        
        #read intm input
        addi $v0, $0, 5
        syscall
        sw $v0, intm
        
        
	#loaded intn and intm 
        lw $t0, intn
        lw $t1, intm

        #pythagorean operation - a 
        mult $t0, $t0
        mflo $t2
	mult $t1, $t1
        mflo $t3
        sub $t3, $t3, $t2
        sw $t3, inta       
        
	#pythagorean operation - b
        addi $t2, $0, 2
        mult $t1, $t0
        mflo $t3
        mult $t2, $t3	
        mflo $t3        
        sw $t3, intb
        
        #pythagorean operation - c 
        mult $t0, $t0
        mflo $t2
	mult $t1, $t1
        mflo $t3
        add $t3, $t3, $t2
        sw $t3, intc
        
        
        #print outputprompt
	la $a0, outputprompt
        addi $v0, $0, 4
        syscall
        
        #print inta
	lw $a0, inta
        addi $v0, $0, 1
        syscall
        
        #print space
	la $a0, space
        addi $v0, $0, 4
        syscall
             
        #print intb
	lw $a0, intb
        addi $v0, $0, 1
        syscall
        
        #print space
	la $a0, space
        addi $v0, $0, 4
        syscall
              
	#print intc
	lw $a0, intc
        addi $v0, $0, 1
        syscall    

        #newline
        la $a0, newline
        addi $v0, $0, 4
	syscall 

	#exit
        addi $v0, $0, 10
	syscall         
