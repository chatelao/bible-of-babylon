XQuery Pivot View
=================

.. list-table:: XQuery Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: xquery

           let $x := 42
     - XQuery uses 'let' for variable binding.
   * - IfElse
     - .. code-block:: xquery

           if ($x > 0) then 1 else 0
     - Functional if-then-else expression; both branches are required.
   * - Loop
     - .. code-block:: xquery

           for $i in 1 to $x return $i
     - XQuery uses 'for' expressions for iteration over sequences.
   * - FunctionDefinition
     - .. code-block:: xquery

           declare function local:add(
               $a as xs:integer,
               $b as xs:integer
           ) as xs:integer {
               $a + $b
           };
     - Functions must be declared in a namespace (e.g., 'local').
   * - ProcedureDefinition
     - .. code-block:: xquery

           declare function local:log-message(
               $msg as xs:string
           ) as empty-sequence() {
               (); (: side effects in XQuery are implementation-defined or via extensions :)
           };
     - XQuery functions return empty-sequence() to simulate procedures.
   * - TryCatch
     - .. code-block:: xquery

           try {
               do_something()
           } catch * {
               handle($err)
           }
     - XQuery 3.0+ supports try-catch; $err is a variable containing error information.
   * - Raise
     - .. code-block:: xquery

           fn:error(fn:QName('http://example.com/errors', 'MY_ERROR'), 'Error')
     - The fn:error() function signals a dynamic error.
   * - SingleLineComment
     - .. code-block:: xquery

           (: comment :)
     - XQuery uses (: :) for single-line comments.
   * - MultiLineComment
     - .. code-block:: xquery

           (: line 1
              line 2 :)
     - XQuery uses (: :) for multi-line comments.
   * - Print
     - .. code-block:: xquery

           "Hello, World!"
     - In XQuery, a string literal is often the result of an expression and is automatically serialized to output.
   * - Import
     - .. code-block:: xquery

           import module namespace utils = "http://example.com/utils";
     - Imports a library module by its namespace URI.
   * - SwitchCase
     - .. code-block:: xquery

           switch ($x)
             case 1 return "one"
             case 2 return "two"
             default return "none"
     - The 'switch' expression was introduced in XQuery 3.0.
   * - Constant
     - .. code-block:: xquery

           declare variable $MAX as xs:integer := 100;
     - In XQuery, variables declared in the prolog are immutable by default.
   * - Addition
     - .. code-block:: xquery

           a + b
     - Uses 'div' for division and 'idiv' for integer division.
   * - Subtraction
     - .. code-block:: xquery

           a - b
     - Uses 'div' for division and 'idiv' for integer division.
   * - Multiplication
     - .. code-block:: xquery

           a * b
     - Uses 'div' for division and 'idiv' for integer division.
   * - Division
     - .. code-block:: xquery

           a div b
     - Uses 'div' for division and 'idiv' for integer division.
   * - Remainder
     - .. code-block:: xquery

           a mod b
     - Uses 'div' for division and 'idiv' for integer division.
   * - Floor
     - .. code-block:: xquery

           floor(a)
     - Uses 'div' for division and 'idiv' for integer division.
   * - Rounding
     - .. code-block:: xquery

           round(a)
     - Uses 'div' for division and 'idiv' for integer division.
   * - Increment
     - .. code-block:: xquery

           a + 1
     - Uses 'div' for division and 'idiv' for integer division.
   * - Decrement
     - .. code-block:: xquery

           a - 1
     - Uses 'div' for division and 'idiv' for integer division.
   * - LeftShift
     - N/A
     - Uses 'div' for division and 'idiv' for integer division.
   * - RightShift
     - N/A
     - Uses 'div' for division and 'idiv' for integer division.
   * - BitAnd
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - BitOr
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - BitXor
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - BitNot
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - Float4VectorMultiplication
     - .. code-block:: xquery

           for $i in 1 to 4 return $a[$i] * $b[$i]
     - Uses a for expression to iterate over indices.
   * - Float4VectorDotProduct
     - .. code-block:: xquery

           sum(for $i in 1 to 4 return $a[$i] * $b[$i])
     - Uses the built-in sum() function over a sequence of products.
   * - Float4VectorCrossProduct
     - .. code-block:: xquery

           ($a[2]*$b[3] - $a[3]*$b[2], $a[3]*$b[1] - $a[1]*$b[3], $a[1]*$b[2] - $a[2]*$b[1], 0.0)
     - Uses sequence indexing (1-indexed).