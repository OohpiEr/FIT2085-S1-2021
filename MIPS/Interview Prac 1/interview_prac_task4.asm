.globl		bubble_sort
		.data

		.text
		
		# stack frame diagram for main:
		# the_list 	is at -12($fp)
		# i 		is at -8($fp)
		# end 		is at -4($fp)
		# saved fp 	is at ($fp) (by convention)
		# saved ra 	is at +4($fp) (by convention)

		# stack frame diagram for bubble_sort:
		# item_to_right	is at -20($fp)
		# item		is at -16($fp)	
		# a 		is at -12($fp)		
		# i 		is at -8($fp)
		# n 		is at -4($fp)
		# saved fp 	is at ($fp) (by convention)
		# saved ra 	is at +4($fp) (by convention)
		# the_list 	is at +8($fp)
			
main:			# set $fp and make space for locals
				addi $fp, $sp, 0 # copy $sp into $fp
				addi $sp, $sp, -12 # allocates local variables on stack

				#CREATE ARRAY ========================================================
				#the_list = [4, -2, 6, 7]
            	
            	#allocate memory
            	addi $v0, $0, 9

            	#create array of size 4
				addi $t0, $0, 5		#size including length = 4 + 1 = 5 (first element is length of array) 
				sll $a0, $t0, 2		#address of array = size including length * 4
            	syscall
            	sw $v0, -12($fp)		#saves address of array to the_list (pointer)

            	#set length as first element in array
				addi $t0, $0, 4		#loads size of array (4) to $t0
            	lw $t1, -12($fp)		#loads address of array (the_list) to $t1
            	sw $t0, ($t1)		#saves size ($t0) to the first address of array ($t1)
				#set 4 (index i = 0) as second element in array
				addi $t3, $0, 4		#loads 4 to $t3
				lw $t2, -12($fp)		#loads address of array (the_list) to $t2
            	sw $t3, 4($t2)		#saves 4 to (address of element 0) + 4, (address of element 0 = start address, +4 to skip over length of array)
				#set -2 (index i = 1) as third element in array
				addi $t3, $0, -2		#loads -2 to $t3
				lw $t2, -12($fp)		#loads address of array (the_list) to $t2
				addi $t1, $t2, 4 	#address of element 1 = start address + (1 * 4) = start address + 4
            	sw $t3, 4($t1)		#saves -2 to (address of element 1) + 4, (+4 to skip over length of array)
				#set 6 (index i = 2) as fourth element in array
				addi $t3, $0, 6		#loads 6 to $t3
				lw $t2, -12($fp)		#loads address of array (the_list) to $t2
				addi $t1, $t2, 8		#address of element 2 = start address + (2 * 4) = start address + 8
            	sw $t3, 4($t1)		#saves 6 to (address of element 2) + 4, (+4 to skip over length of array)
				#set 7 (index i = 3) as fifth element in array
				addi $t3, $0, 7		#loads 7 to $t3
				lw $t2, -12($fp)		#loads address of array (the_list) to $t2
				addi $t1, $t2, 12	#address of element 3 = start address + (3 * 4) = start address + 12
            	sw $t3, 4($t1)		#saves 7 to (address of element 3) + 4, (+4 to skip over length of array)
            	
            	# Call bubble_sort(the_list) ==============================================
				# push 4 bytes of arguments
				addi $sp, $sp, -4
		
				# arg = the_list
				lw $t0, -12($fp) # load the_list
				sw $t0, 0($sp) # arg = the_list
            	
            	# link and goto bubble_sort
				jal bubble_sort
            	
            	# for loop main =============================================================
loop_main:		#for i in range(len(the_list)):     	
				lw $t0, -8($fp)			#loads i to $t0
				lw $t1, -12($fp)			#loads start address of array (the_list) to $t1		
				lw $t2, ($t1)			#loads length of array stored in start address of the_list to $t2
            	beq $t0, $t2, exit		#if i == length of array, goto exit

				#print(the_list[i], end='')
				#load the_list[i]
				lw $t0, -8($fp)			#loads i to $t0
				sll $t1, $t0, 2			#$t1 = i * 4
				lw $t2, -12($fp)			#loads address of array (the_list) to $t2 		
				add $t1, $t1, $t2		#address of element i = start address + (i * 4)
				lw $t0, 4($t1)			#loads value stored in (address of element i) + 4 to $t0, (+4 to skip over length of array)
				#print the_list[i] 
				add $a0, $0, $t0
				addi $v0, $0, 1
				syscall
				
				#increase i by 1
				lw $t0, -8($fp)		#loads i to $t0
				addi $t0, $t0, 1		#i = i + 1
            	sw $t0,-8($fp)		#saves i + 1 to i
		
				#loop back to loop_i
            	j loop_main
		

