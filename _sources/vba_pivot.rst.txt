VBA Pivot View
==============

.. list-table:: VBA Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: vb.net

           Dim x As Integer
           x = 42
     - Variables are declared using 'Dim'; statically typed with 'As Type'.
   * - CollectionDefinition
     - .. code-block:: vb.net

           Dim arr As Variant
           arr = Array(1, 2, 3)
     - Arrays can be initialized using the Array() function or static array declaration.
   * - AssociativeArrayDefinition
     - .. code-block:: vb.net

           Dim dict As Object
           Set dict = CreateObject("Scripting.Dictionary")
           dict.Add "a", 1
     - Requires Scripting.Dictionary or Collection object for key-value pairs.
   * - Sort
     - .. code-block:: vb.net

           ' Manual sorting implementation
     - VBA has no built-in array sort method; requires custom sorting algorithm or Excel Range.Sort.
   * - Distinct
     - .. code-block:: vb.net

           ' Using Scripting.Dictionary
     - Commonly achieved by inserting elements as keys into a Dictionary.
   * - ToCharDate
     - .. code-block:: vb.net

           Format(dateVal, "dd.mm.yyyy")
     - Uses the Format function with date format specifiers.
   * - ToCharDateTimezone
     - .. code-block:: vb.net

           Format(dateVal, "yyyy-mm-dd hh:nn:ss")
     - VBA Date type does not store timezone information; timezone must be handled separately.
   * - ToCharNumberThousandSeparator
     - .. code-block:: vb.net

           Format(num, "#,##0")
     - Uses the Format function with digit placeholders and comma.
   * - ToCharNumberNegativeBrackets
     - .. code-block:: vb.net

           Format(num, "#,##0;(#,##0)")
     - Format function supports positive;negative sections separated by a semicolon.
   * - ToCharNumberFixedDecimals
     - .. code-block:: vb.net

           Format(num, "0.00")
     - Formats a number with a fixed number of decimal places.
   * - ToDate
     - .. code-block:: vb.net

           CDate("31.12.2023")
     - Converts string or numeric expressions to a Date using locale settings or CDate/DateValue.
   * - ForEach
     - .. code-block:: vb.net

           For Each item In collection
               ' body
           Next item
     - Iterates over items in a collection or array.
   * - Equal
     - .. code-block:: vb.net

           a = b
     - In VBA, = is used for both assignment and equality comparison.
   * - NotEqual
     - .. code-block:: vb.net

           a <> b
     - VBA uses <> for inequality.
   * - GreaterThan
     - .. code-block:: vb.net

           a > b
     - Standard greater than operator.
   * - LogicalAnd
     - .. code-block:: vb.net

           a And b
     - The And operator is bitwise when used with numbers, logical when used with booleans.
   * - LogicalOr
     - .. code-block:: vb.net

           a Or b
     - The Or operator performs logical or bitwise disjunction.
   * - LogicalXor
     - .. code-block:: vb.net

           a Xor b
     - VBA provides a native Xor logical/bitwise operator.
   * - ProcedureDefinition
     - .. code-block:: vb.net

           Sub LogMessage(msg As String)
               Debug.Print msg
           End Sub
     - Procedures in VBA are defined with 'Sub' and return no value.
   * - FunctionDefinition
     - .. code-block:: vb.net

           Function Add(a As Integer, b As Integer) As Integer
               Add = a + b
           End Function
     - Functions return values by assigning to the function name.
   * - IfElse
     - .. code-block:: vb.net

           If x > 0 Then
               ' then branch
           Else
               ' else branch
           End If
     - Uses If-Then-Else-End If block syntax.
   * - SwitchCase
     - .. code-block:: vb.net

           Select Case x
               Case 1
                   ' case 1
               Case 2
                   ' case 2
               Case Else
                   ' default
           End Select
     - VBA uses Select Case statements for multi-way branching.
   * - Loop
     - .. code-block:: vb.net

           Do While x > 0
               x = x - 1
           Loop
     - Do While ... Loop repeatedly executes while condition is true.
   * - ForLoop
     - .. code-block:: vb.net

           For i = 0 To 9
               ' body
           Next i
     - Standard count-controlled loop in VBA.
   * - LineContinuation
     - .. code-block:: vb.net

            _
     - VBA uses a space followed by an underscore character for line continuation.
   * - TryCatch
     - .. code-block:: vb.net

           On Error GoTo ErrorHandler
               do_something
               Exit Sub
           ErrorHandler:
               handle Err
     - VBA error handling uses 'On Error GoTo' labels.
   * - Raise
     - .. code-block:: vb.net

           Err.Raise vbObjectError + 513, "Source", "Error"
     - Uses Err.Raise to throw errors.
   * - Thread
     - N/A
     - VBA is single-threaded; multi-threading is not natively supported.
   * - SendMessage
     - N/A
     - Not natively supported in VBA.
   * - ReceiveMessage
     - N/A
     - Not natively supported in VBA.
   * - MutexDefinition
     - .. code-block:: vb.net

           Dim hMutex As LongPtr
           hMutex = CreateMutex(0, 0, "MyMutex")
     - Requires Windows API CreateMutex function declaration.
   * - MutexLock
     - .. code-block:: vb.net

           WaitForSingleObject hMutex, INFINITE
     - Uses Win32 API WaitForSingleObject.
   * - MutexUnlock
     - .. code-block:: vb.net

           ReleaseMutex hMutex
     - Uses Win32 API ReleaseMutex.
   * - SemaphoreDefinition
     - .. code-block:: vb.net

           Dim hSem As LongPtr
           hSem = CreateSemaphore(0, 1, 10, "MySem")
     - Requires Windows API CreateSemaphore function declaration.
   * - SemaphoreWait
     - .. code-block:: vb.net

           WaitForSingleObject hSem, INFINITE
     - Uses Win32 API WaitForSingleObject.
   * - SemaphoreSignal
     - .. code-block:: vb.net

           ReleaseSemaphore hSem, 1, 0
     - Uses Win32 API ReleaseSemaphore.
   * - SingleLineComment
     - .. code-block:: vb.net

           ' comment
     - Single-line comments start with an apostrophe.
   * - MultiLineComment
     - N/A
     - VBA does not support multi-line comments; multiple single-line apostrophe comments must be used.
   * - Print
     - .. code-block:: vb.net

           Debug.Print "Hello, World!"
     - Outputs text to the Immediate Window.
   * - Import
     - .. code-block:: vb.net

           ' Tools -> References
     - External libraries are imported via IDE References.
   * - Constant
     - .. code-block:: vb.net

           Const MAX As Integer = 100
     - Declared using the Const keyword.
   * - Addition
     - .. code-block:: vb.net

           a + b
     - Standard arithmetic operator.
   * - Subtraction
     - .. code-block:: vb.net

           a - b
     - Standard arithmetic operator.
   * - Multiplication
     - .. code-block:: vb.net

           a * b
     - Standard arithmetic operator.
   * - Division
     - .. code-block:: vb.net

           a / b
     - Standard floating-point division; use \ for integer division.
   * - Remainder
     - .. code-block:: vb.net

           a Mod b
     - The Mod operator returns the remainder of division.
   * - Floor
     - .. code-block:: vb.net

           Int(a)
     - Int() returns the greatest integer <= number.
   * - Rounding
     - .. code-block:: vb.net

           Round(a, 0)
     - Round() performs banker's rounding.
   * - Increment
     - .. code-block:: vb.net

           a = a + 1
     - VBA does not support ++ or += operators.
   * - Decrement
     - .. code-block:: vb.net

           a = a - 1
     - VBA does not support -- or -= operators.
   * - LeftShift
     - .. code-block:: vb.net

           a * (2 ^ b)
     - No bitwise shift operator in VBA; simulated via multiplication by powers of 2.
   * - RightShift
     - .. code-block:: vb.net

           a \ (2 ^ b)
     - Simulated via integer division by powers of 2.
   * - BitAnd
     - .. code-block:: vb.net

           a And b
     - The And operator performs bitwise AND when applied to numeric operands.
   * - BitOr
     - .. code-block:: vb.net

           a Or b
     - The Or operator performs bitwise OR when applied to numeric operands.
   * - BitXor
     - .. code-block:: vb.net

           a Xor b
     - The Xor operator performs bitwise XOR when applied to numeric operands.
   * - BitNot
     - .. code-block:: vb.net

           Not a
     - The Not operator performs bitwise NOT when applied to numeric operands.
   * - Float4VectorMultiplication
     - .. code-block:: vb.net

           For i = 0 To 3: c(i) = a(i) * b(i): Next i
     - Element-wise multiplication using a loop.
   * - Float4VectorDotProduct
     - .. code-block:: vb.net

           dot = a(0)*b(0) + a(1)*b(1) + a(2)*b(2) + a(3)*b(3)
     - Calculated by summing the products of corresponding components.
   * - Float4VectorCrossProduct
     - .. code-block:: vb.net

           c(0) = a(1)*b(2) - a(2)*b(1)
           c(1) = a(2)*b(0) - a(0)*b(2)
           c(2) = a(0)*b(1) - a(1)*b(0)
           c(3) = 0.0
     - Calculated component-wise for 3D cross product.
   * - SetFiltering
     - .. code-block:: vb.net

           For Each item In col
               If condition(item) Then res.Add item
           Next item
     - Iterates over a collection and adds matching elements to a result collection.
   * - SetJoin
     - .. code-block:: vb.net

           For Each a In colA
               For Each b In colB
                   If a.id = b.id Then ' join logic
               Next b
           Next a
     - Nested loops used to join elements from two collections.
