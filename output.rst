

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

   * - Language
     - Syntax
     - Notes
   * - CVar
     - .. code-block:: c

           int x = 42;
     - Static typing, terminated by semicolon.
   * - JavaVar
     - .. code-block:: java

           int x = 42;
     - Strongly typed, similar to C.
   * - RustVar
     - .. code-block:: rust

           let x: i32 = 42;
     - Immutable by default; supports type inference.
   * - PythonVar
     - .. code-block:: python

           x = 42
     - Dynamically typed, no explicit type declaration needed.
   * - PhpVar
     - .. code-block:: php

           $x = 42;
     - Variables start with a dollar sign; dynamically typed but supports type declarations.
   * - ErlangVar
     - .. code-block:: erlang

           X = 42.
     - Single assignment; must start with an uppercase letter.
   * - LispVar
     - .. code-block:: common-lisp

           (defparameter x 42)
     - Dynamic typing; defined using defparameter or defvar.
   * - BashVar
     - .. code-block:: bash

           x=42
     - No spaces around the assignment operator.
   * - CmdVar
     - .. code-block:: doscon

           set x=42
     - Used in Windows Command Prompt.
   * - PowerShellVar
     - .. code-block:: powershell

           $x = 42
     - Variables start with a dollar sign.
   * - SqlVar
     - .. code-block:: sql

           DECLARE @x INT = 42;
     - T-SQL syntax for variable declaration.
   * - XQueryVar
     - .. code-block:: xquery

           let $x := 42
     - XQuery uses 'let' for variable binding.
   * - CssVar
     - .. code-block:: css

           --x: 42;
     - CSS custom properties (variables).
   * - CudaVar
     - .. code-block:: cpp

           __device__ int x = 42;
     - Uses __device__ qualifier for GPU memory.
   * - X86Var
     - .. code-block:: nasm

           x   dd 42
     - Defined in the .data section (Intel syntax).
   * - RiscvVar
     - .. code-block:: asm

           x:  .word 42
     - Defined in the .data section.
   * - PrologVariableDeclaration
     - .. code-block:: prolog

           X = 42.
     - Uses unification for assignment; variables must start with an uppercase letter.
   * - JavaBytecodeVar
     - .. code-block:: jasmin

           .field private static x I = 42
     - In Jasmin syntax, static fields represent global-like variables.
   * - CamelVar
     - .. code-block:: ocaml

           let x = 42
     - Immutable binding by default; type inference is used.
   * - ArmAarch64Var
     - .. code-block:: asm

           x:  .quad 42
     - Defined in the .data section.
   * - GoVar
     - .. code-block:: go

           var x int = 42
     - Static typing with optional type inference.
   * - HaskellVar
     - .. code-block:: haskell

           let x = 42
     - Immutable binding within a scope; part of let-in or where clause.
   * - TypeScriptVar
     - .. code-block:: typescript

           let x: number = 42;
     - Supports static typing on top of JavaScript.
   * - TclVar
     - .. code-block:: tcl

           set x 42
     - Variables are untyped strings; set is used for assignment.
   * - CobolVariableDeclaration
     - .. code-block:: cobol

           01 X PIC 9(4) VALUE 42.
     - Variables are defined in the DATA DIVISION; PIC (picture) clause specifies the data type and size.
   * - FortranVariableDeclaration
     - .. code-block:: fortran

           integer :: x = 42
     - Static typing; :: is used to separate attributes from the variable name.



ProcedureDefinition
-------------------


:description: Declaration of a reusable block of code with parameters and no return value.


Parameters:

* name: String

* parameters: List<String>

* body: Block

* syntax: String

* notes: String



.. list-table:: ProcedureDefinition Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CProcedure
     - .. code-block:: c

           void log_message(const char *msg) {
               printf("%s\n", msg);
           }
     - In C, a procedure is a function with a void return type.
   * - JavaProcedure
     - .. code-block:: java

           public void logMessage(String msg) {
               System.out.println(msg);
           }
     - Uses the 'void' keyword to indicate no return value.
   * - RustProcedure
     - .. code-block:: rust

           fn log_message(msg: &str) {
               println!("{}", msg);
           }
     - Functions without a return type implicitly return the unit type ().
   * - PythonProcedure
     - .. code-block:: python

           def log_message(msg):
               print(msg)
     - Procedures in Python are functions that don't return a value (implicitly return None).
   * - PhpProcedure
     - .. code-block:: php

           function log_message(string $msg): void {
               echo $msg;
           }
     - Uses the 'void' return type hint (PHP 7.1+).
   * - BashProcedure
     - .. code-block:: bash

           log_message() {
               echo "$1"
           }
     - In Bash, all functions are effectively procedures; return values are exit codes.
   * - PowerShellProcedure
     - .. code-block:: powershell

           function log-message($msg) {
               Write-Host $msg
           }
     - Functions without a return statement output nothing to the pipeline.
   * - CmdProcedure
     - .. code-block:: doscon

           :log_message
           echo %~1
           goto :eof
     - Procedures are labels called with 'call'; they return using 'goto :eof' or 'exit /b'.
   * - SqlProcedure
     - .. code-block:: sql

           CREATE PROCEDURE log_message @msg NVARCHAR(MAX)
           AS
           BEGIN
               PRINT @msg;
           END
     - T-SQL uses CREATE PROCEDURE for blocks that perform actions.
   * - ErlangProcedure
     - .. code-block:: erlang

           log_message(Msg) ->
               io:format("~p~n", [Msg]).
     - In Erlang, every function returns a value; 'ok' is commonly used for procedures.
   * - LispProcedure
     - .. code-block:: common-lisp

           (defun log-message (msg)
             (format t "~A~%" msg))
     - Lisp functions always return the value of the last expression; procedures return nil or some status.
   * - XQueryProcedure
     - .. code-block:: xquery

           declare function local:log-message(
               $msg as xs:string
           ) as empty-sequence() {
               (); (: side effects in XQuery are implementation-defined or via extensions :)
           };
     - XQuery functions return empty-sequence() to simulate procedures.
   * - CssProcedure
     - N/A
     - CSS does not support procedures.
   * - CudaProcedure
     - .. code-block:: cpp

           __device__ void log_message(const char *msg) {
               printf("%s\n", msg);
           }
     - Similar to C, procedures use the void return type.
   * - X86Procedure
     - .. code-block:: nasm

           log_message:
               push edx
               call printf
               add esp, 4
               ret
     - Implemented as a label followed by code and a ret instruction.
   * - RiscvProcedure
     - .. code-block:: asm

           log_message:
               addi sp, sp, -16
               sd ra, 8(sp)
               call printf
               ld ra, 8(sp)
               addi sp, sp, 16
               ret
     - Follows standard calling convention; must save/restore return address (ra) if calling other functions.
   * - PrologProcedure
     - .. code-block:: prolog

           log_message(Msg) :- writeln(Msg).
     - Predicates without an output argument act as procedures.
   * - JavaBytecodeProcedure
     - .. code-block:: jasmin

           .method public static logMessage(Ljava/lang/String;)V
               .limit stack 2
               .limit locals 1
               getstatic java/lang/System/out Ljava/io/PrintStream;
               aload_0
               invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
               return
           .end method
     - Methods with a 'V' return descriptor are procedures; 'return' instruction is used for void return.
   * - CamelProcedure
     - .. code-block:: ocaml

           let log_message msg = print_endline msg
     - Procedures in OCaml return the unit type ().
   * - ArmAarch64Procedure
     - .. code-block:: asm

           log_message:
               stp x29, x30, [sp, -16]!
               mov x29, sp
               bl printf
               ldp x29, x30, [sp], 16
               ret
     - Uses stp/ldp to save and restore the frame pointer (x29) and link register (x30).
   * - GoProcedure
     - .. code-block:: go

           func logMessage(msg string) {
               fmt.Println(msg)
           }
     - Procedures are functions with no return value.
   * - HaskellProcedure
     - .. code-block:: haskell

           logMessage :: String -> IO ()
           logMessage msg = putStrLn msg
     - Procedures are functions that return an IO action.
   * - TypeScriptProcedure
     - .. code-block:: typescript

           function logMessage(msg: string): void {
               console.log(msg);
           }
     - Procedures use the 'void' return type.
   * - TclProcedure
     - .. code-block:: tcl

           proc logMessage {msg} {
               puts $msg
           }
     - Uses 'proc' to define a command.
   * - CobolProcedure
     - .. code-block:: cobol

           IDENTIFICATION DIVISION.
           PROGRAM-ID. LOG-MSG.
           ...
           DISPLAY MSG.
           EXIT PROGRAM.
     - Procedures are typically implemented as separate programs or paragraphs.
   * - FortranProcedure
     - .. code-block:: fortran

           subroutine log_msg(msg)
               character(len=*), intent(in) :: msg
               print *, msg
           end subroutine log_msg
     - Subroutines are used for procedures that do not return a value.



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

   * - Language
     - Syntax
     - Notes
   * - CFunction
     - .. code-block:: c

           int add(int a, int b) {
               return a + b;
           }
     - Standard C function with static types and curly braces.
   * - JavaFunction
     - .. code-block:: java

           public int add(int a, int b) {
               return a + b;
           }
     - Similar to C, but typically within a class with an access modifier.
   * - RustFunction
     - .. code-block:: rust

           fn add(a: i32, b: i32) -> i32 {
               a + b
           }
     - Uses 'fn' keyword; return type preceded by '->'; last expression is returned implicitly.
   * - PythonFunction
     - .. code-block:: python

           def add(a, b):
               return a + b
     - Uses 'def' keyword; indentation defines the block.
   * - PhpFunction
     - .. code-block:: php

           function add(int $a, int $b): int {
               return $a + $b;
           }
     - Uses 'function' keyword; supports type hints for parameters and return values.
   * - BashFunction
     - .. code-block:: bash

           add() {
               echo $(($1 + $2))
           }
     - Parameters are accessed via $1, $2, etc.; return values are typically exit codes or printed to stdout.
   * - PowerShellFunction
     - .. code-block:: powershell

           function add($a, $b) {
               return $a + $b
           }
     - Uses 'function' keyword; parameters are variables starting with $.
   * - CmdFunction
     - .. code-block:: doscon

           :add
           set /a res=%~1+%~2
           exit /b %res%
     - Functions are labels; called with 'call :label'; arguments are %1, %2.
   * - SqlFunction
     - .. code-block:: sql

           CREATE FUNCTION add(@a INT, @b INT)
           RETURNS INT AS
           BEGIN
               RETURN @a + @b
           END
     - T-SQL syntax for Scalar-Valued Functions.
   * - ErlangFunction
     - .. code-block:: erlang

           add(A, B) -> A + B.
     - Erlang functions use pattern matching on arguments; the last expression's value is returned.
   * - LispFunction
     - .. code-block:: common-lisp

           (defun add (a b) (+ a b))
     - Functions are defined with 'defun'; Lisp follows prefix notation.
   * - XQueryFunction
     - .. code-block:: xquery

           declare function local:add(
               $a as xs:integer,
               $b as xs:integer
           ) as xs:integer {
               $a + $b
           };
     - Functions must be declared in a namespace (e.g., 'local').
   * - CssFunction
     - N/A
     - CSS does not support user-defined functions in the traditional sense (excluding Houdini or preprocessors).
   * - CudaFunction
     - .. code-block:: cpp

           __device__ int add(int a, int b) {
               return a + b;
           }
     - Functions can be qualified with __device__, __host__, or __global__.
   * - X86Function
     - .. code-block:: nasm

           add_func:
               add eax, ebx
               ret
     - Functions are labels; parameters usually passed via registers or stack.
   * - RiscvFunction
     - .. code-block:: asm

           add:
               add a0, a0, a1
               ret
     - Functions follow the RISC-V calling convention; a0-a7 are argument registers.
   * - PrologFunctionDefinition
     - .. code-block:: prolog

           add(A, B, Res) :- Res is A + B.
     - Functions are predicates; return values are typically unified with an output argument.
   * - JavaBytecodeFunction
     - .. code-block:: jasmin

           .method public static add(II)I
               .limit stack 2
               .limit locals 2
               iload_0
               iload_1
               iadd
               ireturn
           .end method
     - Methods define stack and local variable limits; parameters are accessed by index.
   * - CamelFunction
     - .. code-block:: ocaml

           let add a b = a + b
     - Functions are defined with let; parameters are space-separated.
   * - ArmAarch64Function
     - .. code-block:: asm

           add:
               add x0, x0, x1
               ret
     - Standard AArch64 calling convention; x0-x7 are argument registers, x0 is the return register.
   * - GoFunction
     - .. code-block:: go

           func add(a int, b int) int {
               return a + b
           }
     - Functions use the 'func' keyword; return type follows the parameter list.
   * - HaskellFunction
     - .. code-block:: haskell

           add :: Int -> Int -> Int
           add a b = a + b
     - Function types are usually declared explicitly; arguments are space-separated.
   * - TypeScriptFunction
     - .. code-block:: typescript

           function add(a: number, b: number): number {
               return a + b;
           }
     - Functions support typed parameters and return values.
   * - TclFunction
     - .. code-block:: tcl

           proc add {a b} {
               return [expr {$a + $b}]
           }
     - Procedures can return values using the return command.
   * - CobolFunctionDefinition
     - .. code-block:: cobol

           FUNCTION-ID. ADD-FUNC.
           ...
           COMPUTE RESULT = A + B
           ...
           END FUNCTION ADD-FUNC.
     - User-defined functions were introduced in modern COBOL (COBOL 2002).
   * - FortranFunction
     - .. code-block:: fortran

           function add(a, b) result(res)
               integer, intent(in) :: a, b
               integer :: res
               res = a + b
           end function add
     - Functions return a value; 'intent(in)' specifies that parameters are read-only.



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

   * - Language
     - Syntax
     - Notes
   * - CIfElse
     - .. code-block:: c

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C if-else statement.
   * - JavaIfElse
     - .. code-block:: java

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Identical to C.
   * - RustIfElse
     - .. code-block:: rust

           if x > 0 {
               1
           } else {
               0
           }
     - Rust if-else is an expression; parentheses around condition are not required.
   * - PythonIfElse
     - .. code-block:: python

           1 if x > 0 else 0
     - Uses ternary expression; multi-line if-else uses colons and indentation.
   * - PhpIfElse
     - .. code-block:: php

           if ($x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C-like if-else statement.
   * - BashIfElse
     - .. code-block:: bash

           if [ $x -gt 0 ]; then
               exit 1
           else
               exit 0
           fi
     - Uses if-then-else-fi structure; brackets are for test command.
   * - PowerShellIfElse
     - .. code-block:: powershell

           if ($x -gt 0) {
               return 1
           } else {
               return 0
           }
     - Uses PowerShell comparison operators (e.g., -gt).
   * - CmdIfElse
     - .. code-block:: doscon

           if %x% GTR 0 (exit /b 1) else (exit /b 0)
     - Uses GTR for 'greater than'; blocks are enclosed in parentheses.
   * - SqlIfElse
     - .. code-block:: sql

           IF @x > 0
           BEGIN
               RETURN 1
           END
           ELSE
           BEGIN
               RETURN 0
           END
     - Uses IF-ELSE with BEGIN-END blocks.
   * - ErlangIfElse
     - .. code-block:: erlang

           if X > 0 -> 1; true -> 0 end
     - Erlang 'if' uses guards; 'true' acts as an 'else' branch.
   * - LispIfElse
     - .. code-block:: common-lisp

           (if (> x 0) 1 0)
     - The 'if' expression evaluates the condition and returns the corresponding branch result.
   * - XQueryIfElse
     - .. code-block:: xquery

           if ($x > 0) then 1 else 0
     - Functional if-then-else expression; both branches are required.
   * - CssIfElse
     - .. code-block:: css

           @media (min-width: 0px) { .element { color: red; } }
     - Media queries provide conditional styling; no true else branch exists.
   * - CudaIfElse
     - .. code-block:: cpp

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C-like if-else statement.
   * - X86IfElse
     - .. code-block:: nasm

               cmp eax, 0
               jle .else
               mov eax, 1
               jmp .end
           .else:
               mov eax, 0
           .end:
     - Implemented using comparison and jump instructions (Intel syntax).
   * - RiscvIfElse
     - .. code-block:: asm

               blez t0, .else
               li a0, 1
               j .end
           .else:
               li a0, 0
           .end:
     - Uses branch instructions like blez (branch if less than or equal to zero).
   * - PrologIfElse
     - .. code-block:: prolog

           (X > 0 -> Result = 1 ; Result = 0)
     - Uses the (Condition -> Then ; Else) control construct.
   * - JavaBytecodeIfElse
     - .. code-block:: jasmin

               getstatic MyClass/x I
               ifgt LabelThen
               iconst_0
               ireturn
           LabelThen:
               iconst_1
               ireturn
     - Implemented using stack operations and branch instructions (ifgt).
   * - CamelIfElse
     - .. code-block:: ocaml

           if x > 0 then 1 else 0
     - If-then-else is an expression; both branches must return the same type.
   * - ArmAarch64IfElse
     - .. code-block:: asm

               cmp x0, #0
               ble .else
               mov x0, #1
               b .end
           .else:
               mov x0, #0
           .end:
     - Implemented using comparison and branch instructions (ble).
   * - GoIfElse
     - .. code-block:: go

           if x > 0 {
               return 1
           } else {
               return 0
           }
     - Parentheses around condition are not required; braces are mandatory.
   * - HaskellIfElse
     - .. code-block:: haskell

           if x > 0 then 1 else 0
     - If-then-else is an expression; both branches must be present and have the same type.
   * - TypeScriptIfElse
     - .. code-block:: typescript

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C-style if-else statement.
   * - TclIfElse
     - .. code-block:: tcl

           if {$x > 0} {
               return 1
           } else {
               return 0
           }
     - Uses braces for the condition and branches.
   * - CobolIfElse
     - .. code-block:: cobol

           IF X > 0 THEN
               MOVE 1 TO RESULT
           ELSE
               MOVE 0 TO RESULT
           END-IF.
     - Uses IF-THEN-ELSE-END-IF structure; periods are used to terminate sentences.
   * - FortranIfElse
     - .. code-block:: fortran

           if (x > 0) then
               res = 1
           else
               res = 0
           end if
     - Standard block if-then-else-end if.



SwitchCase
----------


:description: Multi-way branch based on the value of an expression.


Parameters:

* expression: String

* syntax: String

* notes: String



.. list-table:: SwitchCase Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CSwitchCase
     - .. code-block:: c

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - Standard C switch statement with case labels and default.
   * - JavaSwitchCase
     - .. code-block:: java

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - Identical to C; modern Java also supports switch expressions.
   * - RustSwitchCase
     - .. code-block:: rust

           match x {
               1 => 1,
               2 => 2,
               _ => 0,
           }
     - Rust uses 'match' for pattern matching, which is exhaustive.
   * - PythonSwitchCase
     - .. code-block:: python

           match x:
               case 1:
                   return 1
               case 2:
                   return 2
               case _:
                   return 0
     - Introduced in Python 3.10 as structural pattern matching.
   * - PhpSwitchCase
     - .. code-block:: php

           switch ($x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - Standard C-like switch statement; match expression is also available in PHP 8.0+.
   * - BashSwitchCase
     - .. code-block:: bash

           case $x in
               1)
                   echo "one"
                   ;;
               2)
                   echo "two"
                   ;;
               *)
                   echo "none"
                   ;;
           esac
     - Uses case-in-esac structure; patterns end with ) and blocks end with ;;.
   * - PowerShellSwitchCase
     - .. code-block:: powershell

           switch ($x) {
               1 { "one" }
               2 { "two" }
               default { "none" }
           }
     - Versatile switch statement that supports multiple types and patterns.
   * - CmdSwitchCase
     - .. code-block:: doscon

           if "%x%"=="1" (goto :one) else if "%x%"=="2" (goto :two) else (goto :none)
     - Cmd does not have a native switch; it is typically simulated with if/else or goto.
   * - SqlSwitchCase
     - .. code-block:: sql

           CASE @x
               WHEN 1 THEN 'one'
               WHEN 2 THEN 'two'
               ELSE 'none'
           END
     - The CASE expression is used for conditional logic in SQL.
   * - ErlangSwitchCase
     - .. code-block:: erlang

           case X of
               1 -> one;
               2 -> two;
               _ -> none
           end
     - Uses 'case' for pattern matching; _ is the catch-all pattern.
   * - LispSwitchCase
     - .. code-block:: common-lisp

           (case x
             (1 "one")
             (2 "two")
             (t "none"))
     - Standard 'case' macro; 't' or 'otherwise' is the default branch.
   * - XQuerySwitchCase
     - .. code-block:: xquery

           switch ($x)
             case 1 return "one"
             case 2 return "two"
             default return "none"
     - The 'switch' expression was introduced in XQuery 3.0.
   * - CssSwitchCase
     - N/A
     - CSS does not support switch/case logic.
   * - CudaSwitchCase
     - .. code-block:: cpp

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - Standard C-like switch statement.
   * - X86SwitchCase
     - .. code-block:: nasm

               cmp eax, 1
               je .case1
               cmp eax, 2
               je .case2
               jmp .default
           .case1:
               ; ...
           .case2:
               ; ...
           .default:
               ; ...
     - Implemented using a series of comparison and jump instructions.
   * - RiscvSwitchCase
     - .. code-block:: asm

               li t1, 1
               beq t0, t1, .case1
               li t1, 2
               beq t0, t1, .case2
               j .default
     - Typically implemented using comparison and branch instructions.
   * - PrologSwitchCase
     - .. code-block:: prolog

           (   X = 1 -> writeln('one')
           ;   X = 2 -> writeln('two')
           ;   writeln('none')
           )
     - Usually implemented using nested (If -> Then ; Else) or multiple clauses.
   * - JavaBytecodeSwitchCase
     - .. code-block:: jasmin

               getstatic MyClass/x I
               lookupswitch
                   1: Label1
                   2: Label2
                   default: LabelDefault
           Label1:
               ; ...
           Label2:
               ; ...
           LabelDefault:
               ; ...
     - Uses lookupswitch or tableswitch instructions for multi-way branching.
   * - CamelSwitchCase
     - .. code-block:: ocaml

           match x with
           | 1 -> 1
           | 2 -> 2
           | _ -> 0
     - Structural pattern matching using the match expression.
   * - ArmAarch64SwitchCase
     - .. code-block:: asm

               cmp x0, #1
               beq .case1
               cmp x0, #2
               beq .case2
               b .default
     - Implemented using comparison and branch instructions.
   * - GoSwitchCase
     - .. code-block:: go

           switch x {
           case 1:
               return 1
           case 2:
               return 2
           default:
               return 0
           }
     - Switch cases do not fall through by default in Go.
   * - HaskellSwitchCase
     - .. code-block:: haskell

           case x of
               1 -> 1
               2 -> 2
               _ -> 0
     - Uses pattern matching in a case expression.
   * - TypeScriptSwitchCase
     - .. code-block:: typescript

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - Standard C-style switch statement.
   * - TclSwitchCase
     - .. code-block:: tcl

           switch $x {
               1 {
                   return 1
               }
               2 {
                   return 2
               }
               default {
                   return 0
               }
           }
     - The switch command provides multi-way branching.
   * - CobolSwitchCase
     - .. code-block:: cobol

           EVALUATE X
               WHEN 1
                   DISPLAY 'One'
               WHEN 2
                   DISPLAY 'Two'
               WHEN OTHER
                   DISPLAY 'Other'
           END-EVALUATE.
     - The EVALUATE statement is used for multi-way branching.
   * - FortranSwitchCase
     - .. code-block:: fortran

           select case (x)
           case (1)
               res = 1
           case (2)
               res = 2
           case default
               res = 0
           end select
     - The select case construct is used for branching based on values.



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

   * - Language
     - Syntax
     - Notes
   * - CLoop
     - .. code-block:: c

           while (x > 0) {
               x = x - 1;
           }
     - Standard C while loop.
   * - JavaLoop
     - .. code-block:: java

           while (x > 0) {
               x = x - 1;
           }
     - Identical to C.
   * - RustLoop
     - .. code-block:: rust

           while x > 0 {
               x -= 1;
           }
     - Condition does not require parentheses.
   * - PythonLoop
     - .. code-block:: python

           while x > 0: x = x - 1
     - Uses colon and indentation for the body; parentheses around condition are not required.
   * - PhpLoop
     - .. code-block:: php

           while ($x > 0) {
               $x = $x - 1;
           }
     - Standard C-like while loop.
   * - BashLoop
     - .. code-block:: bash

           while [ $x -gt 0 ]; do
               x=$((x-1))
           done
     - Uses while-do-done structure.
   * - PowerShellLoop
     - .. code-block:: powershell

           while ($x -gt 0) {
               $x = $x - 1
           }
     - Standard while loop with C-like block syntax.
   * - CmdLoop
     - .. code-block:: doscon

           :loop
           if %x% GTR 0 (set /a x=x-1 & goto loop)
     - Loops are typically implemented using labels and goto.
   * - SqlLoop
     - .. code-block:: sql

           WHILE @x > 0
           BEGIN
               SET @x = @x - 1
           END
     - Standard WHILE loop in T-SQL.
   * - ErlangLoop
     - .. code-block:: erlang

           loop(0) -> ok; loop(X) when X > 0 -> loop(X - 1).
     - Erlang uses recursion for looping; there are no built-in while/for loops.
   * - LispLoop
     - .. code-block:: common-lisp

           (loop while (> x 0) do (setq x (1- x)))
     - Common Lisp 'loop' macro provides a versatile way to iterate.
   * - XQueryLoop
     - .. code-block:: xquery

           for $i in 1 to $x return $i
     - XQuery uses 'for' expressions for iteration over sequences.
   * - CssLoop
     - N/A
     - CSS does not support loops natively.
   * - CudaLoop
     - .. code-block:: cpp

           while (x > 0) {
               x = x - 1;
           }
     - Standard C-like while loop.
   * - X86Loop
     - .. code-block:: nasm

           .loop:
               cmp ecx, 0
               jle .end
               dec ecx
               jmp .loop
           .end:
     - Implemented using labels and conditional jumps.
   * - RiscvLoop
     - .. code-block:: asm

           .loop:
               blez t0, .end
               addi t0, t0, -1
               j .loop
           .end:
     - Uses conditional branches and jumps to implement loops.
   * - PrologLoop
     - .. code-block:: prolog

           loop(0) :- !.
           loop(X) :- X > 0, X1 is X - 1, loop(X1).
     - Prolog uses recursion and tail-call optimization for looping.
   * - JavaBytecodeLoop
     - .. code-block:: jasmin

           LoopStart:
               getstatic MyClass/x I
               ifle LoopEnd
               getstatic MyClass/x I
               iconst_1
               isub
               putstatic MyClass/x I
               goto LoopStart
           LoopEnd:
     - Loops are built with labels and jump instructions (goto, ifle).
   * - CamelLoop
     - .. code-block:: ocaml

           while !x > 0 do
               x := !x - 1
           done
     - Uses references for mutable state in while loops.
   * - ArmAarch64Loop
     - .. code-block:: asm

           .loop:
               cmp x0, #0
               ble .end
               sub x0, x0, #1
               b .loop
           .end:
     - Uses conditional branches to implement loops.
   * - GoLoop
     - .. code-block:: go

           for x > 0 {
               x = x - 1
           }
     - Go uses 'for' for all looping constructs, including while-like loops.
   * - HaskellLoop
     - .. code-block:: haskell

           loop x = if x > 0 then loop (x - 1) else return ()
     - Haskell uses recursion for iteration as it is a pure functional language.
   * - TypeScriptLoop
     - .. code-block:: typescript

           while (x > 0) {
               x = x - 1;
           }
     - Standard while loop.
   * - TclLoop
     - .. code-block:: tcl

           while {$x > 0} {
               set x [expr {$x - 1}]
           }
     - Standard while loop; expr is used for mathematical evaluation.
   * - CobolLoop
     - .. code-block:: cobol

           PERFORM UNTIL X <= 0
               SUBTRACT 1 FROM X
           END-PERFORM.
     - The PERFORM UNTIL construct is used for conditional looping.
   * - FortranLoop
     - .. code-block:: fortran

           do while (x > 0)
               x = x - 1
           end do
     - Standard do while loop.



