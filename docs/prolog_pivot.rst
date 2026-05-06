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