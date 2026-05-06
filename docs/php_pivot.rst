PHP Pivot View
==============

.. list-table:: PHP Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: php

           $x = 42;
     - Variables start with a dollar sign; dynamically typed but supports type declarations.
   * - IfElse
     - .. code-block:: php

           if ($x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C-like if-else statement.
   * - Loop
     - .. code-block:: php

           while ($x > 0) {
               $x = $x - 1;
           }
     - Standard C-like while loop.
   * - FunctionDefinition
     - .. code-block:: php

           function add(int $a, int $b): int {
               return $a + $b;
           }
     - Uses 'function' keyword; supports type hints for parameters and return values.
   * - TryCatch
     - .. code-block:: php

           try {
               do_something();
           } catch (Exception $e) {
               handle($e);
           }
     - Standard PHP exception handling using try-catch blocks.
   * - Raise
     - .. code-block:: php

           throw new Exception("Error");
     - Uses 'throw' to trigger an exception.
   * - SingleLineComment
     - .. code-block:: php

           // comment
     - Supports // and # for single-line comments.
   * - MultiLineComment
     - .. code-block:: php

           /* line 1
              line 2 */
     - Standard C-style block comments.
   * - Print
     - .. code-block:: php

           echo "Hello, World!";
     - The echo statement is used to output text.
   * - Import
     - .. code-block:: php

           require 'utils.php';
     - Uses include, require, include_once, or require_once to include other files.
   * - SwitchCase
     - .. code-block:: php

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
     - .. code-block:: php

           define('MAX', 100);
     - Constants can be defined using define() or the 'const' keyword (for class constants or global constants in modern PHP).