ForLoop
-------


:description: Iterating over a range or collection.


Parameters:

* syntax: String

* notes: String



.. list-table:: ForLoop Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CForLoop
     - .. code-block:: c

           for (int i = 0; i < 10; i++) {
               // body
           }
     - Standard C for loop with initialization, condition, and increment.
   * - JavaForLoop
     - .. code-block:: java

           for (int i = 0; i < 10; i++) {
               // body
           }
     - Identical to C; also supports enhanced for-each loops.
   * - RustForLoop
     - .. code-block:: rust

           for i in 0..10 {
               // body
           }
     - Uses ranges; 0..10 is exclusive of the upper bound.
   * - PythonForLoop
     - .. code-block:: python

           for i in range(10):
               # body
     - Iterates over a sequence (typically generated by range()).
   * - PhpForLoop
     - .. code-block:: php

           for ($i = 0; $i < 10; $i++) {
               // body
           }
     - Standard C-style for loop.
   * - ErlangForLoop
     - .. code-block:: erlang

           lists:foreach(fun(I) -> ok end, lists:seq(1, 10)).
     - Erlang uses recursion or library functions like lists:foreach for iteration.
   * - LispForLoop
     - .. code-block:: common-lisp

           (loop for i from 0 to 9 do
               #| body |#)
     - The loop macro provides a highly expressive way to iterate.
   * - BashForLoop
     - .. code-block:: bash

           for i in {0..9}; do
               # body
           done
     - Uses brace expansion for ranges; also supports C-style for loops.
   * - CmdForLoop
     - .. code-block:: doscon

           for /L %%i in (0,1,9) do (
               rem body
           )
     - The /L switch is used for iterative loops (start, step, end).
   * - PowerShellForLoop
     - .. code-block:: powershell

           for ($i = 0; $i -lt 10; $i++) {
               # body
           }
     - Standard C-style for loop with PowerShell comparison operators.
   * - SqlForLoop
     - .. code-block:: sql

           DECLARE @i INT = 0;
           WHILE @i < 10
           BEGIN
               -- body
               SET @i = @i + 1;
           END
     - T-SQL uses WHILE loops; there is no native FOR loop for ranges.
   * - XQueryForLoop
     - .. code-block:: xquery

           for $i in 1 to 10
           return $i
     - Iterates over a sequence and returns a new sequence.
   * - CssForLoop
     - N/A
     - CSS does not support for loops natively.
   * - CudaForLoop
     - .. code-block:: cpp

           for (int i = 0; i < 10; i++) {
               // body
           }
     - Standard C for loop, usable within kernels.
   * - X86ForLoop
     - .. code-block:: nasm

               mov ecx, 10
           .loop:
               ; body
               loop .loop
     - The loop instruction uses the ECX register as a counter.
   * - RiscvForLoop
     - .. code-block:: asm

               li t0, 0
               li t1, 10
           .loop:
               bge t0, t1, .end
               ; body
               addi t0, t0, 1
               j .loop
           .end:
     - Implemented using a counter register and conditional branches.
   * - PrologForLoop
     - .. code-block:: prolog

           forall(between(0, 9, I), do_something(I)).
     - Uses between/3 to generate values and forall/2 to iterate over them.
   * - JavaBytecodeForLoop
     - .. code-block:: jasmin

               iconst_0
               istore_1 ; i = 0
           LoopStart:
               iload_1
               bipush 10
               if_icmpge LoopEnd
               ; body
               iinc 1 1 ; i++
               goto LoopStart
           LoopEnd:
     - Built using labels, conditional jumps (if_icmpge), and iinc.
   * - CamelForLoop
     - .. code-block:: ocaml

           for i = 0 to 9 do
               (* body *)
           done
     - OCaml provides a simple for loop for integer ranges.
   * - ArmAarch64ForLoop
     - .. code-block:: asm

               mov x0, #0
           .loop:
               cmp x0, #10
               b.ge .end
               ; body
               add x0, x0, #1
               b .loop
           .end:
     - Uses a register for the counter and conditional branches.
   * - GoForLoop
     - .. code-block:: go

           for i := 0; i < 10; i++ {
               // body
           }
     - Go's only looping construct is 'for'.
   * - HaskellForLoop
     - .. code-block:: haskell

           mapM_ (\i -> return ()) [0..9]
     - Haskell uses mapM_ or forM_ (Control.Monad) for imperative-style iteration.
   * - TypeScriptForLoop
     - .. code-block:: typescript

           for (let i = 0; i < 10; i++) {
               // body
           }
     - Identical to JavaScript; supports typed loop variables.
   * - TclForLoop
     - .. code-block:: tcl

           for {set i 0} {$i < 10} {incr i} {
               # body
           }
     - Standard for loop; all arguments are Tcl scripts.
   * - CobolForLoop
     - .. code-block:: cobol

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 10
               *> body
           END-PERFORM.
     - PERFORM VARYING is the COBOL equivalent of a for loop.
   * - FortranForLoop
     - .. code-block:: fortran

           do i = 1, 10
               ! body
           end do
     - The do loop is used for iteration over ranges.



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

   * - Language
     - Syntax
     - Notes
   * - CTryCatch
     - N/A
     - C does not have native try-catch blocks; error handling is usually manual.
   * - JavaTryCatch
     - .. code-block:: java

           try {
               do_something();
           } catch (Exception e) {
               handle(e);
           }
     - Standard Java exception handling.
   * - RustTryCatch
     - .. code-block:: rust

           match do_something() {
               Ok(v) => v,
               Err(e) => handle(e)
           }
     - Rust uses Result type and pattern matching instead of traditional try-catch.
   * - PythonTryCatch
     - .. code-block:: python

           try:
               do_something()
           except Exception as e:
               handle(e)
     - Standard Python exception handling using try-except.
   * - PhpTryCatch
     - .. code-block:: php

           try {
               do_something();
           } catch (Exception $e) {
               handle($e);
           }
     - Standard PHP exception handling using try-catch blocks.
   * - BashTryCatch
     - .. code-block:: bash

           do_something || handle_error
     - Shells often use command chaining (||) for basic error handling based on exit codes; $? stores the exit status.
   * - PowerShellTryCatch
     - .. code-block:: powershell

           try {
               do_something
           } catch {
               handle_error($_)
           }
     - PowerShell supports try-catch-finally blocks; $_ (or $PSItem) refers to the current error.
   * - CmdTryCatch
     - .. code-block:: doscon

           do_something || call :handle_error
     - Cmd uses || to execute a command if the previous one failed (non-zero errorlevel).
   * - SqlTryCatch
     - .. code-block:: sql

           BEGIN TRY
               EXEC do_something;
           END TRY
           BEGIN CATCH
               EXEC handle_error;
           END CATCH
     - T-SQL supports BEGIN TRY...END TRY and BEGIN CATCH...END CATCH blocks.
   * - ErlangTryCatch
     - .. code-block:: erlang

           try
               do_something()
           catch
               error:Reason -> handle(Reason)
           end
     - Erlang uses try...catch blocks; the type can be throw, error, or exit (defaulting to throw if omitted).
   * - LispTryCatch
     - .. code-block:: common-lisp

           (handler-case (do_something) (error (c) (handle c)))
     - Common Lisp uses handler-case for high-level error handling.
   * - XQueryTryCatch
     - .. code-block:: xquery

           try {
               do_something()
           } catch * {
               handle($err)
           }
     - XQuery 3.0+ supports try-catch; $err is a variable containing error information.
   * - CssTryCatch
     - N/A
     - CSS does not have native error handling mechanisms like try-catch.
   * - CudaTryCatch
     - N/A
     - CUDA does not support C++ exceptions in device code.
   * - X86TryCatch
     - N/A
     - No high-level try-catch; requires OS-specific mechanisms like SEH.
   * - RiscvTryCatch
     - N/A
     - No native try-catch; relies on return codes or trap handlers for errors.
   * - PrologTryCatch
     - .. code-block:: prolog

           catch(do_something, E, handle(E))
     - Standard Prolog error handling using the catch/3 predicate.
   * - JavaBytecodeTryCatch
     - .. code-block:: jasmin

           .catch java/lang/Exception from TryStart to TryEnd using CatchHandler
           TryStart:
               invokestatic MyClass/do_something()V
           TryEnd:
               goto Done
           CatchHandler:
               astore_1
               aload_1
               invokestatic MyClass/handle(Ljava/lang/Exception;)V
           Done:
     - Exception handlers are defined via .catch directives for specific code ranges.
   * - CamelTryCatch
     - .. code-block:: ocaml

           try do_something () with e -> handle e
     - Uses the try...with construct for exception handling.
   * - ArmAarch64TryCatch
     - N/A
     - No native try-catch; relies on return codes or exception levels/traps for errors.
   * - GoTryCatch
     - .. code-block:: go

           if err := do_something(); err != nil {
               handle(err)
           }
     - Go handles errors explicitly by returning them as values.
   * - HaskellTryCatch
     - .. code-block:: haskell

           do_something `catch` \(e :: SomeException) -> handle e
     - Exception handling using the catch function from Control.Exception.
   * - TypeScriptTryCatch
     - .. code-block:: typescript

           try {
               do_something();
           } catch (e) {
               handle(e);
           }
     - Standard JavaScript exception handling.
   * - TclTryCatch
     - .. code-block:: tcl

           try {
               do_something
           } on error {e} {
               handle $e
           }
     - The try command handles errors and exceptions (Tcl 8.6+).
   * - CobolTryCatch
     - .. code-block:: cobol

           ADD A TO B ON SIZE ERROR
               DISPLAY 'Arithmetic Overflow'
           END-ADD.
     - COBOL uses imperative 'ON ERROR' clauses for specific operations.
   * - FortranTryCatch
     - N/A
     - Fortran does not have high-level try-catch blocks; uses iostat for I/O errors.



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

   * - Language
     - Syntax
     - Notes
   * - CRaise
     - .. code-block:: c

           exit(1);
     - C uses exit() or signals for severe errors.
   * - JavaRaise
     - .. code-block:: java

           throw new RuntimeException("Error");
     - Uses 'throw' to raise an exception.
   * - RustRaise
     - .. code-block:: rust

           panic!("Error");
     - Uses 'panic!' for unrecoverable errors.
   * - PythonRaise
     - .. code-block:: python

           raise Exception("Error")
     - Uses 'raise' to trigger an exception.
   * - PhpRaise
     - .. code-block:: php

           throw new Exception("Error");
     - Uses 'throw' to trigger an exception.
   * - BashRaise
     - .. code-block:: bash

           exit 1
     - Terminates the script or subshell with a non-zero exit code.
   * - PowerShellRaise
     - .. code-block:: powershell

           throw "Error"
     - Uses 'throw' to create a terminating error.
   * - CmdRaise
     - .. code-block:: doscon

           exit /b 1
     - Sets the errorlevel and exits the current script or function.
   * - SqlRaise
     - .. code-block:: sql

           THROW 50000, 'Error', 1;
     - The THROW statement raises an exception and transfers execution to a CATCH block.
   * - ErlangRaise
     - .. code-block:: erlang

           error("Error")
     - The error/1 BIF is used to stop execution and provide a stack trace.
   * - LispRaise
     - .. code-block:: common-lisp

           (error "Error")
     - Signals a continuous error that must be handled or it enters the debugger.
   * - XQueryRaise
     - .. code-block:: xquery

           fn:error(fn:QName('http://example.com/errors', 'MY_ERROR'), 'Error')
     - The fn:error() function signals a dynamic error.
   * - CssRaise
     - N/A
     - CSS does not have a mechanism to raise exceptions.
   * - CudaRaise
     - N/A
     - No native exception mechanism in CUDA device code.
   * - X86Raise
     - .. code-block:: nasm

               int 3
     - Software interrupts (like int 3) can be used to signal errors or breakpoints.
   * - RiscvRaise
     - .. code-block:: asm

               ebreak
     - The ebreak instruction triggers a debug trap; ecall can be used for system calls.
   * - PrologRaise
     - .. code-block:: prolog

           throw(error(Error))
     - Uses throw/1 to raise an exception.
   * - JavaBytecodeRaise
     - .. code-block:: jasmin

               new java/lang/RuntimeException
               dup
               ldc "Error"
               invokespecial java/lang/RuntimeException/<init>(Ljava/lang/String;)V
               athrow
     - Exceptions are instantiated and then thrown using the athrow instruction.
   * - CamelRaise
     - .. code-block:: ocaml

           raise (Failure "Error")
     - Standard way to raise an exception.
   * - ArmAarch64Raise
     - .. code-block:: asm

               brk #0
     - The brk instruction triggers a breakpoint exception.
   * - GoRaise
     - .. code-block:: go

           panic("Error")
     - Uses 'panic' for unrecoverable errors.
   * - HaskellRaise
     - .. code-block:: haskell

           error "Error"
     - The 'error' function stops execution and displays a message.
   * - TypeScriptRaise
     - .. code-block:: typescript

           throw new Error("Error");
     - Uses 'throw' to raise an error.
   * - TclRaise
     - .. code-block:: tcl

           error "Error"
     - Signals an error condition.
   * - CobolRaise
     - N/A
     - No standard mechanism to 'throw' exceptions; execution is managed via status codes.
   * - FortranRaise
     - .. code-block:: fortran

           error stop "Error"
     - The 'error stop' statement terminates execution with an error message (Fortran 2008+).



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

   * - Language
     - Syntax
     - Notes
   * - ErlangThread
     - .. code-block:: erlang

           Pid = spawn(fun() -> do_work() end).
     - Creates a new process (lightweight thread) and returns its PID.
   * - RustThread
     - .. code-block:: rust

           thread::spawn(|| { do_work(); });
     - Spawns a native OS thread. Closures are used for the thread body.
   * - JavaThread
     - .. code-block:: java

           new Thread(() -> { do_work(); }).start();
     - Spawns a new platform thread; virtual threads are available in newer versions.
   * - CudaThread
     - .. code-block:: cpp

           kernel<<<grid, block>>>();
     - Launches a grid of threads on the GPU.
   * - X86Thread
     - .. code-block:: nasm

               push offset do_work
               call CreateThread
     - Spawning threads requires calling OS-specific APIs (e.g., Win32 CreateThread).
   * - RiscvThread
     - .. code-block:: asm

               li a7, 220 # clone syscall
               ecall
     - Thread creation typically involves invoking OS system calls (e.g., clone in Linux).
   * - PrologThread
     - .. code-block:: prolog

           thread_create(do_work, Id, []).
     - Creates a new thread using thread_create/3 (ISO Prolog / SWI-Prolog).
   * - JavaBytecodeThread
     - .. code-block:: jasmin

               new java/lang/Thread
               dup
               new MyRunnable
               dup
               invokespecial MyRunnable/<init>()V
               invokespecial java/lang/Thread/<init>(Ljava/lang/Runnable;)V
               invokevirtual java/lang/Thread/start()V
     - Involves instantiating a Thread object with a Runnable and calling start().
   * - CamelThread
     - .. code-block:: ocaml

           Thread.create do_work ()
     - Requires the 'threads' library.
   * - ArmAarch64Thread
     - .. code-block:: asm

               mov x8, #220 // clone syscall
               svc #0
     - Thread creation typically involves invoking OS system calls (e.g., clone on Linux).
   * - GoThread
     - .. code-block:: go

           go do_work()
     - The 'go' keyword starts a new goroutine (lightweight thread).
   * - HaskellThread
     - .. code-block:: haskell

           forkIO (do_work)
     - forkIO creates a lightweight thread (requires Control.Concurrent).
   * - TypeScriptThread
     - .. code-block:: typescript

           new Worker('worker.js');
     - Concurrency is typically handled via Web Workers or asynchronous programming (Promises/async-await).
   * - TclThread
     - .. code-block:: tcl

           thread::create { do_work }
     - Requires the Thread package.
   * - CobolThread
     - N/A
     - Standard COBOL does not support multi-threading.
   * - FortranThread
     - N/A
     - Fortran uses Coarrays or OpenMP/MPI for parallelism, but not a simple 'thread spawn' primitive.



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

   * - Language
     - Syntax
     - Notes
   * - ErlangSendMessage
     - .. code-block:: erlang

           Pid ! hello.
     - Asynchronous message passing using the ! operator.
   * - RustSendMessage
     - .. code-block:: rust

           tx.send(42).unwrap();
     - Using a channel sender. Result must be handled.
   * - JavaSendMessage
     - .. code-block:: java

           queue.put(42);
     - Commonly implemented using BlockingQueue; put() may block if the queue is full.
   * - CudaSendMessage
     - N/A
     - CUDA threads typically communicate via shared memory or atomics, not explicit message passing.
   * - X86SendMessage
     - .. code-block:: nasm

               push msg
               push thread_id
               call PostThreadMessage
     - Message passing is done via OS APIs.
   * - RiscvSendMessage
     - .. code-block:: asm

               li a7, 139 # rt_sigqueueinfo
               ecall
     - Inter-process/thread communication is managed by the OS.
   * - PrologSendMessage
     - .. code-block:: prolog

           thread_send_message(Id, hello).
     - Sends a message to a thread's message queue.
   * - JavaBytecodeSendMessage
     - .. code-block:: jasmin

               aload_0 ; queue
               bipush 42
               invokestatic java/lang/Integer/valueOf(I)Ljava/lang/Integer;
               invokevirtual java/util/concurrent/BlockingQueue/put(Ljava/lang/Object;)V
     - Typically uses standard Java concurrent collections like BlockingQueue.
   * - CamelSendMessage
     - .. code-block:: ocaml

           Event.sync (Event.send ch 42)
     - Synchronous communication using the Event module.
   * - ArmAarch64SendMessage
     - .. code-block:: asm

               mov x8, #139 // rt_sigqueueinfo
               svc #0
     - Inter-process/thread communication is managed via OS system calls.
   * - GoSendMessage
     - .. code-block:: go

           ch <- 42
     - Sends a value to a channel.
   * - HaskellSendMessage
     - .. code-block:: haskell

           writeChan chan 42
     - Writes a value to a Chan (unbounded FIFO channel).
   * - TypeScriptSendMessage
     - .. code-block:: typescript

           worker.postMessage(42);
     - Communicates with a Web Worker.
   * - TclSendMessage
     - .. code-block:: tcl

           thread::send $id $msg
     - Sends a message to a thread.
   * - CobolSendMessage
     - N/A
     - Message passing is not a native COBOL feature.
   * - FortranSendMessage
     - .. code-block:: fortran

           target_var[image] = data
     - Coarrays use distributed memory and assignment to 'images' for communication.



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

   * - Language
     - Syntax
     - Notes
   * - ErlangReceiveMessage
     - .. code-block:: erlang

           receive hello -> handle_hello() end.
     - Selective receive; blocks until a matching message is in the mailbox.
   * - RustReceiveMessage
     - .. code-block:: rust

           let msg = rx.recv().unwrap(); handle(msg);
     - Using a channel receiver; blocks until a message is available.
   * - JavaReceiveMessage
     - .. code-block:: java

           int msg = queue.take(); handle(msg);
     - Using BlockingQueue.take(); blocks until an element becomes available.
   * - CudaReceiveMessage
     - N/A
     - Communication is memory-based.
   * - X86ReceiveMessage
     - .. code-block:: nasm

               call GetMessage
     - Message retrieval via OS APIs.
   * - RiscvReceiveMessage
     - .. code-block:: asm

               li a7, 128 # rt_sigtimedwait
               ecall
     - Receiving signals or messages involves OS system calls.
   * - PrologReceiveMessage
     - .. code-block:: prolog

           thread_get_message(hello).
     - Retrieves a matching message from the current thread's queue.
   * - JavaBytecodeReceiveMessage
     - .. code-block:: jasmin

               aload_0 ; queue
               invokevirtual java/util/concurrent/BlockingQueue/take()Ljava/lang/Object;
               checkcast java/lang/Integer
               invokevirtual java/lang/Integer/intValue()I
               istore_1 ; msg
               iload_1
               invokestatic MyClass/handle(I)V
     - Blocking retrieval from a concurrent collection.
   * - CamelReceiveMessage
     - .. code-block:: ocaml

           let msg = Event.sync (Event.receive ch) in handle msg
     - Receives a message from a channel.
   * - ArmAarch64ReceiveMessage
     - .. code-block:: asm

               mov x8, #128 // rt_sigtimedwait
               svc #0
     - Receiving signals or messages involves OS system calls.
   * - GoReceiveMessage
     - .. code-block:: go

           msg := <-ch
           handle(msg)
     - Receives a value from a channel; blocks until data is available.
   * - HaskellReceiveMessage
     - .. code-block:: haskell

           msg <- readChan chan
           handle msg
     - Reads a value from a Chan; blocks if the channel is empty.
   * - TypeScriptReceiveMessage
     - .. code-block:: typescript

           worker.onmessage = (e) => { handle(e.data); };
     - Handles messages from a Web Worker.
   * - TclReceiveMessage
     - .. code-block:: tcl

           vwait msg; handle $msg
     - vwait blocks until a variable is written.
   * - CobolReceiveMessage
     - N/A
     - Not supported natively.
   * - FortranReceiveMessage
     - .. code-block:: fortran

           sync images(*)
     - Synchronization is used to ensure data consistency in Coarrays.



SingleLineComment
-----------------


:description: Way to add non-executable explanatory text to a single line of source code.


Parameters:

* syntax: String

* notes: String



.. list-table:: SingleLineComment Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CSingleLineComment
     - .. code-block:: c

           // comment
     - Standard C single-line comment.
   * - JavaSingleLineComment
     - .. code-block:: java

           // comment
     - Identical to C.
   * - RustSingleLineComment
     - .. code-block:: rust

           // comment
     - Standard Rust single-line comment.
   * - PythonSingleLineComment
     - .. code-block:: python

           # comment
     - Standard Python single-line comment.
   * - PhpSingleLineComment
     - .. code-block:: php

           // comment
     - Supports // and # for single-line comments.
   * - BashSingleLineComment
     - .. code-block:: bash

           # comment
     - Bash only supports single-line comments starting with #.
   * - PowerShellSingleLineComment
     - .. code-block:: powershell

           # comment
     - Standard PowerShell single-line comment.
   * - CmdSingleLineComment
     - .. code-block:: doscon

           REM comment
     - Uses REM or :: (label hack) for comments.
   * - SqlSingleLineComment
     - .. code-block:: sql

           -- comment
     - Standard SQL single-line comment.
   * - ErlangSingleLineComment
     - .. code-block:: erlang

           % comment
     - Erlang only supports single-line comments starting with %.
   * - LispSingleLineComment
     - .. code-block:: common-lisp

           ; comment
     - Standard Lisp single-line comment using semicolon.
   * - XQuerySingleLineComment
     - .. code-block:: xquery

           (: comment :)
     - XQuery uses (: :) for single-line comments.
   * - CssSingleLineComment
     - N/A
     - CSS does not natively support single-line comments (though // is common in preprocessors).
   * - CudaSingleLineComment
     - .. code-block:: cpp

           // comment
     - Standard C-like single-line comment.
   * - X86SingleLineComment
     - .. code-block:: nasm

           ; comment
     - Most assemblers use semicolon for single-line comments (Intel syntax).
   * - RiscvSingleLineComment
     - .. code-block:: asm

           # comment
     - RISC-V assembly typically uses the hash character for single-line comments.
   * - PrologSingleLineComment
     - .. code-block:: prolog

           % comment
     - Standard Prolog single-line comment.
   * - JavaBytecodeSingleLineComment
     - .. code-block:: jasmin

           ; comment
     - Jasmin uses semicolons for single-line comments.
   * - CamelSingleLineComment
     - .. code-block:: ocaml

           (* comment *)
     - OCaml uses (* *) for all comments.
   * - ArmAarch64SingleLineComment
     - .. code-block:: asm

           // comment
     - AArch64 assembly often uses // or ; for single-line comments.
   * - GoSingleLineComment
     - .. code-block:: go

           // comment
     - Standard single-line comment.
   * - HaskellSingleLineComment
     - .. code-block:: haskell

           -- comment
     - Standard single-line comment.
   * - TypeScriptSingleLineComment
     - .. code-block:: typescript

           // comment
     - Standard single-line comment.
   * - TclSingleLineComment
     - .. code-block:: tcl

           # comment
     - Hashes start comments; must be at the beginning of a command.
   * - CobolSingleLineComment
     - .. code-block:: cobol

           *> comment
     - *> is used for inline comments in free-format COBOL.
   * - FortranSingleLineComment
     - .. code-block:: fortran

           ! comment
     - Exclamation mark starts a comment to the end of the line.



MultiLineComment
----------------


:description: Way to add non-executable explanatory text spanning multiple lines of source code.


Parameters:

* syntax: String

* notes: String



.. list-table:: MultiLineComment Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CMultiLineComment
     - .. code-block:: c

           /* line 1
              line 2 */
     - Standard C multi-line comment.
   * - JavaMultiLineComment
     - .. code-block:: java

           /* line 1
              line 2 */
     - Identical to C.
   * - RustMultiLineComment
     - .. code-block:: rust

           /* line 1
              line 2 */
     - Supports nested multi-line comments.
   * - PythonMultiLineComment
     - .. code-block:: python

           """ line 1
               line 2 """
     - Multi-line comments are typically implemented using docstrings.
   * - PhpMultiLineComment
     - .. code-block:: php

           /* line 1
              line 2 */
     - Standard C-style block comments.
   * - BashMultiLineComment
     - N/A
     - Bash does not have a native multi-line comment syntax; multiple single-line comments are used.
   * - PowerShellMultiLineComment
     - .. code-block:: powershell

           <# line 1
              line 2 #>
     - Uses <# and #> for block comments.
   * - CmdMultiLineComment
     - N/A
     - Command Prompt does not support multi-line comments.
   * - SqlMultiLineComment
     - .. code-block:: sql

           /* line 1
              line 2 */
     - Standard SQL multi-line comment.
   * - ErlangMultiLineComment
     - N/A
     - Erlang does not have a native multi-line comment syntax.
   * - LispMultiLineComment
     - .. code-block:: common-lisp

           #| line 1
              line 2 |#
     - Uses ``#|`` and ``|#`` for block comments.
   * - XQueryMultiLineComment
     - .. code-block:: xquery

           (: line 1
              line 2 :)
     - XQuery uses (: :) for multi-line comments.
   * - CssMultiLineComment
     - .. code-block:: css

           /* line 1
              line 2 */
     - Standard CSS block comment.
   * - CudaMultiLineComment
     - .. code-block:: cpp

           /* line 1
              line 2 */
     - Standard C-like block comment.
   * - X86MultiLineComment
     - N/A
     - Most assemblers do not have a native multi-line comment syntax.
   * - RiscvMultiLineComment
     - N/A
     - RISC-V assembly does not have a native multi-line comment syntax.
   * - PrologMultiLineComment
     - .. code-block:: prolog

           /* line 1
              line 2 */
     - Standard C-style block comment.
   * - JavaBytecodeMultiLineComment
     - N/A
     - Java Bitcode (Jasmin) does not have a native multi-line comment syntax; multiple semicolons are used.
   * - CamelMultiLineComment
     - .. code-block:: ocaml

           (* line 1
              line 2 *)
     - Supports nested comments.
   * - ArmAarch64MultiLineComment
     - N/A
     - AArch64 assembly does not have a native multi-line comment syntax.
   * - GoMultiLineComment
     - .. code-block:: go

           /* line 1
              line 2 */
     - Standard block comment.
   * - HaskellMultiLineComment
     - .. code-block:: haskell

           {- line 1
              line 2 -}
     - Standard block comment; can be nested.
   * - TypeScriptMultiLineComment
     - .. code-block:: typescript

           /* line 1
              line 2 */
     - Standard block comment.
   * - TclMultiLineComment
     - N/A
     - Tcl has no native multi-line comment syntax.
   * - CobolMultiLineComment
     - N/A
     - No native multi-line comment syntax; multiple * or *> must be used.
   * - FortranMultiLineComment
     - N/A
     - Fortran does not support multi-line comments natively.



Print
-----


:description: Outputting text to the console or standard output.


Parameters:

* value: String

* syntax: String

* notes: String



.. list-table:: Print Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CPrint
     - .. code-block:: c

           printf("Hello, World!\n");
     - Uses the standard library's printf function; requires stdio.h.
   * - JavaPrint
     - .. code-block:: java

           System.out.println("Hello, World!");
     - Uses System.out for standard output; includes a newline.
   * - RustPrint
     - .. code-block:: rust

           println!("Hello, World!");
     - Uses a macro for formatted output to standard output with a newline.
   * - PythonPrint
     - .. code-block:: python

           print("Hello, World!")
     - The print() function adds a newline by default.
   * - PhpPrint
     - .. code-block:: php

           echo "Hello, World!";
     - The echo statement is used to output text.
   * - BashPrint
     - .. code-block:: bash

           echo "Hello, World!"
     - The echo command outputs text followed by a newline.
   * - PowerShellPrint
     - .. code-block:: powershell

           Write-Host "Hello, World!"
     - Write-Host outputs directly to the console host.
   * - CmdPrint
     - .. code-block:: doscon

           echo Hello, World!
     - Echo displays messages in Windows Command Prompt.
   * - SqlPrint
     - .. code-block:: sql

           PRINT 'Hello, World!';
     - T-SQL PRINT statement outputs a message to the client.
   * - ErlangPrint
     - .. code-block:: erlang

           io:format("Hello, World!~n").
     - The io:format function is used for formatted output; ~n is the newline sequence.
   * - LispPrint
     - .. code-block:: common-lisp

           (format t "Hello, World!~%")
     - The format function with 't' outputs to standard output; ~% is a newline.
   * - XQueryPrint
     - .. code-block:: xquery

           "Hello, World!"
     - In XQuery, a string literal is often the result of an expression and is automatically serialized to output.
   * - CssPrint
     - .. code-block:: css

           .element::before { content: "Hello, World!"; }
     - CSS can 'print' text using the content property in pseudo-elements.
   * - CudaPrint
     - .. code-block:: cpp

           printf("Hello, World!\n");
     - CUDA supports printf within device kernels for debugging.
   * - X86Print
     - .. code-block:: nasm

           push offset hello_msg
           call printf
     - Printing in assembler usually involves calling C library functions or OS-specific system calls.
   * - RiscvPrint
     - .. code-block:: asm

               la a0, hello_msg
               call printf
     - Typically uses the C library printf or writes to stdout via system calls.
   * - PrologPrint
     - .. code-block:: prolog

           writeln('Hello, World!').
     - Outputs text followed by a newline.
   * - JavaBytecodePrint
     - .. code-block:: jasmin

               getstatic java/lang/System/out Ljava/io/PrintStream;
               ldc "Hello, World!"
               invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
     - Calls println on the static System.out field.
   * - CamelPrint
     - .. code-block:: ocaml

           print_endline "Hello, World!"
     - Outputs a string followed by a newline.
   * - ArmAarch64Print
     - .. code-block:: asm

               adrp x0, hello_msg
               add x0, x0, :lo12:hello_msg
               bl printf
     - Typically uses the C library printf; adrp/add are used for PC-relative addressing.
   * - GoPrint
     - .. code-block:: go

           fmt.Println("Hello, World!")
     - Uses the fmt package for formatted I/O.
   * - HaskellPrint
     - .. code-block:: haskell

           putStrLn "Hello, World!"
     - Outputs a string followed by a newline in the IO monad.
   * - TypeScriptPrint
     - .. code-block:: typescript

           console.log("Hello, World!");
     - Outputs to the console.
   * - TclPrint
     - .. code-block:: tcl

           puts "Hello, World!"
     - Outputs a string to stdout followed by a newline.
   * - CobolPrint
     - .. code-block:: cobol

           DISPLAY "Hello World".
     - DISPLAY outputs data to the system console or standard output.
   * - FortranPrint
     - .. code-block:: fortran

           print *, "Hello World"
     - The print statement with * (default format) outputs to stdout.



Import
------


:description: Including external modules, packages, or files into the current scope.


Parameters:

* module_name: String

* syntax: String

* notes: String



.. list-table:: Import Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CImport
     - .. code-block:: c

           #include <stdio.h>
     - Standard C way to include header files.
   * - JavaImport
     - .. code-block:: java

           import java.util.List;
     - Imports a specific class; can use * for all classes in a package.
   * - RustImport
     - .. code-block:: rust

           use std::collections::HashMap;
     - Brings a path into scope using the 'use' keyword.
   * - PythonImport
     - .. code-block:: python

           import math
     - Standard Python import; can also use 'from ... import ...'.
   * - PhpImport
     - .. code-block:: php

           require 'utils.php';
     - Uses include, require, include_once, or require_once to include other files.
   * - BashImport
     - .. code-block:: bash

           source utils.sh
     - The 'source' (or .) command executes a script in the current shell context.
   * - PowerShellImport
     - .. code-block:: powershell

           Import-Module ActiveDirectory
     - Loads a module into the current session.
   * - CmdImport
     - .. code-block:: doscon

           call other.cmd
     - The 'call' command is used to run another batch file from within one.
   * - SqlImport
     - N/A
     - Standard SQL does not have a native 'import' keyword for code; database objects are globally accessible or schema-qualified.
   * - ErlangImport
     - .. code-block:: erlang

           -include("header.hrl").
     - Includes header files; module functions are typically called using Module:Function syntax.
   * - LispImport
     - .. code-block:: common-lisp

           (use-package :iter)
     - Makes symbols from the specified package available in the current package.
   * - XQueryImport
     - .. code-block:: xquery

           import module namespace utils = "http://example.com/utils";
     - Imports a library module by its namespace URI.
   * - CssImport
     - .. code-block:: css

           @import "base.css";
     - Imports styles from another stylesheet.
   * - CudaImport
     - .. code-block:: cpp

           #include <cuda_runtime.h>
     - Same as C; used to include CUDA runtime headers.
   * - X86Import
     - .. code-block:: nasm

           include 'macros.inc'
     - Includes another assembly file; syntax varies by assembler (e.g., FASM uses 'include').
   * - RiscvImport
     - .. code-block:: asm

           .include "macros.s"
     - Uses the .include directive to include external source files.
   * - PrologImport
     - .. code-block:: prolog

           use_module(library(math)).
     - Imports predicates from a library module.
   * - JavaBytecodeImport
     - .. code-block:: jasmin

           Ljava/util/List;
     - Internal descriptors are used to reference external classes.
   * - CamelImport
     - .. code-block:: ocaml

           open List
     - Opens a module namespace.
   * - ArmAarch64Import
     - .. code-block:: asm

           .include "macros.s"
     - Uses the .include directive for external source files.
   * - GoImport
     - .. code-block:: go

           import "fmt"
     - Imports a package by its path.
   * - HaskellImport
     - .. code-block:: haskell

           import Data.List
     - Imports symbols from a module into the current namespace.
   * - TypeScriptImport
     - .. code-block:: typescript

           import { add } from './math';
     - ESM import syntax.
   * - TclImport
     - .. code-block:: tcl

           package require Tcl
     - Loads a package into the interpreter.
   * - CobolImport
     - .. code-block:: cobol

           COPY DEFS.
     - The COPY statement includes text from a library at compile time.
   * - FortranImport
     - .. code-block:: fortran

           use math_mod
     - The 'use' statement imports a module's public variables and procedures.



Constant
--------


:description: Declaration of an immutable value that remains unchanged throughout the program's execution.


Parameters:

* name: String

* type: String

* value: String

* syntax: String

* notes: String



.. list-table:: Constant Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CConstant
     - .. code-block:: c

           const int MAX = 100;
     - The 'const' qualifier makes the variable immutable after initialization.
   * - JavaConstant
     - .. code-block:: java

           public static final int MAX = 100;
     - Uses 'final' to prevent modification; typically combined with 'static' for class-level constants.
   * - RustConstant
     - .. code-block:: rust

           const MAX: i32 = 100;
     - Constants are always immutable and must have their types explicitly declared.
   * - PythonConstant
     - .. code-block:: python

           MAX = 100
     - Python does not have true constants; uppercase naming is a convention to indicate immutability.
   * - PhpConstant
     - .. code-block:: php

           define('MAX', 100);
     - Constants can be defined using define() or the 'const' keyword (for class constants or global constants in modern PHP).
   * - BashConstant
     - .. code-block:: bash

           readonly MAX=100
     - The 'readonly' command prevents the variable from being redefined or unset.
   * - PowerShellConstant
     - .. code-block:: powershell

           Set-Variable -Name MAX -Value 100 -Option ReadOnly
     - Using Set-Variable with the ReadOnly option; Constant option is even more restrictive.
   * - CmdConstant
     - .. code-block:: doscon

           set MAX=100
     - Cmd has no native support for constants; developers must manually ensure the value is not changed.
   * - SqlConstant
     - .. code-block:: sql

           DECLARE @MAX INT = 100;
     - T-SQL variables are not strictly constant, but can be treated as such within a batch or procedure.
   * - ErlangConstant
     - .. code-block:: erlang

           -define(MAX, 100).
     - Uses preprocessor macros to define constants; replaced at compile time.
   * - LispConstant
     - .. code-block:: common-lisp

           (defconstant +max+ 100)
     - Defines a global constant; by convention, names are often wrapped in + signs.
   * - XQueryConstant
     - .. code-block:: xquery

           declare variable $MAX as xs:integer := 100;
     - In XQuery, variables declared in the prolog are immutable by default.
   * - CssConstant
     - .. code-block:: css

           --MAX: 100;
     - CSS custom properties act as constants within their scope.
   * - CudaConstant
     - .. code-block:: cpp

           __constant__ int MAX = 100;
     - The __constant__ qualifier places the variable in the constant memory space of the GPU.
   * - X86Constant
     - .. code-block:: nasm

           MAX equ 100
     - Uses the EQU directive to define a symbolic constant (Intel syntax).
   * - RiscvConstant
     - .. code-block:: asm

           .equiv MAX, 100
     - Uses the .equiv or .set directive to define constants.
   * - PrologConstant
     - .. code-block:: prolog

           max(100).
     - Constants are represented as atomic values or facts; Prolog variables themselves are single-assignment.
   * - JavaBytecodeConstant
     - .. code-block:: jasmin

           .field public static final MAX I = 100
     - Constants are represented as static final fields.
   * - CamelConstant
     - .. code-block:: ocaml

           let max = 100
     - Top-level let bindings are effectively constant.
   * - ArmAarch64Constant
     - .. code-block:: asm

           .equiv MAX, 100
     - Uses the .equiv directive to define constants.
   * - GoConstant
     - .. code-block:: go

           const MAX = 100
     - Constants are declared with the 'const' keyword.
   * - HaskellConstant
     - .. code-block:: haskell

           maxVal = 100
     - Top-level bindings are immutable and effectively constant.
   * - TypeScriptConstant
     - .. code-block:: typescript

           const MAX: number = 100;
     - Uses 'const' for immutable declarations.
   * - TclConstant
     - .. code-block:: tcl

           set MAX 100
     - Tcl does not have true constants; naming conventions are used.
   * - CobolConstant
     - .. code-block:: cobol

           01 MAX-VAL PIC 9(3) VALUE 100 CONSTANT.
     - The CONSTANT keyword defines a symbolic constant (COBOL 2002).
   * - FortranConstant
     - .. code-block:: fortran

           integer, parameter :: MAX = 100
     - The 'parameter' attribute makes the variable a named constant.



Addition
--------


:description: Addition of two numeric values.


Parameters:

* syntax: String

* notes: String



.. list-table:: Addition Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CAddition
     - .. code-block:: c

           a + b
     - Standard C operators.
   * - JavaAddition
     - .. code-block:: java

           a + b
     - Standard operators; Math class provides rounding and floor functions.
   * - RustAddition
     - .. code-block:: rust

           a + b
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonAddition
     - .. code-block:: python

           a + b
     - Standard Python arithmetic operator.
   * - PhpAddition
     - .. code-block:: php

           a + b
     - Standard PHP arithmetic operators.
   * - BashAddition
     - .. code-block:: bash

           ((a + b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellAddition
     - .. code-block:: powershell

           a + b
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdAddition
     - .. code-block:: doscon

           set /a res=a+b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlAddition
     - .. code-block:: sql

           a + b
     - Standard SQL arithmetic functions.
   * - ErlangAddition
     - .. code-block:: erlang

           A + B
     - Standard Erlang arithmetic operator.
   * - LispAddition
     - .. code-block:: common-lisp

           (+ a b)
     - Prefix notation for all mathematical operations.
   * - XQueryAddition
     - .. code-block:: xquery

           a + b
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssAddition
     - .. code-block:: css

           calc(a + b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaAddition
     - .. code-block:: cpp

           a + b
     - Same as C; device-side math functions are optimized for GPU.
   * - X86Addition
     - .. code-block:: nasm

           add eax, ebx
     - Operates on registers or memory.
   * - RiscvAddition
     - .. code-block:: asm

           add t0, t1, t2
     - Standard RISC-V instructions.
   * - PrologAddition
     - .. code-block:: prolog

           Res is A + B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeAddition
     - .. code-block:: jasmin

           iadd
     - Stack-based arithmetic instructions for integers.
   * - CamelAddition
     - .. code-block:: ocaml

           a + b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64Addition
     - .. code-block:: asm

           add x0, x1, x2
     - Standard A64 instructions.
   * - GoAddition
     - .. code-block:: go

           a + b
     - Standard arithmetic operators.
   * - HaskellAddition
     - .. code-block:: haskell

           a + b
     - Standard mathematical operators.
   * - TypeScriptAddition
     - .. code-block:: typescript

           a + b
     - Standard JavaScript operators.
   * - TclAddition
     - .. code-block:: tcl

           [expr {$a + $b}]
     - Math operations require the expr command.
   * - CobolAddition
     - .. code-block:: cobol

           ADD A TO B.
     - Adds the value of A to B and stores it in B.
   * - FortranAddition
     - .. code-block:: fortran

           a + b
     - Standard arithmetic operator.



Subtraction
-----------


:description: Subtraction of two numeric values.


Parameters:

* syntax: String

* notes: String



.. list-table:: Subtraction Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CSubtraction
     - .. code-block:: c

           a - b
     - Standard C operators.
   * - JavaSubtraction
     - .. code-block:: java

           a - b
     - Standard operators; Math class provides rounding and floor functions.
   * - RustSubtraction
     - .. code-block:: rust

           a - b
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonSubtraction
     - .. code-block:: python

           a - b
     - Standard Python arithmetic operator.
   * - PhpSubtraction
     - .. code-block:: php

           a - b
     - Standard PHP arithmetic operators.
   * - BashSubtraction
     - .. code-block:: bash

           ((a - b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellSubtraction
     - .. code-block:: powershell

           a - b
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdSubtraction
     - .. code-block:: doscon

           set /a res=a-b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlSubtraction
     - .. code-block:: sql

           a - b
     - Standard SQL arithmetic functions.
   * - ErlangSubtraction
     - .. code-block:: erlang

           A - B
     - Standard Erlang arithmetic operator.
   * - LispSubtraction
     - .. code-block:: common-lisp

           (- a b)
     - Prefix notation for all mathematical operations.
   * - XQuerySubtraction
     - .. code-block:: xquery

           a - b
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssSubtraction
     - .. code-block:: css

           calc(a - b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaSubtraction
     - .. code-block:: cpp

           a - b
     - Same as C; device-side math functions are optimized for GPU.
   * - X86Subtraction
     - .. code-block:: nasm

           sub eax, ebx
     - Operates on registers or memory.
   * - RiscvSubtraction
     - .. code-block:: asm

           sub t0, t1, t2
     - Standard RISC-V instructions.
   * - PrologSubtraction
     - .. code-block:: prolog

           Res is A - B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeSubtraction
     - .. code-block:: jasmin

           isub
     - Stack-based arithmetic instructions for integers.
   * - CamelSubtraction
     - .. code-block:: ocaml

           a - b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64Subtraction
     - .. code-block:: asm

           sub x0, x1, x2
     - Standard A64 instructions.
   * - GoSubtraction
     - .. code-block:: go

           a - b
     - Standard arithmetic operators.
   * - HaskellSubtraction
     - .. code-block:: haskell

           a - b
     - Standard mathematical operators.
   * - TypeScriptSubtraction
     - .. code-block:: typescript

           a - b
     - Standard JavaScript operators.
   * - TclSubtraction
     - .. code-block:: tcl

           [expr {$a - $b}]
     - Math operations require the expr command.
   * - CobolSubtraction
     - .. code-block:: cobol

           SUBTRACT A FROM B.
     - Subtracts A from B and stores it in B.
   * - FortranSubtraction
     - .. code-block:: fortran

           a - b
     - Standard arithmetic operator.



Multiplication
--------------


:description: Multiplication of two numeric values.


Parameters:

* syntax: String

* notes: String



.. list-table:: Multiplication Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CMultiplication
     - .. code-block:: c

           a * b
     - Standard C operators.
   * - JavaMultiplication
     - .. code-block:: java

           a * b
     - Standard operators; Math class provides rounding and floor functions.
   * - RustMultiplication
     - .. code-block:: rust

           a * b
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonMultiplication
     - .. code-block:: python

           a * b
     - Standard Python arithmetic operator.
   * - PhpMultiplication
     - .. code-block:: php

           a * b
     - Standard PHP arithmetic operators.
   * - BashMultiplication
     - .. code-block:: bash

           ((a * b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellMultiplication
     - .. code-block:: powershell

           a * b
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdMultiplication
     - .. code-block:: doscon

           set /a res=a*b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlMultiplication
     - .. code-block:: sql

           a * b
     - Standard SQL arithmetic functions.
   * - ErlangMultiplication
     - .. code-block:: erlang

           A * B
     - Standard Erlang arithmetic operator.
   * - LispMultiplication
     - .. code-block:: common-lisp

           (* a b)
     - Prefix notation for all mathematical operations.
   * - XQueryMultiplication
     - .. code-block:: xquery

           a * b
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssMultiplication
     - .. code-block:: css

           calc(a * b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaMultiplication
     - .. code-block:: cpp

           a * b
     - Same as C; device-side math functions are optimized for GPU.
   * - X86Multiplication
     - .. code-block:: nasm

           imul eax, ebx
     - Operates on registers or memory.
   * - RiscvMultiplication
     - .. code-block:: asm

           mul t0, t1, t2
     - Standard RISC-V M-extension instructions.
   * - PrologMultiplication
     - .. code-block:: prolog

           Res is A * B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeMultiplication
     - .. code-block:: jasmin

           imul
     - Stack-based arithmetic instructions for integers.
   * - CamelMultiplication
     - .. code-block:: ocaml

           a * b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64Multiplication
     - .. code-block:: asm

           mul x0, x1, x2
     - Standard A64 instructions.
   * - GoMultiplication
     - .. code-block:: go

           a * b
     - Standard arithmetic operators.
   * - HaskellMultiplication
     - .. code-block:: haskell

           a * b
     - Standard mathematical operators.
   * - TypeScriptMultiplication
     - .. code-block:: typescript

           a * b
     - Standard JavaScript operators.
   * - TclMultiplication
     - .. code-block:: tcl

           [expr {$a * $b}]
     - Math operations require the expr command.
   * - CobolMultiplication
     - .. code-block:: cobol

           MULTIPLY A BY B.
     - Multiplies A and B and stores the result in B.
   * - FortranMultiplication
     - .. code-block:: fortran

           a * b
     - Standard arithmetic operator.



Division
--------


:description: Division of two numeric values.


Parameters:

* syntax: String

* notes: String



.. list-table:: Division Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CDivision
     - .. code-block:: c

           a / b
     - Standard C operators.
   * - JavaDivision
     - .. code-block:: java

           a / b
     - Standard operators; Math class provides rounding and floor functions.
   * - RustDivision
     - .. code-block:: rust

           a / b
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonDivision
     - .. code-block:: python

           a / b
     - Standard Python arithmetic operator.
   * - PhpDivision
     - .. code-block:: php

           a / b
     - Standard PHP arithmetic operators.
   * - BashDivision
     - .. code-block:: bash

           ((a / b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellDivision
     - .. code-block:: powershell

           a / b
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdDivision
     - .. code-block:: doscon

           set /a res=a/b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlDivision
     - .. code-block:: sql

           a / b
     - Standard SQL arithmetic functions.
   * - ErlangDivision
     - .. code-block:: erlang

           A / B
     - Standard Erlang arithmetic operator.
   * - LispDivision
     - .. code-block:: common-lisp

           (/ a b)
     - Prefix notation for all mathematical operations.
   * - XQueryDivision
     - .. code-block:: xquery

           a div b
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssDivision
     - .. code-block:: css

           calc(a / b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaDivision
     - .. code-block:: cpp

           a / b
     - Same as C; device-side math functions are optimized for GPU.
   * - X86Division
     - .. code-block:: nasm

           idiv ebx
     - Operates on registers or memory.
   * - RiscvDivision
     - .. code-block:: asm

           div t0, t1, t2
     - Standard RISC-V M-extension instructions.
   * - PrologDivision
     - .. code-block:: prolog

           Res is A / B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeDivision
     - .. code-block:: jasmin

           idiv
     - Stack-based arithmetic instructions for integers.
   * - CamelDivision
     - .. code-block:: ocaml

           a / b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64Division
     - .. code-block:: asm

           sdiv x0, x1, x2
     - Standard A64 instructions.
   * - GoDivision
     - .. code-block:: go

           a / b
     - Standard arithmetic operators.
   * - HaskellDivision
     - .. code-block:: haskell

           a / b
     - Haskell uses / for floating-point and 'div' or 'quot' for integer division.
   * - TypeScriptDivision
     - .. code-block:: typescript

           a / b
     - Standard JavaScript operators.
   * - TclDivision
     - .. code-block:: tcl

           [expr {$a / $b}]
     - Math operations require the expr command.
   * - CobolDivision
     - .. code-block:: cobol

           DIVIDE A BY B GIVING C.
     - Divides A by B and stores the quotient in C.
   * - FortranDivision
     - .. code-block:: fortran

           a / b
     - Standard arithmetic operator.



Remainder
---------


:description: The remainder after division of one number by another (modulo).


Parameters:

* syntax: String

* notes: String



.. list-table:: Remainder Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CRemainder
     - .. code-block:: c

           a % b
     - Standard C operators.
   * - JavaRemainder
     - .. code-block:: java

           a % b
     - Standard operators; Math class provides rounding and floor functions.
   * - RustRemainder
     - .. code-block:: rust

           a % b
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonRemainder
     - .. code-block:: python

           a % b
     - Standard Python arithmetic operator.
   * - PhpRemainder
     - .. code-block:: php

           a % b
     - Standard PHP arithmetic operators.
   * - BashRemainder
     - .. code-block:: bash

           ((a % b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellRemainder
     - .. code-block:: powershell

           a % b
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdRemainder
     - .. code-block:: doscon

           set /a res=a%%b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlRemainder
     - .. code-block:: sql

           a % b
     - Standard SQL arithmetic functions.
   * - ErlangRemainder
     - .. code-block:: erlang

           A rem B
     - Standard Erlang arithmetic operator.
   * - LispRemainder
     - .. code-block:: common-lisp

           (mod a b)
     - Prefix notation for all mathematical operations.
   * - XQueryRemainder
     - .. code-block:: xquery

           a mod b
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssRemainder
     - .. code-block:: css

           mod(a, b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaRemainder
     - .. code-block:: cpp

           a % b
     - Same as C; device-side math functions are optimized for GPU.
   * - X86Remainder
     - N/A
     - Operates on registers or memory.
   * - RiscvRemainder
     - .. code-block:: asm

           rem t0, t1, t2
     - Standard RISC-V M-extension instructions.
   * - PrologRemainder
     - .. code-block:: prolog

           Res is A mod B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeRemainder
     - .. code-block:: jasmin

           irem
     - Stack-based arithmetic instructions for integers.
   * - CamelRemainder
     - .. code-block:: ocaml

           a mod b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64Remainder
     - N/A
     - Modulo is typically calculated via sdiv and msub.
   * - GoRemainder
     - .. code-block:: go

           a % b
     - Standard arithmetic operators.
   * - HaskellRemainder
     - .. code-block:: haskell

           a `mod` b
     - Standard mathematical operators.
   * - TypeScriptRemainder
     - .. code-block:: typescript

           a % b
     - Standard JavaScript operators.
   * - TclRemainder
     - .. code-block:: tcl

           [expr {$a % $b}]
     - Math operations require the expr command.
   * - CobolRemainder
     - .. code-block:: cobol

           DIVIDE A BY B GIVING Q REMAINDER R.
     - Calculates both the quotient and the remainder.
   * - FortranRemainder
     - .. code-block:: fortran

           mod(a, b)
     - Built-in function for remainder.



Floor
-----


:description: The largest integer less than or equal to a given number.


Parameters:

* syntax: String

* notes: String



.. list-table:: Floor Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CFloor
     - .. code-block:: c

           floor(a)
     - Standard C operators; floor and round require math.h.
   * - JavaFloor
     - .. code-block:: java

           Math.floor(a)
     - Standard operators; Math class provides rounding and floor functions.
   * - RustFloor
     - .. code-block:: rust

           a.floor()
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonFloor
     - .. code-block:: python

           math.floor(a)
     - Standard Python arithmetic operator.
   * - PhpFloor
     - .. code-block:: php

           floor(a)
     - Standard PHP arithmetic operators.
   * - BashFloor
     - .. code-block:: bash

           echo "a / 1" | bc
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellFloor
     - .. code-block:: powershell

           [Math]::Floor(a)
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdFloor
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlFloor
     - .. code-block:: sql

           FLOOR(a)
     - Standard SQL arithmetic functions.
   * - ErlangFloor
     - .. code-block:: erlang

           floor(A)
     - Standard Erlang arithmetic operator.
   * - LispFloor
     - .. code-block:: common-lisp

           (floor a)
     - Prefix notation for all mathematical operations.
   * - XQueryFloor
     - .. code-block:: xquery

           floor(a)
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssFloor
     - N/A
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaFloor
     - .. code-block:: cpp

           floor(a)
     - Same as C; device-side math functions are optimized for GPU.
   * - X86Floor
     - N/A
     - Operates on registers or memory.
   * - RiscvFloor
     - N/A
     - Standard RISC-V instructions.
   * - PrologFloor
     - .. code-block:: prolog

           Res is floor(A)
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeFloor
     - N/A
     - Stack-based arithmetic instructions for integers.
   * - CamelFloor
     - .. code-block:: ocaml

           floor a
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64Floor
     - N/A
     - Standard A64 instructions.
   * - GoFloor
     - .. code-block:: go

           math.Floor(a)
     - Requires the math package.
   * - HaskellFloor
     - .. code-block:: haskell

           floor a
     - Standard mathematical operators.
   * - TypeScriptFloor
     - .. code-block:: typescript

           Math.floor(a)
     - Standard JavaScript operators.
   * - TclFloor
     - .. code-block:: tcl

           [expr {floor($a)}]
     - Math operations require the expr command.
   * - CobolFloor
     - .. code-block:: cobol

           FUNCTION INTEGER(A)
     - The INTEGER intrinsic function returns the greatest integer <= A.
   * - FortranFloor
     - .. code-block:: fortran

           floor(a)
     - Built-in function for the floor of a real number.



Rounding
--------


:description: Rounding a number to the nearest integer.


Parameters:

* syntax: String

* notes: String



.. list-table:: Rounding Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CRounding
     - .. code-block:: c

           round(a)
     - Standard C operators; floor and round require math.h.
   * - JavaRounding
     - .. code-block:: java

           Math.round(a)
     - Standard operators; Math class provides rounding and floor functions.
   * - RustRounding
     - .. code-block:: rust

           a.round()
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonRounding
     - .. code-block:: python

           round(a)
     - Standard Python arithmetic operator.
   * - PhpRounding
     - .. code-block:: php

           round(a)
     - Standard PHP arithmetic operators.
   * - BashRounding
     - .. code-block:: bash

           printf "%.0f" "$a"
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellRounding
     - .. code-block:: powershell

           [Math]::Round(a)
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdRounding
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlRounding
     - .. code-block:: sql

           ROUND(a, 0)
     - Standard SQL arithmetic functions.
   * - ErlangRounding
     - .. code-block:: erlang

           round(A)
     - Standard Erlang arithmetic operator.
   * - LispRounding
     - .. code-block:: common-lisp

           (round a)
     - Prefix notation for all mathematical operations.
   * - XQueryRounding
     - .. code-block:: xquery

           round(a)
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssRounding
     - .. code-block:: css

           round(a)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaRounding
     - .. code-block:: cpp

           round(a)
     - Same as C; device-side math functions are optimized for GPU.
   * - X86Rounding
     - N/A
     - Operates on registers or memory.
   * - RiscvRounding
     - N/A
     - Standard RISC-V instructions.
   * - PrologRounding
     - .. code-block:: prolog

           Res is round(A)
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeRounding
     - N/A
     - Stack-based arithmetic instructions for integers.
   * - CamelRounding
     - .. code-block:: ocaml

           Float.round a
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64Rounding
     - N/A
     - Standard A64 instructions.
   * - GoRounding
     - .. code-block:: go

           math.Round(a)
     - Requires the math package.
   * - HaskellRounding
     - .. code-block:: haskell

           round a
     - Standard mathematical operators.
   * - TypeScriptRounding
     - .. code-block:: typescript

           Math.round(a)
     - Standard JavaScript operators.
   * - TclRounding
     - .. code-block:: tcl

           [expr {round($a)}]
     - Math operations require the expr command.
   * - CobolRounding
     - .. code-block:: cobol

           ADD A TO B ROUNDED.
     - The ROUNDED phrase specifies that any fractional part should be rounded.
   * - FortranRounding
     - .. code-block:: fortran

           nint(a)
     - Built-in function for the nearest integer.



Increment
---------


:description: Increasing the value of a variable by one.


Parameters:

* syntax: String

* notes: String



.. list-table:: Increment Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CIncrement
     - .. code-block:: c

           a++
     - Standard C operators.
   * - JavaIncrement
     - .. code-block:: java

           a++
     - Standard operators; Math class provides rounding and floor functions.
   * - RustIncrement
     - .. code-block:: rust

           a += 1
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonIncrement
     - .. code-block:: python

           a += 1
     - Standard Python arithmetic operator.
   * - PhpIncrement
     - .. code-block:: php

           a++
     - Standard PHP arithmetic operators.
   * - BashIncrement
     - .. code-block:: bash

           ((a++))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellIncrement
     - .. code-block:: powershell

           a++
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdIncrement
     - .. code-block:: doscon

           set /a a+=1
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlIncrement
     - .. code-block:: sql

           a + 1
     - Standard SQL arithmetic functions.
   * - ErlangIncrement
     - .. code-block:: erlang

           A + 1
     - Standard Erlang arithmetic operator.
   * - LispIncrement
     - .. code-block:: common-lisp

           (1+ a)
     - Prefix notation for all mathematical operations.
   * - XQueryIncrement
     - .. code-block:: xquery

           a + 1
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssIncrement
     - .. code-block:: css

           calc(a + 1)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaIncrement
     - .. code-block:: cpp

           a++
     - Same as C; device-side math functions are optimized for GPU.
   * - X86Increment
     - .. code-block:: nasm

           inc eax
     - Operates on registers or memory.
   * - RiscvIncrement
     - .. code-block:: asm

           addi t0, t0, 1
     - Standard RISC-V instructions.
   * - PrologIncrement
     - .. code-block:: prolog

           Res is A + 1
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeIncrement
     - .. code-block:: jasmin

           iinc index, 1
     - Stack-based arithmetic instructions for integers.
   * - CamelIncrement
     - .. code-block:: ocaml

           a + 1
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64Increment
     - .. code-block:: asm

           add x0, x0, #1
     - Standard A64 instructions.
   * - GoIncrement
     - .. code-block:: go

           a++
     - Go supports postfix increment as a statement, not an expression.
   * - HaskellIncrement
     - .. code-block:: haskell

           a + 1
     - No native increment operator; use addition.
   * - TypeScriptIncrement
     - .. code-block:: typescript

           a++
     - Standard JavaScript operators.
   * - TclIncrement
     - .. code-block:: tcl

           incr a
     - The incr command increments an integer variable.
   * - CobolIncrement
     - .. code-block:: cobol

           ADD 1 TO A.
     - Increments the value of A by 1.
   * - FortranIncrement
     - .. code-block:: fortran

           a = a + 1
     - No native increment operator; uses assignment.



Decrement
---------


:description: Decreasing the value of a variable by one.


Parameters:

* syntax: String

* notes: String



.. list-table:: Decrement Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CDecrement
     - .. code-block:: c

           a--
     - Standard C operators.
   * - JavaDecrement
     - .. code-block:: java

           a--
     - Standard operators; Math class provides rounding and floor functions.
   * - RustDecrement
     - .. code-block:: rust

           a -= 1
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonDecrement
     - .. code-block:: python

           a -= 1
     - Standard Python arithmetic operator.
   * - PhpDecrement
     - .. code-block:: php

           a--
     - Standard PHP arithmetic operators.
   * - BashDecrement
     - .. code-block:: bash

           ((a--))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellDecrement
     - .. code-block:: powershell

           a--
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdDecrement
     - .. code-block:: doscon

           set /a a-=1
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlDecrement
     - .. code-block:: sql

           a - 1
     - Standard SQL arithmetic functions.
   * - ErlangDecrement
     - .. code-block:: erlang

           A - 1
     - Standard Erlang arithmetic operator.
   * - LispDecrement
     - .. code-block:: common-lisp

           (1- a)
     - Prefix notation for all mathematical operations.
   * - XQueryDecrement
     - .. code-block:: xquery

           a - 1
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssDecrement
     - .. code-block:: css

           calc(a - 1)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaDecrement
     - .. code-block:: cpp

           a--
     - Same as C; device-side math functions are optimized for GPU.
   * - X86Decrement
     - .. code-block:: nasm

           dec eax
     - Operates on registers or memory.
   * - RiscvDecrement
     - .. code-block:: asm

           addi t0, t0, -1
     - Standard RISC-V instructions.
   * - PrologDecrement
     - .. code-block:: prolog

           Res is A - 1
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeDecrement
     - .. code-block:: jasmin

           iinc index, -1
     - Stack-based arithmetic instructions for integers.
   * - CamelDecrement
     - .. code-block:: ocaml

           a - 1
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64Decrement
     - .. code-block:: asm

           sub x0, x0, #1
     - Standard A64 instructions.
   * - GoDecrement
     - .. code-block:: go

           a--
     - Go supports postfix decrement as a statement, not an expression.
   * - HaskellDecrement
     - .. code-block:: haskell

           a - 1
     - No native decrement operator; use subtraction.
   * - TypeScriptDecrement
     - .. code-block:: typescript

           a--
     - Standard JavaScript operators.
   * - TclDecrement
     - .. code-block:: tcl

           incr a -1
     - The incr command can decrement if a negative value is provided.
   * - CobolDecrement
     - .. code-block:: cobol

           SUBTRACT 1 FROM A.
     - Decrements the value of A by 1.
   * - FortranDecrement
     - .. code-block:: fortran

           a = a - 1
     - No native decrement operator; uses assignment.



LeftShift
---------


:description: Shifting the bits of a number to the left.


Parameters:

* syntax: String

* notes: String



.. list-table:: LeftShift Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CLeftShift
     - .. code-block:: c

           a << b
     - Standard C operators; floor and round require math.h.
   * - JavaLeftShift
     - .. code-block:: java

           a << b
     - Standard operators; Math class provides rounding and floor functions.
   * - RustLeftShift
     - .. code-block:: rust

           a << b
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonLeftShift
     - .. code-block:: python

           a << b
     - Standard Python arithmetic operator.
   * - PhpLeftShift
     - .. code-block:: php

           a << b
     - Standard PHP arithmetic operators.
   * - BashLeftShift
     - .. code-block:: bash

           ((a << b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellLeftShift
     - .. code-block:: powershell

           a -shl b
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdLeftShift
     - .. code-block:: doscon

           set /a res=a<<b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlLeftShift
     - N/A
     - Standard SQL arithmetic functions.
   * - ErlangLeftShift
     - .. code-block:: erlang

           A bsl B
     - Standard Erlang arithmetic operator.
   * - LispLeftShift
     - .. code-block:: common-lisp

           (ash a b)
     - Prefix notation for all mathematical operations.
   * - XQueryLeftShift
     - N/A
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssLeftShift
     - N/A
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaLeftShift
     - .. code-block:: cpp

           a << b
     - Same as C; device-side math functions are optimized for GPU.
   * - X86LeftShift
     - .. code-block:: nasm

           shl eax, cl
     - Operates on registers or memory.
   * - RiscvLeftShift
     - .. code-block:: asm

           sll t0, t1, t2
     - Standard RISC-V instructions.
   * - PrologLeftShift
     - .. code-block:: prolog

           Res is A << B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeLeftShift
     - .. code-block:: jasmin

           ishl
     - Stack-based arithmetic instructions for integers.
   * - CamelLeftShift
     - .. code-block:: ocaml

           a lsl b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64LeftShift
     - .. code-block:: asm

           lsl x0, x1, x2
     - Standard A64 instructions.
   * - GoLeftShift
     - .. code-block:: go

           a << b
     - Standard bitwise shift operators.
   * - HaskellLeftShift
     - .. code-block:: haskell

           shiftL a b
     - Requires Data.Bits.
   * - TypeScriptLeftShift
     - .. code-block:: typescript

           a << b
     - Standard JavaScript operators.
   * - TclLeftShift
     - .. code-block:: tcl

           [expr {$a << $b}]
     - Math operations require the expr command.
   * - CobolLeftShift
     - N/A
     - COBOL does not have native bitwise shift operators.
   * - FortranLeftShift
     - .. code-block:: fortran

           ishft(a, b)
     - The ishft function performs a logical shift.



RightShift
----------


:description: Shifting the bits of a number to the right.


Parameters:

* syntax: String

* notes: String



.. list-table:: RightShift Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CRightShift
     - .. code-block:: c

           a >> b
     - Standard C operators; floor and round require math.h.
   * - JavaRightShift
     - .. code-block:: java

           a >> b
     - Standard operators; Math class provides rounding and floor functions.
   * - RustRightShift
     - .. code-block:: rust

           a >> b
     - Operators for primitive types; floor and round are methods on float types.
   * - PythonRightShift
     - .. code-block:: python

           a >> b
     - Standard Python arithmetic operator.
   * - PhpRightShift
     - .. code-block:: php

           a >> b
     - Standard PHP arithmetic operators.
   * - BashRightShift
     - .. code-block:: bash

           ((a >> b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - PowerShellRightShift
     - .. code-block:: powershell

           a -shr b
     - Standard operators; uses .NET Math class for advanced functions.
   * - CmdRightShift
     - .. code-block:: doscon

           set /a res=a>>b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - SqlRightShift
     - N/A
     - Standard SQL arithmetic functions.
   * - ErlangRightShift
     - .. code-block:: erlang

           A bsr B
     - Standard Erlang arithmetic operator.
   * - LispRightShift
     - .. code-block:: common-lisp

           (ash a -b)
     - Prefix notation for all mathematical operations.
   * - XQueryRightShift
     - N/A
     - Uses 'div' for division and 'idiv' for integer division.
   * - CssRightShift
     - N/A
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - CudaRightShift
     - .. code-block:: cpp

           a >> b
     - Same as C; device-side math functions are optimized for GPU.
   * - X86RightShift
     - .. code-block:: nasm

           shr eax, cl
     - Operates on registers or memory.
   * - RiscvRightShift
     - .. code-block:: asm

           srl t0, t1, t2
     - Standard RISC-V instructions.
   * - PrologRightShift
     - .. code-block:: prolog

           Res is A >> B
     - Uses the 'is' operator to evaluate arithmetic expressions.
   * - JavaBytecodeRightShift
     - .. code-block:: jasmin

           ishr
     - Stack-based arithmetic instructions for integers.
   * - CamelRightShift
     - .. code-block:: ocaml

           a lsr b
     - Standard operators; OCaml uses separate operators for floats (e.g., +.).
   * - ArmAarch64RightShift
     - .. code-block:: asm

           lsr x0, x1, x2
     - Standard A64 instructions.
   * - GoRightShift
     - .. code-block:: go

           a >> b
     - Standard bitwise shift operators.
   * - HaskellRightShift
     - .. code-block:: haskell

           shiftR a b
     - Requires Data.Bits.
   * - TypeScriptRightShift
     - .. code-block:: typescript

           a >> b
     - Standard JavaScript operators.
   * - TclRightShift
     - .. code-block:: tcl

           [expr {$a >> $b}]
     - Math operations require the expr command.
   * - CobolRightShift
     - N/A
     - COBOL does not have native bitwise shift operators.
   * - FortranRightShift
     - .. code-block:: fortran

           ishft(a, -b)
     - Negative shift counts in ishft perform a right shift.



BitAnd
------


:description: Bitwise AND operation.


Parameters:

* syntax: String

* notes: String



.. list-table:: BitAnd Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CBitAnd
     - .. code-block:: c

           a & b
     - Standard bitwise operators in C.
   * - JavaBitAnd
     - .. code-block:: java

           a & b
     - Standard bitwise operators in Java.
   * - RustBitAnd
     - .. code-block:: rust

           a & b
     - Bitwise NOT uses the ! operator.
   * - PythonBitAnd
     - .. code-block:: python

           a & b
     - Standard bitwise operators.
   * - PhpBitAnd
     - .. code-block:: php

           a & b
     - Standard bitwise operators.
   * - BashBitAnd
     - .. code-block:: bash

           ((a & b))
     - Bitwise operations within double parentheses.
   * - PowerShellBitAnd
     - .. code-block:: powershell

           a -band b
     - Uses prefixed operators for bitwise logic.
   * - CmdBitAnd
     - .. code-block:: doscon

           set /a res="a & b"
     - Bitwise operators within set /a expressions.
   * - SqlBitAnd
     - .. code-block:: sql

           a & b
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - ErlangBitAnd
     - .. code-block:: erlang

           A band B
     - Bitwise operators are keywords (band, bor, bxor, bnot, bsl, bsr).
   * - LispBitAnd
     - .. code-block:: common-lisp

           (logand a b)
     - Common Lisp bitwise operations; ash is used for both left and right shifts.
   * - XQueryBitAnd
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - CssBitAnd
     - N/A
     - CSS does not support bitwise operations.
   * - CudaBitAnd
     - .. code-block:: cpp

           a & b
     - Standard bitwise operators supported in kernels.
   * - X86BitAnd
     - .. code-block:: nasm

           and eax, ebx
     - Bitwise instructions for general-purpose registers.
   * - RiscvBitAnd
     - .. code-block:: asm

           and t0, t1, t2
     - Core bitwise logical and shift instructions.
   * - PrologBitAnd
     - .. code-block:: prolog

           Res is A /\ B
     - Bitwise operators within arithmetic expressions.
   * - JavaBytecodeBitAnd
     - .. code-block:: jasmin

           iand
     - Stack-based bitwise instructions; NOT is implemented as XOR with -1.
   * - CamelBitAnd
     - .. code-block:: ocaml

           a land b
     - Bitwise operators are keywords.
   * - ArmAarch64BitAnd
     - .. code-block:: asm

           and x0, x1, x2
     - Core bitwise logical and shift instructions.
   * - GoBitAnd
     - .. code-block:: go

           a & b
     - Bitwise NOT is implemented using the bitwise XOR operator with no left operand.
   * - HaskellBitAnd
     - .. code-block:: haskell

           a .&. b
     - Requires Data.Bits.
   * - TypeScriptBitAnd
     - .. code-block:: typescript

           a & b
     - Standard bitwise operators.
   * - TclBitAnd
     - .. code-block:: tcl

           [expr {$a & $b}]
     - Math operations require the expr command.
   * - CobolBitAnd
     - N/A
     - Not natively supported in standard COBOL.
   * - FortranBitAnd
     - .. code-block:: fortran

           iand(a, b)
     - Built-in function for bitwise AND.



BitOr
-----


:description: Bitwise OR operation.


Parameters:

* syntax: String

* notes: String



.. list-table:: BitOr Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CBitOr
     - .. code-block:: c

           a | b
     - Standard bitwise operators in C.
   * - JavaBitOr
     - .. code-block:: java

           a | b
     - Standard bitwise operators in Java.
   * - RustBitOr
     - .. code-block:: rust

           a | b
     - Bitwise NOT uses the ! operator.
   * - PythonBitOr
     - .. code-block:: python

           a | b
     - Standard bitwise operators.
   * - PhpBitOr
     - .. code-block:: php

           a | b
     - Standard bitwise operators.
   * - BashBitOr
     - .. code-block:: bash

           ((a | b))
     - Bitwise operations within double parentheses.
   * - PowerShellBitOr
     - .. code-block:: powershell

           a -bor b
     - Uses prefixed operators for bitwise logic.
   * - CmdBitOr
     - .. code-block:: doscon

           set /a res="a | b"
     - Bitwise operators within set /a expressions.
   * - SqlBitOr
     - .. code-block:: sql

           a | b
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - ErlangBitOr
     - .. code-block:: erlang

           A bor B
     - Bitwise operators are keywords (band, bor, bxor, bnot, bsl, bsr).
   * - LispBitOr
     - .. code-block:: common-lisp

           (logior a b)
     - Common Lisp bitwise operations; ash is used for both left and right shifts.
   * - XQueryBitOr
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - CssBitOr
     - N/A
     - CSS does not support bitwise operations.
   * - CudaBitOr
     - .. code-block:: cpp

           a | b
     - Standard bitwise operators supported in kernels.
   * - X86BitOr
     - .. code-block:: nasm

           or eax, ebx
     - Bitwise instructions for general-purpose registers.
   * - RiscvBitOr
     - .. code-block:: asm

           or t0, t1, t2
     - Core bitwise logical and shift instructions.
   * - PrologBitOr
     - .. code-block:: prolog

           Res is A \/ B
     - Bitwise operators within arithmetic expressions.
   * - JavaBytecodeBitOr
     - .. code-block:: jasmin

           ior
     - Stack-based bitwise instructions; NOT is implemented as XOR with -1.
   * - CamelBitOr
     - .. code-block:: ocaml

           a lor b
     - Bitwise operators are keywords.
   * - ArmAarch64BitOr
     - .. code-block:: asm

           orr x0, x1, x2
     - Core bitwise logical and shift instructions.
   * - GoBitOr
     - .. code-block:: go

           a | b
     - Bitwise NOT is implemented using the bitwise XOR operator with no left operand.
   * - HaskellBitOr
     - .. code-block:: haskell

           a .|. b
     - Requires Data.Bits.
   * - TypeScriptBitOr
     - .. code-block:: typescript

           a | b
     - Standard bitwise operators.
   * - TclBitOr
     - .. code-block:: tcl

           [expr {$a | $b}]
     - Math operations require the expr command.
   * - CobolBitOr
     - N/A
     - Not natively supported in standard COBOL.
   * - FortranBitOr
     - .. code-block:: fortran

           ior(a, b)
     - Built-in function for bitwise OR.



BitXor
------


:description: Bitwise XOR operation.


Parameters:

* syntax: String

* notes: String



.. list-table:: BitXor Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CBitXor
     - .. code-block:: c

           a ^ b
     - Standard bitwise operators in C.
   * - JavaBitXor
     - .. code-block:: java

           a ^ b
     - Standard bitwise operators in Java.
   * - RustBitXor
     - .. code-block:: rust

           a ^ b
     - Bitwise NOT uses the ! operator.
   * - PythonBitXor
     - .. code-block:: python

           a ^ b
     - Standard bitwise operators.
   * - PhpBitXor
     - .. code-block:: php

           a ^ b
     - Standard bitwise operators.
   * - BashBitXor
     - .. code-block:: bash

           ((a ^ b))
     - Bitwise operations within double parentheses.
   * - PowerShellBitXor
     - .. code-block:: powershell

           a -bxor b
     - Uses prefixed operators for bitwise logic.
   * - CmdBitXor
     - .. code-block:: doscon

           set /a res="a ^ b"
     - Bitwise operators within set /a expressions.
   * - SqlBitXor
     - .. code-block:: sql

           a ^ b
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - ErlangBitXor
     - .. code-block:: erlang

           A bxor B
     - Bitwise operators are keywords (band, bor, bxor, bnot, bsl, bsr).
   * - LispBitXor
     - .. code-block:: common-lisp

           (logxor a b)
     - Common Lisp bitwise operations; ash is used for both left and right shifts.
   * - XQueryBitXor
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - CssBitXor
     - N/A
     - CSS does not support bitwise operations.
   * - CudaBitXor
     - .. code-block:: cpp

           a ^ b
     - Standard bitwise operators supported in kernels.
   * - X86BitXor
     - .. code-block:: nasm

           xor eax, ebx
     - Bitwise instructions for general-purpose registers.
   * - RiscvBitXor
     - .. code-block:: asm

           xor t0, t1, t2
     - Core bitwise logical and shift instructions.
   * - PrologBitXor
     - .. code-block:: prolog

           Res is A xor B
     - Bitwise operators within arithmetic expressions.
   * - JavaBytecodeBitXor
     - .. code-block:: jasmin

           ixor
     - Stack-based bitwise instructions; NOT is implemented as XOR with -1.
   * - CamelBitXor
     - .. code-block:: ocaml

           a lxor b
     - Bitwise operators are keywords.
   * - ArmAarch64BitXor
     - .. code-block:: asm

           eor x0, x1, x2
     - Core bitwise logical and shift instructions.
   * - GoBitXor
     - .. code-block:: go

           a ^ b
     - Bitwise NOT is implemented using the bitwise XOR operator with no left operand.
   * - HaskellBitXor
     - .. code-block:: haskell

           xor a b
     - Requires Data.Bits.
   * - TypeScriptBitXor
     - .. code-block:: typescript

           a ^ b
     - Standard bitwise operators.
   * - TclBitXor
     - .. code-block:: tcl

           [expr {$a ^ $b}]
     - Math operations require the expr command.
   * - CobolBitXor
     - N/A
     - Not natively supported in standard COBOL.
   * - FortranBitXor
     - .. code-block:: fortran

           ieor(a, b)
     - Built-in function for bitwise XOR.



BitNot
------


:description: Bitwise NOT operation (bitwise complement).


Parameters:

* syntax: String

* notes: String



.. list-table:: BitNot Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CBitNot
     - .. code-block:: c

           ~a
     - Standard bitwise operators in C.
   * - JavaBitNot
     - .. code-block:: java

           ~a
     - Standard bitwise operators in Java.
   * - RustBitNot
     - .. code-block:: rust

           !a
     - Bitwise NOT uses the ! operator.
   * - PythonBitNot
     - .. code-block:: python

           ~a
     - Standard bitwise operators.
   * - PhpBitNot
     - .. code-block:: php

           ~a
     - Standard bitwise operators.
   * - BashBitNot
     - .. code-block:: bash

           ((~a))
     - Bitwise operations within double parentheses.
   * - PowerShellBitNot
     - .. code-block:: powershell

           -bnot a
     - Uses prefixed operators for bitwise logic.
   * - CmdBitNot
     - .. code-block:: doscon

           set /a res="~a"
     - Bitwise operators within set /a expressions.
   * - SqlBitNot
     - .. code-block:: sql

           ~a
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - ErlangBitNot
     - .. code-block:: erlang

           bnot A
     - Bitwise operators are keywords (band, bor, bxor, bnot, bsl, bsr).
   * - LispBitNot
     - .. code-block:: common-lisp

           (lognot a)
     - Common Lisp bitwise operations; ash is used for both left and right shifts.
   * - XQueryBitNot
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - CssBitNot
     - N/A
     - CSS does not support bitwise operations.
   * - CudaBitNot
     - .. code-block:: cpp

           ~a
     - Standard bitwise operators supported in kernels.
   * - X86BitNot
     - .. code-block:: nasm

           not eax
     - Bitwise instructions for general-purpose registers.
   * - RiscvBitNot
     - .. code-block:: asm

           not t0, t1
     - Core bitwise logical and shift instructions.
   * - PrologBitNot
     - .. code-block:: prolog

           Res is \ A
     - Bitwise operators within arithmetic expressions.
   * - JavaBytecodeBitNot
     - .. code-block:: jasmin

           iconst_m1
           ixor
     - Stack-based bitwise instructions; NOT is implemented as XOR with -1.
   * - CamelBitNot
     - .. code-block:: ocaml

           lnot a
     - Bitwise operators are keywords.
   * - ArmAarch64BitNot
     - .. code-block:: asm

           mvn x0, x1
     - Core bitwise logical and shift instructions.
   * - GoBitNot
     - .. code-block:: go

           ^a
     - Bitwise NOT is implemented using the bitwise XOR operator with no left operand.
   * - HaskellBitNot
     - .. code-block:: haskell

           complement a
     - Requires Data.Bits.
   * - TypeScriptBitNot
     - .. code-block:: typescript

           ~a
     - Standard bitwise operators.
   * - TclBitNot
     - .. code-block:: tcl

           [expr {~$a}]
     - Math operations require the expr command.
   * - CobolBitNot
     - N/A
     - Not natively supported in standard COBOL.
   * - FortranBitNot
     - .. code-block:: fortran

           not(a)
     - Built-in function for bitwise NOT.



Float4VectorMultiplication
--------------------------


:description: Element-wise multiplication of two 4-component floating-point vectors.


Parameters:

* syntax: String

* notes: String



.. list-table:: Float4VectorMultiplication Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CFloat4VectorMultiplication
     - .. code-block:: c

           for (int i = 0; i < 4; i++) c[i] = a[i] * b[i];
     - Standard C requires a loop for element-wise multiplication of arrays.
   * - JavaFloat4VectorMultiplication
     - .. code-block:: java

           for (int i = 0; i < 4; i++) c[i] = a[i] * b[i];
     - Standard Java uses loops; the Vector API (incubating) provides SIMD support.
   * - RustFloat4VectorMultiplication
     - .. code-block:: rust

           for i in 0..4 { c[i] = a[i] * b[i]; }
     - Usually implemented with loops or iterator zipping; crates like nalgebra or glam provide dedicated types.
   * - PythonFloat4VectorMultiplication
     - .. code-block:: python

           c = [ai * bi for ai, bi in zip(a, b)]
     - Uses list comprehension with zip; NumPy is preferred for performance.
   * - PhpFloat4VectorMultiplication
     - .. code-block:: php

           $c = array_map(fn($ai, $bi) => $ai * $bi, $a, $b);
     - Uses array_map with an arrow function.
   * - BashFloat4VectorMultiplication
     - .. code-block:: bash

           for i in {0..3}; do c[$i]=$(echo "${a[$i]} * ${b[$i]}" | bc); done
     - Requires external tools like bc for floating-point arithmetic.
   * - PowerShellFloat4VectorMultiplication
     - .. code-block:: powershell

           $c = 0..3 | ForEach-Object { $a[$_] * $b[$_] }
     - Uses a pipeline and ForEach-Object to iterate over indices.
   * - CmdFloat4VectorMultiplication
     - N/A
     - Cmd does not natively support floating-point arithmetic or vectors.
   * - SqlFloat4VectorMultiplication
     - .. code-block:: sql

           SELECT a1*b1, a2*b2, a3*b3, a4*b4
     - SQL typically operates on columns; vector operations are dialect-specific.
   * - ErlangFloat4VectorMultiplication
     - .. code-block:: erlang

           [Ai * Bi || {Ai, Bi} <- lists:zip(A, B)].
     - Uses list comprehension and lists:zip.
   * - LispFloat4VectorMultiplication
     - .. code-block:: common-lisp

           (mapcar #'* a b)
     - Applies the multiplication function element-wise to the lists.
   * - XQueryFloat4VectorMultiplication
     - .. code-block:: xquery

           for $i in 1 to 4 return $a[$i] * $b[$i]
     - Uses a for expression to iterate over indices.
   * - CssFloat4VectorMultiplication
     - N/A
     - CSS does not support vector types or element-wise multiplication.
   * - CudaFloat4VectorMultiplication
     - .. code-block:: cpp

           c.x = a.x * b.x; c.y = a.y * b.y; c.z = a.z * b.z; c.w = a.w * b.w;
     - The float4 type in CUDA is a struct; multiplication is done per-component.
   * - X86Float4VectorMultiplication
     - .. code-block:: nasm

           mulps xmm0, xmm1
     - SSE instruction for packed single-precision floating-point multiplication (4 floats).
   * - RiscvFloat4VectorMultiplication
     - .. code-block:: asm

           vsetvli t0, x0, e32, m1
           vfmul.vv v1, v2, v3
     - Uses the RISC-V Vector extension (RVV) for element-wise float multiplication.
   * - PrologFloat4VectorMultiplication
     - .. code-block:: prolog

           maplist(multiply, A, B, C).
     - Uses maplist to apply a predicate element-wise.
   * - JavaBytecodeFloat4VectorMultiplication
     - .. code-block:: jasmin

           fload_1
           fload_2
           fmul
     - Java Bytecode uses fmul for individual floats; vectorization is typically handled by the JIT.
   * - CamelFloat4VectorMultiplication
     - .. code-block:: ocaml

           Array.map2 (fun ai bi -> ai *. bi) a b
     - OCaml uses specific operators for floating-point arithmetic (*.).
   * - ArmAarch64Float4VectorMultiplication
     - .. code-block:: asm

           fmul v0.4s, v1.4s, v2.4s
     - NEON instruction for 4-lane single-precision floating-point multiplication.
   * - GoFloat4VectorMultiplication
     - .. code-block:: go

           for i := range a { c[i] = a[i] * b[i] }
     - Iterates over the indices of the slices or arrays.
   * - HaskellFloat4VectorMultiplication
     - .. code-block:: haskell

           zipWith (*) a b
     - Applies multiplication element-wise to two lists.
   * - TypeScriptFloat4VectorMultiplication
     - .. code-block:: typescript

           const c = a.map((v, i) => v * b[i]);
     - Uses the Array.map method with the index parameter.
   * - TclFloat4VectorMultiplication
     - .. code-block:: tcl

           foreach ai $a bi $b { lappend c [expr {$ai * $bi}] }
     - Uses a multi-variable foreach loop to zip and multiply.
   * - CobolFloat4VectorMultiplication
     - .. code-block:: cobol

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 4
               COMPUTE C(I) = A(I) * B(I)
           END-PERFORM.
     - Requires a loop over the array elements.
   * - FortranFloat4VectorMultiplication
     - .. code-block:: fortran

           c = a * b
     - Fortran supports element-wise operations on arrays natively.



Float4VectorDotProduct
----------------------


:description: Scalar product of two 4-component floating-point vectors.


Parameters:

* syntax: String

* notes: String



.. list-table:: Float4VectorDotProduct Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CFloat4VectorDotProduct
     - .. code-block:: c

           float dot = 0; for (int i = 0; i < 4; i++) dot += a[i] * b[i];
     - Standard C implementation using a loop and an accumulator.
   * - JavaFloat4VectorDotProduct
     - .. code-block:: java

           float dot = 0; for (int i = 0; i < 4; i++) dot += a[i] * b[i];
     - Standard Java implementation using a loop; Vector API provides optimized dot product.
   * - RustFloat4VectorDotProduct
     - .. code-block:: rust

           let dot: f32 = a.iter().zip(b.iter()).map(|(x, y)| x * y).sum();
     - Functional approach using iterators, zip, map, and sum.
   * - PythonFloat4VectorDotProduct
     - .. code-block:: python

           dot = sum(ai * bi for ai, bi in zip(a, b))
     - Uses a generator expression with zip and sum; NumPy's np.dot is standard for performance.
   * - PhpFloat4VectorDotProduct
     - .. code-block:: php

           $dot = array_sum(array_map(fn($ai, $bi) => $ai * $bi, $a, $b));
     - Combines array_map and array_sum.
   * - BashFloat4VectorDotProduct
     - .. code-block:: bash

           dot=0; for i in {0..3}; do dot=$(echo "$dot + (${a[$i]} * ${b[$i]})" | bc); done
     - Requires bc for floating-point accumulation.
   * - PowerShellFloat4VectorDotProduct
     - .. code-block:: powershell

           $dot = 0; 0..3 | ForEach-Object { $dot += $a[$_] * $b[$_] }
     - Iterates over indices and accumulates the product.
   * - CmdFloat4VectorDotProduct
     - N/A
     - Cmd has no native support for floating-point arithmetic.
   * - SqlFloat4VectorDotProduct
     - .. code-block:: sql

           SELECT a1*b1 + a2*b2 + a3*b3 + a4*b4
     - Calculated by manually summing component-wise products.
   * - ErlangFloat4VectorDotProduct
     - .. code-block:: erlang

           Dot = lists:foldl(fun({Ai, Bi}, Acc) -> Ai * Bi + Acc end, 0.0, lists:zip(A, B)).
     - Uses lists:zip and lists:foldl to calculate the sum of products.
   * - LispFloat4VectorDotProduct
     - .. code-block:: common-lisp

           (reduce #'+ (mapcar #'* a b))
     - Maps multiplication over lists and reduces the result with addition.
   * - XQueryFloat4VectorDotProduct
     - .. code-block:: xquery

           sum(for $i in 1 to 4 return $a[$i] * $b[$i])
     - Uses the built-in sum() function over a sequence of products.
   * - CssFloat4VectorDotProduct
     - N/A
     - CSS does not support vector dot products.
   * - CudaFloat4VectorDotProduct
     - .. code-block:: cpp

           float dot = a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w;
     - Manually calculated using the components of the float4 struct.
   * - X86Float4VectorDotProduct
     - .. code-block:: nasm

           dpps xmm0, xmm1, 0xF1
     - SSE4.1 instruction for Dot Product of Packed Singles. 0xF1 mask controls input/output lanes.
   * - RiscvFloat4VectorDotProduct
     - .. code-block:: asm

           vsetvli t0, x0, e32, m1
           vfmul.vv v1, v2, v3
           vfredusum.vs v4, v1, v5
     - Uses vfmul.vv for multiplication and vfredusum.vs for a horizontal sum.
   * - PrologFloat4VectorDotProduct
     - .. code-block:: prolog

           dot_product(A, B, Dot) :- maplist(multiply, A, B, Products), sum_list(Products, Dot).
     - Commonly implemented using maplist and sum_list.
   * - JavaBytecodeFloat4VectorDotProduct
     - .. code-block:: jasmin

           fload_1 ; a[i]
           fload_2 ; b[i]
           fmul
           fadd
     - Dot product is built by repeating fmul and fadd instructions on the stack.
   * - CamelFloat4VectorDotProduct
     - .. code-block:: ocaml

           let dot = List.fold_left2 (fun acc ai bi -> acc +. ai *. bi) 0.0 a b
     - Uses fold_left2 for efficient simultaneous iteration over two lists.
   * - ArmAarch64Float4VectorDotProduct
     - .. code-block:: asm

           fmul v0.4s, v1.4s, v2.4s
           faddp v0.4s, v0.4s, v0.4s
           faddp s0, v0.2s
     - Uses fmul for component-wise multiplication and faddp for horizontal pairwise addition.
   * - GoFloat4VectorDotProduct
     - .. code-block:: go

           dot := 0.0
           for i := range a { dot += a[i] * b[i] }
     - Standard imperative loop for accumulating the sum of products.
   * - HaskellFloat4VectorDotProduct
     - .. code-block:: haskell

           dot = sum $ zipWith (*) a b
     - Pure functional approach using zipWith, multiplication, and sum.
   * - TypeScriptFloat4VectorDotProduct
     - .. code-block:: typescript

           const dot = a.reduce((acc, v, i) => acc + v * b[i], 0);
     - Uses Array.reduce to accumulate the product of elements.
   * - TclFloat4VectorDotProduct
     - .. code-block:: tcl

           set dot 0
           foreach ai $a bi $b { set dot [expr {$dot + ($ai * $bi)}] }
     - Uses a multi-variable foreach loop to multiply and accumulate using expr.
   * - CobolFloat4VectorDotProduct
     - .. code-block:: cobol

           MOVE 0 TO DOT-PRODUCT.
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 4
               COMPUTE DOT-PRODUCT = DOT-PRODUCT + (A(I) * B(I))
           END-PERFORM.
     - Calculated by accumulating products in a loop.
   * - FortranFloat4VectorDotProduct
     - .. code-block:: fortran

           res = dot_product(a, b)
     - The dot_product intrinsic function calculates the dot product of two vectors.



Float4VectorCrossProduct
------------------------


:description: 3D cross product of two 4-component floating-point vectors (using the first three components).


Parameters:

* syntax: String

* notes: String



.. list-table:: Float4VectorCrossProduct Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - CFloat4VectorCrossProduct
     - .. code-block:: c

           c[0] = a[1]*b[2] - a[2]*b[1];
           c[1] = a[2]*b[0] - a[0]*b[2];
           c[2] = a[0]*b[1] - a[1]*b[0];
           c[3] = 0.0f;
     - Calculated manually for the first three components.
   * - JavaFloat4VectorCrossProduct
     - .. code-block:: java

           c[0] = a[1]*b[2] - a[2]*b[1];
           c[1] = a[2]*b[0] - a[0]*b[2];
           c[2] = a[0]*b[1] - a[1]*b[0];
           c[3] = 0.0f;
     - Standard Java implementation using array indexing.
   * - RustFloat4VectorCrossProduct
     - .. code-block:: rust

           c[0] = a[1]*b[2] - a[2]*b[1];
           c[1] = a[2]*b[0] - a[0]*b[2];
           c[2] = a[0]*b[1] - a[1]*b[0];
           c[3] = 0.0;
     - Direct implementation; libraries like glam provide a cross() method.
   * - PythonFloat4VectorCrossProduct
     - .. code-block:: python

           c = [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0], 0.0]
     - Uses list indexing; NumPy's np.cross is typically used for 3D vectors.
   * - PhpFloat4VectorCrossProduct
     - .. code-block:: php

           $c = [$a[1]*$b[2] - $a[2]*$b[1], $a[2]*$b[0] - $a[0]*$b[2], $a[0]*$b[1] - $a[1]*$b[0], 0.0];
     - Calculated using array indexing and the cross product formula.
   * - BashFloat4VectorCrossProduct
     - .. code-block:: bash

           c[0]=$(echo "${a[1]}*${b[2]} - ${a[2]}*${b[1]}" | bc)
           c[1]=$(echo "${a[2]}*${b[0]} - ${a[0]}*${b[2]}" | bc)
           c[2]=$(echo "${a[0]}*${b[1]} - ${a[1]}*${b[0]}" | bc)
           c[3]=0
     - Requires bc for floating-point calculations.
   * - PowerShellFloat4VectorCrossProduct
     - .. code-block:: powershell

           $c = @($a[1]*$b[2] - $a[2]*$b[1], $a[2]*$b[0] - $a[0]*$b[2], $a[0]*$b[1] - $a[1]*$b[0], 0.0)
     - Uses array literal syntax with expressions.
   * - CmdFloat4VectorCrossProduct
     - N/A
     - Cmd does not support floating-point arithmetic.
   * - SqlFloat4VectorCrossProduct
     - .. code-block:: sql

           SELECT a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1, 0.0
     - Computed using column-wise arithmetic.
   * - ErlangFloat4VectorCrossProduct
     - .. code-block:: erlang

           C = [lists:nth(2,A)*lists:nth(3,B) - lists:nth(3,A)*lists:nth(2,B),
                lists:nth(3,A)*lists:nth(1,B) - lists:nth(1,A)*lists:nth(3,B),
                lists:nth(1,A)*lists:nth(2,B) - lists:nth(2,A)*lists:nth(1,B), 0.0].
     - Uses lists:nth (1-indexed) to access vector components.
   * - LispFloat4VectorCrossProduct
     - .. code-block:: common-lisp

           (list (- (* (nth 1 a) (nth 2 b)) (* (nth 2 a) (nth 1 b)))
                 (- (* (nth 2 a) (nth 0 b)) (* (nth 0 a) (nth 2 b)))
                 (- (* (nth 0 a) (nth 1 b)) (* (nth 1 a) (nth 0 b)))
                 0.0)
     - Uses nth and basic arithmetic functions.
   * - XQueryFloat4VectorCrossProduct
     - .. code-block:: xquery

           ($a[2]*$b[3] - $a[3]*$b[2], $a[3]*$b[1] - $a[1]*$b[3], $a[1]*$b[2] - $a[2]*$b[1], 0.0)
     - Uses sequence indexing (1-indexed).
   * - CssFloat4VectorCrossProduct
     - N/A
     - CSS does not support vector cross products.
   * - CudaFloat4VectorCrossProduct
     - .. code-block:: cpp

           c.x = a.y*b.z - a.z*b.y; c.y = a.z*b.x - a.x*b.z; c.z = a.x*b.y - a.y*b.x;
     - Manually calculated using the components of the float4 struct.
   * - X86Float4VectorCrossProduct
     - .. code-block:: nasm

           movaps xmm2, xmm0
           shufps xmm0, xmm0, 0xC9 ; y z x w
           shufps xmm2, xmm2, 0xD2 ; z x y w
           movaps xmm3, xmm1
           shufps xmm1, xmm1, 0xD2 ; z x y w
           shufps xmm3, xmm3, 0xC9 ; y z x w
           mulps xmm0, xmm1
           mulps xmm2, xmm3
           subps xmm0, xmm2
     - A common SSE sequence for 3D cross product using shuffles and multiplications.
   * - RiscvFloat4VectorCrossProduct
     - N/A
     - RISC-V Vector extension does not have a dedicated cross product instruction; requires multiple operations.
   * - PrologFloat4VectorCrossProduct
     - .. code-block:: prolog

           cross_product([A1,A2,A3|_], [B1,B2,B3|_], [C1,C2,C3,0.0]) :-
               C1 is A2*B3 - A3*B2,
               C2 is A3*B1 - A1*B3,
               C3 is A1*B2 - A2*B1.
     - Implemented using list pattern matching and arithmetic evaluation.
   * - JavaBytecodeFloat4VectorCrossProduct
     - .. code-block:: jasmin

           fload 1 ; ay
           fload 6 ; bz
           fmul
           fload 2 ; az
           fload 5 ; by
           fmul
           fsub ; -> cx
           fload 2 ; az
           fload 4 ; bx
           fmul
           fload 0 ; ax
           fload 6 ; bz
           fmul
           fsub ; -> cy
           fload 0 ; ax
           fload 5 ; by
           fmul
           fload 1 ; ay
           fload 4 ; bx
           fmul
           fsub ; -> cz
     - Calculated component-wise using stack operations.
   * - CamelFloat4VectorCrossProduct
     - .. code-block:: ocaml

           [| a.(1) *. b.(2) -. a.(2) *. b.(1);
              a.(2) *. b.(0) -. a.(0) *. b.(2);
              a.(0) *. b.(1) -. a.(1) *. b.(0);
              0.0 |]
     - Uses array indexing and floating-point operators (*. and -.).
   * - ArmAarch64Float4VectorCrossProduct
     - .. code-block:: asm

           fmul s2, v0.s[1], v1.s[2]
           fmls s2, v0.s[2], v1.s[1]
           fmul s3, v0.s[2], v1.s[0]
           fmls s3, v0.s[0], v1.s[2]
           fmul s4, v0.s[0], v1.s[1]
           fmls s4, v0.s[1], v1.s[0]
     - Calculated component-wise using scalar NEON instructions.
   * - GoFloat4VectorCrossProduct
     - .. code-block:: go

           c := [4]float64{
               a[1]*b[2] - a[2]*b[1],
               a[2]*b[0] - a[0]*b[2],
               a[0]*b[1] - a[1]*b[0],
               0,
           }
     - Calculated using array indexing in a composite literal.
   * - HaskellFloat4VectorCrossProduct
     - .. code-block:: haskell

           cross [a1,a2,a3,_] [b1,b2,b3,_] = [a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1, 0.0]
     - Pure functional implementation using pattern matching.
   * - TypeScriptFloat4VectorCrossProduct
     - .. code-block:: typescript

           const c = [
               a[1]*b[2] - a[2]*b[1],
               a[2]*b[0] - a[0]*b[2],
               a[0]*b[1] - a[1]*b[0],
               0
           ];
     - Uses array indexing to compute the components.
   * - TclFloat4VectorCrossProduct
     - .. code-block:: tcl

           set c [list [expr {[lindex $a 1]*[lindex $b 2] - [lindex $a 2]*[lindex $b 1]}] \
                       [expr {[lindex $a 2]*[lindex $b 0] - [lindex $a 0]*[lindex $b 2]}] \
                       [expr {[lindex $a 0]*[lindex $b 1] - [lindex $a 1]*[lindex $b 0]}] 0.0]
     - Uses expr and lindex for calculation.
   * - CobolFloat4VectorCrossProduct
     - .. code-block:: cobol

           COMPUTE C(1) = A(2) * B(3) - A(3) * B(2).
           COMPUTE C(2) = A(3) * B(1) - A(1) * B(3).
           COMPUTE C(3) = A(1) * B(2) - A(2) * B(1).
     - Calculated component-wise using COMPUTE.
   * - FortranFloat4VectorCrossProduct
     - .. code-block:: fortran

           c = [a(2)*b(3) - a(3)*b(2), &
                a(3)*b(1) - a(1)*b(3), &
                a(1)*b(2) - a(2)*b(1), 0.0]
     - Calculated component-wise using an array constructor.