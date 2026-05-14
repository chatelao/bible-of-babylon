Tcl Pivot View
==============

.. list-table:: Tcl Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: tcl

           set x 42
     - Variables are untyped strings; set is used for assignment.
   * - CollectionDefinition
     - .. code-block:: tcl

           set l [list 1 2 3]
     - Lists are a fundamental data type in Tcl.
   * - AssociativeArrayDefinition
     - .. code-block:: tcl

           array set m {a 1 b 2}
     - Tcl supports associative arrays with the 'array' command.
   * - IfElse
     - .. code-block:: tcl

           if {$x > 0} {
               return 1
           } else {
               return 0
           }
     - Uses braces for the condition and branches.
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
     - The switch command provides multi-way branching.
   * - Loop
     - .. code-block:: tcl

           while {$x > 0} {
               set x [expr {$x - 1}]
           }
     - Standard while loop; expr is used for mathematical evaluation.
   * - FunctionDefinition
     - .. code-block:: tcl

           proc add {a b} {
               return [expr {$a + $b}]
           }
     - Procedures can return values using the return command.
   * - ProcedureDefinition
     - .. code-block:: tcl

           proc logMessage {msg} {
               puts $msg
           }
     - Uses 'proc' to define a command.
   * - TryCatch
     - .. code-block:: tcl

           try {
               do_something
           } on error {e} {
               handle $e
           }
     - The try command handles errors and exceptions (Tcl 8.6+).
   * - Raise
     - .. code-block:: tcl

           error "Error"
     - Signals an error condition.
   * - Thread
     - .. code-block:: tcl

           thread::create { do_work }
     - Requires the Thread package.
   * - SendMessage
     - .. code-block:: tcl

           thread::send $id $msg
     - Sends a message to a thread.
   * - ReceiveMessage
     - .. code-block:: tcl

           vwait msg; handle $msg
     - vwait blocks until a variable is written.
   * - SingleLineComment
     - .. code-block:: tcl

           # comment
     - Hashes start comments; must be at the beginning of a command.
   * - MultiLineComment
     - N/A
     - Tcl has no native multi-line comment syntax.
   * - Print
     - .. code-block:: tcl

           puts "Hello, World!"
     - Outputs a string to stdout followed by a newline.
   * - Import
     - .. code-block:: tcl

           package require Tcl
     - Loads a package into the interpreter.
   * - Constant
     - .. code-block:: tcl

           set MAX 100
     - Tcl does not have true constants; naming conventions are used.
   * - Addition
     - .. code-block:: tcl

           [expr {$a + $b}]
     - Math operations require the expr command.
   * - Subtraction
     - .. code-block:: tcl

           [expr {$a - $b}]
     - Math operations require the expr command.
   * - Multiplication
     - .. code-block:: tcl

           [expr {$a * $b}]
     - Math operations require the expr command.
   * - Division
     - .. code-block:: tcl

           [expr {$a / $b}]
     - Math operations require the expr command.
   * - Remainder
     - .. code-block:: tcl

           [expr {$a % $b}]
     - Math operations require the expr command.
   * - Floor
     - .. code-block:: tcl

           [expr {floor($a)}]
     - Math operations require the expr command.
   * - Rounding
     - .. code-block:: tcl

           [expr {round($a)}]
     - Math operations require the expr command.
   * - Increment
     - .. code-block:: tcl

           incr a
     - The incr command increments an integer variable.
   * - Decrement
     - .. code-block:: tcl

           incr a -1
     - The incr command can decrement if a negative value is provided.
   * - LeftShift
     - .. code-block:: tcl

           [expr {$a << $b}]
     - Math operations require the expr command.
   * - RightShift
     - .. code-block:: tcl

           [expr {$a >> $b}]
     - Math operations require the expr command.
   * - BitAnd
     - .. code-block:: tcl

           [expr {$a & $b}]
     - Math operations require the expr command.
   * - BitOr
     - .. code-block:: tcl

           [expr {$a | $b}]
     - Math operations require the expr command.
   * - BitXor
     - .. code-block:: tcl

           [expr {$a ^ $b}]
     - Math operations require the expr command.
   * - BitNot
     - .. code-block:: tcl

           [expr {~$a}]
     - Math operations require the expr command.
   * - Float4VectorMultiplication
     - .. code-block:: tcl

           foreach ai $a bi $b { lappend c [expr {$ai * $bi}] }
     - Uses a multi-variable foreach loop to zip and multiply.
   * - Float4VectorDotProduct
     - .. code-block:: tcl

           set dot 0
           foreach ai $a bi $b { set dot [expr {$dot + ($ai * $bi)}] }
     - Uses a multi-variable foreach loop to multiply and accumulate using expr.
   * - Float4VectorCrossProduct
     - .. code-block:: tcl

           set c [list [expr {[lindex $a 1]*[lindex $b 2] - [lindex $a 2]*[lindex $b 1]}] \
                       [expr {[lindex $a 2]*[lindex $b 0] - [lindex $a 0]*[lindex $b 2]}] \
                       [expr {[lindex $a 0]*[lindex $b 1] - [lindex $a 1]*[lindex $b 0]}] 0.0]
     - Uses expr and lindex for calculation.
   * - ForLoop
     - .. code-block:: tcl

           for {set i 0} {$i < 10} {incr i} {
               # body
           }
     - Standard for loop; all arguments are Tcl scripts.
   * - ForEach
     - .. code-block:: tcl

           foreach item $collection {
               # body
           }
     - The foreach command iterates over elements of one or more lists.
   * - Equal
     - .. code-block:: tcl

           [expr {$a == $b}]
     - Comparisons are performed within the expr command.
   * - NotEqual
     - .. code-block:: tcl

           [expr {$a != $b}]
     -
   * - GreaterThan
     - .. code-block:: tcl

           [expr {$a > $b}]
     -
   * - SetFiltering
     - .. code-block:: tcl

           lmap x $a {if {$x > 0} {set x} else continue}
     - The lmap command can be used for filtering by skipping elements.
   * - SetJoin
     - .. code-block:: tcl

           foreach a $listA { foreach b $listB { if {[dict get $a id] == [dict get $b id]} { lappend res [dict merge $a $b] } } }
     - Uses nested foreach loops and dict operations.