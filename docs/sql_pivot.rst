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
   * - SwitchCase
     - .. code-block:: sql

           CASE @x
               WHEN 1 THEN 'one'
               WHEN 2 THEN 'two'
               ELSE 'none'
           END
     - The CASE expression is used for conditional logic in SQL.
   * - Constant
     - .. code-block:: sql

           DECLARE @MAX INT = 100;
     - T-SQL variables are not strictly constant, but can be treated as such within a batch or procedure.