Python Pivot View
=================

.. list-table:: Python Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Bit and
     - Bit or
     - Bit xor
     - Bit not
     - Bit lshift
     - Bit rshift
     - Notes
   * - VariableDeclaration
     - .. code-block:: python

           x = 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Dynamically typed, no explicit type declaration needed.
   * - IfElse
     - .. code-block:: python

           1 if x > 0 else 0
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses ternary expression; multi-line if-else uses colons and indentation.
   * - Loop
     - .. code-block:: python

           while x > 0: x = x - 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses colon and indentation for the body; parentheses around condition are not required.
   * - FunctionDefinition
     - .. code-block:: python

           def add(a, b):
               return a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'def' keyword; indentation defines the block.
   * - ProcedureDefinition
     - .. code-block:: python

           def log_message(msg):
               print(msg)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Procedures in Python are functions that don't return a value (implicitly return None).
   * - TryCatch
     - .. code-block:: python

           try:
               do_something()
           except Exception as e:
               handle(e)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python exception handling using try-except.
   * - Raise
     - .. code-block:: python

           raise Exception("Error")
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'raise' to trigger an exception.
   * - SingleLineComment
     - .. code-block:: python

           # comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python single-line comment.
   * - MultiLineComment
     - .. code-block:: python

           """ line 1
               line 2 """
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Multi-line comments are typically implemented using docstrings.
   * - Print
     - .. code-block:: python

           print("Hello, World!")
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The print() function adds a newline by default.
   * - Import
     - .. code-block:: python

           import math
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python import; can also use 'from ... import ...'.
   * - SwitchCase
     - .. code-block:: python

           match x:
               case 1:
                   return 1
               case 2:
                   return 2
               case _:
                   return 0
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Introduced in Python 3.10 as structural pattern matching.
   * - Constant
     - .. code-block:: python

           MAX = 100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Python does not have true constants; uppercase naming is a convention to indicate immutability.
   * - Addition
     - .. code-block:: python

           a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - Subtraction
     - .. code-block:: python

           a - b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - Multiplication
     - .. code-block:: python

           a * b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - Division
     - .. code-block:: python

           a / b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - Remainder
     - .. code-block:: python

           a % b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - Floor
     - .. code-block:: python

           math.floor(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - Rounding
     - .. code-block:: python

           round(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - Increment
     - .. code-block:: python

           a += 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - Decrement
     - .. code-block:: python

           a -= 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - LeftShift
     - .. code-block:: python

           a << b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - RightShift
     - .. code-block:: python

           a >> b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Python arithmetic operator.
   * - Bitwise
     - N/A
     - .. code-block:: python

           a & b
     - .. code-block:: python

           a | b
     - .. code-block:: python

           a ^ b
     - .. code-block:: python

           ~a
     - .. code-block:: python

           a << b
     - .. code-block:: python

           a >> b
     - Standard bitwise operators.