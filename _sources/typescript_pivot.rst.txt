TypeScript Pivot View
=====================

.. list-table:: TypeScript Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: typescript

           let x: number = 42;
     - Supports static typing on top of JavaScript.
   * - CollectionDefinition
     - .. code-block:: typescript

           const a: number[] = [1, 2, 3];
     - Arrays are the primary collection type in TypeScript.
   * - AssociativeArrayDefinition
     - .. code-block:: typescript

           const m: Map<string, number> = new Map([['a', 1], ['b', 2]]);
     - The Map object provides associative mapping.
   * - IfElse
     - .. code-block:: typescript

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C-style if-else statement.
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
     - Standard C-style switch statement.
   * - Loop
     - .. code-block:: typescript

           while (x > 0) {
               x = x - 1;
           }
     - Standard while loop.
   * - FunctionDefinition
     - .. code-block:: typescript

           function add(a: number, b: number): number {
               return a + b;
           }
     - Functions support typed parameters and return values.
   * - ProcedureDefinition
     - .. code-block:: typescript

           function logMessage(msg: string): void {
               console.log(msg);
           }
     - Procedures use the 'void' return type.
   * - TryCatch
     - .. code-block:: typescript

           try {
               do_something();
           } catch (e) {
               handle(e);
           }
     - Standard JavaScript exception handling.
   * - Raise
     - .. code-block:: typescript

           throw new Error("Error");
     - Uses 'throw' to raise an error.
   * - Thread
     - .. code-block:: typescript

           new Worker('worker.js');
     - Concurrency is typically handled via Web Workers or asynchronous programming (Promises/async-await).
   * - SendMessage
     - .. code-block:: typescript

           worker.postMessage(42);
     - Communicates with a Web Worker.
   * - ReceiveMessage
     - .. code-block:: typescript

           worker.onmessage = (e) => { handle(e.data); };
     - Handles messages from a Web Worker.
   * - SingleLineComment
     - .. code-block:: typescript

           // comment
     - Standard single-line comment.
   * - MultiLineComment
     - .. code-block:: typescript

           /* line 1
              line 2 */
     - Standard block comment.
   * - Print
     - .. code-block:: typescript

           console.log("Hello, World!");
     - Outputs to the console.
   * - Import
     - .. code-block:: typescript

           import { add } from './math';
     - ESM import syntax.
   * - Constant
     - .. code-block:: typescript

           const MAX: number = 100;
     - Uses 'const' for immutable declarations.
   * - Addition
     - .. code-block:: typescript

           a + b
     - Standard JavaScript operators.
   * - Subtraction
     - .. code-block:: typescript

           a - b
     - Standard JavaScript operators.
   * - Multiplication
     - .. code-block:: typescript

           a * b
     - Standard JavaScript operators.
   * - Division
     - .. code-block:: typescript

           a / b
     - Standard JavaScript operators.
   * - Remainder
     - .. code-block:: typescript

           a % b
     - Standard JavaScript operators.
   * - Floor
     - .. code-block:: typescript

           Math.floor(a)
     - Standard JavaScript operators.
   * - Rounding
     - .. code-block:: typescript

           Math.round(a)
     - Standard JavaScript operators.
   * - Increment
     - .. code-block:: typescript

           a++
     - Standard JavaScript operators.
   * - Decrement
     - .. code-block:: typescript

           a--
     - Standard JavaScript operators.
   * - LeftShift
     - .. code-block:: typescript

           a << b
     - Standard JavaScript operators.
   * - RightShift
     - .. code-block:: typescript

           a >> b
     - Standard JavaScript operators.
   * - BitAnd
     - .. code-block:: typescript

           a & b
     - Standard bitwise operators.
   * - BitOr
     - .. code-block:: typescript

           a | b
     - Standard bitwise operators.
   * - BitXor
     - .. code-block:: typescript

           a ^ b
     - Standard bitwise operators.
   * - BitNot
     - .. code-block:: typescript

           ~a
     - Standard bitwise operators.
   * - Float4VectorMultiplication
     - .. code-block:: typescript

           const c = a.map((v, i) => v * b[i]);
     - Uses the Array.map method with the index parameter.
   * - Float4VectorDotProduct
     - .. code-block:: typescript

           const dot = a.reduce((acc, v, i) => acc + v * b[i], 0);
     - Uses Array.reduce to accumulate the product of elements.
   * - Float4VectorCrossProduct
     - .. code-block:: typescript

           const c = [
               a[1]*b[2] - a[2]*b[1],
               a[2]*b[0] - a[0]*b[2],
               a[0]*b[1] - a[1]*b[0],
               0
           ];
     - Uses array indexing to compute the components.
   * - ForLoop
     - .. code-block:: typescript

           for (let i = 0; i < 10; i++) {
               // body
           }
     - Identical to JavaScript; supports typed loop variables.
   * - ForEach
     - .. code-block:: typescript

           for (const item of collection) {
               // body
           }
     - The 'for...of' loop is the modern way to iterate over iterables.
   * - LogicalAnd
     - .. code-block:: typescript

           a && b
     - Short-circuiting logical AND.
   * - LogicalOr
     - .. code-block:: typescript

           a || b
     - Short-circuiting logical OR.
   * - LogicalXor
     - .. code-block:: typescript

           a != b
     - TypeScript uses != for logical XOR between booleans.
   * - Equal
     - .. code-block:: typescript

           a == b
     - Loose equality; === is preferred for strict equality.
   * - NotEqual
     - .. code-block:: typescript

           a != b
     - Loose inequality; !== is preferred for strict inequality.
   * - GreaterThan
     - .. code-block:: typescript

           a > b
     -
   * - SetFiltering
     - .. code-block:: typescript

           const b = a.filter(x => x > 0);
     - Uses the Array.prototype.filter method.
   * - SetJoin
     - .. code-block:: typescript

           const res = a.flatMap(x => b.filter(y => x.id === y.id).map(y => ({...x, ...y})));
     - Uses flatMap and filter for a functional approach.