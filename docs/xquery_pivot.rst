XQuery Pivot
============

.. list-table:: XQuery Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Multi line
     - String val
     - Number val
     - Boolean val
     - Notes
   * - VariableDeclaration
     - ``let $x := 42``
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery uses 'let' for variable binding.
   * - IfElse
     - ``if ($x > 0) then 1 else 0``
     - N/A
     - N/A
     - N/A
     - N/A
     - Functional if-then-else expression; both branches are required.
   * - Loop
     - ``for $i in 1 to $x return $i``
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery uses 'for' expressions for iteration over sequences.
   * - FunctionDefinition
     - ::

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
     - Functions must be declared in a namespace (e.g., 'local').
   * - TryCatch
     - ::

           try {
               do_something()
           } catch * {
               handle($err)
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery 3.0+ supports try-catch; $err is a variable containing error information.
   * - Raise
     - ``fn:error(fn:QName('http://example.com/errors', 'MY_ERROR'), 'Error')``
     - N/A
     - N/A
     - N/A
     - N/A
     - The fn:error() function signals a dynamic error.
   * - SingleLineComment
     - ``(: comment :)``
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery uses (: :) for single-line comments.
   * - MultiLineComment
     - ::

           (: line 1
              line 2 :)
     - N/A
     - N/A
     - N/A
     - N/A
     - XQuery uses (: :) for multi-line comments.
   * - Print
     - ``"Hello, World!"``
     - N/A
     - N/A
     - N/A
     - N/A
     - In XQuery, a string literal is often the result of an expression and is automatically serialized to output.
   * - Import
     - ``import module namespace utils = "http://example.com/utils";``
     - N/A
     - N/A
     - N/A
     - N/A
     - Imports a library module by its namespace URI.
   * - SwitchCase
     - ::

           switch ($x)
             case 1 return "one"
             case 2 return "two"
             default return "none"
     - N/A
     - N/A
     - N/A
     - N/A
     - The 'switch' expression was introduced in XQuery 3.0.
   * - Constant
     - ``declare variable $MAX as xs:integer := 100;``
     - N/A
     - N/A
     - N/A
     - N/A
     - In XQuery, variables declared in the prolog are immutable by default.