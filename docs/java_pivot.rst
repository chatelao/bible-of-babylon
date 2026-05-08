Java Pivot View
===============

.. list-table:: Java Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: java

           int x = 42;
     - Strongly typed, similar to C.
   * - IfElse
     - .. code-block:: java

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Identical to C.
   * - Loop
     - .. code-block:: java

           while (x > 0) {
               x = x - 1;
           }
     - Identical to C.
   * - FunctionDefinition
     - .. code-block:: java

           public int add(int a, int b) {
               return a + b;
           }
     - Similar to C, but typically within a class with an access modifier.
   * - ProcedureDefinition
     - .. code-block:: java

           public void logMessage(String msg) {
               System.out.println(msg);
           }
     - Uses the 'void' keyword to indicate no return value.
   * - TryCatch
     - .. code-block:: java

           try {
               do_something();
           } catch (Exception e) {
               handle(e);
           }
     - Standard Java exception handling.
   * - Raise
     - .. code-block:: java

           throw new RuntimeException("Error");
     - Uses 'throw' to raise an exception.
   * - Thread
     - .. code-block:: java

           new Thread(() -> { do_work(); }).start();
     - Spawns a new platform thread; virtual threads are available in newer versions.
   * - SendMessage
     - .. code-block:: java

           queue.put(42);
     - Commonly implemented using BlockingQueue; put() may block if the queue is full.
   * - ReceiveMessage
     - .. code-block:: java

           int msg = queue.take(); handle(msg);
     - Using BlockingQueue.take(); blocks until an element becomes available.
   * - SingleLineComment
     - .. code-block:: java

           // comment
     - Identical to C.
   * - MultiLineComment
     - .. code-block:: java

           /* line 1
              line 2 */
     - Identical to C.
   * - Print
     - .. code-block:: java

           System.out.println("Hello, World!");
     - Uses System.out for standard output; includes a newline.
   * - Import
     - .. code-block:: java

           import java.util.List;
     - Imports a specific class; can use * for all classes in a package.
   * - SwitchCase
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
   * - Constant
     - .. code-block:: java

           public static final int MAX = 100;
     - Uses 'final' to prevent modification; typically combined with 'static' for class-level constants.
   * - Addition
     - .. code-block:: java

           a + b
     - Standard operators; Math class provides rounding and floor functions.
   * - Subtraction
     - .. code-block:: java

           a - b
     - Standard operators; Math class provides rounding and floor functions.
   * - Multiplication
     - .. code-block:: java

           a * b
     - Standard operators; Math class provides rounding and floor functions.
   * - Division
     - .. code-block:: java

           a / b
     - Standard operators; Math class provides rounding and floor functions.
   * - Remainder
     - .. code-block:: java

           a % b
     - Standard operators; Math class provides rounding and floor functions.
   * - Floor
     - .. code-block:: java

           Math.floor(a)
     - Standard operators; Math class provides rounding and floor functions.
   * - Rounding
     - .. code-block:: java

           Math.round(a)
     - Standard operators; Math class provides rounding and floor functions.
   * - Increment
     - .. code-block:: java

           a++
     - Standard operators; Math class provides rounding and floor functions.
   * - Decrement
     - .. code-block:: java

           a--
     - Standard operators; Math class provides rounding and floor functions.
   * - LeftShift
     - .. code-block:: java

           a << b
     - Standard operators; Math class provides rounding and floor functions.
   * - RightShift
     - .. code-block:: java

           a >> b
     - Standard operators; Math class provides rounding and floor functions.
   * - BitAnd
     - .. code-block:: java

           a & b
     - Standard bitwise operators in Java.
   * - BitOr
     - .. code-block:: java

           a | b
     - Standard bitwise operators in Java.
   * - BitXor
     - .. code-block:: java

           a ^ b
     - Standard bitwise operators in Java.
   * - BitNot
     - .. code-block:: java

           ~a
     - Standard bitwise operators in Java.
   * - Float4VectorMultiplication
     - .. code-block:: java

           for (int i = 0; i < 4; i++) c[i] = a[i] * b[i];
     - Standard Java uses loops; the Vector API (incubating) provides SIMD support.
   * - Float4VectorDotProduct
     - .. code-block:: java

           float dot = 0; for (int i = 0; i < 4; i++) dot += a[i] * b[i];
     - Standard Java implementation using a loop; Vector API provides optimized dot product.
   * - Float4VectorCrossProduct
     - .. code-block:: java

           c[0] = a[1]*b[2] - a[2]*b[1];
           c[1] = a[2]*b[0] - a[0]*b[2];
           c[2] = a[0]*b[1] - a[1]*b[0];
           c[3] = 0.0f;
     - Standard Java implementation using array indexing.