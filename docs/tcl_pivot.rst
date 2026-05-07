Tcl Pivot View
==============

.. list-table:: Tcl Pivot Table
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
     - .. code-block:: tcl

           set x 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Variables are untyped strings; set is used for assignment.
   * - IfElse
     - .. code-block:: tcl

           if {$x > 0} {
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
     - Uses braces for the condition and branches.
   * - Loop
     - .. code-block:: tcl

           while {$x > 0} {
               set x [expr {$x - 1}]
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard while loop; expr is used for mathematical evaluation.
   * - FunctionDefinition
     - .. code-block:: tcl

           proc add {a b} {
               return [expr {$a + $b}]
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Procedures can return values using the return command.
   * - ProcedureDefinition
     - .. code-block:: tcl

           proc logMessage {msg} {
               puts $msg
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'proc' to define a command.
   * - TryCatch
     - .. code-block:: tcl

           try {
               do_something
           } on error {e} {
               handle $e
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The try command handles errors and exceptions (Tcl 8.6+).
   * - Raise
     - .. code-block:: tcl

           error "Error"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Signals an error condition.
   * - Thread
     - .. code-block:: tcl

           thread::create { do_work }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Requires the Thread package.
   * - SendMessage
     - .. code-block:: tcl

           thread::send $id $msg
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Sends a message to a thread.
   * - ReceiveMessage
     - .. code-block:: tcl

           vwait msg; handle $msg
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - vwait blocks until a variable is written.
   * - SingleLineComment
     - .. code-block:: tcl

           # comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Hashes start comments; must be at the beginning of a command.
   * - MultiLineComment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Tcl has no native multi-line comment syntax.
   * - Print
     - .. code-block:: tcl

           puts "Hello, World!"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Outputs a string to stdout followed by a newline.
   * - Import
     - .. code-block:: tcl

           package require Tcl
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Loads a package into the interpreter.
   * - SwitchCase
     - .. code-block:: tcl

           switch $x {
               1 {
                   return 1
               }
               2 {
                   return 2
               }
               default {
                   return 0
               }
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The switch command provides multi-way branching.
   * - Constant
     - .. code-block:: tcl

           set MAX 100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Tcl does not have true constants; naming conventions are used.
   * - Addition
     - .. code-block:: tcl

           [expr {$a + $b}]
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Math operations require the expr command.
   * - Subtraction
     - .. code-block:: tcl

           [expr {$a - $b}]
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Math operations require the expr command.
   * - Multiplication
     - .. code-block:: tcl

           [expr {$a * $b}]
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Math operations require the expr command.
   * - Division
     - .. code-block:: tcl

           [expr {$a / $b}]
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Math operations require the expr command.
   * - Remainder
     - .. code-block:: tcl

           [expr {$a % $b}]
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Math operations require the expr command.
   * - Floor
     - .. code-block:: tcl

           [expr {floor($a)}]
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Math operations require the expr command.
   * - Rounding
     - .. code-block:: tcl

           [expr {round($a)}]
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Math operations require the expr command.
   * - Increment
     - .. code-block:: tcl

           incr a
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The incr command increments an integer variable.
   * - Decrement
     - .. code-block:: tcl

           incr a -1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The incr command can decrement if a negative value is provided.
   * - LeftShift
     - .. code-block:: tcl

           [expr {$a << $b}]
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Math operations require the expr command.
   * - RightShift
     - .. code-block:: tcl

           [expr {$a >> $b}]
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Math operations require the expr command.
   * - Bitwise
     - N/A
     - .. code-block:: tcl

           [expr {$a & $b}]
     - .. code-block:: tcl

           [expr {$a | $b}]
     - .. code-block:: tcl

           [expr {$a ^ $b}]
     - .. code-block:: tcl

           [expr {~$a}]
     - .. code-block:: tcl

           [expr {$a << $b}]
     - .. code-block:: tcl

           [expr {$a >> $b}]
     - Math operations require the expr command.