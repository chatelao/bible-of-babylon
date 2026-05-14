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

           $x: Int = 42
     - Variables in GraphQL are prefixed with $ and used in operation definitions.
   * - CollectionDefinition
     - .. code-block:: graphql

           $l: [Int] = [1, 2, 3]
     - Lists in GraphQL are defined with square brackets.
   * - AssociativeArrayDefinition
     - N/A
     - GraphQL does not have a native associative array type for variables.
   * - Equal
     - N/A
     - GraphQL does not have a native equality operator in the query language itself.
   * - NotEqual
     - N/A
     - N/A
   * - ForEach
     - N/A
     - N/A
   * - GreaterThan
     - N/A
     - N/A
   * - ProcedureDefinition
     - N/A
     - GraphQL does not support procedure definitions.
   * - FunctionDefinition
     - .. code-block:: graphql

           query getUser($id: ID) {
               user(id: $id) {
                   name
               }
           }
     - Operations (query, mutation, subscription) are the closest equivalent to functions.
   * - IfElse
     - .. code-block:: graphql

           @skip(if: $condition) or @include(if: $condition)
     - Directives provide conditional inclusion of fields.
   * - SwitchCase
     - N/A
     - N/A
   * - Loop
     - N/A
     - GraphQL does not support loops in queries.
   * - ForLoop
     - N/A
     - N/A
   * - TryCatch
     - N/A
     - Errors are returned in the 'errors' field of the response.
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
     - .. code-block:: graphql

           subscription { ... }
     - Subscriptions allow receiving real-time updates.
   * - SingleLineComment
     - .. code-block:: graphql

           # comment
     - Standard GraphQL comment.
   * - MultiLineComment
     - .. code-block:: graphql

           """ comment """
     - Block strings can be used as multi-line descriptions/comments.
   * - Print
     - N/A
     - N/A
   * - Import
     - N/A
     - Schema stitching or federation is used to combine schemas.
   * - Constant
     - N/A
     - N/A
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
     - .. code-block:: graphql

           user(id: 42)
     - Filtering is typically done via field arguments.
   * - SetJoin
     - .. code-block:: graphql

           user { posts { title } }
     - Joins are expressed through nested selection sets.