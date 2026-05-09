Cpp Pivot View
==============

.. list-table:: Cpp Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: cpp

           int x = 42;
     - Static typing, similar to C.
   * - Equal
     - .. code-block:: cpp

           a == b
     - Standard equality operator.
   * - NotEqual
     - .. code-block:: cpp

           a != b
     - Standard inequality operator.
   * - GreaterThan
     - .. code-block:: cpp

           a > b
     - Standard greater than operator.
   * - ProcedureDefinition
     - .. code-block:: cpp

           void logMessage(std::string msg) {
               std::cout << msg << std::endl;
           }
     - Procedures use the 'void' return type.
   * - FunctionDefinition
     - .. code-block:: cpp

           int add(int a, int b) {
               return a + b;
           }
     - Standard C-style function definition.
   * - IfElse
     - .. code-block:: cpp

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C-style if-else statement.
   * - SwitchCase
     - .. code-block:: cpp

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - Standard C-style switch statement.
   * - Loop
     - .. code-block:: cpp

           while (x > 0) {
               x = x - 1;
           }
     - Standard C-style while loop.
   * - ForLoop
     - .. code-block:: cpp

           for (int i = 0; i < 10; i++) {
               // body
           }
     - Standard C-style for loop.
   * - Addition
     - .. code-block:: cpp

           a + b
     - Standard arithmetic operator.
   * - Subtraction
     - .. code-block:: cpp

           a - b
     - Standard arithmetic operator.
   * - Multiplication
     - .. code-block:: cpp

           a * b
     - Standard arithmetic operator.
   * - Division
     - .. code-block:: cpp

           a / b
     - Standard arithmetic operator.
   * - Remainder
     - .. code-block:: cpp

           a % b
     - Standard arithmetic operator.
   * - Floor
     - .. code-block:: cpp

           std::floor(a)
     - Requires <cmath>.
   * - Rounding
     - .. code-block:: cpp

           std::round(a)
     - Requires <cmath>.
   * - Increment
     - .. code-block:: cpp

           a++
     - Standard increment operator.
   * - Decrement
     - .. code-block:: cpp

           a--
     - Standard decrement operator.
   * - LeftShift
     - .. code-block:: cpp

           a << b
     - Standard bitwise shift operator.
   * - RightShift
     - .. code-block:: cpp

           a >> b
     - Standard bitwise shift operator.
   * - BitAnd
     - .. code-block:: cpp

           a & b
     - Standard bitwise operator.
   * - BitOr
     - .. code-block:: cpp

           a | b
     - Standard bitwise operator.
   * - BitXor
     - .. code-block:: cpp

           a ^ b
     - Standard bitwise operator.
   * - BitNot
     - .. code-block:: cpp

           ~a
     - Standard bitwise operator.
   * - TryCatch
     - .. code-block:: cpp

           try {
               do_something();
           } catch (const std::exception& e) {
               handle(e);
           }
     - Standard C++ exception handling using try-catch blocks.
   * - Raise
     - .. code-block:: cpp

           throw std::runtime_error("Error");
     - Uses 'throw' to raise an exception.
   * - Thread
     - .. code-block:: cpp

           std::thread t(do_work);
           t.join();
     - Uses std::thread (C++11 and later).
   * - SendMessage
     - .. code-block:: cpp

           queue.push(42);
     - Communication is typically handled via shared data structures and synchronization primitives.
   * - ReceiveMessage
     - .. code-block:: cpp

           int msg = queue.front();
           queue.pop();
           handle(msg);
     - Typically involves pulling from a thread-safe queue.
   * - SingleLineComment
     - .. code-block:: cpp

           // comment
     - Standard C++ single-line comment.
   * - MultiLineComment
     - .. code-block:: cpp

           /* line 1
              line 2 */
     - Standard C++ multi-line comment.
   * - Print
     - .. code-block:: cpp

           std::cout << "Hello, World!" << std::endl;
     - Uses std::cout for standard output; requires <iostream>.
   * - Import
     - .. code-block:: cpp

           #include <iostream>
     - Standard way to include headers.
   * - Constant
     - .. code-block:: cpp

           const int MAX = 100;
     - The 'const' keyword defines an immutable value.
   * - Float4VectorMultiplication
     - .. code-block:: cpp

           for (int i = 0; i < 4; i++) c[i] = a[i] * b[i];
     - Standard C++ requires a loop or explicit component-wise multiplication for arrays.
   * - Float4VectorDotProduct
     - .. code-block:: cpp

           float dot = 0; for (int i = 0; i < 4; i++) dot += a[i] * b[i];
     - Calculated by accumulating component-wise products in a loop.
   * - Float4VectorCrossProduct
     - .. code-block:: cpp

           c[0] = a[1]*b[2] - a[2]*b[1];
           c[1] = a[2]*b[0] - a[0]*b[2];
           c[2] = a[0]*b[1] - a[1]*b[0];
           c[3] = 0.0f;
     - Manual implementation for the first three components.
   * - SetFiltering
     - .. code-block:: cpp

           std::copy_if(v.begin(), v.end(), std::back_inserter(res), condition);
     - Uses the standard library algorithm copy_if.
   * - SetJoin
     - .. code-block:: cpp

           std::set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), std::back_inserter(res));
     - Uses set_intersection for sorted ranges; otherwise uses nested loops.