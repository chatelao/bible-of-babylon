Clojure Pivot View
==================

.. list-table:: Clojure Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: clojure

           (def x 42)
     - Variables are defined using 'def'; they are immutable by default in the sense of 'binding'.
   * - CollectionDefinition
     - .. code-block:: clojure

           (def l [1 2 3])
     - Vectors are the standard ordered collection in Clojure.
   * - AssociativeArrayDefinition
     - .. code-block:: clojure

           (def m {:a 1 :b 2})
     - Maps are used for key-value pairs.
   * - Equal
     - .. code-block:: clojure

           (= a b)
     - Structural equality.
   * - NotEqual
     - .. code-block:: clojure

           (not= a b)
     - Negated equality.
   * - GreaterThan
     - .. code-block:: clojure

           (> a b)
     - Standard comparison.
   * - ProcedureDefinition
     - .. code-block:: clojure

           (defn my-proc [args]
             (println args))
     - Procedures in Clojure are functions that return nil.
   * - FunctionDefinition
     - .. code-block:: clojure

           (defn my-func [x]
             (+ x 1))
     - Functions return the result of the last expression.
   * - IfElse
     - .. code-block:: clojure

           (if (> x 0) 1 0)
     - Standard if-then-else.
   * - SwitchCase
     - .. code-block:: clojure

           (case x
             1 "one"
             2 "two"
             "default")
     - The 'case' macro provides constant-time dispatch.
   * - Loop
     - .. code-block:: clojure

           (loop [i 0]
             (when (< i 10)
               (println i)
               (recur (inc i))))
     - The 'loop/recur' form is the standard way to perform recursion in constant stack space.
   * - ForLoop
     - .. code-block:: clojure

           (doseq [i (range 10)]
             (println i))
     - The 'doseq' macro is used for side-effecting iterations.
   * - ForEach
     - .. code-block:: clojure

           (doseq [item collection]
             (println item))
     - The 'doseq' macro is also the standard way to iterate over collections.
   * - TryCatch
     - .. code-block:: clojure

           (try
             (/ 1 0)
             (catch Exception e
               (println (.getMessage e))))
     - Clojure's error handling interops with Java's exceptions.
   * - Raise
     - .. code-block:: clojure

           (throw (Exception. "Error"))
     - Throws a Java exception.
   * - Thread
     - .. code-block:: clojure

           (future (println "Hello from thread"))
     - Futures are a simple way to run code on another thread.
   * - SendMessage
     - .. code-block:: clojure

           (send my-agent (fn [state] (inc state)))
     - Agents provide a way to manage asynchronous state updates.
   * - ReceiveMessage
     - .. code-block:: clojure

           @my-agent
     - The '@' or 'deref' function is used to get the current state of an agent or the result of a future.
   * - SingleLineComment
     - .. code-block:: clojure

           ; comment
     - Semicolon starts a single-line comment.
   * - MultiLineComment
     - .. code-block:: clojure

           (comment
             (some code))
     - The 'comment' macro ignores its body, effectively serving as a multi-line comment.
   * - Print
     - .. code-block:: clojure

           (println "Hello, World!")
     - Standard output with a newline.
   * - Import
     - .. code-block:: clojure

           (require '[clojure.string :as str])
     - The 'require' form is used to load namespaces.
   * - Constant
     - .. code-block:: clojure

           (def ^:const my-const 10)
     - Constants are defined with the ^:const metadata for compiler optimization.
   * - Addition
     - .. code-block:: clojure

           (+ a b)
     - Prefix notation for addition.
   * - Subtraction
     - .. code-block:: clojure

           (- a b)
     - Prefix notation for subtraction.
   * - Multiplication
     - .. code-block:: clojure

           (* a b)
     - Prefix notation for multiplication.
   * - Division
     - .. code-block:: clojure

           (/ a b)
     - Prefix notation for division.
   * - Remainder
     - .. code-block:: clojure

           (rem a b)
     - Returns the remainder of division.
   * - Floor
     - .. code-block:: clojure

           (Math/floor x)
     - Uses Java interop for floor.
   * - Rounding
     - .. code-block:: clojure

           (Math/round x)
     - Uses Java interop for rounding.
   * - Increment
     - .. code-block:: clojure

           (inc x)
     - Increments the value by 1.
   * - Decrement
     - .. code-block:: clojure

           (dec x)
     - Decrements the value by 1.
   * - LeftShift
     - .. code-block:: clojure

           (bit-shift-left x n)
     - Bitwise left shift.
   * - RightShift
     - .. code-block:: clojure

           (bit-shift-right x n)
     - Bitwise right shift.
   * - BitAnd
     - .. code-block:: clojure

           (bit-and a b)
     - Bitwise AND.
   * - BitOr
     - .. code-block:: clojure

           (bit-or a b)
     - Bitwise OR.
   * - BitXor
     - .. code-block:: clojure

           (bit-xor a b)
     - Bitwise XOR.
   * - BitNot
     - .. code-block:: clojure

           (bit-not x)
     - Bitwise NOT.
   * - Float4VectorMultiplication
     - .. code-block:: clojure

           (mapv * a b)
     - Element-wise multiplication of vectors.
   * - Float4VectorDotProduct
     - .. code-block:: clojure

           (reduce + (map * a b))
     - Standard dot product implementation.
   * - Float4VectorCrossProduct
     - .. code-block:: clojure

           (let [[ax ay az] a
                 [bx by bz] b]
             [(- (* ay bz) (* az by))
              (- (* az bx) (* ax bz))
              (- (* ax by) (* ay bx))
              0.0])
     - Uses destructuring and vector literal.
   * - SetFiltering
     - .. code-block:: clojure

           (filter #(= % :val) my-set)
     - Higher-order function for filtering.
   * - SetJoin
     - .. code-block:: clojure

           (clojure.set/join set-a set-b)
     - Relational join operation from the clojure.set namespace.
   * - MutexDefinition
     - .. code-block:: clojure

           (def mtx (Object.))
     - Any object can be used as a monitor in Clojure.
   * - MutexLock
     - .. code-block:: clojure

           (locking mtx ...)
     - The locking macro acquires the monitor.
   * - MutexUnlock
     - N/A
     - Released automatically at the end of the locking block.
   * - SemaphoreDefinition
     - .. code-block:: clojure

           (def sem (java.util.concurrent.Semaphore. 1))
     - Uses Java interop for semaphores.
   * - SemaphoreWait
     - .. code-block:: clojure

           (.acquire sem)
     - N/A
   * - SemaphoreSignal
     - .. code-block:: clojure

           (.release sem)
     - N/A