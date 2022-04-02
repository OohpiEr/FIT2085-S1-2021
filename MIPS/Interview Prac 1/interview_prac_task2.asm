		        .data
size:		    .word 0 	#array size
the_list:	    .word 0 	#pointer to array
min_item: 	    .word 0     #value of minimum element
i:         	    .word 0	    #for loop counter

promptSize:	    .asciiz "Array length: "
promptNum:	    .asciiz "Enter num: "
promptOutput: 	.asciiz "The minimum element in this list is "
newline: 	    .asciiz "\n"


		        .text
main:		    #size = int(input("Array length: "))
                #Print "Array length: "
                la $a0, promptSize
                addi $v0, $0, 4
                syscall

                #read size
                addi $v0, $0, 5
            	syscall
            	sw $v0, size
            	
            	#CREATE ARRAY ========================================================
            	#the_list = [None] * size
            	
            	#allocate memory
            	addi $v0, $0, 9

            	#create array of input size
            	lw $t0, size
                addi $t0, $t0, 1		#size + 1
                sll $a0, $t0, 2		    #address of array = (size + 1) * 4
            	syscall
            	sw $v0, the_list		#saves address of array to the_list (pointer)

            	#set length as first element in array
            	lw $t0, size		    #loads size of array to $t0
            	lw $t1, the_list		#loads address of array to $t1
            	sw $t0, ($t1)		    #saves size ($t0) to the first address of array ($t1)
            	
		        #FOR LOOP ========================================================
for:		    #for i in range(len(the_list)):       	
		        lw $t0, i		            #loads i to $t0
            	lw $t1, size		        #loads size to $t1
            	beq $t0, $t1, printMinItem	#if i == size, goto printMinItem

            	#the_list[i] = int(input("Enter num: "))
            	#print "Enter num: "
            	la $a0, promptNum
            	addi $v0, $0, 4
            	syscall

            	#read and save input
            	addi $v0, $0, 5
            	syscall			        #input is in $v0

            	lw $t0, i		        #loads i to $t0
            	sll $t1, $t0, 2		    #$t1 = i * 4
            	lw $t2, the_list		#loads address of array to $t2 		
            	add $t1, $t1, $t2	    #address of element i = start address + (i * 4)
            	sw $v0, 4($t1)		    #saves input to (address of element i) + 4, (+4 to skip over length of array)
            
ifBoolCheck1:	#if i == 0
		        lw $t0, i		            #load i into $t0
		        beq $t0, $0, saveMinItem    #branch to saveMinItem if i == 0 
		
ifBoolCheck2:	#if min_item > the_list[i]:
                #load the_list[i]
                lw $t0, i		    #load i into $t0
                sll $t1, $t0, 2		#$t1 = i * 4
                lw $t2, the_list	#loads address of array to $t2 		
                add $t1, $t1, $t2	#address of element i = start address + (i * 4)
                lw $t0, 4($t1)		#loads value stored in (address of element i) + 4 to $t0, (+4 to skip over length of array)
                
                #if min_item > the_list[i]:
                lw $t1, min_item		    #loads min_item to $t1
                slt $t2, $t0, $t1	        #is the_list[i] < min_item?
                beq $t2, $0, loopBackFor	#branch to loopBackFor if !(the_list[i] < min_item)
                
saveMinItem:	#min_item = the_list[i]
                #load the_list[i]
                lw $t0, i		    #load i into $t0
                sll $t1, $t0, 2		#$t1 = i * 4
                lw $t2, the_list	#loads address of array to $t2 		
                add $t1, $t1, $t2	#address of element i = start address + (i * 4)
                lw $t0, 4($t1)		#loads value stored in (address of element i) + 4 to $t0, (+4 to skip over length of array)
                
                #save the_list[i] to min_item
                sw $t0, min_item
		
loopBackFor:	#increase index by 1
		        lw $t0, i		    #loads i to $t0
            	addi $t0, $t0, 1	#i = i + 1
            	sw $t0,i			#saves i + 1 to i
		
		        #loop back to for
            	j for			
            	
                #PRINT RESULT ========================================================

printMinItem:	#print("The minimum element in this list is " + str(min_item))
                #Print "The minimum element in this list is "
                la $a0, promptOutput
                addi $v0, $0, 4
                syscall
                
                #print result
                lw $a0, min_item
                addi $v0, $0, 1
                syscall
                
                #print newline
                addi $v0, $0, 4
                la $a0, newline
                syscall

                #EXIT ========================================================            	            	
exit:		    #Exit the program
            	addi $v0, $0, 10
            	syscall       