bubble_sort:	# Save $ra and $fp in stack
				addi $sp, $sp, -8 # make space
				sw $ra, 4($sp) # save $ra
				sw $fp, 0($sp) # save $fp
				
				# Copy $sp to $fp
				addi $fp, $sp, 0
				
				# Allocate local variables
				addi $sp, $sp, -20
				
				# n = len(the_list)
				lw $t1, 8($fp)		#loads start address of array (the_list) to $t1		
				lw $t2, ($t1)		#loads length of array stored in start address of the_list to $t2
				sw $t2, -4($fp)		#saves length of array to n
		
loop_a:			# for a in range(n-1):      	
				lw $t0, -12($fp)			#loads a to $t0
				lw $t1, -4($fp)			#loads n to $t1
				addi $t2, $0, 1			#loads 1 to $t2
				sub $t2, $t1, $t2		#$t2 = n - 1
            	beq $t0, $t2, end_bubble_sort	#if a == (n - 1), goto end_bubble_sort
				# check if array is empty (if n == 0)
				lw $t2, -4($fp)			#loads n to $t2
				beq $t2, $0, end_bubble_sort	#if n == 0, goto end_bubble_sort

loop_i:			# for i in range(n-1):    	
				lw $t0, -8($fp)			#loads i to $t0
				lw $t1, -4($fp)			#loads n to $t1
				addi $t2, $0, 1			#loads 1 to $t2
				sub $t2, $t1, $t2		#$t2 = n - 1
            	beq $t0, $t2, loop_back_a	#if i == (n - 1), goto loop_a
            	
            	#item = the_list[i]
				#load the_list[i]
				lw $t0, -8($fp)			#loads i to $t0
				sll $t1, $t0, 2			#$t1 = i * 4
				lw $t2, 8($fp)			#loads address of array (the_list) to $t2 		
				add $t1, $t1, $t2		#address of element i = start address + (i * 4)
				lw $t0, 4($t1)			#loads value stored in (address of element i) + 4 to $t0, (+4 to skip over length of array)
				#save the_list[i] to item
				sw $t0, -16($fp)	
				
				#item_to_right = the_list[i+1]
				#load the_list[i+1]
				lw $t0, -8($fp)			#loads i to $t0
				addi $t0, $t0, 1			#$t0 = i + 1
				sll $t1, $t0, 2			#$t1 = (i + 1) * 4
				lw $t2, 8($fp)			#loads address of array (the_list) to $t2 		
				add $t1, $t1, $t2		#address of element i + 1 = start address + ((i + 1) * 4)
				lw $t0, 4($t1)			#loads value stored in (address of element i + 1) + 4 to $t0, (+4 to skip over length of array)
				#save the_list[i+1] to item_to_right
				sw $t0, -20($fp)
		
if:				#if item > item_to_right: 
				lw $t0, -20($fp)		#loads item_to_right to $t0
                lw $t1, -16($fp)		#loads item to $t1
                slt $t2, $t0, $t1	#is item_to_right < item?
                beq $t2, $0, loop_back_i	#branch to loop_i if !(item_to_right < item)
                
                #the_list[i] = item_to_right
				lw $t3, -20($fp)		#loads item_to_right to $t3
                lw $t0, -8($fp)		#loads i to $t0
            	sll $t1, $t0, 2		#$t1 = i * 4
            	lw $t2, 8($fp)		#loads address of array to $t2 		
            	add $t1, $t1, $t2	#address of element i = start address + (i * 4)
            	sw $t3, 4($t1)		#saves item_to_right to (address of element i) + 4, (+4 to skip over length of array)
            
            	#the_list[i+1] = item 
				lw $t3, -16($fp)		#loads item to $t3
                lw $t0, -8($fp)		#loads i to $t0
				addi $t0, $t0, 1		#$t0 = i + 1
				sll $t1, $t0, 2		#$t1 = (i + 1) * 4
            	lw $t2, 8($fp)		#loads address of array to $t2 		
            	add $t1, $t1, $t2	#address of element i = start address + ((i + 1) * 4)
            	sw $t3, 4($t1)		#saves item to (address of element i + 1) + 4, (+4 to skip over length of array)

loop_back_i:	#increase i by 1
				lw $t0, -8($fp)		#loads i to $t0
            	addi $t0, $t0, 1		#i = i + 1
            	sw $t0,-8($fp)		#saves i + 1 to i
		
				#loop back to loop_i
            	j loop_i
            	
loop_back_a:    #resets i
				sw $0, -8($fp)

				#increase a by 1
				lw $t0, -12($fp)		#loads a to $t0
            	addi $t0, $t0, 1		#a = a + 1
            	sw $t0,-12($fp)		#saves a + 1 to a
		
				#loop back to loop_i
            	j loop_a         	

end_bubble_sort:	#bubble_sort Function return
				# Deallocate local variable
				addi $sp, $sp, 20
		
				# Restore $fp and $ra
				lw $fp, 0($sp) # restore $fp
				lw $ra, 4($sp) # restore $ra
				addi $sp, $sp, 8 # dealloc
				
				# return
				jr $ra
		
exit:			#exit
				addi $v0, $0, 10
				syscall 			

            	
            	
            	
            	
            	
            	
            	
            	
