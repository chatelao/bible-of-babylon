Overpass Turbo Pivot View
=========================

.. list-table:: Overpass Turbo Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: text

           .setname
     - Overpass QL uses sets (prefixed with .) to store results.
   * - Equal
     - .. code-block:: text

           ["name"="Berlin"]
     - Equality is used in attribute filters.
   * - NotEqual
     - .. code-block:: text

           ["name"!="Berlin"]
     - Inequality in attribute filters.
   * - GreaterThan
     - N/A
     - Overpass QL has limited support for numeric comparisons in some implementations.
   * - ProcedureDefinition
     - N/A
     - N/A
   * - FunctionDefinition
     - N/A
     - N/A
   * - IfElse
     - .. code-block:: text

           if (condition) { ... } else { ... }
     - Control flow statements were added in recent versions of Overpass QL.
   * - SwitchCase
     - N/A
     - N/A
   * - Loop
     - .. code-block:: text

           foreach .a ( ... )
     - The foreach statement iterates over the elements of a set.
   * - ForLoop
     - .. code-block:: text

           for ( ... )
     - Overpass QL supports C-style for loops in recent versions.
   * - TryCatch
     - N/A
     - N/A
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
     - .. code-block:: text

           // comment
     - C-style single-line comments.
   * - MultiLineComment
     - .. code-block:: text

           /* comment */
     - C-style multi-line comments.
   * - Print
     - .. code-block:: text

           out;
     - The out statement produces the result of the query.
   * - Import
     - .. code-block:: text

           [out:json];
     - Settings (like output format) are specified at the beginning of the script.
   * - Constant
     - .. code-block:: text

           {{key=value}}
     - Overpass Turbo (the web interface) supports mustache-style constants.
   * - Addition
     - N/A
     - N/A
   * - Subtraction
     - N/A
     - N/A
   * - Multiplication
     - N/A
     - N/A
   * - Division
     - N/A
     - N/A
   * - Remainder
     - N/A
     - N/A
   * - Floor
     - N/A
     - N/A
   * - Rounding
     - N/A
     - N/A
   * - Increment
     - N/A
     - N/A
   * - Decrement
     - N/A
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
     - .. code-block:: text

           node["name"="Berlin"];
     - Filters elements by tags or location.
   * - SetJoin
     - .. code-block:: text

           (node(area); way(area););
     - Unions and recursion (e.g., node(w)) are used to combine sets.