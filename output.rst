
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