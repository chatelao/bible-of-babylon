COBOL Pivot View
================

.. list-table:: COBOL Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: cobol

           01 X PIC 9(4) VALUE 42.
     - Variables are defined in the DATA DIVISION; PIC (picture) clause specifies the data type and size.
   * - IfElse
     - .. code-block:: cobol

           IF X > 0 THEN
               MOVE 1 TO RESULT
           ELSE
               MOVE 0 TO RESULT
           END-IF.
     - Uses IF-THEN-ELSE-END-IF structure; periods are used to terminate sentences.
   * - SwitchCase
     - .. code-block:: cobol

           EVALUATE X
               WHEN 1
                   DISPLAY 'One'
               WHEN 2
                   DISPLAY 'Two'
               WHEN OTHER
                   DISPLAY 'Other'
           END-EVALUATE.
     - The EVALUATE statement is used for multi-way branching.
   * - Loop
     - .. code-block:: cobol

           PERFORM UNTIL X <= 0
               SUBTRACT 1 FROM X
           END-PERFORM.
     - The PERFORM UNTIL construct is used for conditional looping.
   * - ForLoop
     - .. code-block:: cobol

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 10
               *> body
           END-PERFORM.
     - PERFORM VARYING is the COBOL equivalent of a for loop.
   * - FunctionDefinition
     - .. code-block:: cobol

           FUNCTION-ID. ADD-FUNC.
           ...
           COMPUTE RESULT = A + B
           ...
           END FUNCTION ADD-FUNC.
     - User-defined functions were introduced in modern COBOL (COBOL 2002).
   * - ProcedureDefinition
     - .. code-block:: cobol

           IDENTIFICATION DIVISION.
           PROGRAM-ID. LOG-MSG.
           ...
           DISPLAY MSG.
           EXIT PROGRAM.
     - Procedures are typically implemented as separate programs or paragraphs.
   * - TryCatch
     - .. code-block:: cobol

           ADD A TO B ON SIZE ERROR
               DISPLAY 'Arithmetic Overflow'
           END-ADD.
     - COBOL uses imperative 'ON ERROR' clauses for specific operations.
   * - Raise
     - N/A
     - No standard mechanism to 'throw' exceptions; execution is managed via status codes.
   * - Thread
     - N/A
     - Standard COBOL does not support multi-threading.
   * - SendMessage
     - N/A
     - Message passing is not a native COBOL feature.
   * - ReceiveMessage
     - N/A
     - Not supported natively.
   * - SingleLineComment
     - .. code-block:: cobol

           *> comment
     - *> is used for inline comments in free-format COBOL.
   * - MultiLineComment
     - N/A
     - No native multi-line comment syntax; multiple * or *> must be used.
   * - Print
     - .. code-block:: cobol

           DISPLAY "Hello World".
     - DISPLAY outputs data to the system console or standard output.
   * - Import
     - .. code-block:: cobol

           COPY DEFS.
     - The COPY statement includes text from a library at compile time.
   * - Constant
     - .. code-block:: cobol

           01 MAX-VAL PIC 9(3) VALUE 100 CONSTANT.
     - The CONSTANT keyword defines a symbolic constant (COBOL 2002).
   * - Addition
     - .. code-block:: cobol

           ADD A TO B.
     - Adds the value of A to B and stores it in B.
   * - Subtraction
     - .. code-block:: cobol

           SUBTRACT A FROM B.
     - Subtracts A from B and stores it in B.
   * - Multiplication
     - .. code-block:: cobol

           MULTIPLY A BY B.
     - Multiplies A and B and stores the result in B.
   * - Division
     - .. code-block:: cobol

           DIVIDE A BY B GIVING C.
     - Divides A by B and stores the quotient in C.
   * - Remainder
     - .. code-block:: cobol

           DIVIDE A BY B GIVING Q REMAINDER R.
     - Calculates both the quotient and the remainder.
   * - Floor
     - .. code-block:: cobol

           FUNCTION INTEGER(A)
     - The INTEGER intrinsic function returns the greatest integer <= A.
   * - Rounding
     - .. code-block:: cobol

           ADD A TO B ROUNDED.
     - The ROUNDED phrase specifies that any fractional part should be rounded.
   * - Increment
     - .. code-block:: cobol

           ADD 1 TO A.
     - Increments the value of A by 1.
   * - Decrement
     - .. code-block:: cobol

           SUBTRACT 1 FROM A.
     - Decrements the value of A by 1.
   * - LeftShift
     - N/A
     - COBOL does not have native bitwise shift operators.
   * - RightShift
     - N/A
     - COBOL does not have native bitwise shift operators.
   * - BitAnd
     - N/A
     - Not natively supported in standard COBOL.
   * - BitOr
     - N/A
     - Not natively supported in standard COBOL.
   * - BitXor
     - N/A
     - Not natively supported in standard COBOL.
   * - BitNot
     - N/A
     - Not natively supported in standard COBOL.
   * - Float4VectorMultiplication
     - .. code-block:: cobol

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 4
               COMPUTE C(I) = A(I) * B(I)
           END-PERFORM.
     - Requires a loop over the array elements.
   * - Float4VectorDotProduct
     - .. code-block:: cobol

           MOVE 0 TO DOT-PRODUCT.
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 4
               COMPUTE DOT-PRODUCT = DOT-PRODUCT + (A(I) * B(I))
           END-PERFORM.
     - Calculated by accumulating products in a loop.
   * - Float4VectorCrossProduct
     - .. code-block:: cobol

           COMPUTE C(1) = A(2) * B(3) - A(3) * B(2).
           COMPUTE C(2) = A(3) * B(1) - A(1) * B(3).
           COMPUTE C(3) = A(1) * B(2) - A(2) * B(1).
     - Calculated component-wise using COMPUTE.
   * - Equal
     - .. code-block:: cobol

           IF A = B
     -
   * - NotEqual
     - .. code-block:: cobol

           IF A NOT = B
     -
   * - GreaterThan
     - .. code-block:: cobol

           IF A > B
     -
   * - SetFiltering
     - .. code-block:: cobol

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > N
               IF A(I) > 0
                   MOVE A(I) TO B(J)
                   ADD 1 TO J
               END-IF
           END-PERFORM.
     - Manual filtering using a loop and conditional MOVE.
   * - SetJoin
     - .. code-block:: cobol

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > N
               PERFORM VARYING J FROM 1 BY 1 UNTIL J > M
                   IF ID-A(I) = ID-B(J)
                       MOVE TABLE-A(I) TO JOIN-RESULT(K)
                       ...
                   END-IF
               END-PERFORM
           END-PERFORM.
     - Implemented using nested PERFORM VARYING loops.