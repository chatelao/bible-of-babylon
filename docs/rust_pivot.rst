Rust Pivot View
===============

.. list-table:: Rust Pivot Table
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
     - .. code-block:: rust

           let x: i32 = 42;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Immutable by default; supports type inference.
   * - IfElse
     - .. code-block:: rust

           if x > 0 {
               1
           } else {
               0
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Rust if-else is an expression; parentheses around condition are not required.
   * - Loop
     - .. code-block:: rust

           while x > 0 {
               x -= 1;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Condition does not require parentheses.
   * - FunctionDefinition
     - .. code-block:: rust

           fn add(a: i32, b: i32) -> i32 {
               a + b
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'fn' keyword; return type preceded by '->'; last expression is returned implicitly.
   * - ProcedureDefinition
     - .. code-block:: rust

           fn log_message(msg: &str) {
               println!("{}", msg);
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions without a return type implicitly return the unit type ().
   * - TryCatch
     - .. code-block:: rust

           match do_something() {
               Ok(v) => v,
               Err(e) => handle(e)
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Rust uses Result type and pattern matching instead of traditional try-catch.
   * - Raise
     - .. code-block:: rust

           panic!("Error");
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'panic!' for unrecoverable errors.
   * - Thread
     - .. code-block:: rust

           thread::spawn(|| { do_work(); });
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Spawns a native OS thread. Closures are used for the thread body.
   * - SendMessage
     - .. code-block:: rust

           tx.send(42).unwrap();
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Using a channel sender. Result must be handled.
   * - ReceiveMessage
     - .. code-block:: rust

           let msg = rx.recv().unwrap(); handle(msg);
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Using a channel receiver; blocks until a message is available.
   * - SingleLineComment
     - .. code-block:: rust

           // comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Rust single-line comment.
   * - MultiLineComment
     - .. code-block:: rust

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Supports nested multi-line comments.
   * - Print
     - .. code-block:: rust

           println!("Hello, World!");
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses a macro for formatted output to standard output with a newline.
   * - Import
     - .. code-block:: rust

           use std::collections::HashMap;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Brings a path into scope using the 'use' keyword.
   * - SwitchCase
     - .. code-block:: rust

           match x {
               1 => 1,
               2 => 2,
               _ => 0,
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Rust uses 'match' for pattern matching, which is exhaustive.
   * - Constant
     - .. code-block:: rust

           const MAX: i32 = 100;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Constants are always immutable and must have their types explicitly declared.
   * - Addition
     - .. code-block:: rust

           a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - Subtraction
     - .. code-block:: rust

           a - b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - Multiplication
     - .. code-block:: rust

           a * b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - Division
     - .. code-block:: rust

           a / b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - Remainder
     - .. code-block:: rust

           a % b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - Floor
     - .. code-block:: rust

           a.floor()
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - Rounding
     - .. code-block:: rust

           a.round()
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - Increment
     - .. code-block:: rust

           a += 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - Decrement
     - .. code-block:: rust

           a -= 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - LeftShift
     - .. code-block:: rust

           a << b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - RightShift
     - .. code-block:: rust

           a >> b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Operators for primitive types; floor and round are methods on float types.
   * - Bitwise
     - N/A
     - .. code-block:: rust

           a & b
     - .. code-block:: rust

           a | b
     - .. code-block:: rust

           a ^ b
     - .. code-block:: rust

           !a
     - .. code-block:: rust

           a << b
     - .. code-block:: rust

           a >> b
     - Bitwise NOT uses the ! operator.