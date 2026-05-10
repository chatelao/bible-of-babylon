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
     - Global var definition; for local bindings, 'let' is used.
   * - IfElse
     - .. code-block:: clojure

           (if (> x 0) 1 0)
     - Standard functional if-expression.
   * - SwitchCase
     - .. code-block:: clojure

           (case x
             1 1
             2 2
             0)
     - The case macro dispatches on constant values.
   * - Loop
     - .. code-block:: clojure

           (while (> x 0)
             (println x))
     - While macro for side-effecting loops.
   * - ForLoop
     - .. code-block:: clojure

           (doseq [i (range 10)]
             (println i))
     - Iterates over a sequence for side effects.
   * - FunctionDefinition
     - .. code-block:: clojure

           (defn add [a b]
             (+ a b))
     - Standard function definition; the last expression is returned.
   * - ProcedureDefinition
     - .. code-block:: clojure

           (defn log-message [msg]
             (println msg))
     - Procedures are functions that typically return nil.
   * - TryCatch
     - .. code-block:: clojure

           (try
             (do-something)
             (catch Exception e
               (handle e)))
     - Standard exception handling using try-catch blocks.
   * - Raise
     - .. code-block:: clojure

           (throw (Exception. "Error"))
     - Uses 'throw' to raise an exception object.
   * - Thread
     - .. code-block:: clojure

           (future (do-work))
     - The future macro runs code in another thread and returns a handle to the result.
   * - SendMessage
     - .. code-block:: clojure

           (send a + 42)
     - Asynchronous message passing using agents.
   * - ReceiveMessage
     - .. code-block:: clojure

           (let [msg @c] (handle msg))
     - Dereferencing a promise or future (using @) blocks until the value is available.
   * - SingleLineComment
     - .. code-block:: clojure

           ; comment
     - Standard Clojure single-line comment.
   * - MultiLineComment
     - .. code-block:: clojure

           (comment
             line 1
             line 2)
     - The comment macro is used for multi-line blocks; they are treated as code that returns nil.
   * - Print
     - .. code-block:: clojure

           (println "Hello, World!")
     - Prints to stdout with a newline.
   * - Import
     - .. code-block:: clojure

           (:require [clojure.string :as str])
     - Imports a namespace; usually within an ns macro.
   * - Constant
     - .. code-block:: clojure

           (def ^:const MAX 100)
     - Defines a constant value.
   * - Addition
     - .. code-block:: clojure

           (+ a b)
     - Standard prefix arithmetic operator.
   * - Subtraction
     - .. code-block:: clojure

           (- a b)
     - Standard prefix arithmetic operator.
   * - Multiplication
     - .. code-block:: clojure

           (* a b)
     - Standard prefix arithmetic operator.
   * - Division
     - .. code-block:: clojure

           (/ a b)
     - Standard prefix arithmetic operator.
   * - Remainder
     - .. code-block:: clojure

           (rem a b)
     - Standard prefix arithmetic operator.
   * - Equal
     - .. code-block:: clojure

           (= a b)
     - Standard equality operator.
   * - NotEqual
     - .. code-block:: clojure

           (not= a b)
     - Standard inequality operator.
   * - GreaterThan
     - .. code-block:: clojure

           (> a b)
     - Standard greater than operator.
   * - BitAnd
     - .. code-block:: clojure

           (bit-and a b)
     - Standard bitwise operators.
   * - BitOr
     - .. code-block:: clojure

           (bit-or a b)
     - Standard bitwise operators.
   * - BitXor
     - .. code-block:: clojure

           (bit-xor a b)
     - Standard bitwise operators.
   * - BitNot
     - .. code-block:: clojure

           (bit-not a)
     - Standard bitwise operators.
   * - LeftShift
     - .. code-block:: clojure

           (bit-shift-left a b)
     - Standard bitwise operators.
   * - RightShift
     - .. code-block:: clojure

           (bit-shift-right a b)
     - Standard bitwise operators.
   * - Floor
     - .. code-block:: clojure

           (Math/floor a)
     - Uses Java interop for floor.
   * - Rounding
     - .. code-block:: clojure

           (Math/round a)
     - Uses Java interop for rounding.
   * - Increment
     - .. code-block:: clojure

           (inc a)
     - Standard increment function.
   * - Decrement
     - .. code-block:: clojure

           (dec a)
     - Standard decrement function.
   * - SetFiltering
     - .. code-block:: clojure

           (filter #(> % 0) a)
     - Uses the higher-order filter function with a predicate.
   * - SetJoin
     - .. code-block:: clojure

           (clojure.set/join list-a list-b {:id :id})
     - The clojure.set namespace provides a join function for sets of maps.
   * - Float4VectorMultiplication
     - .. code-block:: clojure

           (mapv * a b)
     - Applies multiplication element-wise to vectors and returns a new vector.
   * - Float4VectorDotProduct
     - .. code-block:: clojure

           (reduce + (map * a b))
     - Functional approach using map and reduce.
   * - Float4VectorCrossProduct
     - .. code-block:: clojure

           [( - (* (a 1) (b 2)) (* (a 2) (b 1)))
            ( - (* (a 2) (b 0)) (* (a 0) (b 2)))
            ( - (* (a 0) (b 1)) (* (a 1) (b 0)))
            0.0]
     - Manual implementation for 3D cross product using vector indexing.