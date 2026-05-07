CSS Pivot View
==============

.. list-table:: CSS Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: css

           --x: 42;
     - CSS custom properties (variables).
   * - IfElse
     - .. code-block:: css

           @media (min-width: 0px) { .element { color: red; } }
     - Media queries provide conditional styling; no true else branch exists.
   * - Loop
     - N/A
     - CSS does not support loops natively.
   * - FunctionDefinition
     - N/A
     - CSS does not support user-defined functions in the traditional sense (excluding Houdini or preprocessors).
   * - ProcedureDefinition
     - N/A
     - CSS does not support procedures.
   * - TryCatch
     - N/A
     - CSS does not have native error handling mechanisms like try-catch.
   * - Raise
     - N/A
     - CSS does not have a mechanism to raise exceptions.
   * - SingleLineComment
     - N/A
     - CSS does not natively support single-line comments (though // is common in preprocessors).
   * - MultiLineComment
     - .. code-block:: css

           /* line 1
              line 2 */
     - Standard CSS block comment.
   * - Print
     - .. code-block:: css

           .element::before { content: "Hello, World!"; }
     - CSS can 'print' text using the content property in pseudo-elements.
   * - Import
     - .. code-block:: css

           @import "base.css";
     - Imports styles from another stylesheet.
   * - SwitchCase
     - N/A
     - CSS does not support switch/case logic.
   * - Constant
     - .. code-block:: css

           --MAX: 100;
     - CSS custom properties act as constants within their scope.
   * - Addition
     - .. code-block:: css

           calc(a + b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - Subtraction
     - .. code-block:: css

           calc(a - b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - Multiplication
     - .. code-block:: css

           calc(a * b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - Division
     - .. code-block:: css

           calc(a / b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - Remainder
     - .. code-block:: css

           mod(a, b)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - Floor
     - N/A
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - Rounding
     - .. code-block:: css

           round(a)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - Increment
     - .. code-block:: css

           calc(a + 1)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - Decrement
     - .. code-block:: css

           calc(a - 1)
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - LeftShift
     - N/A
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - RightShift
     - N/A
     - calc() function allows basic math; mod() and round() are in newer CSS specs.
   * - Bitwise
     - N/A
     - CSS does not support bitwise operations.