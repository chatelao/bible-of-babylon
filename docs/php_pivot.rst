PHP Pivot
=========

.. list-table:: PHP Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - ::

           $x = 42;
     - Variables start with a dollar sign; dynamically typed but supports type declarations.
   * - IfElse
     - ::

           if ($x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C-like if-else statement.
   * - Loop
     - ::

           while ($x > 0) {
               $x = $x - 1;
           }
     - Standard C-like while loop.
   * - FunctionDefinition
     - ::

           function add(int $a, int $b): int {
               return $a + $b;
           }
     - Uses 'function' keyword; supports type hints for parameters and return values.
   * - TryCatch
     - ::

           try {
               do_something();
           } catch (Exception $e) {
               handle($e);
           }
     - Standard PHP exception handling using try-catch blocks.
   * - Raise
     - ::

           throw new Exception("Error");
     - Uses 'throw' to trigger an exception.
   * - SingleLineComment
     - ::

           // comment
     - Supports // and # for single-line comments.
   * - MultiLineComment
     - ::

           /* line 1
              line 2 */
     - Standard C-style block comments.
   * - Print
     - ::

           echo "Hello, World!";
     - The echo statement is used to output text.
   * - Import
     - ::

           require 'utils.php';
     - Uses include, require, include_once, or require_once to include other files.
   * - SwitchCase
     - ::

           switch ($x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - Standard C-like switch statement; match expression is also available in PHP 8.0+.
   * - Constant
     - ::

           define('MAX', 100);
     - Constants can be defined using define() or the 'const' keyword (for class constants or global constants in modern PHP).