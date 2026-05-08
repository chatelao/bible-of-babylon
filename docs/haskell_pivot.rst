Haskell Pivot View
==================

.. list-table:: Haskell Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: haskell

           let x = 42
     - Immutable binding within a scope; part of let-in or where clause.
   * - IfElse
     - .. code-block:: haskell

           if x > 0 then 1 else 0
     - If-then-else is an expression; both branches must be present and have the same type.
   * - Loop
     - .. code-block:: haskell

           loop x = if x > 0 then loop (x - 1) else return ()
     - Haskell uses recursion for iteration as it is a pure functional language.
   * - FunctionDefinition
     - .. code-block:: haskell

           add :: Int -> Int -> Int
           add a b = a + b
     - Function types are usually declared explicitly; arguments are space-separated.
   * - ProcedureDefinition
     - .. code-block:: haskell

           logMessage :: String -> IO ()
           logMessage msg = putStrLn msg
     - Procedures are functions that return an IO action.
   * - TryCatch
     - .. code-block:: haskell

           do_something `catch` \(e :: SomeException) -> handle e
     - Exception handling using the catch function from Control.Exception.
   * - Raise
     - .. code-block:: haskell

           error "Error"
     - The 'error' function stops execution and displays a message.
   * - Thread
     - .. code-block:: haskell

           forkIO (do_work)
     - forkIO creates a lightweight thread (requires Control.Concurrent).
   * - SendMessage
     - .. code-block:: haskell

           writeChan chan 42
     - Writes a value to a Chan (unbounded FIFO channel).
   * - ReceiveMessage
     - .. code-block:: haskell

           msg <- readChan chan
           handle msg
     - Reads a value from a Chan; blocks if the channel is empty.
   * - SingleLineComment
     - .. code-block:: haskell

           -- comment
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: haskell

           {- line 1
              line 2 -}
     - Standard block comment; can be nested.
   * - Print
     - .. code-block:: haskell

           putStrLn "Hello, World!"
     - Outputs a string followed by a newline in the IO monad.
   * - Import
     - .. code-block:: haskell

           import Data.List
     - Imports symbols from a module into the current namespace.
   * - SwitchCase
     - .. code-block:: haskell

           case x of
               1 -> 1
               2 -> 2
               _ -> 0
     - Uses pattern matching in a case expression.
   * - Constant
     - .. code-block:: haskell

           maxVal = 100
     - Top-level bindings are immutable and effectively constant.
   * - Addition
     - .. code-block:: haskell

           a + b
     - Standard mathematical operators.
   * - Subtraction
     - .. code-block:: haskell

           a - b
     - Standard mathematical operators.
   * - Multiplication
     - .. code-block:: haskell

           a * b
     - Standard mathematical operators.
   * - Division
     - .. code-block:: haskell

           a / b
     - Haskell uses / for floating-point and 'div' or 'quot' for integer division.
   * - Remainder
     - .. code-block:: haskell

           a `mod` b
     - Standard mathematical operators.
   * - Floor
     - .. code-block:: haskell

           floor a
     - Standard mathematical operators.
   * - Rounding
     - .. code-block:: haskell

           round a
     - Standard mathematical operators.
   * - Increment
     - .. code-block:: haskell

           a + 1
     - No native increment operator; use addition.
   * - Decrement
     - .. code-block:: haskell

           a - 1
     - No native decrement operator; use subtraction.
   * - LeftShift
     - .. code-block:: haskell

           shiftL a b
     - Requires Data.Bits.
   * - RightShift
     - .. code-block:: haskell

           shiftR a b
     - Requires Data.Bits.
   * - BitAnd
     - .. code-block:: haskell

           a .&. b
     - Requires Data.Bits.
   * - BitOr
     - .. code-block:: haskell

           a .|. b
     - Requires Data.Bits.
   * - BitXor
     - .. code-block:: haskell

           xor a b
     - Requires Data.Bits.
   * - BitNot
     - .. code-block:: haskell

           complement a
     - Requires Data.Bits.
   * - Float4VectorMultiplication
     - .. code-block:: haskell

           zipWith (*) a b
     - Applies multiplication element-wise to two lists.
   * - Float4VectorDotProduct
     - .. code-block:: haskell

           dot = sum $ zipWith (*) a b
     - Pure functional approach using zipWith, multiplication, and sum.
   * - Float4VectorCrossProduct
     - .. code-block:: haskell

           cross [a1,a2,a3,_] [b1,b2,b3,_] = [a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1, 0.0]
     - Pure functional implementation using pattern matching.