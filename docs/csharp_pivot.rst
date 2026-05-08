CSharp Pivot View
=================

.. list-table:: CSharp Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: csharp

           int x = 42;
     - Static typing, similar to C++ and Java.
   * - IfElse
     - .. code-block:: csharp

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C-style if-else statement.
   * - SwitchCase
     - .. code-block:: csharp

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - Standard C-style switch; supports pattern matching in newer versions.
   * - Loop
     - .. code-block:: csharp

           while (x > 0) {
               x = x - 1;
           }
     - Standard while loop.
   * - ForLoop
     - .. code-block:: csharp

           for (int i = 0; i < 10; i++) {
               // body
           }
     - Standard C-style for loop.
   * - FunctionDefinition
     - .. code-block:: csharp

           public int Add(int a, int b) {
               return a + b;
           }
     - Methods are typically defined within classes.
   * - ProcedureDefinition
     - .. code-block:: csharp

           public void LogMessage(string msg) {
               Console.WriteLine(msg);
           }
     - Uses the 'void' keyword for procedures.
   * - TryCatch
     - .. code-block:: csharp

           try {
               do_something();
           } catch (Exception ex) {
               handle(ex);
           }
     - Standard try-catch block for exception handling.
   * - Raise
     - .. code-block:: csharp

           throw new Exception("Error");
     - Uses the 'throw' keyword to raise an exception.
   * - Thread
     - .. code-block:: csharp

           new Thread(() => { do_work(); }).start();
     - Uses the System.Threading.Thread class; Task.Run is often preferred in modern C#.
   * - SendMessage
     - .. code-block:: csharp

           await channel.Writer.WriteAsync(42);
     - Using System.Threading.Channels for asynchronous message passing.
   * - ReceiveMessage
     - .. code-block:: csharp

           var msg = await channel.Reader.ReadAsync();
           handle(msg);
     - Using System.Threading.Channels for asynchronous message receiving.
   * - SingleLineComment
     - .. code-block:: csharp

           // comment
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: csharp

           /* line 1
              line 2 */
     - Standard block comment.
   * - Print
     - .. code-block:: csharp

           Console.WriteLine("Hello, World!");
     - Outputs text to the console with a trailing newline.
   * - Import
     - .. code-block:: csharp

           using System.Collections.Generic;
     - The 'using' directive imports namespaces.
   * - Constant
     - .. code-block:: csharp

           const int Max = 100;
     - The 'const' keyword defines a compile-time constant.
   * - Addition
     - .. code-block:: csharp

           a + b
     - Standard arithmetic operator.
   * - Subtraction
     - .. code-block:: csharp

           a - b
     - Standard arithmetic operator.
   * - Multiplication
     - .. code-block:: csharp

           a * b
     - Standard arithmetic operator.
   * - Division
     - .. code-block:: csharp

           a / b
     - Standard arithmetic operator.
   * - Remainder
     - .. code-block:: csharp

           a % b
     - Standard arithmetic operator.
   * - Floor
     - .. code-block:: csharp

           Math.Floor(a)
     - Uses the System.Math class.
   * - Rounding
     - .. code-block:: csharp

           Math.Round(a)
     - Uses the System.Math class.
   * - Increment
     - .. code-block:: csharp

           a++
     - Standard increment operator.
   * - Decrement
     - .. code-block:: csharp

           a--
     - Standard decrement operator.
   * - LeftShift
     - .. code-block:: csharp

           a << b
     - Standard bitwise shift operator.
   * - RightShift
     - .. code-block:: csharp

           a >> b
     - Standard bitwise shift operator.
   * - BitAnd
     - .. code-block:: csharp

           a & b
     - Standard bitwise operator.
   * - BitOr
     - .. code-block:: csharp

           a | b
     - Standard bitwise operator.
   * - BitXor
     - .. code-block:: csharp

           a ^ b
     - Standard bitwise operator.
   * - BitNot
     - .. code-block:: csharp

           ~a
     - Standard bitwise operator.
   * - Float4VectorMultiplication
     - .. code-block:: csharp

           c = a * b;
     - System.Numerics.Vector4 supports overloaded operators for element-wise multiplication.
   * - Float4VectorDotProduct
     - .. code-block:: csharp

           float dot = Vector4.Dot(a, b);
     - System.Numerics.Vector4.Dot provides the scalar product.
   * - Float4VectorCrossProduct
     - .. code-block:: csharp

           var res = Vector3.Cross(new Vector3(a.X, a.Y, a.Z), new Vector3(b.X, b.Y, b.Z));
     - Cross product is defined for 3D vectors in System.Numerics.Vector3.