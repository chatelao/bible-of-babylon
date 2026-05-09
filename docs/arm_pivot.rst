ARM AArch64 Assembler Pivot View
================================

.. list-table:: ARM AArch64 Assembler Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: asm

           x:  .quad 42
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
     - Implemented using comparison and branch instructions (ble).
   * - SwitchCase
     - .. code-block:: asm

               cmp x0, #1
               beq .case1
               cmp x0, #2
               beq .case2
               b .default
     - Implemented using comparison and branch instructions.
   * - Loop
     - .. code-block:: asm

           .loop:
               cmp x0, #0
               ble .end
               sub x0, x0, #1
               b .loop
           .end:
     - Uses conditional branches to implement loops.
   * - FunctionDefinition
     - .. code-block:: asm

           add:
               add x0, x0, x1
               ret
     - Standard AArch64 calling convention; x0-x7 are argument registers, x0 is the return register.
   * - ProcedureDefinition
     - .. code-block:: asm

           log_message:
               stp x29, x30, [sp, -16]!
               mov x29, sp
               bl printf
               ldp x29, x30, [sp], 16
               ret
     - Uses stp/ldp to save and restore the frame pointer (x29) and link register (x30).
   * - TryCatch
     - N/A
     - No native try-catch; relies on return codes or exception levels/traps for errors.
   * - Raise
     - .. code-block:: asm

               brk #0
     - The brk instruction triggers a breakpoint exception.
   * - Thread
     - .. code-block:: asm

               mov x8, #220 // clone syscall
               svc #0
     - Thread creation typically involves invoking OS system calls (e.g., clone on Linux).
   * - SendMessage
     - .. code-block:: asm

               mov x8, #139 // rt_sigqueueinfo
               svc #0
     - Inter-process/thread communication is managed via OS system calls.
   * - ReceiveMessage
     - .. code-block:: asm

               mov x8, #128 // rt_sigtimedwait
               svc #0
     - Receiving signals or messages involves OS system calls.
   * - SingleLineComment
     - .. code-block:: asm

           // comment
     - AArch64 assembly often uses // or ; for single-line comments.
   * - MultiLineComment
     - N/A
     - AArch64 assembly does not have a native multi-line comment syntax.
   * - Print
     - .. code-block:: asm

               adrp x0, hello_msg
               add x0, x0, :lo12:hello_msg
               bl printf
     - Typically uses the C library printf; adrp/add are used for PC-relative addressing.
   * - Import
     - .. code-block:: asm

           .include "macros.s"
     - Uses the .include directive for external source files.
   * - Constant
     - .. code-block:: asm

           .equiv MAX, 100
     - Uses the .equiv directive to define constants.
   * - Addition
     - .. code-block:: asm

           add x0, x1, x2
     - Standard A64 instructions.
   * - Subtraction
     - .. code-block:: asm

           sub x0, x1, x2
     - Standard A64 instructions.
   * - Multiplication
     - .. code-block:: asm

           mul x0, x1, x2
     - Standard A64 instructions.
   * - Division
     - .. code-block:: asm

           sdiv x0, x1, x2
     - Standard A64 instructions.
   * - Remainder
     - N/A
     - Modulo is typically calculated via sdiv and msub.
   * - Floor
     - N/A
     - Standard A64 instructions.
   * - Rounding
     - N/A
     - Standard A64 instructions.
   * - Increment
     - .. code-block:: asm

           add x0, x0, #1
     - Standard A64 instructions.
   * - Decrement
     - .. code-block:: asm

           sub x0, x0, #1
     - Standard A64 instructions.
   * - LeftShift
     - .. code-block:: asm

           lsl x0, x1, x2
     - Standard A64 instructions.
   * - RightShift
     - .. code-block:: asm

           lsr x0, x1, x2
     - Standard A64 instructions.
   * - BitAnd
     - .. code-block:: asm

           and x0, x1, x2
     - Core bitwise logical and shift instructions.
   * - BitOr
     - .. code-block:: asm

           orr x0, x1, x2
     - Core bitwise logical and shift instructions.
   * - BitXor
     - .. code-block:: asm

           eor x0, x1, x2
     - Core bitwise logical and shift instructions.
   * - BitNot
     - .. code-block:: asm

           mvn x0, x1
     - Core bitwise logical and shift instructions.
   * - Float4VectorMultiplication
     - .. code-block:: asm

           fmul v0.4s, v1.4s, v2.4s
     - NEON instruction for 4-lane single-precision floating-point multiplication.
   * - Float4VectorDotProduct
     - .. code-block:: asm

           fmul v0.4s, v1.4s, v2.4s
           faddp v0.4s, v0.4s, v0.4s
           faddp s0, v0.2s
     - Uses fmul for component-wise multiplication and faddp for horizontal pairwise addition.
   * - Float4VectorCrossProduct
     - .. code-block:: asm

           fmul s2, v0.s[1], v1.s[2]
           fmls s2, v0.s[2], v1.s[1]
           fmul s3, v0.s[2], v1.s[0]
           fmls s3, v0.s[0], v1.s[2]
           fmul s4, v0.s[0], v1.s[1]
           fmls s4, v0.s[1], v1.s[0]
     - Calculated component-wise using scalar NEON instructions.
   * - ForLoop
     - .. code-block:: asm

               mov x0, #0
           .loop:
               cmp x0, #10
               b.ge .end
               ; body
               add x0, x0, #1
               b .loop
           .end:
     - Uses a register for the counter and conditional branches.
   * - Equal
     - .. code-block:: asm

           cmp x0, x1
           b.eq .equal
     -
   * - NotEqual
     - .. code-block:: asm

           cmp x0, x1
           b.ne .not_equal
     -
   * - GreaterThan
     - .. code-block:: asm

           cmp x0, x1
           b.gt .greater
     -
   * - SetFiltering
     - .. code-block:: asm

               cmp x0, #0
               b.le .skip
               str x0, [x1], #8
           .skip:
     - Uses comparison and conditional branch to skip elements.
   * - SetJoin
     - .. code-block:: asm

               ; Nested loops with comparisons
     - Requires manual implementation of nested loops and equality checks.