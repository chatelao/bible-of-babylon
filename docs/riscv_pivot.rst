RISC-V Assembler Pivot View
===========================

.. list-table:: RISC-V Assembler Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Plus
     - Minus
     - Times
     - Divide
     - Mod
     - Increment
     - Decrement
     - Lshift
     - Rshift
     - Bit and
     - Bit or
     - Bit xor
     - Bit not
     - Bit lshift
     - Bit rshift
     - Notes
   * - VariableDeclaration
     - .. code-block:: asm

           x:  .word 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Defined in the .data section.
   * - IfElse
     - .. code-block:: asm

               blez t0, .else
               li a0, 1
               j .end
           .else:
               li a0, 0
           .end:
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses branch instructions like blez (branch if less than or equal to zero).
   * - Loop
     - .. code-block:: asm

           .loop:
               blez t0, .end
               addi t0, t0, -1
               j .loop
           .end:
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses conditional branches and jumps to implement loops.
   * - FunctionDefinition
     - .. code-block:: asm

           add:
               add a0, a0, a1
               ret
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
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
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Follows standard calling convention; must save/restore return address (ra) if calling other functions.
   * - TryCatch
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - No native try-catch; relies on return codes or trap handlers for errors.
   * - Raise
     - .. code-block:: asm

               ebreak
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The ebreak instruction triggers a debug trap; ecall can be used for system calls.
   * - Thread
     - .. code-block:: asm

               li a7, 220 # clone syscall
               ecall
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Thread creation typically involves invoking OS system calls (e.g., clone in Linux).
   * - SendMessage
     - .. code-block:: asm

               li a7, 139 # rt_sigqueueinfo
               ecall
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Inter-process/thread communication is managed by the OS.
   * - ReceiveMessage
     - .. code-block:: asm

               li a7, 128 # rt_sigtimedwait
               ecall
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Receiving signals or messages involves OS system calls.
   * - SingleLineComment
     - .. code-block:: asm

           # comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - RISC-V assembly typically uses the hash character for single-line comments.
   * - MultiLineComment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - RISC-V assembly does not have a native multi-line comment syntax.
   * - Print
     - .. code-block:: asm

               la a0, hello_msg
               call printf
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Typically uses the C library printf or writes to stdout via system calls.
   * - Import
     - .. code-block:: asm

           .include "macros.s"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the .include directive to include external source files.
   * - SwitchCase
     - .. code-block:: asm

               li t1, 1
               beq t0, t1, .case1
               li t1, 2
               beq t0, t1, .case2
               j .default
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Typically implemented using comparison and branch instructions.
   * - Constant
     - .. code-block:: asm

           .equiv MAX, 100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the .equiv or .set directive to define constants.
   * - Arithmetic
     - N/A
     - .. code-block:: asm

           add t0, t1, t2
     - .. code-block:: asm

           sub t0, t1, t2
     - .. code-block:: asm

           mul t0, t1, t2
     - .. code-block:: asm

           div t0, t1, t2
     - .. code-block:: asm

           rem t0, t1, t2
     - .. code-block:: asm

           addi t0, t0, 1
     - .. code-block:: asm

           addi t0, t0, -1
     - .. code-block:: asm

           sll t0, t1, t2
     - .. code-block:: asm

           srl t0, t1, t2
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard RISC-V M-extension instructions.
   * - Bitwise
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - .. code-block:: asm

           and t0, t1, t2
     - .. code-block:: asm

           or t0, t1, t2
     - .. code-block:: asm

           xor t0, t1, t2
     - .. code-block:: asm

           not t0, t1
     - .. code-block:: asm

           sll t0, t1, t2
     - .. code-block:: asm

           srl t0, t1, t2
     - Core bitwise logical and shift instructions.