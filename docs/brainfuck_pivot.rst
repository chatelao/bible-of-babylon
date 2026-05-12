Brainfuck Pivot View
====================

.. list-table:: Brainfuck Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - N/A
     - Brainfuck uses an implicit array of memory cells; there are no named variables.
   * - Loop
     - .. code-block:: brainfuck

           [ ... ]
     - Standard Brainfuck loop: jump past ] if current cell is zero.
   * - Increment
     - .. code-block:: brainfuck

           +
     - Increments the byte at the data pointer.
   * - Decrement
     - .. code-block:: brainfuck

           -
     - Decrements the byte at the data pointer.
   * - Print
     - .. code-block:: brainfuck

           .
     - Outputs the byte at the data pointer as an ASCII character.
   * - SingleLineComment
     - .. code-block:: brainfuck

           any text
     - All characters except '><+-.,[]' are ignored and can be used as comments.
   * - MultiLineComment
     - .. code-block:: brainfuck

           any text
     - All characters except '><+-.,[]' are ignored and can be used as comments.
   * - Addition
     - .. code-block:: brainfuck

           [->+<]
     - Typically implemented by moving the value of one cell into another using a loop.
   * - Subtraction
     - .. code-block:: brainfuck

           [->-<]
     - Typically implemented by decrementing one cell while decrementing another in a loop.
   * - ForEach
     - N/A
     - Iterating over a collection is not natively supported as there are no high-level collection types.
   * - CollectionDefinition
     - N/A
     - The entire memory is a single linear collection of cells.
   * - AssociativeArrayDefinition
     - N/A
     - Not supported natively.
   * - Equal
     - .. code-block:: brainfuck

           [->+<]>[-<+>]<[->-<]+>[<->[-]]<
     - Compares two cells for equality; requires a complex sequence of loops and temporary cells.
   * - NotEqual
     - .. code-block:: brainfuck

           [->-<]>[-<+>]<
     - Compares two cells for inequality (results in a non-zero value if not equal).
   * - GreaterThan
     - N/A
     - Requires a complex algorithm involving nested loops and multiple temporary cells.
   * - LogicalAnd
     - .. code-block:: brainfuck

           [->[->+<]<]
     - Simulated by checking if both cells are non-zero (assuming inputs are 0 or 1).
   * - LogicalOr
     - .. code-block:: brainfuck

           [->+<]>[-<+>]<
     - Simulated by checking if either cell is non-zero.
   * - LogicalXor
     - N/A
     - Typically implemented using subtraction and checking the result.
   * - ProcedureDefinition
     - N/A
     - Brainfuck does not support procedures or subroutines.
   * - FunctionDefinition
     - N/A
     - Brainfuck does not support functions.
   * - IfElse
     - .. code-block:: brainfuck

           [ ... [-]]
     - If-else is simulated by executing a loop once and zeroing the cell, or using additional flag cells.
   * - SwitchCase
     - N/A
     - Not supported natively.
   * - ForLoop
     - N/A
     - Typically implemented using a cell as a counter and a while loop [].
   * - TryCatch
     - N/A
     - No error handling mechanisms.
   * - Raise
     - N/A
     - No mechanism to raise exceptions.
   * - Thread
     - N/A
     - No native support for concurrency.
   * - SendMessage
     - N/A
     - No native messaging system.
   * - ReceiveMessage
     - N/A
     - No native messaging system.
   * - Import
     - N/A
     - Brainfuck has no module or import system.
   * - Constant
     - N/A
     - Constants are represented by repeatedly incrementing a cell.
   * - Multiplication
     - .. code-block:: brainfuck

           [->[->+>+<<]>[-<+>]<<]
     - Implemented using nested loops to add a value to a destination multiple times.
   * - Division
     - N/A
     - Highly complex to implement; requires multiple temporary cells and nested loops.
   * - Remainder
     - N/A
     - Highly complex to implement.
   * - Floor
     - N/A
     - Not applicable as Brainfuck typically operates on integers/bytes.
   * - Rounding
     - N/A
     - Not applicable.
   * - LeftShift
     - N/A
     - Bitwise operations are not natively supported.
   * - RightShift
     - N/A
     - Bitwise operations are not natively supported.
   * - BitAnd
     - N/A
     - Not supported natively.
   * - BitOr
     - N/A
     - Not supported natively.
   * - BitXor
     - N/A
     - Not supported natively.
   * - BitNot
     - N/A
     - Not supported natively.
   * - Float4VectorMultiplication
     - N/A
     - Not supported natively.
   * - Float4VectorDotProduct
     - N/A
     - Not supported natively.
   * - Float4VectorCrossProduct
     - N/A
     - Not supported natively.
   * - SetFiltering
     - N/A
     - Not supported natively.
   * - SetJoin
     - N/A
     - Not supported natively.
