#Author: Er Tian Ru
#description: prints a string
#global variables: prompt
        
        .data
        prompt: .asciiz "I am really enjoying MIPS"
        newline: .asciiz "\n"

        .text
main:   #print prompt
        la $a0, prompt
        addi $v0, $0, 4
        syscall

        #newline
        la $a0, newline
        addi $v0, $0, 4
	syscall 

        #exit
        addi $v0, $0, 10
	syscall 
