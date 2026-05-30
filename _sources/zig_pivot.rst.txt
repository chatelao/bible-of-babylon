Zig Pivot View
==============

.. list-table:: Zig Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: zig

           var x: i32 = 42;
     - Variables are declared with 'var' for mutable values.
   * - CollectionDefinition
     - .. code-block:: zig

           var a = [_]i32{1, 2, 3};
     - Zig uses array literals with the { } syntax; [_] infers the size.
   * - AssociativeArrayDefinition
     - .. code-block:: zig

           var map = std.AutoHashMap(i32, i32).init(allocator);
     - Zig's standard library provides HashMap types; they require an allocator for initialization.
   * - Equal
     - .. code-block:: zig

           a == b
     - Standard equality operator for primitive types.
   * - NotEqual
     - .. code-block:: zig

           a != b
     - Standard inequality operator.
   * - GreaterThan
     - .. code-block:: zig

           a > b
     - Standard comparison operator.
   * - LogicalAnd
     - .. code-block:: zig

           a and b
     - Short-circuiting logical AND.
   * - LogicalOr
     - .. code-block:: zig

           a or b
     - Short-circuiting logical OR.
   * - LogicalXor
     - .. code-block:: zig

           a != b
     - Logical XOR is achieved using inequality for booleans.
   * - ProcedureDefinition
     - .. code-block:: zig

           fn logMessage(msg: []const u8) void {
               std.debug.print("{s}\n", .{msg});
           }
     - Procedures use the 'void' return type.
   * - FunctionDefinition
     - .. code-block:: zig

           fn add(a: i32, b: i32) i32 {
               return a + b;
           }
     - Functions return a type; 'return' is required.
   * - IfElse
     - .. code-block:: zig

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard if-else statement; parentheses around the condition are required.
   * - SwitchCase
     - .. code-block:: zig

           switch (x) {
               1 => return 1,
               2 => return 2,
               else => return 0,
           }
     - Zig's switch is an expression and must be exhaustive.
   * - Loop
     - .. code-block:: zig

           while (x > 0) {
               x -= 1;
           }
     - Standard while loop.
   * - ForLoop
     - .. code-block:: zig

           for (0..10) |i| {
               // body
           }
     - Zig's for loop iterates over ranges or collections.
   * - ForEach
     - .. code-block:: zig

           for (collection) |item| {
               // body
           }
     - Zig uses the for loop to iterate over elements of an array or slice.
   * - TryCatch
     - .. code-block:: zig

           doSomething() catch |err| {
               handle(err);
           };
     - Zig uses error unions and the catch keyword for error handling.
   * - Raise
     - .. code-block:: zig

           return error.BadThing;
     - Zig uses explicit error return values from the 'error' set.
   * - Thread
     - .. code-block:: zig

           const thread = try std.Thread.spawn(.{}, doWork, .{});
           thread.join();
     - Uses std.Thread.spawn to run a function in a new thread.
   * - SendMessage
     - N/A
     - Zig does not have a native message-passing primitive; usually implemented via shared memory and synchronization.
   * - ReceiveMessage
     - N/A
     - Not supported natively.
   * - MutexDefinition
     - .. code-block:: zig

           var mutex = std.Thread.Mutex{};
     - Provides mutual exclusion.
   * - MutexLock
     - .. code-block:: zig

           mutex.lock();
     - Acquires the lock; blocks if held.
   * - MutexUnlock
     - .. code-block:: zig

           mutex.unlock();
     - Releases the lock.
   * - SemaphoreDefinition
     - .. code-block:: zig

           var sem = std.Thread.Semaphore{ .permits = 1 };
     - Initializes a semaphore with a permit count.
   * - SemaphoreWait
     - .. code-block:: zig

           sem.wait();
     - Decrements the permit count; blocks if zero.
   * - SemaphoreSignal
     - .. code-block:: zig

           sem.post();
     - Increments the permit count.
   * - SingleLineComment
     - .. code-block:: zig

           // comment
     - Standard single-line comment.
   * - MultiLineComment
     - N/A
     - Zig does not have multi-line comments; multiple single-line comments are used.
   * - Print
     - .. code-block:: zig

           std.debug.print("Hello, World!\n", .{});
     - Standard debug print; requires the std library.
   * - Import
     - .. code-block:: zig

           const std = @import("std");
     - The @import built-in function imports a package or file.
   * - Constant
     - .. code-block:: zig

           const MAX: i32 = 100;
     - Constants are declared with 'const' and are immutable.
   * - Addition
     - .. code-block:: zig

           a + b
     - Standard addition operator; Zig also has wrap-around addition with +%.
   * - Subtraction
     - .. code-block:: zig

           a - b
     - Standard subtraction operator.
   * - Multiplication
     - .. code-block:: zig

           a * b
     - Standard multiplication operator.
   * - Division
     - .. code-block:: zig

           a / b
     - Standard division operator.
   * - Remainder
     - .. code-block:: zig

           @mod(a, b)
     - Zig uses the @mod built-in for the remainder.
   * - Floor
     - .. code-block:: zig

           @floor(a)
     - Uses the @floor built-in function for floating-point values.
   * - Rounding
     - .. code-block:: zig

           @round(a)
     - Uses the @round built-in function for floating-point values.
   * - Increment
     - .. code-block:: zig

           a += 1
     - Zig does not support prefix or postfix ++ operators.
   * - Decrement
     - .. code-block:: zig

           a -= 1
     - Zig does not support -- operators.
   * - LeftShift
     - .. code-block:: zig

           a << b
     - Standard bitwise left shift.
   * - RightShift
     - .. code-block:: zig

           a >> b
     - Standard bitwise right shift.
   * - BitAnd
     - .. code-block:: zig

           a & b
     - Bitwise AND operator.
   * - BitOr
     - .. code-block:: zig

           a | b
     - Bitwise OR operator.
   * - BitXor
     - .. code-block:: zig

           a ^ b
     - Bitwise XOR operator.
   * - BitNot
     - .. code-block:: zig

           ~a
     - Bitwise NOT operator.
   * - Float4VectorMultiplication
     - .. code-block:: zig

           const c = a * b;
     - Zig supports native SIMD vector operations for @Vector types.
   * - Float4VectorDotProduct
     - .. code-block:: zig

           const dot = @reduce(.Add, a * b);
     - Uses @reduce with .Add on the element-wise product of vectors.
   * - Float4VectorCrossProduct
     - .. code-block:: zig

           const c = .{ a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0], 0.0 };
     - Manual implementation for 3D cross product of vectors.
   * - SetFiltering
     - .. code-block:: zig

           for (a) |item| { if (condition(item)) try res.append(item); }
     - Typically implemented using a loop and a conditional append to a dynamic list.
   * - SetJoin
     - .. code-block:: zig

           for (listA) |a| { for (listB) |b| { if (a.id == b.id) try res.append(.{ .a = a, .b = b }); } }
     - Implemented using nested loops for joining collections.
   * - LineContinuation
     - N/A
     - Zig treats newlines as whitespace, so explicit line continuation characters are not needed.
