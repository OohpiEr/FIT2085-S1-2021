        .data
array:  .word 20 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
size:   .word 20
first:  .word 0
last:   .word 0
subsize:.word 0
subarray:.word 0
i:      .word 0
temp:   .word 0

ask1:   .asciiz "Input first index (inclusive): "
ask2:   .asciiz "Input last index (inclusive): "
space:  .asciiz " "
newline:.asciiz "\n"

        .text

        #ask for first
        addi $v0, $0, 4
        la $a0, ask1
        syscall

        #read first
        addi $v0, $0, 5
        syscall
        sw $v0, first

        #ask for last
        addi $v0, $0, 4
        la $a0, ask2
        syscall

        #read last
        addi $v0, $0, 5
        syscall
        sw $v0, last

        #compute subsize
        lw $t0, first
        lw $t1, last
        sub $t2, $t1, $t0
        addi $t2, $t2, 1
        sw $t2, subsize

        #Complete the missing lines below
        
        #allocate size for subarray
        #TODO line 1
	lw $t0, subsize
        addi $t0, $t0, 1 # add 1 to store the size (subsize+1)
        #TODO line 2	
	sll $a0, $t0, 2	#$a0 = (subsize+1)*4 --> sll of 2^2 = 4 --> x4
        addi $v0, $0, 9
        syscall
        #TODO line 3
	sw $v0, subarray
        #set size as first array element
        lw $t0, subsize
        lw $t1, subarray
        #TODO line 4        
	sw $t0, ($t1)

        #init for index i
        sw $0, i 

arraywhile:
        # test i < subsize
        lw $t0, i
        lw $t1, subsize
        slt $t2, $t0, $t1
        beq $t2, $0, endarraywhile

        #do while
        #temp = array[first+i]
        lw $t0, i
        lw $t1, first
        add $t1, $t0, $t1	# t1= first + i
        #TODO line 5
	sll $t1, $t1, 2		# t1 = 4*t1
        #TODO line 6
	la $t2, array		# t2 = address of array
        add $t1, $t2, $t1 	# t1 = address of first + i
        #TODO line 7	
	lw $t3, 4($t1)      	# t3 = array[first+i]
        sw $t3, temp      	# temp = t3

        #subarray[i] = temp
        lw $t0, i
	sll $t0, $t0, 2		# t0 = 4i
        lw $t1, subarray		# t1 = address of subarray in heap
        lw $t2, temp		# t2 = temp
        add $t0, $t0, $t1	# t0 = address of i in subarray
	sw $t2, ($t0)		# subarray[i] = temp

        #print(subarray[i], end= ' ')
        #print subarray
        lw $t0, i         # t0 = i
	sll $t0, $t0, 2     # t0 = 4i
	lw $t1, subarray    # t1 = address of subarray in heap
        add $t0, $t0, $t1 # t0 = address of i in subarray
	lw $a0, ($t0)    # a0 = subarray[i]
        addi $v0, $0, 1
        syscall

        #print space
        addi $v0, $0, 4
        la $a0, space
        syscall

        #increment i
        lw $t0, i
        addi $t0, $t0, 1
        sw $t0, i

        #loop back
        j arraywhile

endarraywhile:
        #print newline
        addi $v0, $0, 4
        la $a0, newline
        syscall

        addi $v0, $0, 10
        syscall
