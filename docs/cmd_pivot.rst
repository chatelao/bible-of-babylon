Cmd Pivot View
==============

.. list-table:: Cmd Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: doscon

           set x=42
     - Used in Windows Command Prompt.
   * - SwitchCase
     - .. code-block:: doscon

           if "%x%"=="1" (goto :one) else if "%x%"=="2" (goto :two) else (goto :none)
     - Cmd does not have a native switch; it is typically simulated with if/else or goto.
   * - IfElse
     - .. code-block:: doscon

           if %x% GTR 0 (exit /b 1) else (exit /b 0)
     - Uses GTR for 'greater than'; blocks are enclosed in parentheses.
   * - Loop
     - .. code-block:: doscon

           :loop
           if %x% GTR 0 (set /a x=x-1 & goto loop)
     - Loops are typically implemented using labels and goto.
   * - FunctionDefinition
     - .. code-block:: doscon

           :add
           set /a res=%~1+%~2
           exit /b %res%
     - Functions are labels; called with 'call :label'; arguments are %1, %2.
   * - ProcedureDefinition
     - .. code-block:: doscon

           :log_message
           echo %~1
           goto :eof
     - Procedures are labels called with 'call'; they return using 'goto :eof' or 'exit /b'.
   * - TryCatch
     - .. code-block:: doscon

           do_something || call :handle_error
     - Cmd uses || to execute a command if the previous one failed (non-zero errorlevel).
   * - Raise
     - .. code-block:: doscon

           exit /b 1
     - Sets the errorlevel and exits the current script or function.
   * - SingleLineComment
     - .. code-block:: doscon

           REM comment
     - Uses REM or :: (label hack) for comments.
   * - MultiLineComment
     - N/A
     - Command Prompt does not support multi-line comments.
   * - Print
     - .. code-block:: doscon

           echo Hello, World!
     - Echo displays messages in Windows Command Prompt.
   * - Import
     - .. code-block:: doscon

           call other.cmd
     - The 'call' command is used to run another batch file from within one.
   * - Constant
     - .. code-block:: doscon

           set MAX=100
     - Cmd has no native support for constants; developers must manually ensure the value is not changed.
   * - Addition
     - .. code-block:: doscon

           set /a res=a+b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Subtraction
     - .. code-block:: doscon

           set /a res=a-b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Multiplication
     - .. code-block:: doscon

           set /a res=a*b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Division
     - .. code-block:: doscon

           set /a res=a/b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Remainder
     - .. code-block:: doscon

           set /a res=a%%b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Floor
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Rounding
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Increment
     - .. code-block:: doscon

           set /a a+=1
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Decrement
     - .. code-block:: doscon

           set /a a-=1
     - Uses set /a for integer arithmetic; no native floating point support.
   * - LeftShift
     - .. code-block:: doscon

           set /a res=a<<b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - RightShift
     - .. code-block:: doscon

           set /a res=a>>b
     - Uses set /a for integer arithmetic; no native floating point support.
   * - BitAnd
     - .. code-block:: doscon

           set /a res="a & b"
     - Bitwise operators within set /a expressions.
   * - BitOr
     - .. code-block:: doscon

           set /a res="a | b"
     - Bitwise operators within set /a expressions.
   * - BitXor
     - .. code-block:: doscon

           set /a res="a ^ b"
     - Bitwise operators within set /a expressions.
   * - BitNot
     - .. code-block:: doscon

           set /a res="~a"
     - Bitwise operators within set /a expressions.
   * - Float4VectorMultiplication
     - N/A
     - Cmd does not natively support floating-point arithmetic or vectors.
   * - Float4VectorDotProduct
     - N/A
     - Cmd has no native support for floating-point arithmetic.
   * - Float4VectorCrossProduct
     - N/A
     - Cmd does not support floating-point arithmetic.
   * - ForLoop
     - .. code-block:: doscon

           for /L %%i in (0,1,9) do (
               rem body
           )
     - The /L switch is used for iterative loops (start, step, end).
   * - Equal
     - .. code-block:: doscon

           if %a% EQU %b%
     - Comparison operators are used within if statements.
   * - NotEqual
     - .. code-block:: doscon

           if %a% NEQ %b%
     -
   * - GreaterThan
     - .. code-block:: doscon

           if %a% GTR %b%
     -