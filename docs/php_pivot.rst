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
   * - ProcedureDefinition
     - .. code-block:: php

           function log_message(string $msg): void {
               echo $msg;
           }
     - Uses the 'void' return type hint (PHP 7.1+).
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
   * - Addition
     - .. code-block:: php

           a + b
     - Standard PHP arithmetic operators.
   * - Subtraction
     - .. code-block:: php

           a - b
     - Standard PHP arithmetic operators.
   * - Multiplication
     - .. code-block:: php

           a * b
     - Standard PHP arithmetic operators.
   * - Division
     - .. code-block:: php

           a / b
     - Standard PHP arithmetic operators.
   * - Remainder
     - .. code-block:: php

           a % b
     - Standard PHP arithmetic operators.
   * - Floor
     - .. code-block:: php

           floor(a)
     - Standard PHP arithmetic operators.
   * - Rounding
     - .. code-block:: php

           round(a)
     - Standard PHP arithmetic operators.
   * - Increment
     - .. code-block:: php

           a++
     - Standard PHP arithmetic operators.
   * - Decrement
     - .. code-block:: php

           a--
     - Standard PHP arithmetic operators.
   * - LeftShift
     - .. code-block:: php

           a << b
     - Standard PHP arithmetic operators.
   * - RightShift
     - .. code-block:: php

           a >> b
     - Standard PHP arithmetic operators.
   * - BitAnd
     - .. code-block:: php

           a & b
     - Standard bitwise operators.
   * - BitOr
     - .. code-block:: php

           a | b
     - Standard bitwise operators.
   * - BitXor
     - .. code-block:: php

           a ^ b
     - Standard bitwise operators.
   * - BitNot
     - .. code-block:: php

           ~a
     - Standard bitwise operators.
   * - Float4VectorMultiplication
     - .. code-block:: php

           $c = array_map(fn($ai, $bi) => $ai * $bi, $a, $b);
     - Uses array_map with an arrow function.
   * - Float4VectorDotProduct
     - .. code-block:: php

           $dot = array_sum(array_map(fn($ai, $bi) => $ai * $bi, $a, $b));
     - Combines array_map and array_sum.
   * - Float4VectorCrossProduct
     - .. code-block:: php

           $c = [$a[1]*$b[2] - $a[2]*$b[1], $a[2]*$b[0] - $a[0]*$b[2], $a[0]*$b[1] - $a[1]*$b[0], 0.0];
     - Calculated using array indexing and the cross product formula.