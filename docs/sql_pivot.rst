SQL Pivot View
==============

.. list-table:: SQL Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Plus
     - Minus
     - Times
     - Divide
     - Mod
     - Floor
     - Round
     - Increment
     - Decrement
     - Bit and
     - Bit or
     - Bit xor
     - Bit not
     - Notes
   * - VariableDeclaration
     - .. code-block:: sql

           DECLARE @x INT = 42;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - T-SQL syntax for variable declaration.
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
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses IF-ELSE with BEGIN-END blocks.
   * - Loop
     - .. code-block:: sql

           WHILE @x > 0
           BEGIN
               SET @x = @x - 1
           END
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard WHILE loop in T-SQL.
   * - FunctionDefinition
     - .. code-block:: sql

           CREATE FUNCTION add(@a INT, @b INT)
           RETURNS INT AS
           BEGIN
               RETURN @a + @b
           END
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - T-SQL syntax for Scalar-Valued Functions.
   * - ProcedureDefinition
     - .. code-block:: sql

           CREATE PROCEDURE log_message @msg NVARCHAR(MAX)
           AS
           BEGIN
               PRINT @msg;
           END
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - T-SQL uses CREATE PROCEDURE for blocks that perform actions.
   * - TryCatch
     - .. code-block:: sql

           BEGIN TRY
               EXEC do_something;
           END TRY
           BEGIN CATCH
               EXEC handle_error;
           END CATCH
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - T-SQL supports BEGIN TRY...END TRY and BEGIN CATCH...END CATCH blocks.
   * - Raise
     - .. code-block:: sql

           THROW 50000, 'Error', 1;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The THROW statement raises an exception and transfers execution to a CATCH block.
   * - SingleLineComment
     - .. code-block:: sql

           -- comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard SQL single-line comment.
   * - MultiLineComment
     - .. code-block:: sql

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard SQL multi-line comment.
   * - Print
     - .. code-block:: sql

           PRINT 'Hello, World!';
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - T-SQL PRINT statement outputs a message to the client.
   * - Import
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard SQL does not have a native 'import' keyword for code; database objects are globally accessible or schema-qualified.
   * - SwitchCase
     - .. code-block:: sql

           CASE @x
               WHEN 1 THEN 'one'
               WHEN 2 THEN 'two'
               ELSE 'none'
           END
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The CASE expression is used for conditional logic in SQL.
   * - Constant
     - .. code-block:: sql

           DECLARE @MAX INT = 100;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - T-SQL variables are not strictly constant, but can be treated as such within a batch or procedure.
   * - Arithmetic
     - N/A
     - .. code-block:: sql

           a + b
     - .. code-block:: sql

           a - b
     - .. code-block:: sql

           a * b
     - .. code-block:: sql

           a / b
     - .. code-block:: sql

           a % b
     - .. code-block:: sql

           FLOOR(a)
     - .. code-block:: sql

           ROUND(a, 0)
     - .. code-block:: sql

           a + 1
     - .. code-block:: sql

           a - 1
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard SQL arithmetic functions.
   * - Bitwise
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - .. code-block:: sql

           a & b
     - .. code-block:: sql

           a | b
     - .. code-block:: sql

           a ^ b
     - .. code-block:: sql

           ~a
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.