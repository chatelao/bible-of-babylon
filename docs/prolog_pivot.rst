Prolog Pivot View
=================

.. list-table:: Prolog Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Multi line
     - String val
     - Number val
     - Boolean val
     - Notes
   * - VariableDeclaration
     - ``X = 42.``
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses unification for assignment; variables must start with an uppercase letter.
   * - IfElse
     - ``(X > 0 -> Result = 1 ; Result = 0)``
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the (Condition -> Then ; Else) control construct.
   * - Loop
     - ::

           loop(0) :- !.
           loop(X) :- X > 0, X1 is X - 1, loop(X1).
     - N/A
     - N/A
     - N/A
     - N/A
     - Prolog uses recursion and tail-call optimization for looping.
   * - FunctionDefinition
     - ``add(A, B, Res) :- Res is A + B.``
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions are predicates; return values are typically unified with an output argument.
   * - TryCatch
     - ``catch(do_something, E, handle(E))``
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Prolog error handling using the catch/3 predicate.
   * - Raise
     - ``throw(error(Error))``
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses throw/1 to raise an exception.
   * - Thread
     - ``thread_create(do_work, Id, []).``
     - N/A
     - N/A
     - N/A
     - N/A
     - Creates a new thread using thread_create/3 (ISO Prolog / SWI-Prolog).
   * - SendMessage
     - ``thread_send_message(Id, hello).``
     - N/A
     - N/A
     - N/A
     - N/A
     - Sends a message to a thread's message queue.
   * - ReceiveMessage
     - ``thread_get_message(hello).``
     - N/A
     - N/A
     - N/A
     - N/A
     - Retrieves a matching message from the current thread's queue.
   * - Comment
     - ``% comment``
     - ``/* line 1\n   line 2 */``
     - N/A
     - N/A
     - N/A
     - Uses % for single-line and /* */ for multi-line comments.
   * - Print
     - ``writeln('Hello, World!').``
     - N/A
     - N/A
     - N/A
     - N/A
     - Outputs text followed by a newline.
   * - Import
     - ``use_module(library(math)).``
     - N/A
     - N/A
     - N/A
     - N/A
     - Imports predicates from a library module.
   * - SwitchCase
     - ::

           (   X = 1 -> writeln('one')
           ;   X = 2 -> writeln('two')
           ;   writeln('none')
           )
     - N/A
     - N/A
     - N/A
     - N/A
     - Usually implemented using nested (If -> Then ; Else) or multiple clauses.
   * - Constant
     - ``max(100).``
     - N/A
     - N/A
     - N/A
     - N/A
     - Constants are represented as atomic values or facts; Prolog variables themselves are single-assignment.