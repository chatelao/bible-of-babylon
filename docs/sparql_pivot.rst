SPARQL Pivot View
=================

.. list-table:: SPARQL Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - ForEach
     - N/A
     - N/A
   * - VariableDeclaration
     - .. code-block:: sparql

           BIND(42 AS ?x)
     - The BIND clause assigns a value to a variable.
   * - CollectionDefinition
     - .. code-block:: sparql

           VALUES ?x { 1 2 3 }
     - VALUES can be used to define a set of values for a variable.
   * - AssociativeArrayDefinition
     - N/A
     - SPARQL does not have a native associative array type.
   * - Equal
     - .. code-block:: sparql

           FILTER(?a = ?b)
     - Equality is checked within a FILTER or BIND expression.
   * - NotEqual
     - .. code-block:: sparql

           FILTER(?a != ?b)
     - Inequality check in SPARQL.
   * - GreaterThan
     - .. code-block:: sparql

           FILTER(?a > ?b)
     - Greater than comparison in SPARQL.
   * - ProcedureDefinition
     - N/A
     - SPARQL does not support procedure definitions.
   * - FunctionDefinition
     - N/A
     - User-defined functions are implementation-dependent (e.g., via ARQ).
   * - IfElse
     - .. code-block:: sparql

           BIND(IF(?x > 0, 1, 0) AS ?res)
     - The IF function returns one of two expressions based on a condition.
   * - SwitchCase
     - .. code-block:: sparql

           COALESCE(IF(?x=1, 'one', 1/0), IF(?x=2, 'two', 1/0), 'none')
     - Multi-way branching can be simulated using nested IFs or COALESCE.
   * - Loop
     - N/A
     - SPARQL is a declarative query language and does not have loops.
   * - ForLoop
     - N/A
     - N/A
   * - TryCatch
     - N/A
     - Errors in expressions (like division by zero) result in the value being unbound.
   * - Raise
     - N/A
     - N/A
   * - Thread
     - N/A
     - N/A
   * - SendMessage
     - N/A
     - N/A
   * - ReceiveMessage
     - N/A
     - N/A
   * - SingleLineComment
     - .. code-block:: sparql

           # comment
     - SPARQL comments start with #.
   * - MultiLineComment
     - N/A
     - SPARQL does not support multi-line comments.
   * - Print
     - N/A
     - Results are returned as bindings or a graph.
   * - Import
     - .. code-block:: sparql

           PREFIX dc: <http://purl.org/dc/elements/1.1/>
     - PREFIX defines a namespace prefix.
   * - Constant
     - .. code-block:: sparql

           VALUES ?MAX { 100 }
     - VALUES can be used to provide constant values for variables.
   * - Addition
     - .. code-block:: sparql

           ?a + ?b
     - Arithmetic operators in SPARQL.
   * - Subtraction
     - .. code-block:: sparql

           ?a - ?b
     - Arithmetic operators in SPARQL.
   * - Multiplication
     - .. code-block:: sparql

           ?a * ?b
     - Arithmetic operators in SPARQL.
   * - Division
     - .. code-block:: sparql

           ?a / ?b
     - Arithmetic operators in SPARQL.
   * - Remainder
     - N/A
     - N/A
   * - Floor
     - .. code-block:: sparql

           floor(?a)
     - Standard SPARQL function.
   * - Rounding
     - .. code-block:: sparql

           round(?a)
     - Standard SPARQL function.
   * - Increment
     - .. code-block:: sparql

           ?a + 1
     - N/A
   * - Decrement
     - .. code-block:: sparql

           ?a - 1
     - N/A
   * - LeftShift
     - N/A
     - N/A
   * - RightShift
     - N/A
     - N/A
   * - BitAnd
     - N/A
     - N/A
   * - BitOr
     - N/A
     - N/A
   * - BitXor
     - N/A
     - N/A
   * - BitNot
     - N/A
     - N/A
   * - Float4VectorMultiplication
     - N/A
     - N/A
   * - Float4VectorDotProduct
     - N/A
     - N/A
   * - Float4VectorCrossProduct
     - N/A
     - N/A
   * - SetFiltering
     - .. code-block:: sparql

           FILTER(?x > 0)
     - The FILTER clause restricts the solutions.
   * - SetJoin
     - .. code-block:: sparql

           ?s ?p ?o . ?s ?p2 ?o2
     - Joins are performed by using the same variable in different triple patterns.