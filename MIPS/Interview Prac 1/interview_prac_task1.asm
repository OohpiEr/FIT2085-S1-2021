		.data
first:  		.word 0
second:		.word 0
result:		.word 0

promptFirst:	.asciiz "Enter first: "
promptSecond:	.asciiz "Enter second: "
promptResult:	.asciiz "Result: "
newline: 	.asciiz "\n"

		.text
main:		#first = int(input("Enter first: "))
        		#ask for first
	        addi $v0, $0, 4
		la $a0, promptFirst
		syscall

		#read int
		addi $v0, $0, 5
		syscall
		sw $v0, first
		
		#second = int(input("Enter second: "))
		#ask for second
		addi $v0, $0, 4
		la $a0, promptSecond
		syscall

		#read int
		addi $v0, $0, 5
		syscall
		sw $v0, second
		
ifBoolCheck1:	#if first > 0:
		lw $t0, first			#load first into $t0
		slt $t0, $0, $t0			#is 0 < first?
		beq $t0, $0, elifBoolCheck1 	#branch if !(0 < first)
		
ifBoolCheck2:	#if second >= 0: 	
		lw $t0, second			#load second into $t0
		slt $t0, $t0, $0			#is second < 0? (i.e. !(second >= 0))
		beq $t0, $0, divResult 		#branch if !(second < 0) (i.e. second >= 0)
		
elifBoolCheck1:	#if first == second
		lw $t1, first			#load first into $t1
		lw $t2, second			#load second into $t2
		beq $t1, $t2, multResultElif		#branch if first == second
		
elifBoolCheck2:	#if first < second
		lw $t1, first			#load first into $t1
		lw $t2, second			#load second into $t2		
		slt $t0, $t1, $t2		#is first < second?
		beq $t0, $0, multResultElse 		#branch if !(first < second)

multResultElif:	#result = first * second
		lw $t1, first			#load first into $t1
		lw $t2, second			#load second into $t2		
		mult $t1, $t2			#LO = first * second		
		mflo $t0    			#load LO into $t0
		sw $t0, result			#save $t0 in result				
		j print				#goto print
				
divResult:	#result = second // first
		lw $t0, first			#load first into $t0
		lw $t1, second			#load second into $t1
		div $t1, $t0 			#LO = second // first
		mflo $t0				#load LO into $t0
		sw $t0, result			#save $t0 in result
		j print				#goto print

multResultElse: 	#result = second * 2
		addi $t1, $0, 2			#add 2 into $t1
		lw $t2, second			#load second into $t2
		mult $t1, $t2			#LO = second * 2
		mflo $t0				#load LO into $t0
		sw $t0, result			#save $t0 in result
		j print				#goto print
		
print:		#print promptResult
	        addi $v0, $0, 4
		la $a0, promptResult
		syscall
		#print result
		lw $a0, result
		addi $v0, $0, 1
		syscall
		#print newline
	        addi $v0, $0, 4
		la $a0, newline
		syscall
		
exit:	        #exit
		addi $v0, $0, 10
		syscall 		
		
				
		

		
		
		
		
		
		
		
		
		