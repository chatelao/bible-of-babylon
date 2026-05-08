Prolog Pivot View
=================

.. list-table:: Prolog Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: prolog

           X = 42.
     - Uses unification for assignment; variables must start with an uppercase letter.
   * - IfElse
     - .. code-block:: prolog

           (X > 0 -> Result = 1 ; Result = 0)
     - Uses the (Condition -> Then ; Else) control construct.
   * - Loop
     - .. code-block:: prolog

           loop(0) :- !.
           loop(X) :- X > 0, X1 is X - 1, loop(X1).
     - Prolog uses recursion and tail-call optimization for looping.
   * - FunctionDefinition
     - .. code-block:: prolog

           add(A, B, Res) :- Res is A + B.
     - Functions are predicates; return values are typically unified with an output argument.
   * - ProcedureDefinition
     - .. code-block:: prolog

           log_message(Msg) :- writeln(Msg).
     - Predicates without an output argument act as procedures.
   * - TryCatch
     - .. code-block:: prolog

           catch(do_something, E, handle(E))
     - Standard Prolog error handling using the catch/3 predicate.
   * - Raise
     - .. code-block:: prolog

           throw(error(Error))
     - Uses throw/1 to raise an exception.
   * - Thread
     - .. code-block:: prolog

           thread_create(do_work, Id, []).
     - Creates a new thread using thread_create/3 (ISO Prolog / SWI-Prolog).
   * - SendMessage
     - .. code-block:: prolog

           thread_send_message(Id, hello).
     - Sends a message to a thread's message queue.
   * - ReceiveMessage
     - .. code-block:: prolog

           thread_get_message(hello).
     - Retrieves a matching message from the current thread's queue.
   * - SingleLineComment
     - .. code-block:: prolog

           % comment
     - Standard Prolog single-line comment.
   * - MultiLineComment
     - .. code-block:: prolog

           /* line 1
              line 2 */
     - Standard C-style block comment.
   * - Print
     - .. code-block:: prolog

           writeln('Hello, World!').
     - Outputs text followed by a newline.
   * - Import
     - .. code-block:: prolog

           use_module(library(math)).
     - Imports predicates from a library module.
   * - SwitchCase
     - .. code-block:: prolog

           (   X = 1 -> writeln('one')
           ;   X = 2 -> writeln('two')
           ;   writeln('none')
           )
     - Usually implemented using nested (If -> Then ; Else) or multiple clauses.
   * - Constant
     - .. code-block:: prolog

           max(100).
     - Constants are represented as atomic values or facts; Prolog variables themselves are single-assignment.
   * - Addition
     - .. code-block:: prolog

           Res is A + B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - Subtraction
     - .. code-block:: prolog

           Res is A - B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - Multiplication
     - .. code-block:: prolog

           Res is A * B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - Division
     - .. code-block:: prolog

           Res is A / B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - Remainder
     - .. code-block:: prolog

           Res is A mod B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - Floor
     - .. code-block:: prolog

           Res is floor(A)
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - Rounding
     - .. code-block:: prolog

           Res is round(A)
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - Increment
     - .. code-block:: prolog

           Res is A + 1
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - Decrement
     - .. code-block:: prolog

           Res is A - 1
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - LeftShift
     - .. code-block:: prolog

           Res is A << B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - RightShift
     - .. code-block:: prolog

           Res is A >> B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - BitAnd
     - .. code-block:: prolog

           Res is A /\ B
     - Bitwise operators within arithmetic expressions.
   * - BitOr
     - .. code-block:: prolog

           Res is A \/ B
     - Bitwise operators within arithmetic expressions.
   * - BitXor
     - .. code-block:: prolog

           Res is A xor B
     - Bitwise operators within arithmetic expressions.
   * - BitNot
     - .. code-block:: prolog

           Res is \ A
     - Bitwise operators within arithmetic expressions.
   * - Float4VectorMultiplication
     - .. code-block:: prolog

           maplist(multiply, A, B, C).
     - Uses maplist to apply a predicate element-wise.
   * - Float4VectorDotProduct
     - .. code-block:: prolog

           dot_product(A, B, Dot) :- maplist(multiply, A, B, Products), sum_list(Products, Dot).
     - Commonly implemented using maplist and sum_list.
   * - Float4VectorCrossProduct
     - .. code-block:: prolog

           cross_product([A1,A2,A3|_], [B1,B2,B3|_], [C1,C2,C3,0.0]) :-
               C1 is A2*B3 - A3*B2,
               C2 is A3*B1 - A1*B3,
               C3 is A1*B2 - A2*B1.
     - Implemented using list pattern matching and arithmetic evaluation.