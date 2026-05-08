C Pivot View
============

.. list-table:: C Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: c

           int x = 42;
     - Static typing, terminated by semicolon.
   * - IfElse
     - .. code-block:: c

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C if-else statement.
   * - Loop
     - .. code-block:: c

           while (x > 0) {
               x = x - 1;
           }
     - Standard C while loop.
   * - FunctionDefinition
     - .. code-block:: c

           int add(int a, int b) {
               return a + b;
           }
     - Standard C function with static types and curly braces.
   * - ProcedureDefinition
     - .. code-block:: c

           void log_message(const char *msg) {
               printf("%s\n", msg);
           }
     - In C, a procedure is a function with a void return type.
   * - TryCatch
     - N/A
     - C does not have native try-catch blocks; error handling is usually manual.
   * - Raise
     - .. code-block:: c

           exit(1);
     - C uses exit() or signals for severe errors.
   * - SingleLineComment
     - .. code-block:: c

           // comment
     - Standard C single-line comment.
   * - MultiLineComment
     - .. code-block:: c

           /* line 1
              line 2 */
     - Standard C multi-line comment.
   * - Print
     - .. code-block:: c

           printf("Hello, World!\n");
     - Uses the standard library's printf function; requires stdio.h.
   * - Import
     - .. code-block:: c

           #include <stdio.h>
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
     - Standard C switch statement with case labels and default.
   * - Constant
     - .. code-block:: c

           const int MAX = 100;
     - The 'const' qualifier makes the variable immutable after initialization.
   * - Addition
     - .. code-block:: c

           a + b
     - Standard C operators.
   * - Subtraction
     - .. code-block:: c

           a - b
     - Standard C operators.
   * - Multiplication
     - .. code-block:: c

           a * b
     - Standard C operators.
   * - Division
     - .. code-block:: c

           a / b
     - Standard C operators.
   * - Remainder
     - .. code-block:: c

           a % b
     - Standard C operators.
   * - Floor
     - .. code-block:: c

           floor(a)
     - Standard C operators; floor and round require math.h.
   * - Rounding
     - .. code-block:: c

           round(a)
     - Standard C operators; floor and round require math.h.
   * - Increment
     - .. code-block:: c

           a++
     - Standard C operators.
   * - Decrement
     - .. code-block:: c

           a--
     - Standard C operators.
   * - LeftShift
     - .. code-block:: c

           a << b
     - Standard C operators; floor and round require math.h.
   * - RightShift
     - .. code-block:: c

           a >> b
     - Standard C operators; floor and round require math.h.
   * - BitAnd
     - .. code-block:: c

           a & b
     - Standard bitwise operators in C.
   * - BitOr
     - .. code-block:: c

           a | b
     - Standard bitwise operators in C.
   * - BitXor
     - .. code-block:: c

           a ^ b
     - Standard bitwise operators in C.
   * - BitNot
     - .. code-block:: c

           ~a
     - Standard bitwise operators in C.
   * - Float4VectorMultiplication
     - .. code-block:: c

           for (int i = 0; i < 4; i++) c[i] = a[i] * b[i];
     - Standard C requires a loop for element-wise multiplication of arrays.
   * - Float4VectorDotProduct
     - .. code-block:: c

           float dot = 0; for (int i = 0; i < 4; i++) dot += a[i] * b[i];
     - Standard C implementation using a loop and an accumulator.
   * - Float4VectorCrossProduct
     - .. code-block:: c

           c[0] = a[1]*b[2] - a[2]*b[1];
           c[1] = a[2]*b[0] - a[0]*b[2];
           c[2] = a[0]*b[1] - a[1]*b[0];
           c[3] = 0.0f;
     - Calculated manually for the first three components.