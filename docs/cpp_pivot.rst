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
     - Static typing, identical to C in this case.
   * - IfElse
     - .. code-block:: cpp

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C++ if-else statement.
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
     - Standard C++ switch statement.
   * - Loop
     - .. code-block:: cpp

           while (x > 0) {
               x = x - 1;
           }
     - Standard while loop.
   * - ForLoop
     - .. code-block:: cpp

           for (int i = 0; i < 10; ++i) {
               // body
           }
     - Standard C-style for loop.
   * - FunctionDefinition
     - .. code-block:: cpp

           int add(int a, int b) {
               return a + b;
           }
     - Standard function definition.
   * - ProcedureDefinition
     - .. code-block:: cpp

           void logMessage(const std::string& msg) {
               std::cout << msg << std::endl;
           }
     - Uses 'void' for procedures; passing by const reference is idiomatic for strings.
   * - TryCatch
     - .. code-block:: cpp

           try {
               do_something();
           } catch (const std::exception& e) {
               handle(e);
           }
     - Standard C++ exception handling.
   * - Raise
     - .. code-block:: cpp

           throw std::runtime_error("Error");
     - Uses 'throw' to raise an exception.
   * - Thread
     - .. code-block:: cpp

           std::thread t(do_work);
           t.detach();
     - Uses std::thread from the <thread> header (C++11 and later).
   * - SendMessage
     - .. code-block:: cpp

           queue.push(42);
     - Commonly implemented using thread-safe queues or message passing libraries.
   * - ReceiveMessage
     - .. code-block:: cpp

           int msg; queue.wait_and_pop(msg);
           handle(msg);
     - Requires a thread-safe queue implementation for blocking receive.
   * - SingleLineComment
     - .. code-block:: cpp

           // comment
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: cpp

           /* line 1
              line 2 */
     - Standard block comment.
   * - Print
     - .. code-block:: cpp

           std::cout << "Hello, World!" << std::endl;
     - Uses the iostream library for standard output.
   * - Import
     - .. code-block:: cpp

           #include <vector>
     - Uses #include to include standard library or user headers.
   * - Constant
     - .. code-block:: cpp

           const int MAX = 100;
     - The 'const' keyword defines an immutable value; 'constexpr' can also be used for compile-time constants.
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
     - Uses std::floor from the <cmath> header.
   * - Rounding
     - .. code-block:: cpp

           std::round(a)
     - Uses std::round from the <cmath> header (C++11 and later).
   * - Increment
     - .. code-block:: cpp

           ++a
     - Standard increment operator; prefix version is often preferred for iterators.
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
   * - Float4VectorMultiplication
     - .. code-block:: cpp

           for (int i = 0; i < 4; ++i) c[i] = a[i] * b[i];
     - Can be optimized with SIMD intrinsics (e.g., SSE/AVX) or libraries like Eigen/GLM.
   * - Float4VectorDotProduct
     - .. code-block:: cpp

           float dot = a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + a[3]*b[3];
     - Standard implementation; SIMD intrinsics can provide significant speedup.
   * - Float4VectorCrossProduct
     - .. code-block:: cpp

           c[0] = a[1]*b[2] - a[2]*b[1];
           c[1] = a[2]*b[0] - a[0]*b[2];
           c[2] = a[0]*b[1] - a[1]*b[0];
           c[3] = 0.0f;
     - Calculated component-wise for the first three components.