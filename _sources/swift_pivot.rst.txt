Swift Pivot View
================

.. list-table:: Swift Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: swift

           var x: Int = 42
     - Variables are declared with 'var'; supports type inference.
   * - Equal
     - .. code-block:: swift

           a == b
     - Checks for value equality.
   * - NotEqual
     - .. code-block:: swift

           a != b
     -
   * - GreaterThan
     - .. code-block:: swift

           a > b
     -
   * - ProcedureDefinition
     - .. code-block:: swift

           func logMessage(msg: String) {
               print(msg)
           }
     - Functions without a return value are effectively procedures.
   * - FunctionDefinition
     - .. code-block:: swift

           func add(a: Int, b: Int) -> Int {
               return a + b
           }
     - Uses 'func' keyword; return type is specified with '->'.
   * - IfElse
     - .. code-block:: swift

           if x > 0 {
               return 1
           } else {
               return 0
           }
     - Parentheses around condition are optional; braces are required.
   * - SwitchCase
     - .. code-block:: swift

           switch x {
           case 1:
               return 1
           case 2:
               return 2
           default:
               return 0
           }
     - Switch cases must be exhaustive and do not fall through by default.
   * - Loop
     - .. code-block:: swift

           while x > 0 {
               x -= 1
           }
     - Standard while loop; parentheses around condition are optional.
   * - ForLoop
     - .. code-block:: swift

           for i in 0..<10 {
               // body
           }
     - Uses ranges; ..< is half-open (exclusive of upper bound).
   * - TryCatch
     - .. code-block:: swift

           do {
               try doSomething()
           } catch {
               handle(error)
           }
     - Swift uses do-catch blocks for error handling; functions must be marked with 'throws'.
   * - Raise
     - .. code-block:: swift

           throw MyError.error
     - Uses 'throw' to raise an error that conforms to the Error protocol.
   * - Thread
     - .. code-block:: swift

           Thread.detachNewThread {
               doWork()
           }
     - Spawns a new thread using the Foundation Thread class.
   * - SendMessage
     - .. code-block:: swift

           await actor.handle(msg)
     - Swift actors use asynchronous method calls for communication.
   * - ReceiveMessage
     - N/A
     - Message receiving is handled implicitly by actor method execution.
   * - SingleLineComment
     - .. code-block:: swift

           // comment
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: swift

           /* line 1
              line 2 */
     - Standard block comment; supports nesting.
   * - Print
     - .. code-block:: swift

           print("Hello, World!")
     - Outputs to the console with a trailing newline.
   * - Import
     - .. code-block:: swift

           import Foundation
     - Imports a module or specific symbols from it.
   * - Constant
     - .. code-block:: swift

           let MAX = 100
     - Uses 'let' for immutable declarations.
   * - Addition
     - .. code-block:: swift

           a + b
     -
   * - Subtraction
     - .. code-block:: swift

           a - b
     -
   * - Multiplication
     - .. code-block:: swift

           a * b
     -
   * - Division
     - .. code-block:: swift

           a / b
     -
   * - Remainder
     - .. code-block:: swift

           a % b
     -
   * - Floor
     - .. code-block:: swift

           floor(a)
     - Requires Foundation.
   * - Rounding
     - .. code-block:: swift

           round(a)
     - Requires Foundation.
   * - Increment
     - .. code-block:: swift

           a += 1
     - Swift does not support unary ++.
   * - Decrement
     - .. code-block:: swift

           a -= 1
     - Swift does not support unary --.
   * - LeftShift
     - .. code-block:: swift

           a << b
     -
   * - RightShift
     - .. code-block:: swift

           a >> b
     -
   * - BitAnd
     - .. code-block:: swift

           a & b
     -
   * - BitOr
     - .. code-block:: swift

           a | b
     -
   * - BitXor
     - .. code-block:: swift

           a ^ b
     -
   * - BitNot
     - .. code-block:: swift

           ~a
     -
   * - Float4VectorMultiplication
     - .. code-block:: swift

           let c = zip(a, b).map(*)
     - Functional approach using zip and map.
   * - Float4VectorDotProduct
     - .. code-block:: swift

           let dot = zip(a, b).map(*).reduce(0, +)
     - Functional approach using zip, map, and reduce.
   * - Float4VectorCrossProduct
     - .. code-block:: swift

           let c = [
               a[1]*b[2] - a[2]*b[1],
               a[2]*b[0] - a[0]*b[2],
               a[0]*b[1] - a[1]*b[0],
               0.0
           ]
     - Manual calculation for 3D cross product.