x86 Assembler Pivot View
========================

.. list-table:: x86 Assembler Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: nasm

           x   dd 42
     - Defined in the .data section (Intel syntax).
   * - IfElse
     - .. code-block:: nasm

               cmp eax, 0
               jle .else
               mov eax, 1
               jmp .end
           .else:
               mov eax, 0
           .end:
     - Implemented using comparison and jump instructions (Intel syntax).
   * - Loop
     - .. code-block:: nasm

           .loop:
               cmp ecx, 0
               jle .end
               dec ecx
               jmp .loop
           .end:
     - Implemented using labels and conditional jumps.
   * - FunctionDefinition
     - .. code-block:: nasm

           add_func:
               add eax, ebx
               ret
     - Functions are labels; parameters usually passed via registers or stack.
   * - ProcedureDefinition
     - .. code-block:: nasm

           log_message:
               push edx
               call printf
               add esp, 4
               ret
     - Implemented as a label followed by code and a ret instruction.
   * - TryCatch
     - N/A
     - No high-level try-catch; requires OS-specific mechanisms like SEH.
   * - Raise
     - .. code-block:: nasm

               int 3
     - Software interrupts (like int 3) can be used to signal errors or breakpoints.
   * - Thread
     - .. code-block:: nasm

               push offset do_work
               call CreateThread
     - Spawning threads requires calling OS-specific APIs (e.g., Win32 CreateThread).
   * - SendMessage
     - .. code-block:: nasm

               push msg
               push thread_id
               call PostThreadMessage
     - Message passing is done via OS APIs.
   * - ReceiveMessage
     - .. code-block:: nasm

               call GetMessage
     - Message retrieval via OS APIs.
   * - SingleLineComment
     - .. code-block:: nasm

           ; comment
     - Most assemblers use semicolon for single-line comments (Intel syntax).
   * - MultiLineComment
     - N/A
     - Most assemblers do not have a native multi-line comment syntax.
   * - Print
     - .. code-block:: nasm

           push offset hello_msg
           call printf
     - Printing in assembler usually involves calling C library functions or OS-specific system calls.
   * - Import
     - .. code-block:: nasm

           include 'macros.inc'
     - Includes another assembly file; syntax varies by assembler (e.g., FASM uses 'include').
   * - SwitchCase
     - .. code-block:: nasm

               cmp eax, 1
               je .case1
               cmp eax, 2
               je .case2
               jmp .default
           .case1:
               ; ...
           .case2:
               ; ...
           .default:
               ; ...
     - Implemented using a series of comparison and jump instructions.
   * - Constant
     - .. code-block:: nasm

           MAX equ 100
     - Uses the EQU directive to define a symbolic constant (Intel syntax).
   * - Addition
     - .. code-block:: nasm

           add eax, ebx
     - Operates on registers or memory.
   * - Subtraction
     - .. code-block:: nasm

           sub eax, ebx
     - Operates on registers or memory.
   * - Multiplication
     - .. code-block:: nasm

           imul eax, ebx
     - Operates on registers or memory.
   * - Division
     - .. code-block:: nasm

           idiv ebx
     - Operates on registers or memory.
   * - Remainder
     - N/A
     - Operates on registers or memory.
   * - Floor
     - N/A
     - Operates on registers or memory.
   * - Rounding
     - N/A
     - Operates on registers or memory.
   * - Increment
     - .. code-block:: nasm

           inc eax
     - Operates on registers or memory.
   * - Decrement
     - .. code-block:: nasm

           dec eax
     - Operates on registers or memory.
   * - LeftShift
     - .. code-block:: nasm

           shl eax, cl
     - Operates on registers or memory.
   * - RightShift
     - .. code-block:: nasm

           shr eax, cl
     - Operates on registers or memory.
   * - BitAnd
     - .. code-block:: nasm

           and eax, ebx
     - Bitwise instructions for general-purpose registers.
   * - BitOr
     - .. code-block:: nasm

           or eax, ebx
     - Bitwise instructions for general-purpose registers.
   * - BitXor
     - .. code-block:: nasm

           xor eax, ebx
     - Bitwise instructions for general-purpose registers.
   * - BitNot
     - .. code-block:: nasm

           not eax
     - Bitwise instructions for general-purpose registers.
   * - Float4VectorMultiplication
     - .. code-block:: nasm

           mulps xmm0, xmm1
     - SSE instruction for packed single-precision floating-point multiplication (4 floats).
   * - Float4VectorDotProduct
     - .. code-block:: nasm

           dpps xmm0, xmm1, 0xF1
     - SSE4.1 instruction for Dot Product of Packed Singles. 0xF1 mask controls input/output lanes.
   * - Float4VectorCrossProduct
     - .. code-block:: nasm

           movaps xmm2, xmm0
           shufps xmm0, xmm0, 0xC9 ; y z x w
           shufps xmm2, xmm2, 0xD2 ; z x y w
           movaps xmm3, xmm1
           shufps xmm1, xmm1, 0xD2 ; z x y w
           shufps xmm3, xmm3, 0xC9 ; y z x w
           mulps xmm0, xmm1
           mulps xmm2, xmm3
           subps xmm0, xmm2
     - A common SSE sequence for 3D cross product using shuffles and multiplications.