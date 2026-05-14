Camel Pivot View
================

.. list-table:: Camel Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: ocaml

           let x = 42
     - Immutable binding by default; type inference is used.
   * - CollectionDefinition
     - .. code-block:: ocaml

           let l = [1; 2; 3]
     - Lists in OCaml use semicolons as separators and square brackets.
   * - AssociativeArrayDefinition
     - .. code-block:: ocaml

           let m = Map.empty |> Map.add "a" 1 |> Map.add "b" 2
     - OCaml's Map module provides an immutable associative structure.
   * - IfElse
     - .. code-block:: ocaml

           if x > 0 then 1 else 0
     - If-then-else is an expression; both branches must return the same type.
   * - SwitchCase
     - .. code-block:: ocaml

           match x with
           | 1 -> 1
           | 2 -> 2
           | _ -> 0
     - Structural pattern matching using the match expression.
   * - Loop
     - .. code-block:: ocaml

           while !x > 0 do
               x := !x - 1
           done
     - Uses references for mutable state in while loops.
   * - FunctionDefinition
     - .. code-block:: ocaml

           let add a b = a + b
     - Functions are defined with let; parameters are space-separated.
   * - TryCatch
     - .. code-block:: ocaml

           try do_something () with e -> handle e
     - Uses the try...with construct for exception handling.
   * - Raise
     - .. code-block:: ocaml

           raise (Failure "Error")
     - Standard way to raise an exception.
   * - Thread
     - .. code-block:: ocaml

           Thread.create do_work ()
     - Requires the 'threads' library.
   * - SendMessage
     - .. code-block:: ocaml

           Event.sync (Event.send ch 42)
     - Synchronous communication using the Event module.
   * - ReceiveMessage
     - .. code-block:: ocaml

           let msg = Event.sync (Event.receive ch) in handle msg
     - Receives a message from a channel.
   * - SingleLineComment
     - .. code-block:: ocaml

           (* comment *)
     - OCaml uses (* *) for all comments.
   * - MultiLineComment
     - .. code-block:: ocaml

           (* line 1
              line 2 *)
     - Supports nested comments.
   * - Print
     - .. code-block:: ocaml

           print_endline "Hello, World!"
     - Outputs a string followed by a newline.
   * - Import
     - .. code-block:: ocaml

           open List
     - Opens a module namespace.
   * - Constant
     - .. code-block:: ocaml

           let max = 100
     - Top-level let bindings are effectively constant.
   * - ProcedureDefinition
     - .. code-block:: ocaml

           let log_message msg = print_endline msg
     - Procedures in OCaml return the unit type ().
   * - Addition
     - .. code-block:: ocaml

           a + b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - Subtraction
     - .. code-block:: ocaml

           a - b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - Multiplication
     - .. code-block:: ocaml

           a * b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - Division
     - .. code-block:: ocaml

           a / b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - Remainder
     - .. code-block:: ocaml

           a mod b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - Floor
     - .. code-block:: ocaml

           floor a
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - Rounding
     - .. code-block:: ocaml

           Float.round a
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - Increment
     - .. code-block:: ocaml

           a + 1
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - Decrement
     - .. code-block:: ocaml

           a - 1
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - LeftShift
     - .. code-block:: ocaml

           a lsl b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - RightShift
     - .. code-block:: ocaml

           a lsr b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - BitAnd
     - .. code-block:: ocaml

           a land b
     - Bitwise operators are keywords.
   * - BitOr
     - .. code-block:: ocaml

           a lor b
     - Bitwise operators are keywords.
   * - BitXor
     - .. code-block:: ocaml

           a lxor b
     - Bitwise operators are keywords.
   * - BitNot
     - .. code-block:: ocaml

           lnot a
     - Bitwise operators are keywords.
   * - Float4VectorMultiplication
     - .. code-block:: ocaml

           Array.map2 (fun ai bi -> ai *. bi) a b
     - OCaml uses specific operators for floating-point arithmetic (*.).
   * - Float4VectorDotProduct
     - .. code-block:: ocaml

           let dot = List.fold_left2 (fun acc ai bi -> acc +. ai *. bi) 0.0 a b
     - Uses fold_left2 for efficient simultaneous iteration over two lists.
   * - Float4VectorCrossProduct
     - .. code-block:: ocaml

           [| a.(1) *. b.(2) -. a.(2) *. b.(1);
              a.(2) *. b.(0) -. a.(0) *. b.(2);
              a.(0) *. b.(1) -. a.(1) *. b.(0);
              0.0 |]
     - Uses array indexing and floating-point operators (*. and -.).
   * - ForLoop
     - .. code-block:: ocaml

           for i = 0 to 9 do
               (* body *)
           done
     - OCaml provides a simple for loop for integer ranges.
   * - ForEach
     - .. code-block:: ocaml

           List.iter (fun item -> (* body *)) collection
     - Higher-order functions like List.iter are the idiomatic way to iterate.
   * - Equal
     - .. code-block:: ocaml

           a = b
     - Structural equality; use == for physical equality (identity).
   * - NotEqual
     - .. code-block:: ocaml

           a <> b
     -
   * - GreaterThan
     - .. code-block:: ocaml

           a > b
     -
   * - SetFiltering
     - .. code-block:: ocaml

           List.filter (fun x -> x > 0) list
     - Standard library function for filtering lists.
   * - SetJoin
     - .. code-block:: ocaml

           List.concat (List.map (fun a -> List.filter (fun b -> a.id = b.id) listB |> List.map (fun b -> (a, b))) listA)
     - Uses nested map and filter operations.