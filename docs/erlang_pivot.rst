Erlang Pivot View
=================

.. list-table:: Erlang Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: erlang

           X = 42.
     - Single assignment; must start with an uppercase letter.
   * - CollectionDefinition
     - .. code-block:: erlang

           L = [1, 2, 3].
     - Lists are the standard linked-list structure in Erlang.
   * - AssociativeArrayDefinition
     - .. code-block:: erlang

           M = #{a => 1, b => 2}.
     - Maps are used for key-value pairs in Erlang.
   * - SwitchCase
     - .. code-block:: erlang

           case X of
               1 -> one;
               2 -> two;
               _ -> none
           end
     - Uses 'case' for pattern matching; _ is the catch-all pattern.
   * - IfElse
     - .. code-block:: erlang

           if X > 0 -> 1; true -> 0 end
     - Erlang 'if' uses guards; 'true' acts as an 'else' branch.
   * - Loop
     - .. code-block:: erlang

           loop(0) -> ok; loop(X) when X > 0 -> loop(X - 1).
     - Erlang uses recursion for looping; there are no built-in while/for loops.
   * - FunctionDefinition
     - .. code-block:: erlang

           add(A, B) -> A + B.
     - Erlang functions use pattern matching on arguments; the last expression's value is returned.
   * - ProcedureDefinition
     - .. code-block:: erlang

           log_message(Msg) ->
               io:format("~p~n", [Msg]).
     - In Erlang, every function returns a value; 'ok' is commonly used for procedures.
   * - TryCatch
     - .. code-block:: erlang

           try
               do_something()
           catch
               error:Reason -> handle(Reason)
           end
     - Erlang uses try...catch blocks; the type can be throw, error, or exit (defaulting to throw if omitted).
   * - Raise
     - .. code-block:: erlang

           error("Error")
     - The error/1 BIF is used to stop execution and provide a stack trace.
   * - Thread
     - .. code-block:: erlang

           Pid = spawn(fun() -> do_work() end).
     - Creates a new process (lightweight thread) and returns its PID.
   * - SendMessage
     - .. code-block:: erlang

           Pid ! hello.
     - Asynchronous message passing using the ! operator.
   * - ReceiveMessage
     - .. code-block:: erlang

           receive hello -> handle_hello() end.
     - Selective receive; blocks until a matching message is in the mailbox.
   * - SingleLineComment
     - .. code-block:: erlang

           % comment
     - Erlang only supports single-line comments starting with %.
   * - MultiLineComment
     - N/A
     - Erlang does not have a native multi-line comment syntax.
   * - Print
     - .. code-block:: erlang

           io:format("Hello, World!~n").
     - The io:format function is used for formatted output; ~n is the newline sequence.
   * - Import
     - .. code-block:: erlang

           -include("header.hrl").
     - Includes header files; module functions are typically called using Module:Function syntax.
   * - Constant
     - .. code-block:: erlang

           -define(MAX, 100).
     - Uses preprocessor macros to define constants; replaced at compile time.
   * - Addition
     - .. code-block:: erlang

           A + B
     - Standard Erlang arithmetic operator.
   * - Subtraction
     - .. code-block:: erlang

           A - B
     - Standard Erlang arithmetic operator.
   * - Multiplication
     - .. code-block:: erlang

           A * B
     - Standard Erlang arithmetic operator.
   * - Division
     - .. code-block:: erlang

           A / B
     - Standard Erlang arithmetic operator.
   * - Remainder
     - .. code-block:: erlang

           A rem B
     - Standard Erlang arithmetic operator.
   * - Floor
     - .. code-block:: erlang

           floor(A)
     - Standard Erlang arithmetic operator.
   * - Rounding
     - .. code-block:: erlang

           round(A)
     - Standard Erlang arithmetic operator.
   * - Increment
     - .. code-block:: erlang

           A + 1
     - Standard Erlang arithmetic operator.
   * - Decrement
     - .. code-block:: erlang

           A - 1
     - Standard Erlang arithmetic operator.
   * - LeftShift
     - .. code-block:: erlang

           A bsl B
     - Standard Erlang arithmetic operator.
   * - RightShift
     - .. code-block:: erlang

           A bsr B
     - Standard Erlang arithmetic operator.
   * - BitAnd
     - .. code-block:: erlang

           A band B
     - Bitwise operators are keywords (band, bor, bxor, bnot, bsl, bsr).
   * - BitOr
     - .. code-block:: erlang

           A bor B
     - Bitwise operators are keywords (band, bor, bxor, bnot, bsl, bsr).
   * - BitXor
     - .. code-block:: erlang

           A bxor B
     - Bitwise operators are keywords (band, bor, bxor, bnot, bsl, bsr).
   * - BitNot
     - .. code-block:: erlang

           bnot A
     - Bitwise operators are keywords (band, bor, bxor, bnot, bsl, bsr).
   * - Float4VectorMultiplication
     - .. code-block:: erlang

           [Ai * Bi || {Ai, Bi} <- lists:zip(A, B)].
     - Uses list comprehension and lists:zip.
   * - Float4VectorDotProduct
     - .. code-block:: erlang

           Dot = lists:foldl(fun({Ai, Bi}, Acc) -> Ai * Bi + Acc end, 0.0, lists:zip(A, B)).
     - Uses lists:zip and lists:foldl to calculate the sum of products.
   * - Float4VectorCrossProduct
     - .. code-block:: erlang

           C = [lists:nth(2,A)*lists:nth(3,B) - lists:nth(3,A)*lists:nth(2,B),
                lists:nth(3,A)*lists:nth(1,B) - lists:nth(1,A)*lists:nth(3,B),
                lists:nth(1,A)*lists:nth(2,B) - lists:nth(2,A)*lists:nth(1,B), 0.0].
     - Uses lists:nth (1-indexed) to access vector components.
   * - ForLoop
     - .. code-block:: erlang

           lists:foreach(fun(I) -> ok end, lists:seq(1, 10)).
     - Erlang uses recursion or library functions like lists:foreach for iteration.
   * - ForEach
     - .. code-block:: erlang

           lists:foreach(fun(Item) -> ok end, Collection).
     - Iterates over a list using the lists:foreach function.
   * - Equal
     - .. code-block:: erlang

           A == B
     - Value equality; use =:= for exact (type-safe) equality.
   * - NotEqual
     - .. code-block:: erlang

           A /= B
     - Value inequality; use =/= for exact inequality.
   * - GreaterThan
     - .. code-block:: erlang

           A > B
     -
   * - SetFiltering
     - .. code-block:: erlang

           [X || X <- List, X > 0].
     - Uses list comprehensions with guards for filtering.
   * - SetJoin
     - .. code-block:: erlang

           [{A, B} || A <- ListA, B <- ListB, element(1, A) == element(1, B)].
     - Uses list comprehensions for joins.
   * - MutexDefinition
     - N/A
     - Erlang uses message passing and isolated processes instead of shared-memory locks.
   * - MutexLock
     - N/A
     - N/A
   * - MutexUnlock
     - N/A
     - N/A
   * - SemaphoreDefinition
     - N/A
     - N/A
   * - SemaphoreWait
     - N/A
     - N/A
   * - SemaphoreSignal
     - N/A
     - N/A