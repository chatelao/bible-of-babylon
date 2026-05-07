XQuery Pivot View
=================

.. list-table:: XQuery Pivot Table
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
     - Notes
   * - VariableDeclaration
     - .. code-block:: xquery

           let $x := 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery uses 'let' for variable binding.
   * - IfElse
     - .. code-block:: xquery

           if ($x > 0) then 1 else 0
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functional if-then-else expression; both branches are required.
   * - Loop
     - .. code-block:: xquery

           for $i in 1 to $x return $i
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery uses 'for' expressions for iteration over sequences.
   * - FunctionDefinition
     - .. code-block:: xquery

           declare function local:add(
               $a as xs:integer,
               $b as xs:integer
           ) as xs:integer {
               $a + $b
           };
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions must be declared in a namespace (e.g., 'local').
   * - ProcedureDefinition
     - .. code-block:: xquery

           declare function local:log-message(
               $msg as xs:string
           ) as empty-sequence() {
               (); (: side effects in XQuery are implementation-defined or via extensions :)
           };
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery functions return empty-sequence() to simulate procedures.
   * - TryCatch
     - .. code-block:: xquery

           try {
               do_something()
           } catch * {
               handle($err)
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
     - XQuery 3.0+ supports try-catch; $err is a variable containing error information.
   * - Raise
     - .. code-block:: xquery

           fn:error(fn:QName('http://example.com/errors', 'MY_ERROR'), 'Error')
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The fn:error() function signals a dynamic error.
   * - SingleLineComment
     - .. code-block:: xquery

           (: comment :)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery uses (: :) for single-line comments.
   * - MultiLineComment
     - .. code-block:: xquery

           (: line 1
              line 2 :)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery uses (: :) for multi-line comments.
   * - Print
     - .. code-block:: xquery

           "Hello, World!"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - In XQuery, a string literal is often the result of an expression and is automatically serialized to output.
   * - Import
     - .. code-block:: xquery

           import module namespace utils = "http://example.com/utils";
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Imports a library module by its namespace URI.
   * - SwitchCase
     - .. code-block:: xquery

           switch ($x)
             case 1 return "one"
             case 2 return "two"
             default return "none"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The 'switch' expression was introduced in XQuery 3.0.
   * - Constant
     - .. code-block:: xquery

           declare variable $MAX as xs:integer := 100;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - In XQuery, variables declared in the prolog are immutable by default.
   * - Arithmetic
     - N/A
     - .. code-block:: xquery

           a + b
     - .. code-block:: xquery

           a - b
     - .. code-block:: xquery

           a * b
     - .. code-block:: xquery

           a div b
     - .. code-block:: xquery

           a mod b
     - .. code-block:: xquery

           floor(a)
     - .. code-block:: xquery

           round(a)
     - .. code-block:: xquery

           a + 1
     - .. code-block:: xquery

           a - 1
     - Uses 'div' for division and 'idiv' for integer division.
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
     - Standard XQuery does not have native bitwise operators.