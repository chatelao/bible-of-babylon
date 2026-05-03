
Pattern: VariableDeclaration

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


Pattern: FunctionDefinition

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
     - { raw "set /a res=%1+%2\nexit /b %res%" }
     - :add\nset /a res=%~1+%~2\nexit /b %res%
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


Pattern: IfElse

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


Pattern: Loop

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
     - :loop\nif %x% GTR 0 (set /a x=x-1 & goto loop)
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


Pattern: TryCatch

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


Pattern: Raise

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
     - throw new RuntimeException(\"Error\");
     - Uses 'throw' to raise an exception.
   * - RustRaise
     - Panic
     - Error
     - panic!(\"Error\");
     - Uses 'panic!' for unrecoverable errors.