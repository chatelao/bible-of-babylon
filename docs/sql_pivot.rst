SQL Pivot View
==============

.. list-table:: SQL Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: sql

           DECLARE @x INT = 42;
     - T-SQL syntax for variable declaration.
   * - SwitchCase
     - .. code-block:: sql

           CASE @x
               WHEN 1 THEN 'one'
               WHEN 2 THEN 'two'
               ELSE 'none'
           END
     - The CASE expression is used for conditional logic in SQL.
   * - IfElse
     - .. code-block:: sql

           IF @x > 0
           BEGIN
               RETURN 1
           END
           ELSE
           BEGIN
               RETURN 0
           END
     - Uses IF-ELSE with BEGIN-END blocks.
   * - Loop
     - .. code-block:: sql

           WHILE @x > 0
           BEGIN
               SET @x = @x - 1
           END
     - Standard WHILE loop in T-SQL.
   * - FunctionDefinition
     - .. code-block:: sql

           CREATE FUNCTION add(@a INT, @b INT)
           RETURNS INT AS
           BEGIN
               RETURN @a + @b
           END
     - T-SQL syntax for Scalar-Valued Functions.
   * - ProcedureDefinition
     - .. code-block:: sql

           CREATE PROCEDURE log_message @msg NVARCHAR(MAX)
           AS
           BEGIN
               PRINT @msg;
           END
     - T-SQL uses CREATE PROCEDURE for blocks that perform actions.
   * - TryCatch
     - .. code-block:: sql

           BEGIN TRY
               EXEC do_something;
           END TRY
           BEGIN CATCH
               EXEC handle_error;
           END CATCH
     - T-SQL supports BEGIN TRY...END TRY and BEGIN CATCH...END CATCH blocks.
   * - Raise
     - .. code-block:: sql

           THROW 50000, 'Error', 1;
     - The THROW statement raises an exception and transfers execution to a CATCH block.
   * - SingleLineComment
     - .. code-block:: sql

           -- comment
     - Standard SQL single-line comment.
   * - MultiLineComment
     - .. code-block:: sql

           /* line 1
              line 2 */
     - Standard SQL multi-line comment.
   * - Print
     - .. code-block:: sql

           PRINT 'Hello, World!';
     - T-SQL PRINT statement outputs a message to the client.
   * - Import
     - N/A
     - Standard SQL does not have a native 'import' keyword for code; database objects are globally accessible or schema-qualified.
   * - Constant
     - .. code-block:: sql

           DECLARE @MAX INT = 100;
     - T-SQL variables are not strictly constant, but can be treated as such within a batch or procedure.
   * - Addition
     - .. code-block:: sql

           a + b
     - Standard SQL arithmetic functions.
   * - Subtraction
     - .. code-block:: sql

           a - b
     - Standard SQL arithmetic functions.
   * - Multiplication
     - .. code-block:: sql

           a * b
     - Standard SQL arithmetic functions.
   * - Division
     - .. code-block:: sql

           a / b
     - Standard SQL arithmetic functions.
   * - Remainder
     - .. code-block:: sql

           a % b
     - Standard SQL arithmetic functions.
   * - Floor
     - .. code-block:: sql

           FLOOR(a)
     - Standard SQL arithmetic functions.
   * - Rounding
     - .. code-block:: sql

           ROUND(a, 0)
     - Standard SQL arithmetic functions.
   * - Increment
     - .. code-block:: sql

           a + 1
     - Standard SQL arithmetic functions.
   * - Decrement
     - .. code-block:: sql

           a - 1
     - Standard SQL arithmetic functions.
   * - LeftShift
     - N/A
     - Standard SQL arithmetic functions.
   * - RightShift
     - N/A
     - Standard SQL arithmetic functions.
   * - BitAnd
     - .. code-block:: sql

           a & b
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - BitOr
     - .. code-block:: sql

           a | b
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - BitXor
     - .. code-block:: sql

           a ^ b
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - BitNot
     - .. code-block:: sql

           ~a
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - Float4VectorMultiplication
     - .. code-block:: sql

           SELECT a1*b1, a2*b2, a3*b3, a4*b4
     - SQL typically operates on columns; vector operations are dialect-specific.
   * - Float4VectorDotProduct
     - .. code-block:: sql

           SELECT a1*b1 + a2*b2 + a3*b3 + a4*b4
     - Calculated by manually summing component-wise products.
   * - Float4VectorCrossProduct
     - .. code-block:: sql

           SELECT a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1, 0.0
     - Computed using column-wise arithmetic.
   * - ForLoop
     - .. code-block:: sql

           DECLARE @i INT = 0;
           WHILE @i < 10
           BEGIN
               -- body
               SET @i = @i + 1;
           END
     - T-SQL uses WHILE loops; there is no native FOR loop for ranges.
   * - Equal
     - .. code-block:: sql

           a = b
     - Standard SQL equality operator.
   * - NotEqual
     - .. code-block:: sql

           a <> b
     - Standard SQL inequality operator; some dialects also support !=.
   * - GreaterThan
     - .. code-block:: sql

           a > b
     -