PowerShell Pivot View
=====================

.. list-table:: PowerShell Pivot Table
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
     - .. code-block:: powershell

           $x = 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Variables start with a dollar sign.
   * - IfElse
     - .. code-block:: powershell

           if ($x -gt 0) {
               return 1
           } else {
               return 0
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses PowerShell comparison operators (e.g., -gt).
   * - Loop
     - .. code-block:: powershell

           while ($x -gt 0) {
               $x = $x - 1
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard while loop with C-like block syntax.
   * - FunctionDefinition
     - .. code-block:: powershell

           function add($a, $b) {
               return $a + $b
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'function' keyword; parameters are variables starting with $.
   * - ProcedureDefinition
     - .. code-block:: powershell

           function log-message($msg) {
               Write-Host $msg
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions without a return statement output nothing to the pipeline.
   * - TryCatch
     - .. code-block:: powershell

           try {
               do_something
           } catch {
               handle_error($_)
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - PowerShell supports try-catch-finally blocks; $_ (or $PSItem) refers to the current error.
   * - Raise
     - .. code-block:: powershell

           throw "Error"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'throw' to create a terminating error.
   * - SingleLineComment
     - .. code-block:: powershell

           # comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard PowerShell single-line comment.
   * - MultiLineComment
     - .. code-block:: powershell

           <# line 1
              line 2 #>
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses <# and #> for block comments.
   * - Print
     - .. code-block:: powershell

           Write-Host "Hello, World!"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Write-Host outputs directly to the console host.
   * - Import
     - .. code-block:: powershell

           Import-Module ActiveDirectory
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Loads a module into the current session.
   * - SwitchCase
     - .. code-block:: powershell

           switch ($x) {
               1 { "one" }
               2 { "two" }
               default { "none" }
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Versatile switch statement that supports multiple types and patterns.
   * - Constant
     - .. code-block:: powershell

           Set-Variable -Name MAX -Value 100 -Option ReadOnly
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Using Set-Variable with the ReadOnly option; Constant option is even more restrictive.
   * - Addition
     - .. code-block:: powershell

           a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - Subtraction
     - .. code-block:: powershell

           a - b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - Multiplication
     - .. code-block:: powershell

           a * b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - Division
     - .. code-block:: powershell

           a / b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - Remainder
     - .. code-block:: powershell

           a % b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - Floor
     - .. code-block:: powershell

           [Math]::Floor(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - Rounding
     - .. code-block:: powershell

           [Math]::Round(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - Increment
     - .. code-block:: powershell

           a++
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - Decrement
     - .. code-block:: powershell

           a--
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - LeftShift
     - .. code-block:: powershell

           a -shl b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - RightShift
     - .. code-block:: powershell

           a -shr b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; uses .NET Math class for advanced functions.
   * - Bitwise
     - N/A
     - .. code-block:: powershell

           a -band b
     - .. code-block:: powershell

           a -bor b
     - .. code-block:: powershell

           a -bxor b
     - .. code-block:: powershell

           -bnot a
     - .. code-block:: powershell

           a -shl b
     - .. code-block:: powershell

           a -shr b
     - Uses prefixed operators for bitwise logic.