Lisp Pivot View
===============

.. list-table:: Lisp Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: common-lisp

           (defparameter x 42)
     - Dynamic typing; defined using defparameter or defvar.
   * - SwitchCase
     - .. code-block:: common-lisp

           (case x
             (1 "one")
             (2 "two")
             (t "none"))
     - Standard 'case' macro; 't' or 'otherwise' is the default branch.
   * - IfElse
     - .. code-block:: common-lisp

           (if (> x 0) 1 0)
     - The 'if' expression evaluates the condition and returns the corresponding branch result.
   * - Loop
     - .. code-block:: common-lisp

           (loop while (> x 0) do (setq x (1- x)))
     - Common Lisp 'loop' macro provides a versatile way to iterate.
   * - FunctionDefinition
     - .. code-block:: common-lisp

           (defun add (a b) (+ a b))
     - Functions are defined with 'defun'; Lisp follows prefix notation.
   * - ProcedureDefinition
     - .. code-block:: common-lisp

           (defun log-message (msg)
             (format t "~A~%" msg))
     - Lisp functions always return the value of the last expression; procedures return nil or some status.
   * - TryCatch
     - .. code-block:: common-lisp

           (handler-case (do_something) (error (c) (handle c)))
     - Common Lisp uses handler-case for high-level error handling.
   * - Raise
     - .. code-block:: common-lisp

           (error "Error")
     - Signals a continuous error that must be handled or it enters the debugger.
   * - SingleLineComment
     - .. code-block:: common-lisp

           ; comment
     - Standard Lisp single-line comment using semicolon.
   * - MultiLineComment
     - .. code-block:: common-lisp

           #| line 1
              line 2 |#
     - Uses ``#|`` and ``|#`` for block comments.
   * - Print
     - .. code-block:: common-lisp

           (format t "Hello, World!~%")
     - The format function with 't' outputs to standard output; ~% is a newline.
   * - Import
     - .. code-block:: common-lisp

           (use-package :iter)
     - Makes symbols from the specified package available in the current package.
   * - Constant
     - .. code-block:: common-lisp

           (defconstant +max+ 100)
     - Defines a global constant; by convention, names are often wrapped in + signs.
   * - Addition
     - .. code-block:: common-lisp

           (+ a b)
     - Prefix notation for all mathematical operations.
   * - Subtraction
     - .. code-block:: common-lisp

           (- a b)
     - Prefix notation for all mathematical operations.
   * - Multiplication
     - .. code-block:: common-lisp

           (* a b)
     - Prefix notation for all mathematical operations.
   * - Division
     - .. code-block:: common-lisp

           (/ a b)
     - Prefix notation for all mathematical operations.
   * - Remainder
     - .. code-block:: common-lisp

           (mod a b)
     - Prefix notation for all mathematical operations.
   * - Floor
     - .. code-block:: common-lisp

           (floor a)
     - Prefix notation for all mathematical operations.
   * - Rounding
     - .. code-block:: common-lisp

           (round a)
     - Prefix notation for all mathematical operations.
   * - Increment
     - .. code-block:: common-lisp

           (1+ a)
     - Prefix notation for all mathematical operations.
   * - Decrement
     - .. code-block:: common-lisp

           (1- a)
     - Prefix notation for all mathematical operations.
   * - LeftShift
     - .. code-block:: common-lisp

           (ash a b)
     - Prefix notation for all mathematical operations.
   * - RightShift
     - .. code-block:: common-lisp

           (ash a -b)
     - Prefix notation for all mathematical operations.
   * - BitAnd
     - .. code-block:: common-lisp

           (logand a b)
     - Common Lisp bitwise operations; ash is used for both left and right shifts.
   * - BitOr
     - .. code-block:: common-lisp

           (logior a b)
     - Common Lisp bitwise operations; ash is used for both left and right shifts.
   * - BitXor
     - .. code-block:: common-lisp

           (logxor a b)
     - Common Lisp bitwise operations; ash is used for both left and right shifts.
   * - BitNot
     - .. code-block:: common-lisp

           (lognot a)
     - Common Lisp bitwise operations; ash is used for both left and right shifts.
   * - Float4VectorMultiplication
     - .. code-block:: common-lisp

           (mapcar #'* a b)
     - Applies the multiplication function element-wise to the lists.
   * - Float4VectorDotProduct
     - .. code-block:: common-lisp

           (reduce #'+ (mapcar #'* a b))
     - Maps multiplication over lists and reduces the result with addition.
   * - Float4VectorCrossProduct
     - .. code-block:: common-lisp

           (list (- (* (nth 1 a) (nth 2 b)) (* (nth 2 a) (nth 1 b)))
                 (- (* (nth 2 a) (nth 0 b)) (* (nth 0 a) (nth 2 b)))
                 (- (* (nth 0 a) (nth 1 b)) (* (nth 1 a) (nth 0 b)))
                 0.0)
     - Uses nth and basic arithmetic functions.
   * - ForLoop
     - .. code-block:: common-lisp

           (loop for i from 0 to 9 do
               #| body |#)
     - The loop macro provides a highly expressive way to iterate.
   * - Equal
     - .. code-block:: common-lisp

           (= a b)
     - Numerical equality; use 'eq', 'eql', 'equal', or 'equalp' for other types.
   * - NotEqual
     - .. code-block:: common-lisp

           (/= a b)
     - Returns true if all arguments are not equal to each other.
   * - GreaterThan
     - .. code-block:: common-lisp

           (> a b)
     -
   * - SetFiltering
     - .. code-block:: common-lisp

           (remove-if-not #'evenp list)
     - Common Lisp uses remove-if-not or filter-like functions.
   * - SetJoin
     - .. code-block:: common-lisp

           (loop for a in list-a append
             (loop for b in list-b
               when (= (getf a :id) (getf b :id))
               collect (list a b)))
     - Uses nested loops to join lists of property lists or objects.