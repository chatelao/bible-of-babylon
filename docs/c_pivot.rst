C Pivot
=======

.. list-table:: C Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - ::

           int x = 42;
     - Static typing, terminated by semicolon.
   * - IfElse
     - ::

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C if-else statement.
   * - Loop
     - ::

           while (x > 0) {
               x = x - 1;
           }
     - Standard C while loop.
   * - FunctionDefinition
     - ::

           int add(int a, int b) {
               return a + b;
           }
     - Standard C function with static types and curly braces.
   * - TryCatch
     - N/A
     - C does not have native try-catch blocks; error handling is usually manual.
   * - Raise
     - ::

           exit(1);
     - C uses exit() or signals for severe errors.
   * - SingleLineComment
     - ::

           // comment
     - Standard C single-line comment.
   * - MultiLineComment
     - ::

           /* line 1
              line 2 */
     - Standard C multi-line comment.
   * - Print
     - ::

           printf("Hello, World!\n");
     - Uses the standard library's printf function; requires stdio.h.
   * - Import
     - ::

           #include <stdio.h>
     - Standard C way to include header files.
   * - SwitchCase
     - ::

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
     - ::

           const int MAX = 100;
     - The 'const' qualifier makes the variable immutable after initialization.