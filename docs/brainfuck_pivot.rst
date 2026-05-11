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
