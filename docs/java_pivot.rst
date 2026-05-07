Java Pivot View
===============

.. list-table:: Java Pivot Table
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
     - .. code-block:: java

           int x = 42;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Strongly typed, similar to C.
   * - IfElse
     - .. code-block:: java

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Identical to C.
   * - Loop
     - .. code-block:: java

           while (x > 0) {
               x = x - 1;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Identical to C.
   * - FunctionDefinition
     - .. code-block:: java

           public int add(int a, int b) {
               return a + b;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Similar to C, but typically within a class with an access modifier.
   * - ProcedureDefinition
     - .. code-block:: java

           public void logMessage(String msg) {
               System.out.println(msg);
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses the 'void' keyword to indicate no return value.
   * - TryCatch
     - .. code-block:: java

           try {
               do_something();
           } catch (Exception e) {
               handle(e);
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Java exception handling.
   * - Raise
     - .. code-block:: java

           throw new RuntimeException("Error");
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'throw' to raise an exception.
   * - Thread
     - .. code-block:: java

           new Thread(() -> { do_work(); }).start();
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Spawns a new platform thread; virtual threads are available in newer versions.
   * - SendMessage
     - .. code-block:: java

           queue.put(42);
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Commonly implemented using BlockingQueue; put() may block if the queue is full.
   * - ReceiveMessage
     - .. code-block:: java

           int msg = queue.take(); handle(msg);
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Using BlockingQueue.take(); blocks until an element becomes available.
   * - SingleLineComment
     - .. code-block:: java

           // comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Identical to C.
   * - MultiLineComment
     - .. code-block:: java

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Identical to C.
   * - Print
     - .. code-block:: java

           System.out.println("Hello, World!");
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses System.out for standard output; includes a newline.
   * - Import
     - .. code-block:: java

           import java.util.List;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
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
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Identical to C; modern Java also supports switch expressions.
   * - Constant
     - .. code-block:: java

           public static final int MAX = 100;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'final' to prevent modification; typically combined with 'static' for class-level constants.
   * - Addition
     - .. code-block:: java

           a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - Subtraction
     - .. code-block:: java

           a - b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - Multiplication
     - .. code-block:: java

           a * b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - Division
     - .. code-block:: java

           a / b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - Remainder
     - .. code-block:: java

           a % b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - Floor
     - .. code-block:: java

           Math.floor(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - Rounding
     - .. code-block:: java

           Math.round(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - Increment
     - .. code-block:: java

           a++
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - Decrement
     - .. code-block:: java

           a--
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - LeftShift
     - .. code-block:: java

           a << b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - RightShift
     - .. code-block:: java

           a >> b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard operators; Math class provides rounding and floor functions.
   * - Bitwise
     - N/A
     - .. code-block:: java

           a & b
     - .. code-block:: java

           a | b
     - .. code-block:: java

           a ^ b
     - .. code-block:: java

           ~a
     - .. code-block:: java

           a << b
     - .. code-block:: java

           a >> b
     - Standard bitwise operators in Java.