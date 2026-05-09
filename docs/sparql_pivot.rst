SPARQL Pivot View
=================

.. list-table:: SPARQL Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: sparql

           BIND(42 AS ?x)
     - Variables are prefixed with ? and assigned using BIND.
   * - SingleLineComment
     - .. code-block:: sparql

           # comment
     - SPARQL uses the hash character for single-line comments.
   * - MultiLineComment
     - N/A
     - SPARQL does not have a native multi-line comment syntax.
   * - Print
     - .. code-block:: sparql

           SELECT ("Hello" AS ?msg) {}
     - Output is typically achieved by projecting expressions in the SELECT clause.
   * - Import
     - .. code-block:: sparql

           PREFIX ex: <http://example.org/>
     - PREFIX defines a namespace for IRIs.
   * - Constant
     - .. code-block:: sparql

           VALUES ?MAX { 100 }
     - VALUES provides a way to bind constants to variables.
   * - Equal
     - .. code-block:: sparql

           ?a = ?b
     - Used within FILTER or BIND expressions.
   * - NotEqual
     - .. code-block:: sparql

           ?a != ?b
     -
   * - GreaterThan
     - .. code-block:: sparql

           ?a > ?b
     -
   * - ProcedureDefinition
     - N/A
     - Not supported natively.
   * - FunctionDefinition
     - N/A
     - Not supported natively.
   * - IfElse
     - .. code-block:: sparql

           BIND(IF(?x > 0, 1, 0) AS ?res)
     - The IF function provides conditional logic within expressions.
   * - SwitchCase
     - .. code-block:: sparql

           BIND(COALESCE(IF(?x=1, "one", 1/0), IF(?x=2, "two", 1/0), "none") AS ?res)
     - Can be simulated using nested IFs or COALESCE.
   * - Loop
     - N/A
     - SPARQL is a declarative query language and does not have native loops.
   * - ForLoop
     - N/A
     -
   * - TryCatch
     - .. code-block:: sparql

           COALESCE(?expression, <fallback>)
     - COALESCE can be used to handle potentially failing expressions (like errors during evaluation).
   * - Raise
     - .. code-block:: sparql

           1/0
     - Intentional division by zero can cause an expression error, often used with COALESCE or FILTER.
   * - Thread
     - N/A
     - Not supported natively.
   * - SendMessage
     - N/A
     - Not supported natively.
   * - ReceiveMessage
     - N/A
     - Not supported natively.
   * - Addition
     - .. code-block:: sparql

           ?a + ?b
     - Arithmetic operators are used in BIND or FILTER.
   * - Subtraction
     - .. code-block:: sparql

           ?a - ?b
     -
   * - Multiplication
     - .. code-block:: sparql

           ?a * ?b
     -
   * - Division
     - .. code-block:: sparql

           ?a / ?b
     -
   * - Remainder
     - N/A
     - Standard SPARQL 1.1 does not have a modulo operator.
   * - Floor
     - .. code-block:: sparql

           FLOOR(?a)
     - Standard SPARQL 1.1 functions.
   * - Rounding
     - .. code-block:: sparql

           ROUND(?a)
     - Standard SPARQL 1.1 functions.
   * - Increment
     - .. code-block:: sparql

           ?a + 1
     - No native increment operator.
   * - Decrement
     - .. code-block:: sparql

           ?a - 1
     -
   * - LeftShift
     - N/A
     - Not supported natively.
   * - RightShift
     - N/A
     -
   * - BitAnd
     - N/A
     -
   * - BitOr
     - N/A
     -
   * - BitXor
     - N/A
     -
   * - BitNot
     - N/A
     -
   * - Float4VectorMultiplication
     - N/A
     -
   * - Float4VectorDotProduct
     - N/A
     -
   * - Float4VectorCrossProduct
     - N/A
     -