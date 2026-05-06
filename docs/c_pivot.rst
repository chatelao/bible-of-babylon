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