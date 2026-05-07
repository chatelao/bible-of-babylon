ARM AArch64 Assembler Pivot View
================================

.. list-table:: ARM AArch64 Assembler Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Plus
     - Minus
     - Times
     - Divide
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

           x:  .quad 42
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

               cmp x0, #0
               ble .else
               mov x0, #1
               b .end
           .else:
               mov x0, #0
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
     - Implemented using comparison and branch instructions (ble).
   * - Loop
     - .. code-block:: asm

           .loop:
               cmp x0, #0
               ble .end
               sub x0, x0, #1
               b .loop
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
     - Uses conditional branches to implement loops.
   * - FunctionDefinition
     - .. code-block:: asm

           add:
               add x0, x0, x1
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
     - Standard AArch64 calling convention; x0-x7 are argument registers, x0 is the return register.
   * - ProcedureDefinition
     - .. code-block:: asm

           log_message:
               stp x29, x30, [sp, -16]!
               mov x29, sp
               bl printf
               ldp x29, x30, [sp], 16
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
     - Uses stp/ldp to save and restore the frame pointer (x29) and link register (x30).
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
     - No native try-catch; relies on return codes or exception levels/traps for errors.
   * - Raise
     - .. code-block:: asm

               brk #0
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
     - The brk instruction triggers a breakpoint exception.
   * - Thread
     - .. code-block:: asm

               mov x8, #220 // clone syscall
               svc #0
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
     - Thread creation typically involves invoking OS system calls (e.g., clone on Linux).
   * - SendMessage
     - .. code-block:: asm

               mov x8, #139 // rt_sigqueueinfo
               svc #0
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
     - Inter-process/thread communication is managed via OS system calls.
   * - ReceiveMessage
     - .. code-block:: asm

               mov x8, #128 // rt_sigtimedwait
               svc #0
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

           // comment
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
     - AArch64 assembly often uses // or ; for single-line comments.
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
     - AArch64 assembly does not have a native multi-line comment syntax.
   * - Print
     - .. code-block:: asm

               adrp x0, hello_msg
               add x0, x0, :lo12:hello_msg
               bl printf
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
     - Typically uses the C library printf; adrp/add are used for PC-relative addressing.
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
     - Uses the .include directive for external source files.
   * - SwitchCase
     - .. code-block:: asm

               cmp x0, #1
               beq .case1
               cmp x0, #2
               beq .case2
               b .default
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
     - Implemented using comparison and branch instructions.
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
     - Uses the .equiv directive to define constants.
   * - Arithmetic
     - N/A
     - .. code-block:: asm

           add x0, x1, x2
     - .. code-block:: asm

           sub x0, x1, x2
     - .. code-block:: asm

           mul x0, x1, x2
     - .. code-block:: asm

           sdiv x0, x1, x2
     - .. code-block:: asm

           add x0, x0, #1
     - .. code-block:: asm

           sub x0, x0, #1
     - .. code-block:: asm

           lsl x0, x1, x2
     - .. code-block:: asm

           lsr x0, x1, x2
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard A64 instructions; modulo is typically calculated via sdiv and msub.
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
     - .. code-block:: asm

           and x0, x1, x2
     - .. code-block:: asm

           orr x0, x1, x2
     - .. code-block:: asm

           eor x0, x1, x2
     - .. code-block:: asm

           mvn x0, x1
     - .. code-block:: asm

           lsl x0, x1, x2
     - .. code-block:: asm

           lsr x0, x1, x2
     - Core bitwise logical and shift instructions.