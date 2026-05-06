OCaml Pivot View
================

.. list-table:: Camel Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Plus
     - Minus
     - Times
     - Divide
     - Mod
     - Floor
     - Round
     - Increment
     - Decrement
     - Lshift
     - Rshift
     - Bit and
     - Bit or
     - Bit xor
     - Bit not
     - Bit lshift
     - Bit rshift
     - Notes
   * - VariableDeclaration
     - .. code-block:: ocaml

           let x = 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Immutable binding by default; type inference is used.
   * - IfElse
     - .. code-block:: ocaml

           if x > 0 then 1 else 0
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - If-then-else is an expression; both branches must return the same type.
   * - Loop
     - .. code-block:: ocaml

           while !x > 0 do
               x := !x - 1
           done
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses references for mutable state in while loops.
   * - FunctionDefinition
     - .. code-block:: ocaml

           let add a b = a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions are defined with let; parameters are space-separated.
   * - TryCatch
     - .. code-block:: ocaml

           try do_something () with e -> handle e
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the try...with construct for exception handling.
   * - Raise
     - .. code-block:: ocaml

           raise (Failure "Error")
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard way to raise an exception.
   * - Thread
     - .. code-block:: ocaml

           Thread.create do_work ()
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Requires the 'threads' library.
   * - SendMessage
     - .. code-block:: ocaml

           Event.sync (Event.send ch 42)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Synchronous communication using the Event module.
   * - ReceiveMessage
     - .. code-block:: ocaml

           let msg = Event.sync (Event.receive ch) in handle msg
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Receives a message from a channel.
   * - SingleLineComment
     - .. code-block:: ocaml

           (* comment *)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - OCaml uses (* *) for all comments.
   * - MultiLineComment
     - .. code-block:: ocaml

           (* line 1
              line 2 *)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Supports nested comments.
   * - Print
     - .. code-block:: ocaml

           print_endline "Hello, World!"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Outputs a string followed by a newline.
   * - Import
     - .. code-block:: ocaml

           open List
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Opens a module namespace.
   * - SwitchCase
     - .. code-block:: ocaml

           match x with
           | 1 -> 1
           | 2 -> 2
           | _ -> 0
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Structural pattern matching using the match expression.
   * - Constant
     - .. code-block:: ocaml

           let max = 100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Top-level let bindings are effectively constant.
   * - ProcedureDefinition
     - .. code-block:: ocaml

           let log_message msg = print_endline msg
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Procedures in OCaml return the unit type ().
   * - Arithmetic
     - N/A
     - .. code-block:: ocaml

           a + b
     - .. code-block:: ocaml

           a - b
     - .. code-block:: ocaml

           a * b
     - .. code-block:: ocaml

           a / b
     - .. code-block:: ocaml

           a mod b
     - .. code-block:: ocaml

           floor a
     - .. code-block:: ocaml

           Float.round a
     - .. code-block:: ocaml

           a + 1
     - .. code-block:: ocaml

           a - 1
     - .. code-block:: ocaml

           a lsl b
     - .. code-block:: ocaml

           a lsr b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - Bitwise
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - .. code-block:: ocaml

           a land b
     - .. code-block:: ocaml

           a lor b
     - .. code-block:: ocaml

           a lxor b
     - .. code-block:: ocaml

           lnot a
     - .. code-block:: ocaml

           a lsl b
     - .. code-block:: ocaml

           a lsr b
     - Bitwise operators are keywords.