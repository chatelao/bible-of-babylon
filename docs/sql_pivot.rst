SQL Pivot
=========

.. list-table:: SQL Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Multi line
     - String val
     - Number val
     - Boolean val
     - Notes
   * - VariableDeclaration
     - ``DECLARE @x INT = 42;``
     - N/A
     - N/A
     - N/A
     - N/A
     - T-SQL syntax for variable declaration.
   * - IfElse
     - ::

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
     - Uses IF-ELSE with BEGIN-END blocks.
   * - Loop
     - ::

           WHILE @x > 0
           BEGIN
               SET @x = @x - 1
           END
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard WHILE loop in T-SQL.
   * - FunctionDefinition
     - ::

           CREATE FUNCTION add(@a INT, @b INT)
           RETURNS INT AS
           BEGIN
               RETURN @a + @b
           END
     - N/A
     - N/A
     - N/A
     - N/A
     - T-SQL syntax for Scalar-Valued Functions.
   * - TryCatch
     - ::

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
     - T-SQL supports BEGIN TRY...END TRY and BEGIN CATCH...END CATCH blocks.
   * - Raise
     - ``THROW 50000, 'Error', 1;``
     - N/A
     - N/A
     - N/A
     - N/A
     - The THROW statement raises an exception and transfers execution to a CATCH block.
   * - SingleLineComment
     - ``-- comment``
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard SQL single-line comment.
   * - MultiLineComment
     - ::

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard SQL multi-line comment.
   * - Print
     - ``PRINT 'Hello, World!';``
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
     - Standard SQL does not have a native 'import' keyword for code; database objects are globally accessible or schema-qualified.
   * - SwitchCase
     - ::

           CASE @x
               WHEN 1 THEN 'one'
               WHEN 2 THEN 'two'
               ELSE 'none'
           END
     - N/A
     - N/A
     - N/A
     - N/A
     - The CASE expression is used for conditional logic in SQL.
   * - Constant
     - ``DECLARE @MAX INT = 100;``
     - N/A
     - N/A
     - N/A
     - N/A
     - T-SQL variables are not strictly constant, but can be treated as such within a batch or procedure.