            .data

            .text

main:       # function(27, 2)
            addi $sp, $sp, -8   # allocate space for args
            addi $t0, $0, 27    # load value 27 to $t0
            addi $t1, $0, 2     # load value 2 to $t1 
            sw $t0, 4($sp)      # arg1 = 27
            sw $t1, 0($sp)      # arg2 = 2 

            jal function

            # remove locals and exit program
            addi $sp, $sp, 8
            addi $v0, $0, 10
            syscall

function:   # function entry
            addi $sp, $sp, -8
            sw $ra, 4($sp)      # saves $ra
            sw $fp, 0($sp)      # saves $fp
            addi $fp, $sp, 0

            # if x >= y
            lw $t0, 12($fp)     # loads x to $t0
            lw $t1, 8($fp)      # loads y to $t1
            slt $t2, $t1, $t0   # if y < x
            bne $r2, $0, then   # if false end the if condition
            bne $t0, $t1, endif #if y != x then end

            #return x - y
then:       lw $t0, 12($fp)     # loads x to $t0         
            lw $t1, 8($fp)      # loads y to $t1
            sub $t2, $t0, $t1   # x - y
            add $v0, $0, $t2
            lw $fp, 0($sp)      # restores $fp
            lw $ra, 4($fp)      # restores $ra
            addi $sp, $sp, 8    # deallocate
            jr $ra

            # return 0
endif:      add $v0, $0, $0
            lw $fp, 0($sp)      # restores $fp
            lw $ra, 4($fp)      # restores $ra
            addi $sp, $sp, 8    # deallocate
            jr $ra