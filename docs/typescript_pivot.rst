TypeScript Pivot View
=====================

.. list-table:: TypeScript Pivot Table
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
     - .. code-block:: typescript

           let x: number = 42;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Supports static typing on top of JavaScript.
   * - IfElse
     - .. code-block:: typescript

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
     - Standard C-style if-else statement.
   * - Loop
     - .. code-block:: typescript

           while (x > 0) {
               x = x - 1;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard while loop.
   * - FunctionDefinition
     - .. code-block:: typescript

           function add(a: number, b: number): number {
               return a + b;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions support typed parameters and return values.
   * - ProcedureDefinition
     - .. code-block:: typescript

           function logMessage(msg: string): void {
               console.log(msg);
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Procedures use the 'void' return type.
   * - TryCatch
     - .. code-block:: typescript

           try {
               do_something();
           } catch (e) {
               handle(e);
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript exception handling.
   * - Raise
     - .. code-block:: typescript

           throw new Error("Error");
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'throw' to raise an error.
   * - Thread
     - .. code-block:: typescript

           new Worker('worker.js');
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Concurrency is typically handled via Web Workers or asynchronous programming (Promises/async-await).
   * - SendMessage
     - .. code-block:: typescript

           worker.postMessage(42);
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Communicates with a Web Worker.
   * - ReceiveMessage
     - .. code-block:: typescript

           worker.onmessage = (e) => { handle(e.data); };
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Handles messages from a Web Worker.
   * - SingleLineComment
     - .. code-block:: typescript

           // comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: typescript

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard block comment.
   * - Print
     - .. code-block:: typescript

           console.log("Hello, World!");
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Outputs to the console.
   * - Import
     - .. code-block:: typescript

           import { add } from './math';
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - ESM import syntax.
   * - SwitchCase
     - .. code-block:: typescript

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
     - Standard C-style switch statement.
   * - Constant
     - .. code-block:: typescript

           const MAX: number = 100;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses 'const' for immutable declarations.
   * - Addition
     - .. code-block:: typescript

           a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - Subtraction
     - .. code-block:: typescript

           a - b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - Multiplication
     - .. code-block:: typescript

           a * b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - Division
     - .. code-block:: typescript

           a / b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - Remainder
     - .. code-block:: typescript

           a % b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - Floor
     - .. code-block:: typescript

           Math.floor(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - Rounding
     - .. code-block:: typescript

           Math.round(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - Increment
     - .. code-block:: typescript

           a++
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - Decrement
     - .. code-block:: typescript

           a--
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - LeftShift
     - .. code-block:: typescript

           a << b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - RightShift
     - .. code-block:: typescript

           a >> b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard JavaScript operators.
   * - Bitwise
     - N/A
     - .. code-block:: typescript

           a & b
     - .. code-block:: typescript

           a | b
     - .. code-block:: typescript

           a ^ b
     - .. code-block:: typescript

           ~a
     - .. code-block:: typescript

           a << b
     - .. code-block:: typescript

           a >> b
     - Standard bitwise operators.