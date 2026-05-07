Haskell Pivot View
==================

.. list-table:: Haskell Pivot Table
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
     - .. code-block:: haskell

           let x = 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Immutable binding within a scope; part of let-in or where clause.
   * - IfElse
     - .. code-block:: haskell

           if x > 0 then 1 else 0
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - If-then-else is an expression; both branches must be present and have the same type.
   * - Loop
     - .. code-block:: haskell

           loop x = if x > 0 then loop (x - 1) else return ()
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Haskell uses recursion for iteration as it is a pure functional language.
   * - FunctionDefinition
     - .. code-block:: haskell

           add :: Int -> Int -> Int
           add a b = a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Function types are usually declared explicitly; arguments are space-separated.
   * - ProcedureDefinition
     - .. code-block:: haskell

           logMessage :: String -> IO ()
           logMessage msg = putStrLn msg
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Procedures are functions that return an IO action.
   * - TryCatch
     - .. code-block:: haskell

           do_something `catch` \(e :: SomeException) -> handle e
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Exception handling using the catch function from Control.Exception.
   * - Raise
     - .. code-block:: haskell

           error "Error"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The 'error' function stops execution and displays a message.
   * - Thread
     - .. code-block:: haskell

           forkIO (do_work)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - forkIO creates a lightweight thread (requires Control.Concurrent).
   * - SendMessage
     - .. code-block:: haskell

           writeChan chan 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Writes a value to a Chan (unbounded FIFO channel).
   * - ReceiveMessage
     - .. code-block:: haskell

           msg <- readChan chan
           handle msg
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Reads a value from a Chan; blocks if the channel is empty.
   * - SingleLineComment
     - .. code-block:: haskell

           -- comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: haskell

           {- line 1
              line 2 -}
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard block comment; can be nested.
   * - Print
     - .. code-block:: haskell

           putStrLn "Hello, World!"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Outputs a string followed by a newline in the IO monad.
   * - Import
     - .. code-block:: haskell

           import Data.List
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Imports symbols from a module into the current namespace.
   * - SwitchCase
     - .. code-block:: haskell

           case x of
               1 -> 1
               2 -> 2
               _ -> 0
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses pattern matching in a case expression.
   * - Constant
     - .. code-block:: haskell

           maxVal = 100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Top-level bindings are immutable and effectively constant.
   * - Addition
     - .. code-block:: haskell

           a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard mathematical operators.
   * - Subtraction
     - .. code-block:: haskell

           a - b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard mathematical operators.
   * - Multiplication
     - .. code-block:: haskell

           a * b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard mathematical operators.
   * - Division
     - .. code-block:: haskell

           a / b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Haskell uses / for floating-point and 'div' or 'quot' for integer division.
   * - Remainder
     - .. code-block:: haskell

           a `mod` b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard mathematical operators.
   * - Floor
     - .. code-block:: haskell

           floor a
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard mathematical operators.
   * - Rounding
     - .. code-block:: haskell

           round a
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard mathematical operators.
   * - Increment
     - .. code-block:: haskell

           a + 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - No native increment operator; use addition.
   * - Decrement
     - .. code-block:: haskell

           a - 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - No native decrement operator; use subtraction.
   * - LeftShift
     - .. code-block:: haskell

           shiftL a b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Requires Data.Bits.
   * - RightShift
     - .. code-block:: haskell

           shiftR a b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Requires Data.Bits.
   * - Bitwise
     - N/A
     - .. code-block:: haskell

           a .&. b
     - .. code-block:: haskell

           a .|. b
     - .. code-block:: haskell

           xor a b
     - .. code-block:: haskell

           complement a
     - .. code-block:: haskell

           shiftL a b
     - .. code-block:: haskell

           shiftR a b
     - Requires Data.Bits.