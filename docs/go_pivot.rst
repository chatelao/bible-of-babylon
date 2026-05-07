Go Pivot View
=============

.. list-table:: Go Pivot Table
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
     - .. code-block:: go

           var x int = 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Static typing with optional type inference.
   * - IfElse
     - .. code-block:: go

           if x > 0 {
               return 1
           } else {
               return 0
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Parentheses around condition are not required; braces are mandatory.
   * - Loop
     - .. code-block:: go

           for x > 0 {
               x = x - 1
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Go uses 'for' for all looping constructs, including while-like loops.
   * - FunctionDefinition
     - .. code-block:: go

           func add(a int, b int) int {
               return a + b
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions use the 'func' keyword; return type follows the parameter list.
   * - ProcedureDefinition
     - .. code-block:: go

           func logMessage(msg string) {
               fmt.Println(msg)
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Procedures are functions with no return value.
   * - TryCatch
     - .. code-block:: go

           if err := do_something(); err != nil {
               handle(err)
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Go handles errors explicitly by returning them as values.
   * - Raise
     - .. code-block:: go

           panic("Error")
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'panic' for unrecoverable errors.
   * - Thread
     - .. code-block:: go

           go do_work()
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The 'go' keyword starts a new goroutine (lightweight thread).
   * - SendMessage
     - .. code-block:: go

           ch <- 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Sends a value to a channel.
   * - ReceiveMessage
     - .. code-block:: go

           msg := <-ch
           handle(msg)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Receives a value from a channel; blocks until data is available.
   * - SingleLineComment
     - .. code-block:: go

           // comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: go

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard block comment.
   * - Print
     - .. code-block:: go

           fmt.Println("Hello, World!")
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the fmt package for formatted I/O.
   * - Import
     - .. code-block:: go

           import "fmt"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Imports a package by its path.
   * - SwitchCase
     - .. code-block:: go

           switch x {
           case 1:
               return 1
           case 2:
               return 2
           default:
               return 0
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Switch cases do not fall through by default in Go.
   * - Constant
     - .. code-block:: go

           const MAX = 100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Constants are declared with the 'const' keyword.
   * - Addition
     - .. code-block:: go

           a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard arithmetic operators.
   * - Subtraction
     - .. code-block:: go

           a - b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard arithmetic operators.
   * - Multiplication
     - .. code-block:: go

           a * b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard arithmetic operators.
   * - Division
     - .. code-block:: go

           a / b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard arithmetic operators.
   * - Remainder
     - .. code-block:: go

           a % b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard arithmetic operators.
   * - Floor
     - .. code-block:: go

           math.Floor(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Requires the math package.
   * - Rounding
     - .. code-block:: go

           math.Round(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Requires the math package.
   * - Increment
     - .. code-block:: go

           a++
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Go supports postfix increment as a statement, not an expression.
   * - Decrement
     - .. code-block:: go

           a--
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Go supports postfix decrement as a statement, not an expression.
   * - LeftShift
     - .. code-block:: go

           a << b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard bitwise shift operators.
   * - RightShift
     - .. code-block:: go

           a >> b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard bitwise shift operators.
   * - Bitwise
     - N/A
     - .. code-block:: go

           a & b
     - .. code-block:: go

           a | b
     - .. code-block:: go

           a ^ b
     - .. code-block:: go

           ^a
     - .. code-block:: go

           a << b
     - .. code-block:: go

           a >> b
     - Bitwise NOT is implemented using the bitwise XOR operator with no left operand.