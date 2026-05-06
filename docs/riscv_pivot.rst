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
   * - SwitchCase
     - .. code-block:: asm

               li t1, 1
               beq t0, t1, .case1
               li t1, 2
               beq t0, t1, .case2
               j .default
     - Typically implemented using comparison and branch instructions.
   * - Constant
     - .. code-block:: asm

           .equiv MAX, 100
     - Uses the .equiv or .set directive to define constants.