Go Pivot View
=============

.. list-table:: Go Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: go

           var x int = 42
     - Static typing with optional type inference.
   * - IfElse
     - .. code-block:: go

           if x > 0 {
               return 1
           } else {
               return 0
           }
     - Parentheses around condition are not required; braces are mandatory.
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
     - Switch cases do not fall through by default in Go.
   * - Loop
     - .. code-block:: go

           for x > 0 {
               x = x - 1
           }
     - Go uses 'for' for all looping constructs, including while-like loops.
   * - FunctionDefinition
     - .. code-block:: go

           func add(a int, b int) int {
               return a + b
           }
     - Functions use the 'func' keyword; return type follows the parameter list.
   * - ProcedureDefinition
     - .. code-block:: go

           func logMessage(msg string) {
               fmt.Println(msg)
           }
     - Procedures are functions with no return value.
   * - TryCatch
     - .. code-block:: go

           if err := do_something(); err != nil {
               handle(err)
           }
     - Go handles errors explicitly by returning them as values.
   * - Raise
     - .. code-block:: go

           panic("Error")
     - Uses 'panic' for unrecoverable errors.
   * - Thread
     - .. code-block:: go

           go do_work()
     - The 'go' keyword starts a new goroutine (lightweight thread).
   * - SendMessage
     - .. code-block:: go

           ch <- 42
     - Sends a value to a channel.
   * - ReceiveMessage
     - .. code-block:: go

           msg := <-ch
           handle(msg)
     - Receives a value from a channel; blocks until data is available.
   * - SingleLineComment
     - .. code-block:: go

           // comment
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: go

           /* line 1
              line 2 */
     - Standard block comment.
   * - Print
     - .. code-block:: go

           fmt.Println("Hello, World!")
     - Uses the fmt package for formatted I/O.
   * - Import
     - .. code-block:: go

           import "fmt"
     - Imports a package by its path.
   * - Constant
     - .. code-block:: go

           const MAX = 100
     - Constants are declared with the 'const' keyword.
   * - Addition
     - .. code-block:: go

           a + b
     - Standard arithmetic operators.
   * - Subtraction
     - .. code-block:: go

           a - b
     - Standard arithmetic operators.
   * - Multiplication
     - .. code-block:: go

           a * b
     - Standard arithmetic operators.
   * - Division
     - .. code-block:: go

           a / b
     - Standard arithmetic operators.
   * - Remainder
     - .. code-block:: go

           a % b
     - Standard arithmetic operators.
   * - Floor
     - .. code-block:: go

           math.Floor(a)
     - Requires the math package.
   * - Rounding
     - .. code-block:: go

           math.Round(a)
     - Requires the math package.
   * - Increment
     - .. code-block:: go

           a++
     - Go supports postfix increment as a statement, not an expression.
   * - Decrement
     - .. code-block:: go

           a--
     - Go supports postfix decrement as a statement, not an expression.
   * - LeftShift
     - .. code-block:: go

           a << b
     - Standard bitwise shift operators.
   * - RightShift
     - .. code-block:: go

           a >> b
     - Standard bitwise shift operators.
   * - BitAnd
     - .. code-block:: go

           a & b
     - Bitwise NOT is implemented using the bitwise XOR operator with no left operand.
   * - BitOr
     - .. code-block:: go

           a | b
     - Bitwise NOT is implemented using the bitwise XOR operator with no left operand.
   * - BitXor
     - .. code-block:: go

           a ^ b
     - Bitwise NOT is implemented using the bitwise XOR operator with no left operand.
   * - BitNot
     - .. code-block:: go

           ^a
     - Bitwise NOT is implemented using the bitwise XOR operator with no left operand.
   * - Float4VectorMultiplication
     - .. code-block:: go

           for i := range a { c[i] = a[i] * b[i] }
     - Iterates over the indices of the slices or arrays.
   * - Float4VectorDotProduct
     - .. code-block:: go

           dot := 0.0
           for i := range a { dot += a[i] * b[i] }
     - Standard imperative loop for accumulating the sum of products.
   * - Float4VectorCrossProduct
     - .. code-block:: go

           c := [4]float64{
               a[1]*b[2] - a[2]*b[1],
               a[2]*b[0] - a[0]*b[2],
               a[0]*b[1] - a[1]*b[0],
               0,
           }
     - Calculated using array indexing in a composite literal.
   * - ForLoop
     - .. code-block:: go

           for i := 0; i < 10; i++ {
               // body
           }
     - Go's only looping construct is 'for'.
   * - Equal
     - .. code-block:: go

           a == b
     -
   * - NotEqual
     - .. code-block:: go

           a != b
     -
   * - GreaterThan
     - .. code-block:: go

           a > b
     -
   * - SetFiltering
     - .. code-block:: go

           for _, x := range a {
               if x > 0 {
                   b = append(b, x)
               }
           }
     - Iterates and appends to a slice based on a condition.
   * - SetJoin
     - .. code-block:: go

           for _, a := range listA {
               for _, b := range listB {
                   if a.Id == b.Id {
                       res = append(res, Result{a, b})
                   }
               }
           }
     - Standard imperative nested loop join.