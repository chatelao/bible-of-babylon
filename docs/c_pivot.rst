C Pivot View
============

.. list-table:: C Pivot Table
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
     - .. code-block:: c

           int x = 42;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Static typing, terminated by semicolon.
   * - IfElse
     - .. code-block:: c

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C if-else statement.
   * - Loop
     - .. code-block:: c

           while (x > 0) {
               x = x - 1;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C while loop.
   * - FunctionDefinition
     - .. code-block:: c

           int add(int a, int b) {
               return a + b;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C function with static types and curly braces.
   * - ProcedureDefinition
     - .. code-block:: c

           void log_message(const char *msg) {
               printf("%s\n", msg);
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - In C, a procedure is a function with a void return type.
   * - TryCatch
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - C does not have native try-catch blocks; error handling is usually manual.
   * - Raise
     - .. code-block:: c

           exit(1);
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - C uses exit() or signals for severe errors.
   * - SingleLineComment
     - .. code-block:: c

           // comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C single-line comment.
   * - MultiLineComment
     - .. code-block:: c

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C multi-line comment.
   * - Print
     - .. code-block:: c

           printf("Hello, World!\n");
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the standard library's printf function; requires stdio.h.
   * - Import
     - .. code-block:: c

           #include <stdio.h>
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C way to include header files.
   * - SwitchCase
     - .. code-block:: c

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C switch statement with case labels and default.
   * - Constant
     - .. code-block:: c

           const int MAX = 100;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The 'const' qualifier makes the variable immutable after initialization.
   * - Addition
     - .. code-block:: c

           a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - Subtraction
     - .. code-block:: c

           a - b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - Multiplication
     - .. code-block:: c

           a * b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - Division
     - .. code-block:: c

           a / b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - Remainder
     - .. code-block:: c

           a % b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - Floor
     - .. code-block:: c

           floor(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - Rounding
     - .. code-block:: c

           round(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - Increment
     - .. code-block:: c

           a++
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - Decrement
     - .. code-block:: c

           a--
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - LeftShift
     - .. code-block:: c

           a << b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - RightShift
     - .. code-block:: c

           a >> b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C operators; floor and round require math.h.
   * - Bitwise
     - N/A
     - .. code-block:: c

           a & b
     - .. code-block:: c

           a | b
     - .. code-block:: c

           a ^ b
     - .. code-block:: c

           ~a
     - .. code-block:: c

           a << b
     - .. code-block:: c

           a >> b
     - Standard bitwise operators in C.