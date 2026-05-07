Lisp Pivot View
===============

.. list-table:: Lisp Pivot Table
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
     - .. code-block:: common-lisp

           (defparameter x 42)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Dynamic typing; defined using defparameter or defvar.
   * - IfElse
     - .. code-block:: common-lisp

           (if (> x 0) 1 0)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The 'if' expression evaluates the condition and returns the corresponding branch result.
   * - Loop
     - .. code-block:: common-lisp

           (loop while (> x 0) do (setq x (1- x)))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Common Lisp 'loop' macro provides a versatile way to iterate.
   * - FunctionDefinition
     - .. code-block:: common-lisp

           (defun add (a b) (+ a b))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions are defined with 'defun'; Lisp follows prefix notation.
   * - ProcedureDefinition
     - .. code-block:: common-lisp

           (defun log-message (msg)
             (format t "~A~%" msg))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Lisp functions always return the value of the last expression; procedures return nil or some status.
   * - TryCatch
     - .. code-block:: common-lisp

           (handler-case (do_something) (error (c) (handle c)))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Common Lisp uses handler-case for high-level error handling.
   * - Raise
     - .. code-block:: common-lisp

           (error "Error")
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Signals a continuous error that must be handled or it enters the debugger.
   * - SingleLineComment
     - .. code-block:: common-lisp

           ; comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard Lisp single-line comment using semicolon.
   * - MultiLineComment
     - .. code-block:: common-lisp

           #| line 1
              line 2 |#
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses ``#|`` and ``|#`` for block comments.
   * - Print
     - .. code-block:: common-lisp

           (format t "Hello, World!~%")
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The format function with 't' outputs to standard output; ~% is a newline.
   * - Import
     - .. code-block:: common-lisp

           (use-package :iter)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Makes symbols from the specified package available in the current package.
   * - SwitchCase
     - .. code-block:: common-lisp

           (case x
             (1 "one")
             (2 "two")
             (t "none"))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard 'case' macro; 't' or 'otherwise' is the default branch.
   * - Constant
     - .. code-block:: common-lisp

           (defconstant +max+ 100)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Defines a global constant; by convention, names are often wrapped in + signs.
   * - Addition
     - .. code-block:: common-lisp

           (+ a b)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - Subtraction
     - .. code-block:: common-lisp

           (- a b)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - Multiplication
     - .. code-block:: common-lisp

           (* a b)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - Division
     - .. code-block:: common-lisp

           (/ a b)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - Remainder
     - .. code-block:: common-lisp

           (mod a b)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - Floor
     - .. code-block:: common-lisp

           (floor a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - Rounding
     - .. code-block:: common-lisp

           (round a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - Increment
     - .. code-block:: common-lisp

           (1+ a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - Decrement
     - .. code-block:: common-lisp

           (1- a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - LeftShift
     - .. code-block:: common-lisp

           (ash a b)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - RightShift
     - .. code-block:: common-lisp

           (ash a -b)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Prefix notation for all mathematical operations.
   * - Bitwise
     - N/A
     - .. code-block:: common-lisp

           (logand a b)
     - .. code-block:: common-lisp

           (logior a b)
     - .. code-block:: common-lisp

           (logxor a b)
     - .. code-block:: common-lisp

           (lognot a)
     - .. code-block:: common-lisp

           (ash a b)
     - .. code-block:: common-lisp

           (ash a -b)
     - Common Lisp bitwise operations; ash is used for both left and right shifts.