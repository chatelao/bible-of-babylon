Programming Patterns
====================



VariableDeclaration
-------------------


:description: The act of naming a value and optionally specifying its type.


Parameters:

* name: String

* type: String

* initial_value: Number

* syntax: String

* notes: String



.. list-table:: VariableDeclaration Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - name
     - type
     - initial_value
     - syntax
     - notes
   * - CVar
     - x
     - int
     - 42
     - int x = 42;
     - Static typing, terminated by semicolon.
   * - JavaVar
     - x
     - int
     - 42
     - int x = 42;
     - Strongly typed, similar to C.
   * - RustVar
     - x
     - i32
     - 42
     - let x: i32 = 42;
     - Immutable by default; supports type inference.
   * - PythonVar
     - x
     - None
     - 42
     - x = 42
     - Dynamically typed, no explicit type declaration needed.
   * - ErlangVar
     - X
     - Dynamic
     - 42
     - X = 42.
     - Single assignment; must start with an uppercase letter.
   * - LispVar
     - x
     - Dynamic
     - 42
     - (defparameter x 42)
     - Dynamic typing; defined using defparameter or defvar.
   * - BashVar
     - x
     - Untyped
     - 42
     - x=42
     - No spaces around the assignment operator.
   * - CmdVar
     - x
     - Untyped
     - 42
     - set x=42
     - Used in Windows Command Prompt.
   * - PowerShellVar
     - x
     - Dynamic
     - 42
     - $x = 42
     - Variables start with a dollar sign.
   * - SqlVar
     - x
     - INT
     - 42
     - DECLARE @x INT = 42;
     - T-SQL syntax for variable declaration.
   * - XQueryVar
     - x
     - xs:integer
     - 42
     - let $x := 42
     - XQuery uses 'let' for variable binding.
   * - CssVar
     - x
     - Number
     - 42
     - --x: 42;
     - CSS custom properties (variables).
   * - CudaVar
     - x
     - int
     - 42
     - __device__ int x = 42;
     - Uses __device__ qualifier for GPU memory.
   * - X86Var
     - x
     - DWORD
     - 42
     - x dd 42
     - Defined in the .data section (Intel syntax).



FunctionDefinition
------------------


:description: Declaration of a reusable block of code with parameters and a return value.


Parameters:

* name: String

* parameters: List<String>

* return_type: String

* body: Block

* syntax: String

* notes: String



