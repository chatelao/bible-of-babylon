Prolog Pivot
============

.. list-table:: Prolog Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - ::

           X = 42.
     - Uses unification for assignment; variables must start with an uppercase letter.
   * - IfElse
     - ::

           (X > 0 -> Result = 1 ; Result = 0)
     - Uses the (Condition -> Then ; Else) control construct.
   * - Loop
     - ::

           loop(0) :- !.
           loop(X) :- X > 0, X1 is X - 1, loop(X1).
     - Prolog uses recursion and tail-call optimization for looping.
   * - FunctionDefinition
     - ::

           add(A, B, Res) :- Res is A + B.
     - Functions are predicates; return values are typically unified with an output argument.
   * - TryCatch
     - ::

           catch(do_something, E, handle(E))
     - Standard Prolog error handling using the catch/3 predicate.
   * - Raise
     - ::

           throw(error(Error))
     - Uses throw/1 to raise an exception.
   * - Thread
     - ::

           thread_create(do_work, Id, []).
     - Creates a new thread using thread_create/3 (ISO Prolog / SWI-Prolog).
   * - SendMessage
     - ::

           thread_send_message(Id, hello).
     - Sends a message to a thread's message queue.
   * - ReceiveMessage
     - ::

           thread_get_message(hello).
     - Retrieves a matching message from the current thread's queue.
   * - SingleLineComment
     - ::

           % comment
     - Standard Prolog single-line comment.
   * - MultiLineComment
     - ::

           /* line 1\n   line 2 */
     - Standard C-style block comment.
   * - Print
     - ::

           writeln('Hello, World!').
     - Outputs text followed by a newline.
   * - Import
     - ::

           use_module(library(math)).
     - Imports predicates from a library module.
   * - SwitchCase
     - ::

           (   X = 1 -> writeln('one')
           ;   X = 2 -> writeln('two')
           ;   writeln('none')
           )
     - Usually implemented using nested (If -> Then ; Else) or multiple clauses.
   * - Constant
     - ::

           max(100).
     - Constants are represented as atomic values or facts; Prolog variables themselves are single-assignment.