GraphQL Pivot View
==================

.. list-table:: GraphQL Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: graphql

           query HeroNameAndFriends($episode: Episode) { ... }
     - Variables are prefixed with $ and defined in the operation header.
   * - SingleLineComment
     - .. code-block:: graphql

           # comment
     - GraphQL uses the hash character for single-line comments.
   * - MultiLineComment
     - N/A
     - GraphQL does not have a native multi-line comment syntax; multiple single-line comments are used.
   * - Print
     - N/A
     - GraphQL is a query language and does not have a native print statement.
   * - Import
     - N/A
     - The GraphQL core specification does not define an import mechanism.
   * - Constant
     - N/A
     - GraphQL does not support local constants within queries.
   * - Equal
     - N/A
     - Comparisons are typically handled via field arguments on the server.
   * - NotEqual
     - N/A
     -
   * - GreaterThan
     - N/A
     -
   * - ProcedureDefinition
     - N/A
     - Not supported natively.
   * - FunctionDefinition
     - N/A
     - Not supported natively.
   * - IfElse
     - .. code-block:: graphql

           @include(if: $withFriends)
     - Conditional inclusion/exclusion of fields using directives.
   * - SwitchCase
     - N/A
     - Not supported natively.
   * - Loop
     - N/A
     - GraphQL queries are non-iterative.
   * - ForLoop
     - N/A
     -
   * - TryCatch
     - N/A
     - Errors are returned in the top-level errors key of the response.
   * - Raise
     - N/A
     - Not supported natively.
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
     - N/A
     - GraphQL does not support arithmetic in the query language.
   * - Subtraction
     - N/A
     -
   * - Multiplication
     - N/A
     -
   * - Division
     - N/A
     -
   * - Remainder
     - N/A
     -
   * - Floor
     - N/A
     -
   * - Rounding
     - N/A
     -
   * - Increment
     - N/A
     -
   * - Decrement
     - N/A
     -
   * - LeftShift
     - N/A
     -
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