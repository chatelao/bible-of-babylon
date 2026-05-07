Erlang Pivot View
=================

.. list-table:: Erlang Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Bit and
     - Bit or
     - Bit xor
     - Bit not
     - Bit lshift
     - Bit rshift
     - Notes
   * - VariableDeclaration
     - .. code-block:: erlang

           X = 42.
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Single assignment; must start with an uppercase letter.
   * - IfElse
     - .. code-block:: erlang

           if X > 0 -> 1; true -> 0 end
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Erlang 'if' uses guards; 'true' acts as an 'else' branch.
   * - Loop
     - .. code-block:: erlang

           loop(0) -> ok; loop(X) when X > 0 -> loop(X - 1).
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Erlang uses recursion for looping; there are no built-in while/for loops.
   * - FunctionDefinition
     - .. code-block:: erlang

           add(A, B) -> A + B.
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Erlang functions use pattern matching on arguments; the last expression's value is returned.
   * - ProcedureDefinition
     - .. code-block:: erlang

           log_message(Msg) ->
               io:format("~p~n", [Msg]).
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - In Erlang, every function returns a value; 'ok' is commonly used for procedures.
   * - TryCatch
     - .. code-block:: erlang

           try
               do_something()
           catch
               error:Reason -> handle(Reason)
           end
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Erlang uses try...catch blocks; the type can be throw, error, or exit (defaulting to throw if omitted).
   * - Raise
     - .. code-block:: erlang

           error("Error")
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The error/1 BIF is used to stop execution and provide a stack trace.
   * - Thread
     - .. code-block:: erlang

           Pid = spawn(fun() -> do_work() end).
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Creates a new process (lightweight thread) and returns its PID.
   * - SendMessage
     - .. code-block:: erlang

           Pid ! hello.
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Asynchronous message passing using the ! operator.
   * - ReceiveMessage
     - .. code-block:: erlang

           receive hello -> handle_hello() end.
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Selective receive; blocks until a matching message is in the mailbox.
   * - SingleLineComment
     - .. code-block:: erlang

           % comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Erlang only supports single-line comments starting with %.
   * - MultiLineComment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Erlang does not have a native multi-line comment syntax.
   * - Print
     - .. code-block:: erlang

           io:format("Hello, World!~n").
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The io:format function is used for formatted output; ~n is the newline sequence.
   * - Import
     - .. code-block:: erlang

           -include("header.hrl").
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Includes header files; module functions are typically called using Module:Function syntax.
   * - SwitchCase
     - .. code-block:: erlang

           case X of
               1 -> one;
               2 -> two;
               _ -> none
           end
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'case' for pattern matching; _ is the catch-all pattern.
   * - Constant
     - .. code-block:: erlang

           -define(MAX, 100).
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses preprocessor macros to define constants; replaced at compile time.
   * - Addition
     - .. code-block:: erlang

           A + B
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - Subtraction
     - .. code-block:: erlang

           A - B
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - Multiplication
     - .. code-block:: erlang

           A * B
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - Division
     - .. code-block:: erlang

           A / B
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - Remainder
     - .. code-block:: erlang

           A rem B
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - Floor
     - .. code-block:: erlang

           floor(A)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - Rounding
     - .. code-block:: erlang

           round(A)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - Increment
     - .. code-block:: erlang

           A + 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - Decrement
     - .. code-block:: erlang

           A - 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - LeftShift
     - .. code-block:: erlang

           A bsl B
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - RightShift
     - .. code-block:: erlang

           A bsr B
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Erlang arithmetic operator.
   * - Bitwise
     - N/A
     - .. code-block:: erlang

           A band B
     - .. code-block:: erlang

           A bor B
     - .. code-block:: erlang

           A bxor B
     - .. code-block:: erlang

           bnot A
     - .. code-block:: erlang

           A bsl B
     - .. code-block:: erlang

           A bsr B
     - Bitwise operators are keywords (band, bor, bxor, bnot, bsl, bsr).