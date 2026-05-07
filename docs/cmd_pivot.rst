Cmd Pivot View
==============

.. list-table:: Cmd Pivot Table
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
     - .. code-block:: doscon

           set x=42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Used in Windows Command Prompt.
   * - IfElse
     - .. code-block:: doscon

           if %x% GTR 0 (exit /b 1) else (exit /b 0)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses GTR for 'greater than'; blocks are enclosed in parentheses.
   * - Loop
     - .. code-block:: doscon

           :loop
           if %x% GTR 0 (set /a x=x-1 & goto loop)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Loops are typically implemented using labels and goto.
   * - FunctionDefinition
     - .. code-block:: doscon

           :add
           set /a res=%~1+%~2
           exit /b %res%
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions are labels; called with 'call :label'; arguments are %1, %2.
   * - ProcedureDefinition
     - .. code-block:: doscon

           :log_message
           echo %~1
           goto :eof
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Procedures are labels called with 'call'; they return using 'goto :eof' or 'exit /b'.
   * - TryCatch
     - .. code-block:: doscon

           do_something || call :handle_error
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Cmd uses || to execute a command if the previous one failed (non-zero errorlevel).
   * - Raise
     - .. code-block:: doscon

           exit /b 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Sets the errorlevel and exits the current script or function.
   * - SingleLineComment
     - .. code-block:: doscon

           REM comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses REM or :: (label hack) for comments.
   * - MultiLineComment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Command Prompt does not support multi-line comments.
   * - Print
     - .. code-block:: doscon

           echo Hello, World!
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Echo displays messages in Windows Command Prompt.
   * - Import
     - .. code-block:: doscon

           call other.cmd
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The 'call' command is used to run another batch file from within one.
   * - SwitchCase
     - .. code-block:: doscon

           if "%x%"=="1" (goto :one) else if "%x%"=="2" (goto :two) else (goto :none)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Cmd does not have a native switch; it is typically simulated with if/else or goto.
   * - Constant
     - .. code-block:: doscon

           set MAX=100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Cmd has no native support for constants; developers must manually ensure the value is not changed.
   * - Addition
     - .. code-block:: doscon

           set /a res=a+b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Subtraction
     - .. code-block:: doscon

           set /a res=a-b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Multiplication
     - .. code-block:: doscon

           set /a res=a*b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Division
     - .. code-block:: doscon

           set /a res=a/b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Remainder
     - .. code-block:: doscon

           set /a res=a%%b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Floor
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Rounding
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Increment
     - .. code-block:: doscon

           set /a a+=1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Decrement
     - .. code-block:: doscon

           set /a a-=1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - LeftShift
     - .. code-block:: doscon

           set /a res=a<<b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - RightShift
     - .. code-block:: doscon

           set /a res=a>>b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses set /a for integer arithmetic; no native floating point support.
   * - Bitwise
     - N/A
     - .. code-block:: doscon

           set /a res="a & b"
     - .. code-block:: doscon

           set /a res="a | b"
     - .. code-block:: doscon

           set /a res="a ^ b"
     - .. code-block:: doscon

           set /a res="~a"
     - .. code-block:: doscon

           set /a res="a << b"
     - .. code-block:: doscon

           set /a res="a >> b"
     - Bitwise operators within set /a expressions.