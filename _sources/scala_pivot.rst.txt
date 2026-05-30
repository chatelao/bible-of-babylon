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
     - Variables are declared with 'var'; supports type inference.
   * - Constant
     - .. code-block:: scala

           val MAX = 100
     - Constants are declared with 'val' and are immutable.
   * - SingleLineComment
     - .. code-block:: scala

           // comment
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: scala

           /* line 1
              line 2 */
     - Standard block comment; supports nesting.
   * - Print
     - .. code-block:: scala

           println("Hello, World!")
     - Outputs to the console with a trailing newline.
   * - Import
     - .. code-block:: scala

           import scala.collection.mutable
     - Imports a package or specific members.
   * - LineContinuation
     - N/A
     - Scala automatically handles line continuation if an expression is incomplete.
   * - CollectionDefinition
     - .. code-block:: scala

           val l = List(1, 2, 3)
     - Lists are immutable by default in Scala.
   * - AssociativeArrayDefinition
     - .. code-block:: scala

           val m = Map("a" -> 1, "b" -> 2)
     - Maps store key-value pairs using the -> arrow.
   * - ForEach
     - .. code-block:: scala

           collection.foreach(item => println(item))
     - Higher-order function for iterating over a collection.
   * - SetFiltering
     - .. code-block:: scala

           val filtered = collection.filter(_ > 0)
     - Uses the filter method with a predicate; _ is a shorthand for the element.
   * - SetJoin
     - .. code-block:: scala

           for { a <- listA; b <- listB; if a.id == b.id } yield (a, b)
     - Implemented using for-comprehensions for joining collections.
   * - IfElse
     - .. code-block:: scala

           if (x > 0) 1 else 0
     - If-else is an expression in Scala.
   * - SwitchCase
     - .. code-block:: scala

           x match {
               case 1 => 1
               case 2 => 2
               case _ => 0
           }
     - Scala uses pattern matching with 'match'.
   * - Loop
     - .. code-block:: scala

           while (x > 0) {
               x -= 1
           }
     - Standard while loop.
   * - ForLoop
     - .. code-block:: scala

           for (i <- 0 until 10) {
               // body
           }
     - Iterates over a range; 'until' is exclusive of the upper bound.
   * - Equal
     - .. code-block:: scala

           a == b
     - Checks for structural equality; calls equals().
   * - NotEqual
     - .. code-block:: scala

           a != b
     - Structural inequality.
   * - GreaterThan
     - .. code-block:: scala

           a > b
     - Standard comparison.
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
     - The ^ operator acts as a logical XOR for boolean operands.
   * - FunctionDefinition
     - .. code-block:: scala

           def add(a: Int, b: Int): Int = a + b
     - Functions are defined with 'def'; result is the value of the last expression.
   * - ProcedureDefinition
     - .. code-block:: scala

           def logMessage(msg: String): Unit = {
               println(msg)
           }
     - Procedures return Unit (equivalent to void).
   * - TryCatch
     - .. code-block:: scala

           try {
               doSomething()
           } catch {
               case e: Exception => handle(e)
           }
     - Scala's catch block uses pattern matching.
   * - Raise
     - .. code-block:: scala

           throw new Exception("Error")
     - Uses 'throw' to raise an exception.
   * - Addition
     - .. code-block:: scala

           a + b
     - Standard arithmetic operator.
   * - Subtraction
     - .. code-block:: scala

           a - b
     - Standard arithmetic operator.
   * - Multiplication
     - .. code-block:: scala

           a * b
     - Standard arithmetic operator.
   * - Division
     - .. code-block:: scala

           a / b
     - Standard arithmetic operator.
   * - Remainder
     - .. code-block:: scala

           a % b
     - Standard arithmetic operator.
   * - Floor
     - .. code-block:: scala

           math.floor(a)
     - Uses the scala.math package.
   * - Rounding
     - .. code-block:: scala

           math.round(a)
     - Uses the scala.math package.
   * - Increment
     - .. code-block:: scala

           a += 1
     - Scala does not support ++ operators.
   * - Decrement
     - .. code-block:: scala

           a -= 1
     - Scala does not support -- operators.
   * - LeftShift
     - .. code-block:: scala

           a << b
     - Standard bitwise shift.
   * - RightShift
     - .. code-block:: scala

           a >> b
     - Standard bitwise shift.
   * - BitAnd
     - .. code-block:: scala

           a & b
     - Standard bitwise operator.
   * - BitOr
     - .. code-block:: scala

           a | b
     - Standard bitwise operator.
   * - BitXor
     - .. code-block:: scala

           a ^ b
     - Standard bitwise operator.
   * - BitNot
     - .. code-block:: scala

           ~a
     - Standard bitwise operator.
   * - Float4VectorMultiplication
     - .. code-block:: scala

           a.zip(b).map { case (ai, bi) => ai * bi }
     - Functional approach using zip and map.
   * - Float4VectorDotProduct
     - .. code-block:: scala

           a.zip(b).map { case (ai, bi) => ai * bi }.sum
     - Functional approach combining zip, map, and sum.
   * - Float4VectorCrossProduct
     - .. code-block:: scala

           Array(a(1)*b(2) - a(2)*b(1), a(2)*b(0) - a(0)*b(2), a(0)*b(1) - a(1)*b(0), 0.0f)
     - Manual calculation for 3D cross product.
   * - Thread
     - .. code-block:: scala

           Future { doWork() }
     - Uses Futures for asynchronous execution (requires ExecutionContext).
   * - SendMessage
     - .. code-block:: scala

           actor ! msg
     - Actors use the ! operator for asynchronous message passing (e.g., in Akka/Pekko).
   * - ReceiveMessage
     - .. code-block:: scala

           def receive = { case msg => handle(msg) }
     - Actors define a receive block using pattern matching.
   * - MutexDefinition
     - .. code-block:: scala

           val lock = new AnyRef()
     - Any object can be used as a monitor in Scala.
   * - MutexLock
     - .. code-block:: scala

           lock.synchronized { ... }
     - The synchronized block acquires the object's monitor.
   * - MutexUnlock
     - N/A
     - Released automatically at the end of the synchronized block.
   * - SemaphoreDefinition
     - .. code-block:: scala

           val sem = new java.util.concurrent.Semaphore(1)
     - Uses Java's Semaphore class.
   * - SemaphoreWait
     - .. code-block:: scala

           sem.acquire()
     - Blocks until a permit is available.
   * - SemaphoreSignal
     - .. code-block:: scala

           sem.release()
     - Increments the permit count.
