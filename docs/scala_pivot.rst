Scala Pivot View
================

.. list-table:: Scala Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: scala

           val x: Int = 42
     - In Scala, 'val' is used for immutable variables.
   * - ForEach
     - .. code-block:: scala

           collection.foreach { x =>
               // body
           }
     - Scala's foreach method performs an operation for each element.
   * - CollectionDefinition
     - .. code-block:: scala

           val v = List(1, 2, 3)
     - Lists are immutable by default in Scala.
   * - AssociativeArrayDefinition
     - .. code-block:: scala

           val m = Map("a" -> 1, "b" -> 2)
     - Maps are immutable by default in Scala; the '->' operator creates tuples.
   * - Print
     - .. code-block:: scala

           println("Hello, World!")
     - The println function is part of the Predef object, which is imported by default.
   * - Import
     - .. code-block:: scala

           import scala.collection.mutable.ListBuffer
     - Scala imports can be placed anywhere and can include multiple members using braces.
   * - Constant
     - .. code-block:: scala

           final val X = 42
     - A final val is a compile-time constant in Scala.
   * - Addition
     - .. code-block:: scala

           a + b
     - Scala treats operators as methods on objects.
   * - Subtraction
     - .. code-block:: scala

           a - b
     - N/A
   * - Multiplication
     - .. code-block:: scala

           a * b
     - N/A
   * - Division
     - .. code-block:: scala

           a / b
     - Integer division if both operands are integers.
   * - Remainder
     - .. code-block:: scala

           a % b
     - Standard modulo operator.
   * - Floor
     - .. code-block:: scala

           math.floor(x)
     - Requires using the scala.math library.
   * - Rounding
     - .. code-block:: scala

           math.round(x)
     - Returns the closest Long or Int.
   * - Increment
     - .. code-block:: scala

           x += 1
     - Scala does not have unary ++ operators; requires x to be a var.
   * - Decrement
     - .. code-block:: scala

           x -= 1
     - Scala does not have unary -- operators; requires x to be a var.
   * - LeftShift
     - .. code-block:: scala

           a << b
     - N/A
   * - RightShift
     - .. code-block:: scala

           a >> b
     - Arithmetic right shift.
   * - BitAnd
     - .. code-block:: scala

           a & b
     - N/A
   * - BitOr
     - .. code-block:: scala

           a | b
     - N/A
   * - BitXor
     - .. code-block:: scala

           a ^ b
     - N/A
   * - BitNot
     - .. code-block:: scala

           ~a
     - Bitwise negation.
   * - Equal
     - .. code-block:: scala

           a == b
     - In Scala, == is equivalent to equals() and handles nulls.
   * - NotEqual
     - .. code-block:: scala

           a != b
     - In Scala, != is the negation of ==.
   * - GreaterThan
     - .. code-block:: scala

           a > b
     - N/A
   * - LogicalAnd
     - .. code-block:: scala

           a && b
     - Short-circuiting logical AND.
   * - LogicalOr
     - .. code-block:: scala

           a || b
     - Short-circuiting logical OR.
   * - LogicalXor
     - .. code-block:: scala

           a ^ b
     - Logical XOR for booleans.
   * - IfElse
     - .. code-block:: scala

           if (x > 0) 1 else 0
     - In Scala, if-else is an expression that returns a value.
   * - SwitchCase
     - .. code-block:: scala

           x match {
               case 1 => 1
               case 2 => 2
               case _ => 0
           }
     - Scala uses pattern matching instead of a traditional switch statement.
   * - Loop
     - .. code-block:: scala

           while (true) {
               // body
           }
     - Standard while loop.
   * - ForLoop
     - .. code-block:: scala

           for (i <- 1 to 10) {
               // body
           }
     - Scala for-comprehension used as a simple loop.
   * - ProcedureDefinition
     - .. code-block:: scala

           def greet(name: String): Unit = {
               println("Hello " + name)
           }
     - Procedures in Scala return Unit.
   * - FunctionDefinition
     - .. code-block:: scala

           def add(a: Int, b: Int): Int = {
               a + b
           }
     - The last expression in the body is the return value.
   * - TryCatch
     - .. code-block:: scala

           try {
               // code
           } catch {
               case e: Exception => // handle
           } finally {
               // cleanup
           }
     - Scala uses pattern matching in catch blocks.
   * - Raise
     - .. code-block:: scala

           throw new Exception("error")
     - N/A
   * - Thread
     - .. code-block:: scala

           val t = new Thread(new Runnable {
               def run(): Unit = {
                   // body
               }
           })
           t.start()
     - Scala can use standard Java threads.
   * - SendMessage
     - .. code-block:: scala

           actor ! message
     - Using the Akka or Pekko actor model; the '!' operator is used for fire-and-forget sending.
   * - ReceiveMessage
     - .. code-block:: scala

           def receive: Receive = {
               case msg => // handle
           }
     - Actors define a receive method to handle incoming messages.
   * - MutexDefinition
     - .. code-block:: scala

           val mtx = new Object()
     - Any object can serve as a monitor for synchronization in Scala.
   * - MutexLock
     - .. code-block:: scala

           mtx.synchronized {
               // body
           }
     - The 'synchronized' block acquires the object's monitor.
   * - MutexUnlock
     - N/A
     - Released automatically at the end of the synchronized block.
   * - SemaphoreDefinition
     - .. code-block:: scala

           val sem = new java.util.concurrent.Semaphore(1)
     - Uses Java interop for semaphores.
   * - SemaphoreWait
     - .. code-block:: scala

           sem.acquire()
     - N/A
   * - SemaphoreSignal
     - .. code-block:: scala

           sem.release()
     - N/A
   * - LineContinuation
     - N/A
     - Scala automatically continues lines if they end with an operator or have open parentheses.
   * - SingleLineComment
     - .. code-block:: scala

           // comment
     - Standard C-style single-line comments.
   * - MultiLineComment
     - .. code-block:: scala

           /* comment */
     - Standard C-style multi-line comments; can be nested.
   * - Float4VectorMultiplication
     - .. code-block:: scala

           a.zip(b).map { case (x, y) => x * y }
     - Element-wise multiplication using functional idioms.
   * - Float4VectorDotProduct
     - .. code-block:: scala

           a.zip(b).map { case (x, y) => x * y }.sum
     - Calculated as the sum of element-wise products.
   * - Float4VectorCrossProduct
     - .. code-block:: scala

           Vector(
               a(1)*b(2) - a(2)*b(1),
               a(2)*b(0) - a(0)*b(2),
               a(0)*b(1) - a(1)*b(0),
               0.0
           )
     - Manual implementation of the cross product for 3D vectors with a 4th component.
   * - SetFiltering
     - .. code-block:: scala

           s.filter(x => x > 0)
     - Functional filtering on collections.
   * - SetJoin
     - .. code-block:: scala

           for {
               x <- s1
               y <- s2 if x.id == y.id
           } yield (x, y)
     - Joining two collections using a for-comprehension.
