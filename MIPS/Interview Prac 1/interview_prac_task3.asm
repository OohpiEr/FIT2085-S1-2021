		        # Makes this function globally accessible by other files
.globl 		    get_minimum

                	.data

                	.text
                            
                # stack frame diagram for get_minimum:
                # i 		is at -12($fp)
                # item 		is at -8($fp)
                # min_item 	is at -4($fp)
                # saved fp 	is at ($fp) (by convention)
                # saved ra 	is at +4($fp) (by convention)
                # the_list 	is at +8($fp)
                	

		        # def get_minimum(the_list: List[int]) -> int:
get_minimum:	# saves value of $ra on stack
                addi $sp, $sp, -4
                sw $ra, ($sp)

                # saves value of $fp on stack
                addi $sp, $sp, -4
                sw $fp, ($sp)

                # copies $sp to $fp
                add $fp, $sp, $0

                # allocates local variables on stack
                addi $sp, $sp, -12
                
                #min_item = the_list[0]
                #load the_list[0]
                addi $t0, $0, 0		#load 0 into $t0
                sll $t1, $t0, 2		#$t1 = 0 * 4
                lw $t2, 8($fp)		#loads address of array (the_list) to $t2 		
                add $t1, $t1, $t2	#address of element 0 = start address + (i * 4)
                lw $t0, 4($t1)		#loads value stored in (address of element 0) + 4 to $t0, (+4 to skip over length of array)
                #save the_list[0] to min_item
                sw $t0, -4($fp)		
                
                #set i to 1
            	addi $t0, $0, 1		#$t0 = 1
            	sw $t0, 	-12($fp)		#saves $t0 to i

		        #FOR LOOP ========================================================
for:		    #for i in range(1, len(the_list)):       	
                lw $t0, -12($fp)		        #loads i to $t0
                lw $t1, 8($fp)			#loads start address of array (the_list) to $t1		
                lw $t2, ($t1)			#loads length of array stored in start address of the_list to $t2
            	beq $t0, $t2, return		#if i == length of array, goto return

            	#item = the_list[i]
                #load the_list[i]
                lw $t0, -12($fp)		#load i into $t0
                sll $t1, $t0, 2		#$t1 = i * 4
                lw $t2, 8($fp)		#loads address of array (the_list) to $t2 		
                add $t1, $t1, $t2	#address of element i = start address + (i * 4)
                lw $t0, 4($t1)		#loads value stored in (address of element i) + 4 to $t0, (+4 to skip over length of array)
                
                #save the_list[i] to item
                sw $t0, -8($fp)
		
ifBoolCheck:	#if min_item > item:
		        lw $t0, -8($fp)		#loads item to $t0
                lw $t1, -4($fp)		#loads min_item to $t1
                slt $t2, $t0, $t1	#is item < min_item?
                beq $t2, $0, loopBackFor	#branch to loopBackFor if !(the_list[i] < min_item)
                
		        #min_item = item
                #load item
		        lw $t0, -8($fp)		#loads item to $t0
                sw $t0, -4($fp)		#save item to min_item
		
loopBackFor:	#increase i by 1
		        lw $t0, -12($fp)		#loads i to $t0
            	addi $t0, $t0, 1		#i = i + 1
            	sw $t0, -12($fp)		#saves i + 1 to i
		
		        #loop back to for
            	j for
            	
            	#return min_item
return:		    # sets $v0 to return value
                lw $t0, -4($fp)		#loads min_item to $t0
                add $v0, $0, $t0		#saves min_item to $v0
                
                # clears local variables off stack
        		addi $sp, $sp, 12

       		    # restores saved $fp off stack
        		lw $fp, ($sp)
        		addi $sp, $sp, +4

        		# restores saved $ra off stack
        		lw $ra, ($sp)
        		addi $sp, $sp, +4

        		# returns to caller with jr $ra
        		jr $ra

