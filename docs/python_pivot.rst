Python Pivot View
=================

.. list-table:: Python Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: python

           x = 42
     - Dynamically typed, no explicit type declaration needed.
   * - IfElse
     - .. code-block:: python

           1 if x > 0 else 0
     - Uses ternary expression; multi-line if-else uses colons and indentation.
   * - Loop
     - .. code-block:: python

           while x > 0: x = x - 1
     - Uses colon and indentation for the body; parentheses around condition are not required.
   * - FunctionDefinition
     - .. code-block:: python

           def add(a, b):
               return a + b
     - Uses 'def' keyword; indentation defines the block.
   * - ProcedureDefinition
     - .. code-block:: python

           def log_message(msg):
               print(msg)
     - Procedures in Python are functions that don't return a value (implicitly return None).
   * - TryCatch
     - .. code-block:: python

           try:
               do_something()
           except Exception as e:
               handle(e)
     - Standard Python exception handling using try-except.
   * - Raise
     - .. code-block:: python

           raise Exception("Error")
     - Uses 'raise' to trigger an exception.
   * - SingleLineComment
     - .. code-block:: python

           # comment
     - Standard Python single-line comment.
   * - MultiLineComment
     - .. code-block:: python

           """ line 1
               line 2 """
     - Multi-line comments are typically implemented using docstrings.
   * - Print
     - .. code-block:: python

           print("Hello, World!")
     - The print() function adds a newline by default.
   * - Import
     - .. code-block:: python

           import math
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
     - Introduced in Python 3.10 as structural pattern matching.
   * - Constant
     - .. code-block:: python

           MAX = 100
     - Python does not have true constants; uppercase naming is a convention to indicate immutability.
   * - Addition
     - .. code-block:: python

           a + b
     - Standard Python arithmetic operator.
   * - Subtraction
     - .. code-block:: python

           a - b
     - Standard Python arithmetic operator.
   * - Multiplication
     - .. code-block:: python

           a * b
     - Standard Python arithmetic operator.
   * - Division
     - .. code-block:: python

           a / b
     - Standard Python arithmetic operator.
   * - Remainder
     - .. code-block:: python

           a % b
     - Standard Python arithmetic operator.
   * - Floor
     - .. code-block:: python

           math.floor(a)
     - Standard Python arithmetic operator.
   * - Rounding
     - .. code-block:: python

           round(a)
     - Standard Python arithmetic operator.
   * - Increment
     - .. code-block:: python

           a += 1
     - Standard Python arithmetic operator.
   * - Decrement
     - .. code-block:: python

           a -= 1
     - Standard Python arithmetic operator.
   * - LeftShift
     - .. code-block:: python

           a << b
     - Standard Python arithmetic operator.
   * - RightShift
     - .. code-block:: python

           a >> b
     - Standard Python arithmetic operator.
   * - BitAnd
     - .. code-block:: python

           a & b
     - Standard bitwise operators.
   * - BitOr
     - .. code-block:: python

           a | b
     - Standard bitwise operators.
   * - BitXor
     - .. code-block:: python

           a ^ b
     - Standard bitwise operators.
   * - BitNot
     - .. code-block:: python

           ~a
     - Standard bitwise operators.
   * - Float4VectorMultiplication
     - .. code-block:: python

           c = [ai * bi for ai, bi in zip(a, b)]
     - Uses list comprehension with zip; NumPy is preferred for performance.
   * - Float4VectorDotProduct
     - .. code-block:: python

           dot = sum(ai * bi for ai, bi in zip(a, b))
     - Uses a generator expression with zip and sum; NumPy's np.dot is standard for performance.
   * - Float4VectorCrossProduct
     - .. code-block:: python

           c = [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0], 0.0]
     - Uses list indexing; NumPy's np.cross is typically used for 3D vectors.