x86 Assembler Pivot View
========================

.. list-table:: x86 Assembler Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Bit and
     - Bit or
     - Bit xor
     - Bit not
     - Bit lshift
     - Bit rshift
     - Notes
   * - VariableDeclaration
     - .. code-block:: nasm

           x   dd 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
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
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Implemented using comparison and jump instructions (Intel syntax).
   * - Loop
     - .. code-block:: nasm

           .loop:
               cmp ecx, 0
               jle .end
               dec ecx
               jmp .loop
           .end:
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Implemented using labels and conditional jumps.
   * - FunctionDefinition
     - .. code-block:: nasm

           add_func:
               add eax, ebx
               ret
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions are labels; parameters usually passed via registers or stack.
   * - ProcedureDefinition
     - .. code-block:: nasm

           log_message:
               push edx
               call printf
               add esp, 4
               ret
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Implemented as a label followed by code and a ret instruction.
   * - TryCatch
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - No high-level try-catch; requires OS-specific mechanisms like SEH.
   * - Raise
     - .. code-block:: nasm

               int 3
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Software interrupts (like int 3) can be used to signal errors or breakpoints.
   * - Thread
     - .. code-block:: nasm

               push offset do_work
               call CreateThread
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Spawning threads requires calling OS-specific APIs (e.g., Win32 CreateThread).
   * - SendMessage
     - .. code-block:: nasm

               push msg
               push thread_id
               call PostThreadMessage
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Message passing is done via OS APIs.
   * - ReceiveMessage
     - .. code-block:: nasm

               call GetMessage
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Message retrieval via OS APIs.
   * - SingleLineComment
     - .. code-block:: nasm

           ; comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Most assemblers use semicolon for single-line comments (Intel syntax).
   * - MultiLineComment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Most assemblers do not have a native multi-line comment syntax.
   * - Print
     - .. code-block:: nasm

           push offset hello_msg
           call printf
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Printing in assembler usually involves calling C library functions or OS-specific system calls.
   * - Import
     - .. code-block:: nasm

           include 'macros.inc'
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
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
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Implemented using a series of comparison and jump instructions.
   * - Constant
     - .. code-block:: nasm

           MAX equ 100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the EQU directive to define a symbolic constant (Intel syntax).
   * - Addition
     - .. code-block:: nasm

           add eax, ebx
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - Subtraction
     - .. code-block:: nasm

           sub eax, ebx
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - Multiplication
     - .. code-block:: nasm

           imul eax, ebx
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - Division
     - .. code-block:: nasm

           idiv ebx
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - Remainder
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - Floor
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - Rounding
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - Increment
     - .. code-block:: nasm

           inc eax
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - Decrement
     - .. code-block:: nasm

           dec eax
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - LeftShift
     - .. code-block:: nasm

           shl eax, cl
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - RightShift
     - .. code-block:: nasm

           shr eax, cl
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operates on registers or memory.
   * - Bitwise
     - N/A
     - .. code-block:: nasm

           and eax, ebx
     - .. code-block:: nasm

           or eax, ebx
     - .. code-block:: nasm

           xor eax, ebx
     - .. code-block:: nasm

           not eax
     - .. code-block:: nasm

           shl eax, cl
     - .. code-block:: nasm

           shr eax, cl
     - Bitwise instructions for general-purpose registers.