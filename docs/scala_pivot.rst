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

           var x: Int = 42
     - Scala supports both mutable (var) and immutable (val) variables.
   * - ForEach
     - .. code-block:: scala

           collection.foreach(item => println(item))
     - Commonly used with functional style.
   * - CollectionDefinition
     - .. code-block:: scala

           val list = List(1, 2, 3)
     - Immutable List is the default collection in Scala.
   * - AssociativeArrayDefinition
     - .. code-block:: scala

           val map = Map("a" -> 1, "b" -> 2)
     - Uses the -> operator to create tuples for the map.
   * - Equal
     - .. code-block:: scala

           a == b
     - In Scala, == calls the equals method, handling nulls safely.
   * - NotEqual
     - .. code-block:: scala

           a != b
     - Inverse of ==.
   * - GreaterThan
     - .. code-block:: scala

           a > b
     - Standard comparison operator.
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
     - Bitwise XOR operator used for booleans as well.
   * - ProcedureDefinition
     - .. code-block:: scala

           def log(message: String): Unit = {
               println(message)
           }
     - Procedures return Unit in Scala.
   * - FunctionDefinition
     - .. code-block:: scala

           def addOne(x: Int): Int = {
               x + 1
           }
     - The last expression in a block is the return value.
   * - IfElse
     - .. code-block:: scala

           if (x > 0) 1 else 0
     - if-else is an expression in Scala.
   * - SwitchCase
     - .. code-block:: scala

           x match {
               case 1 => "one"
               case 2 => "two"
               case _ => "many"
           }
     - Pattern matching is a powerful alternative to switch-case.
   * - Loop
     - .. code-block:: scala

           while (x > 0) {
               x -= 1
           }
     - Standard while loop.
   * - ForLoop
     - .. code-block:: scala

           for (i <- 0 until 10) {
               println(i)
           }
     - The for-comprehension is used for iteration.
   * - TryCatch
     - .. code-block:: scala

           try {
               // code
           } catch {
               case e: Exception => println(e)
           } finally {
               // cleanup
           }
     - Uses pattern matching in the catch block.
   * - Raise
     - .. code-block:: scala

           throw new RuntimeException("error")
     - Similar to Java.
   * - Thread
     - .. code-block:: scala

           val t = new Thread(() => {
               println("running")
           })
           t.start()
     - Uses Java's Thread class.
   * - SendMessage
     - .. code-block:: scala

           actor ! message
     - Idiomatic message passing using Akka or Pekko actors.
   * - ReceiveMessage
     - .. code-block:: scala

           def receive = {
               case message => println(message)
           }
     - Actors define a receive partial function.
   * - MutexDefinition
     - .. code-block:: scala

           val lock = new AnyRef
     - Any object can serve as a monitor.
   * - MutexLock
     - .. code-block:: scala

           lock.synchronized {
               // critical section
           }
     - The synchronized block ensures mutual exclusion.
   * - MutexUnlock
     - N/A
     - Released automatically at the end of the synchronized block.
   * - SemaphoreDefinition
     - .. code-block:: scala

           val sem = new java.util.concurrent.Semaphore(1)
     - Uses Java's Semaphore.
   * - SemaphoreWait
     - .. code-block:: scala

           sem.acquire()
     - Blocks until a permit is available.
   * - SemaphoreSignal
     - .. code-block:: scala

           sem.release()
     - Releases a permit.
   * - SingleLineComment
     - .. code-block:: scala

           // comment
     - Standard C-style comment.
   * - MultiLineComment
     - .. code-block:: scala

           /* comment */
     - Standard C-style multi-line comment.
   * - Print
     - .. code-block:: scala

           println("Hello World")
     - Prints to standard output with a newline.
   * - Import
     - .. code-block:: scala

           import scala.collection.mutable.ListBuffer
     - Standard import statement.
   * - Constant
     - .. code-block:: scala

           val PI = 3.14159
     - Immutable variables (val) are used for constants.
   * - Addition
     - .. code-block:: scala

           a + b
     - Standard arithmetic addition.
   * - Subtraction
     - .. code-block:: scala

           a - b
     - Standard arithmetic subtraction.
   * - Multiplication
     - .. code-block:: scala

           a * b
     - Standard arithmetic multiplication.
   * - Division
     - .. code-block:: scala

           a / b
     - Standard arithmetic division.
   * - Remainder
     - .. code-block:: scala

           a % b
     - Standard remainder operator.
   * - Floor
     - .. code-block:: scala

           math.floor(x)
     - Uses the scala.math library.
   * - Rounding
     - .. code-block:: scala

           math.round(x)
     - Uses the scala.math library.
   * - Increment
     - .. code-block:: scala

           x += 1
     - Scala does not have ++ operator.
   * - Decrement
     - .. code-block:: scala

           x -= 1
     - Scala does not have -- operator.
   * - LeftShift
     - .. code-block:: scala

           a << b
     - Bitwise left shift.
   * - RightShift
     - .. code-block:: scala

           a >> b
     - Bitwise right shift.
   * - BitAnd
     - .. code-block:: scala

           a & b
     - Bitwise AND.
   * - BitOr
     - .. code-block:: scala

           a | b
     - Bitwise OR.
   * - BitXor
     - .. code-block:: scala

           a ^ b
     - Bitwise XOR.
   * - BitNot
     - .. code-block:: scala

           ~a
     - Bitwise NOT.
   * - Float4VectorMultiplication
     - .. code-block:: scala

           for (i <- 0 until 4) c(i) = a(i) * b(i)
     - Loops are commonly used for vector operations in basic Scala.
   * - Float4VectorDotProduct
     - .. code-block:: scala

           (0 until 4).map(i => a(i) * b(i)).sum
     - Functional approach using map and sum.
   * - Float4VectorCrossProduct
     - .. code-block:: scala

           res(0) = a(1) * b(2) - a(2) * b(1)
           res(1) = a(2) * b(0) - a(0) * b(2)
           res(2) = a(0) * b(1) - a(1) * b(0)
           res(3) = 0.0
     - Standard 3D cross product implementation.
   * - SetFiltering
     - .. code-block:: scala

           val filtered = list.filter(_ > 0)
     - Higher-order function filter with underscore syntax.
   * - SetJoin
     - .. code-block:: scala

           for (a <- listA; b <- listB if a.id == b.id) yield (a, b)
     - Uses for-comprehension with a guard for joining.
