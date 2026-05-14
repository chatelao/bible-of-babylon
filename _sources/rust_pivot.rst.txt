Rust Pivot View
===============

.. list-table:: Rust Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: rust

           let x: i32 = 42;
     - Immutable by default; supports type inference.
   * - CollectionDefinition
     - .. code-block:: rust

           let v = vec![1, 2, 3];
     - Using the vec! macro for dynamic array creation.
   * - AssociativeArrayDefinition
     - .. code-block:: rust

           let m = HashMap::from([("a", 1), ("b", 2)]);
     - Requires importing std::collections::HashMap.
   * - IfElse
     - .. code-block:: rust

           if x > 0 {
               1
           } else {
               0
           }
     - Rust if-else is an expression; parentheses around condition are not required.
   * - Loop
     - .. code-block:: rust

           while x > 0 {
               x -= 1;
           }
     - Condition does not require parentheses.
   * - SwitchCase
     - .. code-block:: rust

           match x {
               1 => 1,
               2 => 2,
               _ => 0,
           }
     - Rust uses 'match' for pattern matching, which is exhaustive.
   * - FunctionDefinition
     - .. code-block:: rust

           fn add(a: i32, b: i32) -> i32 {
               a + b
           }
     - Uses 'fn' keyword; return type preceded by '->'; last expression is returned implicitly.
   * - ProcedureDefinition
     - .. code-block:: rust

           fn log_message(msg: &str) {
               println!("{}", msg);
           }
     - Functions without a return type implicitly return the unit type ().
   * - TryCatch
     - .. code-block:: rust

           match do_something() {
               Ok(v) => v,
               Err(e) => handle(e)
           }
     - Rust uses Result type and pattern matching instead of traditional try-catch.
   * - Raise
     - .. code-block:: rust

           panic!("Error");
     - Uses 'panic!' for unrecoverable errors.
   * - Thread
     - .. code-block:: rust

           thread::spawn(|| { do_work(); });
     - Spawns a native OS thread. Closures are used for the thread body.
   * - SendMessage
     - .. code-block:: rust

           tx.send(42).unwrap();
     - Using a channel sender. Result must be handled.
   * - ReceiveMessage
     - .. code-block:: rust

           let msg = rx.recv().unwrap(); handle(msg);
     - Using a channel receiver; blocks until a message is available.
   * - MutexDefinition
     - .. code-block:: rust

           let lock = Mutex::new(0);
     - In Rust, Mutexes protect data, not just code.
   * - MutexLock
     - .. code-block:: rust

           let mut data = lock.lock().unwrap();
     - Returns a MutexGuard, which unlocks when dropped.
   * - MutexUnlock
     - .. code-block:: rust

           drop(data);
     - Explicitly dropping the guard releases the lock early.
   * - SemaphoreDefinition
     - .. code-block:: rust

           let sem = Semaphore::new(1);
     - Standard library doesn't have a semaphore; typically used from tokio::sync or similar.
   * - SemaphoreWait
     - .. code-block:: rust

           let _permit = sem.acquire().await.unwrap();
     - Async acquisition in tokio.
   * - SemaphoreSignal
     - .. code-block:: rust

           drop(_permit);
     - Permit is returned to the semaphore when dropped.
   * - SingleLineComment
     - .. code-block:: rust

           // comment
     - Standard Rust single-line comment.
   * - MultiLineComment
     - .. code-block:: rust

           /* line 1
              line 2 */
     - Supports nested multi-line comments.
   * - Print
     - .. code-block:: rust

           println!("Hello, World!");
     - Uses a macro for formatted output to standard output with a newline.
   * - Import
     - .. code-block:: rust

           use std::collections::HashMap;
     - Brings a path into scope using the 'use' keyword.
   * - Constant
     - .. code-block:: rust

           const MAX: i32 = 100;
     - Constants are always immutable and must have their types explicitly declared.
   * - Addition
     - .. code-block:: rust

           a + b
     - Operators for primitive types; floor and round are methods on float types.
   * - Subtraction
     - .. code-block:: rust

           a - b
     - Operators for primitive types; floor and round are methods on float types.
   * - Multiplication
     - .. code-block:: rust

           a * b
     - Operators for primitive types; floor and round are methods on float types.
   * - Division
     - .. code-block:: rust

           a / b
     - Operators for primitive types; floor and round are methods on float types.
   * - Remainder
     - .. code-block:: rust

           a % b
     - Operators for primitive types; floor and round are methods on float types.
   * - Floor
     - .. code-block:: rust

           a.floor()
     - Operators for primitive types; floor and round are methods on float types.
   * - Rounding
     - .. code-block:: rust

           a.round()
     - Operators for primitive types; floor and round are methods on float types.
   * - Increment
     - .. code-block:: rust

           a += 1
     - Operators for primitive types; floor and round are methods on float types.
   * - Decrement
     - .. code-block:: rust

           a -= 1
     - Operators for primitive types; floor and round are methods on float types.
   * - LeftShift
     - .. code-block:: rust

           a << b
     - Operators for primitive types; floor and round are methods on float types.
   * - RightShift
     - .. code-block:: rust

           a >> b
     - Operators for primitive types; floor and round are methods on float types.
   * - BitAnd
     - .. code-block:: rust

           a & b
     - Bitwise NOT uses the ! operator.
   * - BitOr
     - .. code-block:: rust

           a | b
     - Bitwise NOT uses the ! operator.
   * - BitXor
     - .. code-block:: rust

           a ^ b
     - Bitwise NOT uses the ! operator.
   * - BitNot
     - .. code-block:: rust

           !a
     - Bitwise NOT uses the ! operator.
   * - Float4VectorMultiplication
     - .. code-block:: rust

           for i in 0..4 { c[i] = a[i] * b[i]; }
     - Usually implemented with loops or iterator zipping; crates like nalgebra or glam provide dedicated types.
   * - Float4VectorDotProduct
     - .. code-block:: rust

           let dot: f32 = a.iter().zip(b.iter()).map(|(x, y)| x * y).sum();
     - Functional approach using iterators, zip, map, and sum.
   * - Float4VectorCrossProduct
     - .. code-block:: rust

           c[0] = a[1]*b[2] - a[2]*b[1];
           c[1] = a[2]*b[0] - a[0]*b[2];
           c[2] = a[0]*b[1] - a[1]*b[0];
           c[3] = 0.0;
     - Direct implementation; libraries like glam provide a cross() method.
   * - ForLoop
     - .. code-block:: rust

           for i in 0..10 {
               // body
           }
     - Uses ranges; 0..10 is exclusive of the upper bound.
   * - ForEach
     - .. code-block:: rust

           for item in &collection {
               // body
           }
     - Iterates over an iterator provided by the collection.
   * - LogicalAnd
     - .. code-block:: rust

           a && b
     - Short-circuiting logical AND.
   * - LogicalOr
     - .. code-block:: rust

           a || b
     - Short-circuiting logical OR.
   * - LogicalXor
     - .. code-block:: rust

           a ^ b
     - For boolean operands, ^ acts as a non-short-circuiting logical XOR.
   * - Equal
     - .. code-block:: rust

           a == b
     - Requires the PartialEq trait to be implemented.
   * - NotEqual
     - .. code-block:: rust

           a != b
     -
   * - GreaterThan
     - .. code-block:: rust

           a > b
     -
   * - SetFiltering
     - .. code-block:: rust

           let filtered: Vec<_> = v.into_iter().filter(|&x| x > 0).collect();
     - Uses iterators and the filter method.
   * - SetJoin
     - .. code-block:: rust

           list_a.iter().flat_map(|a| list_b.iter().filter(move |b| a.id == b.id).map(move |b| (a, b)));
     - Implemented using flat_map and filter.