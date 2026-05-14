PowerShell Pivot View
=====================

.. list-table:: PowerShell Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: powershell

           $x = 42
     - Variables start with a dollar sign.
   * - CollectionDefinition
     - .. code-block:: powershell

           $a = 1, 2, 3
     - The comma operator creates an array in PowerShell.
   * - AssociativeArrayDefinition
     - .. code-block:: powershell

           $h = @{ a = 1; b = 2 }
     - Hashtables are created using the @{ } syntax.
   * - SwitchCase
     - .. code-block:: powershell

           switch ($x) {
               1 { "one" }
               2 { "two" }
               default { "none" }
           }
     - Versatile switch statement that supports multiple types and patterns.
   * - IfElse
     - .. code-block:: powershell

           if ($x -gt 0) {
               return 1
           } else {
               return 0
           }
     - Uses PowerShell comparison operators (e.g., -gt).
   * - Loop
     - .. code-block:: powershell

           while ($x -gt 0) {
               $x = $x - 1
           }
     - Standard while loop with C-like block syntax.
   * - FunctionDefinition
     - .. code-block:: powershell

           function add($a, $b) {
               return $a + $b
           }
     - Uses 'function' keyword; parameters are variables starting with $.
   * - ProcedureDefinition
     - .. code-block:: powershell

           function log-message($msg) {
               Write-Host $msg
           }
     - Functions without a return statement output nothing to the pipeline.
   * - TryCatch
     - .. code-block:: powershell

           try {
               do_something
           } catch {
               handle_error($_)
           }
     - PowerShell supports try-catch-finally blocks; $_ (or $PSItem) refers to the current error.
   * - Raise
     - .. code-block:: powershell

           throw "Error"
     - Uses 'throw' to create a terminating error.
   * - SingleLineComment
     - .. code-block:: powershell

           # comment
     - Standard PowerShell single-line comment.
   * - MultiLineComment
     - .. code-block:: powershell

           <# line 1
              line 2 #>
     - Uses <# and #> for block comments.
   * - Print
     - .. code-block:: powershell

           Write-Host "Hello, World!"
     - Write-Host outputs directly to the console host.
   * - Import
     - .. code-block:: powershell

           Import-Module ActiveDirectory
     - Loads a module into the current session.
   * - Constant
     - .. code-block:: powershell

           Set-Variable -Name MAX -Value 100 -Option ReadOnly
     - Using Set-Variable with the ReadOnly option; Constant option is even more restrictive.
   * - Addition
     - .. code-block:: powershell

           a + b
     - Standard operators; uses .NET Math class for advanced functions.
   * - Subtraction
     - .. code-block:: powershell

           a - b
     - Standard operators; uses .NET Math class for advanced functions.
   * - Multiplication
     - .. code-block:: powershell

           a * b
     - Standard operators; uses .NET Math class for advanced functions.
   * - Division
     - .. code-block:: powershell

           a / b
     - Standard operators; uses .NET Math class for advanced functions.
   * - Remainder
     - .. code-block:: powershell

           a % b
     - Standard operators; uses .NET Math class for advanced functions.
   * - Floor
     - .. code-block:: powershell

           [Math]::Floor(a)
     - Standard operators; uses .NET Math class for advanced functions.
   * - Rounding
     - .. code-block:: powershell

           [Math]::Round(a)
     - Standard operators; uses .NET Math class for advanced functions.
   * - Increment
     - .. code-block:: powershell

           a++
     - Standard operators; uses .NET Math class for advanced functions.
   * - Decrement
     - .. code-block:: powershell

           a--
     - Standard operators; uses .NET Math class for advanced functions.
   * - LeftShift
     - .. code-block:: powershell

           a -shl b
     - Standard operators; uses .NET Math class for advanced functions.
   * - RightShift
     - .. code-block:: powershell

           a -shr b
     - Standard operators; uses .NET Math class for advanced functions.
   * - BitAnd
     - .. code-block:: powershell

           a -band b
     - Uses prefixed operators for bitwise logic.
   * - BitOr
     - .. code-block:: powershell

           a -bor b
     - Uses prefixed operators for bitwise logic.
   * - BitXor
     - .. code-block:: powershell

           a -bxor b
     - Uses prefixed operators for bitwise logic.
   * - BitNot
     - .. code-block:: powershell

           -bnot a
     - Uses prefixed operators for bitwise logic.
   * - Float4VectorMultiplication
     - .. code-block:: powershell

           $c = 0..3 | ForEach-Object { $a[$_] * $b[$_] }
     - Uses a pipeline and ForEach-Object to iterate over indices.
   * - Float4VectorDotProduct
     - .. code-block:: powershell

           $dot = 0; 0..3 | ForEach-Object { $dot += $a[$_] * $b[$_] }
     - Iterates over indices and accumulates the product.
   * - Float4VectorCrossProduct
     - .. code-block:: powershell

           $c = @($a[1]*$b[2] - $a[2]*$b[1], $a[2]*$b[0] - $a[0]*$b[2], $a[0]*$b[1] - $a[1]*$b[0], 0.0)
     - Uses array literal syntax with expressions.
   * - ForLoop
     - .. code-block:: powershell

           for ($i = 0; $i -lt 10; $i++) {
               # body
           }
     - Standard C-style for loop with PowerShell comparison operators.
   * - ForEach
     - .. code-block:: powershell

           foreach ($item in $collection) {
               # body
           }
     - Powershell's foreach statement iterates over a collection of objects.
   * - Equal
     - .. code-block:: powershell

           $a -eq $b
     - PowerShell uses prefixed operators for comparison.
   * - NotEqual
     - .. code-block:: powershell

           $a -ne $b
     -
   * - GreaterThan
     - .. code-block:: powershell

           $a -gt $b
     -
   * - SetFiltering
     - .. code-block:: powershell

           $b = $a | Where-Object { $_ -gt 0 }
     - Uses the Where-Object cmdlet (alias ?) in a pipeline.
   * - SetJoin
     - .. code-block:: powershell

           foreach ($a in $listA) {
               foreach ($b in $listB) {
                   if ($a.id -eq $b.id) { [PSCustomObject]@{A=$a; B=$b} }
               }
           }
     - Typically implemented using nested foreach loops.