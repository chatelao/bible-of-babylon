C Pivot
=======

.. list-table:: C Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Single line
     - Multi line
     - String val
     - Number val
     - Boolean val
     - Notes
   * - VariableDeclaration
     - ``int x = 42;``
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Static typing, terminated by semicolon.
   * - IfElse
     - ::

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
     - Standard C if-else statement.
   * - Loop
     - ::

           while (x > 0) {
               x = x - 1;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C while loop.
   * - FunctionDefinition
     - ::

           int add(int a, int b) {
               return a + b;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C function with static types and curly braces.
   * - TryCatch
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - C does not have native try-catch blocks; error handling is usually manual.
   * - Raise
     - ``exit(1);``
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - C uses exit() or signals for severe errors.
   * - Comment
     - N/A
     - ``// comment``
     - ::

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - Standard C comment syntax.
   * - Print
     - ``printf("Hello, World!\n");``
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the standard library's printf function; requires stdio.h.
   * - Import
     - ``#include <stdio.h>``
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C way to include header files.
