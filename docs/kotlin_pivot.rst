Kotlin Pivot View
=================

.. list-table:: Kotlin Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: kotlin

           var x: Int = 42
     - Variables are declared with 'var'; static typing with type inference.
   * - Equal
     - .. code-block:: kotlin

           a == b
     - Checks for structural equality; calls equals().
   * - NotEqual
     - .. code-block:: kotlin

           a != b
     -
   * - GreaterThan
     - .. code-block:: kotlin

           a > b
     -
   * - ProcedureDefinition
     - .. code-block:: kotlin

           fun logMessage(msg: String) {
               println(msg)
           }
     - Procedures return Unit, which can be omitted.
   * - FunctionDefinition
     - .. code-block:: kotlin

           fun add(a: Int, b: Int): Int {
               return a + b
           }
     - Uses 'fun' keyword; return type follows the parameter list.
   * - IfElse
     - .. code-block:: kotlin

           if (x > 0) 1 else 0
     - If-else is an expression in Kotlin.
   * - SwitchCase
     - .. code-block:: kotlin

           when (x) {
               1 -> 1
               2 -> 2
               else -> 0
           }
     - Kotlin uses 'when' instead of 'switch'.
   * - Loop
     - .. code-block:: kotlin

           while (x > 0) {
               x -= 1
           }
     - Standard while loop.
   * - ForLoop
     - .. code-block:: kotlin

           for (i in 0 until 10) {
               // body
           }
     - Iterates over a range; 'until' is exclusive of the upper bound.
   * - TryCatch
     - .. code-block:: kotlin

           try {
               doSomething()
           } catch (e: Exception) {
               handle(e)
           }
     - Standard try-catch block; similar to Java.
   * - Raise
     - .. code-block:: kotlin

           throw Exception("Error")
     - Uses 'throw' to raise an exception.
   * - Thread
     - .. code-block:: kotlin

           thread {
               doWork()
           }
     - The thread function from kotlin.concurrent easily spawns a new thread.
   * - SendMessage
     - .. code-block:: kotlin

           channel.send(42)
     - Kotlin coroutines use channels for message passing.
   * - ReceiveMessage
     - .. code-block:: kotlin

           val msg = channel.receive()
           handle(msg)
     - Receives a value from a channel; suspends until data is available.
   * - SingleLineComment
     - .. code-block:: kotlin

           // comment
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: kotlin

           /* line 1
              line 2 */
     - Standard block comment; supports nesting.
   * - Print
     - .. code-block:: kotlin

           println("Hello, World!")
     - Outputs to the console with a trailing newline.
   * - Import
     - .. code-block:: kotlin

           import kotlin.math.*
     - Imports packages or specific classes/functions.
   * - Constant
     - .. code-block:: kotlin

           const val MAX = 100
     - Uses 'const val' for compile-time constants.
   * - Addition
     - .. code-block:: kotlin

           a + b
     -
   * - Subtraction
     - .. code-block:: kotlin

           a - b
     -
   * - Multiplication
     - .. code-block:: kotlin

           a * b
     -
   * - Division
     - .. code-block:: kotlin

           a / b
     -
   * - Remainder
     - .. code-block:: kotlin

           a % b
     -
   * - Floor
     - .. code-block:: kotlin

           floor(a)
     - Requires kotlin.math.floor.
   * - Rounding
     - .. code-block:: kotlin

           round(a)
     - Requires kotlin.math.round.
   * - Increment
     - .. code-block:: kotlin

           a++
     -
   * - Decrement
     - .. code-block:: kotlin

           a--
     -
   * - LeftShift
     - .. code-block:: kotlin

           a shl b
     - Uses infix function 'shl'.
   * - RightShift
     - .. code-block:: kotlin

           a shr b
     - Uses infix function 'shr'.
   * - BitAnd
     - .. code-block:: kotlin

           a and b
     - Uses infix function 'and'.
   * - BitOr
     - .. code-block:: kotlin

           a or b
     - Uses infix function 'or'.
   * - BitXor
     - .. code-block:: kotlin

           a xor b
     - Uses infix function 'xor'.
   * - BitNot
     - .. code-block:: kotlin

           a.inv()
     - Uses 'inv()' method.
   * - Float4VectorMultiplication
     - .. code-block:: kotlin

           val c = a.zip(b) { ai, bi -> ai * bi }
     - Uses zip with a transformation lambda.
   * - Float4VectorDotProduct
     - .. code-block:: kotlin

           val dot = a.zip(b) { ai, bi -> ai * bi }.sum()
     - Uses zip followed by sum.
   * - Float4VectorCrossProduct
     - .. code-block:: kotlin

           val c = floatArrayOf(
               a[1]*b[2] - a[2]*b[1],
               a[2]*b[0] - a[0]*b[2],
               a[0]*b[1] - a[1]*b[0],
               0.0f
           )
     - Manual calculation for 3D cross product.