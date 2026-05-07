PHP Pivot View
==============

.. list-table:: PHP Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Plus
     - Minus
     - Times
     - Divide
     - Mod
     - Floor
     - Round
     - Increment
     - Decrement
     - Lshift
     - Rshift
     - Bit and
     - Bit or
     - Bit xor
     - Bit not
     - Bit lshift
     - Bit rshift
     - Notes
   * - VariableDeclaration
     - .. code-block:: php

           $x = 42;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Variables start with a dollar sign; dynamically typed but supports type declarations.
   * - IfElse
     - .. code-block:: php

           if ($x > 0) {
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
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C-like if-else statement.
   * - Loop
     - .. code-block:: php

           while ($x > 0) {
               $x = $x - 1;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C-like while loop.
   * - FunctionDefinition
     - .. code-block:: php

           function add(int $a, int $b): int {
               return $a + $b;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'function' keyword; supports type hints for parameters and return values.
   * - ProcedureDefinition
     - .. code-block:: php

           function log_message(string $msg): void {
               echo $msg;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the 'void' return type hint (PHP 7.1+).
   * - TryCatch
     - .. code-block:: php

           try {
               do_something();
           } catch (Exception $e) {
               handle($e);
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard PHP exception handling using try-catch blocks.
   * - Raise
     - .. code-block:: php

           throw new Exception("Error");
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'throw' to trigger an exception.
   * - SingleLineComment
     - .. code-block:: php

           // comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Supports // and # for single-line comments.
   * - MultiLineComment
     - .. code-block:: php

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C-style block comments.
   * - Print
     - .. code-block:: php

           echo "Hello, World!";
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The echo statement is used to output text.
   * - Import
     - .. code-block:: php

           require 'utils.php';
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
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
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C-like switch statement; match expression is also available in PHP 8.0+.
   * - Constant
     - .. code-block:: php

           define('MAX', 100);
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Constants can be defined using define() or the 'const' keyword (for class constants or global constants in modern PHP).
   * - Arithmetic
     - N/A
     - .. code-block:: php

           a + b
     - .. code-block:: php

           a - b
     - .. code-block:: php

           a * b
     - .. code-block:: php

           a / b
     - .. code-block:: php

           a % b
     - .. code-block:: php

           floor(a)
     - .. code-block:: php

           round(a)
     - .. code-block:: php

           a++
     - .. code-block:: php

           a--
     - .. code-block:: php

           a << b
     - .. code-block:: php

           a >> b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard PHP arithmetic operators.
   * - Bitwise
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - .. code-block:: php

           a & b
     - .. code-block:: php

           a | b
     - .. code-block:: php

           a ^ b
     - .. code-block:: php

           ~a
     - .. code-block:: php

           a << b
     - .. code-block:: php

           a >> b
     - Standard bitwise operators.