.. list-table:: FunctionDefinition Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - name
     - parameters
     - return_type
     - body
     - syntax
     - notes
   * - CFunction
     - add
     - [int a, int b]
     - int
     - { raw "return a + b;" }
     - int add(int a, int b) { return a + b; }
     - Standard C function with static types and curly braces.
   * - JavaFunction
     - add
     - [int a, int b]
     - int
     - { raw "return a + b;" }
     - public int add(int a, int b) { return a + b; }
     - Similar to C, but typically within a class with an access modifier.
   * - RustFunction
     - add
     - [a: i32, b: i32]
     - i32
     - { raw "a + b" }
     - fn add(a: i32, b: i32) -> i32 { a + b }
     - Uses 'fn' keyword; return type preceded by '->'; last expression is returned implicitly.
   * - PythonFunction
     - add
     - [a, b]
     - Dynamic
     - { raw "return a + b" }
     - def add(a, b): return a + b
     - Uses 'def' keyword; indentation defines the block.
   * - BashFunction
     - add
     - [$1, $2]
     - Exit Code / Stdout
     - { raw "echo $(($1 + $2))" }
     - add() { echo $(($1 + $2)); }
     - Parameters are accessed via $1, $2, etc.; return values are typically exit codes or printed to stdout.
   * - PowerShellFunction
     - add
     - [$a, $b]
     - Dynamic
     - { raw "return $a + $b" }
     - function add($a, $b) { return $a + $b }
     - Uses 'function' keyword; parameters are variables starting with $.
   * - CmdFunction
     - add
     - [%1, %2]
     - ErrorLevel
     - | { raw "set /a res=%1+%2
       | exit /b %res%" }
     - | :add
       | set /a res=%~1+%~2
       | exit /b %res%
     - Functions are labels; called with 'call :label'; arguments are %1, %2.
   * - SqlFunction
     - add
     - [@a INT, @b INT]
     - INT
     - { raw "RETURN @a + @b" }
     - CREATE FUNCTION add(@a INT, @b INT) RETURNS INT AS BEGIN RETURN @a + @b END
     - T-SQL syntax for Scalar-Valued Functions.
   * - ErlangFunction
     - add
     - [A, B]
     - Dynamic
     - { raw "A + B" }
     - add(A, B) -> A + B.
     - Erlang functions use pattern matching on arguments; the last expression's value is returned.
   * - LispFunction
     - add
     - [a, b]
     - Dynamic
     - { raw "(+ a b)" }
     - (defun add (a b) (+ a b))
     - Functions are defined with 'defun'; Lisp follows prefix notation.
   * - XQueryFunction
     - local:add
     - [$a as xs:integer, $b as xs:integer]
     - xs:integer
     - { raw "$a + $b" }
     - declare function local:add($a as xs:integer, $b as xs:integer) as xs:integer { $a + $b };
     - Functions must be declared in a namespace (e.g., 'local').
   * - CssFunction
     - N/A
     - [N/A]
     - N/A
     - { raw "N/A" }
     - N/A
     - CSS does not support user-defined functions in the traditional sense (excluding Houdini or preprocessors).
   * - CudaFunction
     - add
     - [int a, int b]
     - int
     - { raw "return a + b;" }
     - __device__ int add(int a, int b) { return a + b; }
     - Functions can be qualified with __device__, __host__, or __global__.
   * - X86Function
     - add
     - [eax, ebx]
     - eax
     - | { raw "add eax, ebx
       | ret" }
     - | add_func:
       | add eax, ebx
       | ret
     - Functions are labels; parameters usually passed via registers or stack.



IfElse
------


:description: Conditional execution of code blocks.


Parameters:

* condition: String

* then_branch: Block

* else_branch: Block

* syntax: String

* notes: String



.. list-table:: IfElse Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - condition
     - then_branch
     - else_branch
     - syntax
     - notes
   * - CIfElse
     - x > 0
     - { return 1 }
     - { return 0 }
     - if (x > 0) { return 1; } else { return 0; }
     - Standard C if-else statement.
   * - JavaIfElse
     - x > 0
     - { return 1 }
     - { return 0 }
     - if (x > 0) { return 1; } else { return 0; }
     - Identical to C.
   * - RustIfElse
     - x > 0
     - { return 1 }
     - { return 0 }
     - if x > 0 { 1 } else { 0 }
     - Rust if-else is an expression; parentheses around condition are not required.
   * - PythonIfElse
     - x > 0
     - { return 1 }
     - { return 0 }
     - 1 if x > 0 else 0
     - Uses ternary expression; multi-line if-else uses colons and indentation.
   * - BashIfElse
     - x -gt 0
     - { return 1 }
     - { return 0 }
     - if [ $x -gt 0 ]; then exit 1; else exit 0; fi
     - Uses if-then-else-fi structure; brackets are for test command.
   * - PowerShellIfElse
     - $x -gt 0
     - { return 1 }
     - { return 0 }
     - if ($x -gt 0) { return 1 } else { return 0 }
     - Uses PowerShell comparison operators (e.g., -gt).
   * - CmdIfElse
     - x GTR 0
     - { return 1 }
     - { return 0 }
     - if %x% GTR 0 (exit /b 1) else (exit /b 0)
     - Uses GTR for 'greater than'; blocks are enclosed in parentheses.
   * - SqlIfElse
     - @x > 0
     - { return 1 }
     - { return 0 }
     - IF @x > 0 BEGIN RETURN 1 END ELSE BEGIN RETURN 0 END
     - Uses IF-ELSE with BEGIN-END blocks.
   * - ErlangIfElse
     - X > 0
     - { return 1 }
     - { return 0 }
     - if X > 0 -> 1; true -> 0 end
     - Erlang 'if' uses guards; 'true' acts as an 'else' branch.
   * - LispIfElse
     - (> x 0)
     - { return 1 }
     - { return 0 }
     - (if (> x 0) 1 0)
     - The 'if' expression evaluates the condition and returns the corresponding branch result.
   * - XQueryIfElse
     - $x > 0
     - { return 1 }
     - { return 0 }
     - if ($x > 0) then 1 else 0
     - Functional if-then-else expression; both branches are required.
   * - CssIfElse
     - min-width: 0px
     - { raw "color: red;" }
     - { raw "color: blue;" }
     - @media (min-width: 0px) { .element { color: red; } }
     - Media queries provide conditional styling; no true else branch exists.
   * - CudaIfElse
     - x > 0
     - { return 1 }
     - { return 0 }
     - if (x > 0) { return 1; } else { return 0; }
     - Standard C-like if-else statement.
   * - X86IfElse
     - eax > 0
     - { return 1 }
     - { return 0 }
     - | cmp eax, 0
       | jle .else
       | mov eax, 1
       | jmp .end
       | .else:
       | mov eax, 0
       | .end:
     - Implemented using comparison and jump instructions (Intel syntax).



Loop
----


:description: Repeated execution of a code block based on a condition.


Parameters:

* condition: String

* body: Block

* syntax: String

* notes: String



.. list-table:: Loop Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - condition
     - body
     - syntax
     - notes
   * - CLoop
     - x > 0
     - { raw "x = x - 1;" }
     - while (x > 0) { x = x - 1; }
     - Standard C while loop.
   * - JavaLoop
     - x > 0
     - { raw "x = x - 1;" }
     - while (x > 0) { x = x - 1; }
     - Identical to C.
   * - RustLoop
     - x > 0
     - { raw "x -= 1;" }
     - while x > 0 { x -= 1; }
     - Condition does not require parentheses.
   * - PythonLoop
     - x > 0
     - { raw "x = x - 1" }
     - while x > 0: x = x - 1
     - Uses colon and indentation for the body; parentheses around condition are not required.
   * - BashLoop
     - x -gt 0
     - { raw "x=$((x-1))" }
     - while [ $x -gt 0 ]; do x=$((x-1)); done
     - Uses while-do-done structure.
   * - PowerShellLoop
     - $x -gt 0
     - { raw "$x = $x - 1" }
     - while ($x -gt 0) { $x = $x - 1 }
     - Standard while loop with C-like block syntax.
   * - CmdLoop
     - x GTR 0
     - { raw "set /a x=x-1" }
     - | :loop
       | if %x% GTR 0 (set /a x=x-1 & goto loop)
     - Loops are typically implemented using labels and goto.
   * - SqlLoop
     - @x > 0
     - { raw "SET @x = @x - 1" }
     - WHILE @x > 0 BEGIN SET @x = @x - 1 END
     - Standard WHILE loop in T-SQL.
   * - ErlangLoop
     - X > 0
     - { raw "loop(X - 1)" }
     - loop(0) -> ok; loop(X) when X > 0 -> loop(X - 1).
     - Erlang uses recursion for looping; there are no built-in while/for loops.
   * - LispLoop
     - (> x 0)
     - { raw "(setq x (1- x))" }
     - (loop while (> x 0) do (setq x (1- x)))
     - Common Lisp 'loop' macro provides a versatile way to iterate.
   * - XQueryLoop
     - $i in 1 to $x
     - { raw "$i" }
     - for $i in 1 to $x return $i
     - XQuery uses 'for' expressions for iteration over sequences.
   * - CssLoop
     - N/A
     - { raw "N/A" }
     - N/A
     - CSS does not support loops natively.
   * - CudaLoop
     - x > 0
     - { raw "x = x - 1;" }
     - while (x > 0) { x = x - 1; }
     - Standard C-like while loop.
   * - X86Loop
     - ecx > 0
     - { raw "dec ecx" }
     - | .loop:
       | cmp ecx, 0
       | jle .end
       | dec ecx
       | jmp .loop
       | .end:
     - Implemented using labels and conditional jumps.



TryCatch
--------


:description: Handling exceptions or errors within a block of code.


Parameters:

* try_body: Block

* exception_type: String

* error_variable: String

* catch_body: Block

* syntax: String

* notes: String



.. list-table:: TryCatch Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - try_body
     - exception_type
     - error_variable
     - catch_body
     - syntax
     - notes
   * - CTryCatch
     - { call do_something() }
     - N/A
     - N/A
     - { raw "/* Error handling in C is typically done via return codes */" }
     - N/A
     - C does not have native try-catch blocks; error handling is usually manual.
   * - JavaTryCatch
     - { call do_something() }
     - Exception
     - e
     - { call handle(e) }
     - try { do_something(); } catch (Exception e) { handle(e); }
     - Standard Java exception handling.
   * - RustTryCatch
     - { call do_something() }
     - Result
     - e
     - { call handle(e) }
     - match do_something() { Ok(v) => v, Err(e) => handle(e) }
     - Rust uses Result type and pattern matching instead of traditional try-catch.
   * - PythonTryCatch
     - { call do_something() }
     - Exception
     - e
     - { call handle(e) }
     - | try:
       |     do_something()
       | except Exception as e:
       |     handle(e)
     - Standard Python exception handling using try-except.
   * - BashTryCatch
     - { call do_something() }
     - Exit Code
     - EXIT_STATUS
     - { call handle_error() }
     - do_something || handle_error
     - Shells often use command chaining (||) for basic error handling based on exit codes; $? stores the exit status.
   * - PowerShellTryCatch
     - { call do_something() }
     - ErrorRecord
     - PSItem
     - { call handle_error(PSItem) }
     - try { do_something } catch { handle_error($_) }
     - PowerShell supports try-catch-finally blocks; $_ (or $PSItem) refers to the current error.
   * - CmdTryCatch
     - { call do_something() }
     - ErrorLevel
     - %errorlevel%
     - { call handle_error() }
     - do_something || call :handle_error
     - Cmd uses || to execute a command if the previous one failed (non-zero errorlevel).
   * - SqlTryCatch
     - { call do_something() }
     - Error
     - @@ERROR
     - { call handle_error() }
     - | BEGIN TRY
       |     EXEC do_something;
       | END TRY
       | BEGIN CATCH
       |     EXEC handle_error;
       | END CATCH
     - T-SQL supports BEGIN TRY...END TRY and BEGIN CATCH...END CATCH blocks.
   * - ErlangTryCatch
     - { call do_something() }
     - error
     - Reason
     - { call handle(Reason) }
     - try do_something() catch error:Reason -> handle(Reason) end
     - Erlang uses try...catch blocks; the type can be throw, error, or exit (defaulting to throw if omitted).
   * - LispTryCatch
     - { call do_something() }
     - error
     - c
     - { call handle(c) }
     - (handler-case (do_something) (error (c) (handle c)))
     - Common Lisp uses handler-case for high-level error handling.
   * - XQueryTryCatch
     - { call do_something() }
     - *
     - err
     - { raw "handle($err)" }
     - try { do_something() } catch * { handle($err) }
     - XQuery 3.0+ supports try-catch; $err is a variable containing error information.
   * - CssTryCatch
     - { raw "/* N/A */" }
     - N/A
     - N/A
     - { raw "/* N/A */" }
     - N/A
     - CSS does not have native error handling mechanisms like try-catch.
   * - CudaTryCatch
     - { call do_something() }
     - N/A
     - N/A
     - { raw "/* Error handling in CUDA kernels is typically manual */" }
     - N/A
     - CUDA does not support C++ exceptions in device code.
   * - X86TryCatch
     - { call do_something() }
     - N/A
     - N/A
     - { raw "/* SEH or manual error checking */" }
     - N/A
     - No high-level try-catch; requires OS-specific mechanisms like SEH.



Raise
-----


:description: Explicitly triggering an exception or error.


Parameters:

* exception_type: String

* message: String

* syntax: String

* notes: String



.. list-table:: Raise Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - exception_type
     - message
     - syntax
     - notes
   * - CRaise
     - Signal/Exit
     - Error
     - exit(1);
     - C uses exit() or signals for severe errors.
   * - JavaRaise
     - RuntimeException
     - Error
     - throw new RuntimeException("Error");
     - Uses 'throw' to raise an exception.
   * - RustRaise
     - Panic
     - Error
     - panic!("Error");
     - Uses 'panic!' for unrecoverable errors.
   * - PythonRaise
     - Exception
     - Error
     - raise Exception("Error")
     - Uses 'raise' to trigger an exception.
   * - BashRaise
     - Exit
     - Error
     - exit 1
     - Terminates the script or subshell with a non-zero exit code.
   * - PowerShellRaise
     - Exception
     - Error
     - throw "Error"
     - Uses 'throw' to create a terminating error.
   * - CmdRaise
     - ErrorLevel
     - Error
     - exit /b 1
     - Sets the errorlevel and exits the current script or function.
   * - SqlRaise
     - Error
     - Error
     - THROW 50000, 'Error', 1;
     - The THROW statement raises an exception and transfers execution to a CATCH block.
   * - ErlangRaise
     - error
     - Error
     - error("Error")
     - The error/1 BIF is used to stop execution and provide a stack trace.
   * - LispRaise
     - error
     - Error
     - (error "Error")
     - Signals a continuous error that must be handled or it enters the debugger.
   * - XQueryRaise
     - error
     - Error
     - fn:error(fn:QName('http://example.com/errors', 'MY_ERROR'), 'Error')
     - The fn:error() function signals a dynamic error.
   * - CssRaise
     - N/A
     - N/A
     - N/A
     - CSS does not have a mechanism to raise exceptions.
   * - CudaRaise
     - N/A
     - N/A
     - N/A
     - No native exception mechanism in CUDA device code.
   * - X86Raise
     - Interrupt
     - Error
     - int 3
     - Software interrupts (like int 3) can be used to signal errors or breakpoints.



Thread
------


:description: Creating and running a new thread of execution.


Parameters:

* body: Block

* syntax: String

* notes: String



.. list-table:: Thread Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - body
     - syntax
     - notes
   * - ErlangThread
     - { call do_work() }
     - Pid = spawn(fun() -> do_work() end).
     - Creates a new process (lightweight thread) and returns its PID.
   * - RustThread
     - { call do_work() }
     - thread::spawn(|| { do_work(); });
     - Spawns a native OS thread. Closures are used for the thread body.
   * - JavaThread
     - { call do_work() }
     - new Thread(() -> { do_work(); }).start();
     - Spawns a new platform thread; virtual threads are available in newer versions.
   * - CudaThread
     - { call kernel() }
     - kernel<<<grid, block>>>();
     - Launches a grid of threads on the GPU.
   * - X86Thread
     - { call do_work() }
     - | push offset do_work
       | call CreateThread
     - Spawning threads requires calling OS-specific APIs (e.g., Win32 CreateThread).



SendMessage
-----------


:description: Sending a message to another process or thread.


Parameters:

* recipient: String

* message: String

* syntax: String

* notes: String



.. list-table:: SendMessage Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - recipient
     - message
     - syntax
     - notes
   * - ErlangSendMessage
     - Pid
     - hello
     - Pid ! hello.
     - Asynchronous message passing using the ! operator.
   * - RustSendMessage
     - tx
     - 42
     - tx.send(42).unwrap();
     - Using a channel sender. Result must be handled.
   * - JavaSendMessage
     - queue
     - 42
     - queue.put(42);
     - Commonly implemented using BlockingQueue; put() may block if the queue is full.
   * - CudaSendMessage
     - sm_id
     - data
     - N/A
     - CUDA threads typically communicate via shared memory or atomics, not explicit message passing.
   * - X86SendMessage
     - thread_id
     - msg
     - | push msg
       | push thread_id
       | call PostThreadMessage
     - Message passing is done via OS APIs.



ReceiveMessage
--------------


:description: Receiving a message from another process or thread.


Parameters:

* match_pattern: String

* body: Block

* syntax: String

* notes: String



.. list-table:: ReceiveMessage Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - match_pattern
     - body
     - syntax
     - notes
   * - ErlangReceiveMessage
     - hello
     - { call handle_hello() }
     - receive hello -> handle_hello() end.
     - Selective receive; blocks until a matching message is in the mailbox.
   * - RustReceiveMessage
     - msg
     - { call handle(msg) }
     - let msg = rx.recv().unwrap(); handle(msg);
     - Using a channel receiver; blocks until a message is available.
   * - JavaReceiveMessage
     - msg
     - { call handle(msg) }
     - int msg = queue.take(); handle(msg);
     - Using BlockingQueue.take(); blocks until an element becomes available.
   * - CudaReceiveMessage
     - data
     - { raw "/* access shared memory */" }
     - N/A
     - Communication is memory-based.
   * - X86ReceiveMessage
     - msg
     - { call handle(msg) }
     - call GetMessage
     - Message retrieval via OS APIs.



Comment
-------


:description: Way to add non-executable explanatory text to the source code.


Parameters:

* single_line: String

* multi_line: String

* notes: String



.. list-table:: Comment Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - single_line
     - multi_line
     - notes
   * - CComment
     - // comment
     - | /* line 1
       |    line 2 */
     - Standard C comment syntax.
   * - JavaComment
     - // comment
     - | /* line 1
       |    line 2 */
     - Identical to C.
   * - RustComment
     - // comment
     - | /* line 1
       |    line 2 */
     - Supports nested multi-line comments.
   * - PythonComment
     - # comment
     - | """ line 1
       |     line 2 """
     - Multi-line comments are typically implemented using docstrings.
   * - BashComment
     - # comment
     - N/A
     - Bash only supports single-line comments starting with #.
   * - PowerShellComment
     - # comment
     - | <# line 1
       |    line 2 #>
     - Uses <# and #> for block comments.
   * - CmdComment
     - REM comment
     - N/A
     - Uses REM or :: (label hack) for comments.
   * - SqlComment
     - -- comment
     - | /* line 1
       |    line 2 */
     - Standard SQL comment syntax.
   * - ErlangComment
     - % comment
     - N/A
     - Erlang only supports single-line comments starting with %.
   * - LispComment
     - ; comment
     - | #| line 1
       |    line 2 |#
     - Single-line comments use semicolon; multi-line use #| |#.
   * - XQueryComment
     - (: comment :)
     - | (: line 1
       |    line 2 :)
     - XQuery uses (: :) for both single and multi-line comments.
   * - CssComment
     - N/A
     - | /* line 1
       |    line 2 */
     - CSS only supports block comments.
   * - CudaComment
     - // comment
     - | /* line 1
       |    line 2 */
     - Standard C-like comment syntax.
   * - X86Comment
     - ; comment
     - N/A
     - Most assemblers use semicolon for comments (Intel syntax).