Prolog Pivot View
=================

.. list-table:: Prolog Pivot Table
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
     - .. code-block:: prolog

           X = 42.
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
     - Uses unification for assignment; variables must start with an uppercase letter.
   * - IfElse
     - .. code-block:: prolog

           (X > 0 -> Result = 1 ; Result = 0)
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
     - Uses the (Condition -> Then ; Else) control construct.
   * - Loop
     - .. code-block:: prolog

           loop(0) :- !.
           loop(X) :- X > 0, X1 is X - 1, loop(X1).
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
     - Prolog uses recursion and tail-call optimization for looping.
   * - FunctionDefinition
     - .. code-block:: prolog

           add(A, B, Res) :- Res is A + B.
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
     - Functions are predicates; return values are typically unified with an output argument.
   * - ProcedureDefinition
     - .. code-block:: prolog

           log_message(Msg) :- writeln(Msg).
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
     - Predicates without an output argument act as procedures.
   * - TryCatch
     - .. code-block:: prolog

           catch(do_something, E, handle(E))
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
     - Standard Prolog error handling using the catch/3 predicate.
   * - Raise
     - .. code-block:: prolog

           throw(error(Error))
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
     - Uses throw/1 to raise an exception.
   * - Thread
     - .. code-block:: prolog

           thread_create(do_work, Id, []).
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
     - Creates a new thread using thread_create/3 (ISO Prolog / SWI-Prolog).
   * - SendMessage
     - .. code-block:: prolog

           thread_send_message(Id, hello).
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
     - Sends a message to a thread's message queue.
   * - ReceiveMessage
     - .. code-block:: prolog

           thread_get_message(hello).
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
     - Retrieves a matching message from the current thread's queue.
   * - SingleLineComment
     - .. code-block:: prolog

           % comment
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
     - Standard Prolog single-line comment.
   * - MultiLineComment
     - .. code-block:: prolog

           /* line 1
              line 2 */
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
     - Standard C-style block comment.
   * - Print
     - .. code-block:: prolog

           writeln('Hello, World!').
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
     - Outputs text followed by a newline.
   * - Import
     - .. code-block:: prolog

           use_module(library(math)).
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
     - Imports predicates from a library module.
   * - SwitchCase
     - .. code-block:: prolog

           (   X = 1 -> writeln('one')
           ;   X = 2 -> writeln('two')
           ;   writeln('none')
           )
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
     - Usually implemented using nested (If -> Then ; Else) or multiple clauses.
   * - Constant
     - .. code-block:: prolog

           max(100).
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
     - Constants are represented as atomic values or facts; Prolog variables themselves are single-assignment.
   * - Arithmetic
     - N/A
     - .. code-block:: prolog

           Res is A + B
     - .. code-block:: prolog

           Res is A - B
     - .. code-block:: prolog

           Res is A * B
     - .. code-block:: prolog

           Res is A / B
     - .. code-block:: prolog

           Res is A mod B
     - .. code-block:: prolog

           Res is floor(A)
     - .. code-block:: prolog

           Res is round(A)
     - .. code-block:: prolog

           Res is A + 1
     - .. code-block:: prolog

           Res is A - 1
     - .. code-block:: prolog

           Res is A << B
     - .. code-block:: prolog

           Res is A >> B
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the 'is' operator to evaluate arithmetic expressions.
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
     - .. code-block:: prolog

           Res is A /\ B
     - .. code-block:: prolog

           Res is A \/ B
     - .. code-block:: prolog

           Res is A xor B
     - .. code-block:: prolog

           Res is \ A
     - .. code-block:: prolog

           Res is A << B
     - .. code-block:: prolog

           Res is A >> B
     - Bitwise operators within arithmetic expressions.