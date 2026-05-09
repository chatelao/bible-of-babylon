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

           node[name="Foo"]->.x;
     - Variables represent sets of OSM elements and are assigned using ->.name.
   * - SingleLineComment
     - .. code-block:: text

           // comment
     - Standard C-style single-line comment.
   * - MultiLineComment
     - .. code-block:: text

           /* line 1
              line 2 */
     - Standard C-style block comment.
   * - Print
     - .. code-block:: text

           out;
     - Outputs the contents of a set; various levels of verbosity are supported (ids, skel, body, meta).
   * - Import
     - N/A
     - Overpass QL does not have a native import mechanism.
   * - Constant
     - N/A
     - Constants are not supported natively beyond literals in filters/evaluators.
   * - Equal
     - .. code-block:: text

           t["key"] == "value"
     - Equality is used within (if:) filters or convert/make statements.
   * - NotEqual
     - .. code-block:: text

           t["key"] != "value"
     -
   * - GreaterThan
     - .. code-block:: text

           count(nodes) > 10
     -
   * - ProcedureDefinition
     - N/A
     - Not supported natively.
   * - FunctionDefinition
     - N/A
     - Not supported natively.
   * - IfElse
     - .. code-block:: text

           if (count(nodes) > 0) {
             out;
           } else {
             out count;
           }
     - Conditional execution of block statements (version 0.7.55+).
   * - SwitchCase
     - N/A
     - Not supported natively.
   * - Loop
     - .. code-block:: text

           complete { ... }
     - The complete block statement repeatedly expands a set until it stabilizes.
   * - ForLoop
     - .. code-block:: text

           foreach.a->.b { ... }
     - The foreach statement loops over the elements of a set.
   * - TryCatch
     - N/A
     - No native try-catch mechanism.
   * - Raise
     - N/A
     - No native mechanism to raise exceptions.
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
     - .. code-block:: text

           a + b
     - Used within evaluators.
   * - Subtraction
     - .. code-block:: text

           a - b
     -
   * - Multiplication
     - .. code-block:: text

           a * b
     -
   * - Division
     - .. code-block:: text

           a / b
     -
   * - Remainder
     - N/A
     - Overpass QL does not have a native modulo operator.
   * - Floor
     - N/A
     -
   * - Rounding
     - .. code-block:: text

           round(a)
     -
   * - Increment
     - .. code-block:: text

           a + 1
     - No native increment operator.
   * - Decrement
     - .. code-block:: text

           a - 1
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