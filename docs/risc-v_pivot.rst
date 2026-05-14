RISC-V Assembler Pivot View
===========================

.. list-table:: RISC-V Assembler Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: asm

           x:  .word 42
     - Defined in the .data section.
   * - CollectionDefinition
     - .. code-block:: asm

           arr: .word 1, 2, 3
     - A collection is defined as a series of data directives in the data section.
   * - AssociativeArrayDefinition
     - N/A
     - Associative arrays are typically implemented via pointers and memory structures.
   * - SwitchCase
     - .. code-block:: asm

               li t1, 1
               beq t0, t1, .case1
               li t1, 2
               beq t0, t1, .case2
               j .default
     - Typically implemented using comparison and branch instructions.
   * - IfElse
     - .. code-block:: asm

               blez t0, .else
               li a0, 1
               j .end
           .else:
               li a0, 0
           .end:
     - Uses branch instructions like blez (branch if less than or equal to zero).
   * - Loop
     - .. code-block:: asm

           .loop:
               blez t0, .end
               addi t0, t0, -1
               j .loop
           .end:
     - Uses conditional branches and jumps to implement loops.
   * - FunctionDefinition
     - .. code-block:: asm

           add:
               add a0, a0, a1
               ret
     - Functions follow the RISC-V calling convention; a0-a7 are argument registers.
   * - ProcedureDefinition
     - .. code-block:: asm

           log_message:
               addi sp, sp, -16
               sd ra, 8(sp)
               call printf
               ld ra, 8(sp)
               addi sp, sp, 16
               ret
     - Follows standard calling convention; must save/restore return address (ra) if calling other functions.
   * - TryCatch
     - N/A
     - No native try-catch; relies on return codes or trap handlers for errors.
   * - Raise
     - .. code-block:: asm

               ebreak
     - The ebreak instruction triggers a debug trap; ecall can be used for system calls.
   * - Thread
     - .. code-block:: asm

               li a7, 220 # clone syscall
               ecall
     - Thread creation typically involves invoking OS system calls (e.g., clone in Linux).
   * - SendMessage
     - .. code-block:: asm

               li a7, 139 # rt_sigqueueinfo
               ecall
     - Inter-process/thread communication is managed by the OS.
   * - ReceiveMessage
     - .. code-block:: asm

               li a7, 128 # rt_sigtimedwait
               ecall
     - Receiving signals or messages involves OS system calls.
   * - SingleLineComment
     - .. code-block:: asm

           # comment
     - RISC-V assembly typically uses the hash character for single-line comments.
   * - MultiLineComment
     - N/A
     - RISC-V assembly does not have a native multi-line comment syntax.
   * - Print
     - .. code-block:: asm

               la a0, hello_msg
               call printf
     - Typically uses the C library printf or writes to stdout via system calls.
   * - Import
     - .. code-block:: asm

           .include "macros.s"
     - Uses the .include directive to include external source files.
   * - Constant
     - .. code-block:: asm

           .equiv MAX, 100
     - Uses the .equiv or .set directive to define constants.
   * - Addition
     - .. code-block:: asm

           add t0, t1, t2
     - Standard RISC-V instructions.
   * - Subtraction
     - .. code-block:: asm

           sub t0, t1, t2
     - Standard RISC-V instructions.
   * - Multiplication
     - .. code-block:: asm

           mul t0, t1, t2
     - Standard RISC-V M-extension instructions.
   * - Division
     - .. code-block:: asm

           div t0, t1, t2
     - Standard RISC-V M-extension instructions.
   * - Remainder
     - .. code-block:: asm

           rem t0, t1, t2
     - Standard RISC-V M-extension instructions.
   * - Floor
     - N/A
     - Standard RISC-V instructions.
   * - Rounding
     - N/A
     - Standard RISC-V instructions.
   * - Increment
     - .. code-block:: asm

           addi t0, t0, 1
     - Standard RISC-V instructions.
   * - Decrement
     - .. code-block:: asm

           addi t0, t0, -1
     - Standard RISC-V instructions.
   * - LeftShift
     - .. code-block:: asm

           sll t0, t1, t2
     - Standard RISC-V instructions.
   * - RightShift
     - .. code-block:: asm

           srl t0, t1, t2
     - Standard RISC-V instructions.
   * - BitAnd
     - .. code-block:: asm

           and t0, t1, t2
     - Core bitwise logical and shift instructions.
   * - BitOr
     - .. code-block:: asm

           or t0, t1, t2
     - Core bitwise logical and shift instructions.
   * - BitXor
     - .. code-block:: asm

           xor t0, t1, t2
     - Core bitwise logical and shift instructions.
   * - BitNot
     - .. code-block:: asm

           not t0, t1
     - Core bitwise logical and shift instructions.
   * - Float4VectorMultiplication
     - .. code-block:: asm

           vsetvli t0, x0, e32, m1
           vfmul.vv v1, v2, v3
     - Uses the RISC-V Vector extension (RVV) for element-wise float multiplication.
   * - Float4VectorDotProduct
     - .. code-block:: asm

           vsetvli t0, x0, e32, m1
           vfmul.vv v1, v2, v3
           vfredusum.vs v4, v1, v5
     - Uses vfmul.vv for multiplication and vfredusum.vs for a horizontal sum.
   * - Float4VectorCrossProduct
     - N/A
     - RISC-V Vector extension does not have a dedicated cross product instruction; requires multiple operations.
   * - ForLoop
     - .. code-block:: asm

               li t0, 0
               li t1, 10
           .loop:
               bge t0, t1, .end
               ; body
               addi t0, t0, 1
               j .loop
           .end:
     - Implemented using a counter register and conditional branches.
   * - ForEach
     - .. code-block:: asm

               la t0, collection
               li t1, count
           .loop:
               beqz t1, .end
               lw t2, 0(t0)
               ; body (use t2)
               addi t0, t0, 4
               addi t1, t1, -1
               j .loop
           .end:
     - Iterates over an array using a pointer and a countdown.
   * - Equal
     - .. code-block:: asm

           beq t0, t1, .equal
     - Branch if equal.
   * - NotEqual
     - .. code-block:: asm

           bne t0, t1, .not_equal
     - Branch if not equal.
   * - GreaterThan
     - .. code-block:: asm

           bgt t0, t1, .greater
     - Pseudo-instruction that expands to blt with swapped operands.
   * - SetFiltering
     - .. code-block:: asm

               blez t0, .skip
               sw t0, 0(t1)
               addi t1, t1, 4
           .skip:
     - Uses conditional branches to selectively store elements.
   * - SetJoin
     - .. code-block:: asm

               ; Nested loops with comparisons in assembly
     - Requires manual implementation of nested loops and equality checks.