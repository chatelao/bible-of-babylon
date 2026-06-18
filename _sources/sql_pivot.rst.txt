SQL
===

.. list-table:: SQL Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: sql

           DECLARE
             x NUMBER := 42;
           BEGIN
             -- usage
           END;
     - PL/SQL syntax for variable declaration. ANSI SQL uses DECLARE in blocks.
   * - CollectionDefinition
     - .. code-block:: sql

           TYPE NumList IS TABLE OF NUMBER;
           t NumList := NumList(1, 2, 3);
     - Oracle PL/SQL uses collection types (Nested Tables, Varrays).
   * - AssociativeArrayDefinition
     - .. code-block:: sql

           TYPE Dict IS TABLE OF NUMBER INDEX BY VARCHAR2(10);
           t Dict;
           t('a') := 1;
           t('b') := 2;
     - Oracle PL/SQL supports Associative Arrays (index-by tables).
   * - SwitchCase
     - .. code-block:: sql

           CASE x
               WHEN 1 THEN 'one'
               WHEN 2 THEN 'two'
               ELSE 'none'
           END
     - The ANSI CASE expression is supported by almost all SQL databases including Oracle.
   * - IfElse
     - .. code-block:: sql

           IF x > 0 THEN
               RETURN 1;
           ELSE
               RETURN 0;
           END IF;
     - Oracle PL/SQL uses IF-THEN-ELSE syntax.
   * - Loop
     - .. code-block:: sql

           WHILE x > 0 LOOP
               x := x - 1;
           END LOOP;
     - Standard WHILE LOOP in Oracle PL/SQL.
   * - FunctionDefinition
     - .. code-block:: sql

           CREATE OR REPLACE FUNCTION add(a NUMBER, b NUMBER)
           RETURN NUMBER AS
           BEGIN
               RETURN a + b;
           END;
     - Oracle PL/SQL function syntax.
   * - ProcedureDefinition
     - .. code-block:: sql

           CREATE OR REPLACE PROCEDURE log_message(msg IN VARCHAR2) AS
           BEGIN
               DBMS_OUTPUT.PUT_LINE(msg);
           END;
     - Oracle PL/SQL procedure syntax.
   * - TryCatch
     - .. code-block:: sql

           BEGIN
               do_something;
           EXCEPTION
               WHEN OTHERS THEN
                   handle_error;
           END;
     - Oracle PL/SQL uses EXCEPTION blocks for error handling.
   * - Raise
     - .. code-block:: sql

           RAISE_APPLICATION_ERROR(-20001, 'Error');
     - RAISE_APPLICATION_ERROR is used to raise user-defined exceptions in Oracle.
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

           DBMS_OUTPUT.PUT_LINE('Hello, World!');
     - Oracle PL/SQL uses DBMS_OUTPUT.PUT_LINE for console output.
   * - Import
     - N/A
     - Standard SQL does not have a native 'import' keyword for code; database objects are globally accessible or schema-qualified.
   * - Constant
     - .. code-block:: sql

           MAX_VAL CONSTANT NUMBER := 100;
     - Oracle PL/SQL supports constant declarations.
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

           MOD(a, b)
     - Oracle uses the MOD function for remainders.
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

           BITAND(a, b)
     - Oracle provides the BITAND function.
   * - BitOr
     - .. code-block:: sql

           a + b - BITAND(a, b)
     - Oracle does not have a native BITOR; it can be simulated using BITAND.
   * - BitXor
     - .. code-block:: sql

           a + b - 2 * BITAND(a, b)
     - Oracle does not have a native BITXOR; it can be simulated using BITAND.
   * - BitNot
     - N/A
     - Oracle does not have a native BITNOT.
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

           FOR i IN 1..10 LOOP
               -- body
           END LOOP;
     - Oracle PL/SQL provides a native FOR loop for ranges.
   * - ForEach
     - .. code-block:: sql

           FOR r IN (SELECT * FROM table) LOOP
               -- access r.column
           END LOOP;
     - Oracle PL/SQL supports cursor FOR loops for easy iteration over result sets.
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
   * - SetFiltering
     - .. code-block:: sql

           SELECT * FROM table WHERE condition;
     - The WHERE clause is used to filter records.
   * - SetJoin
     - .. code-block:: sql

           SELECT * FROM tableA JOIN tableB ON tableA.id = tableB.id;
     - Standard SQL INNER JOIN.
   * - MutexDefinition
     - N/A
     - Database locks (e.g., SELECT ... FOR UPDATE) are used instead of mutexes.
   * - MutexLock
     - N/A
     - N/A
   * - MutexUnlock
     - N/A
     - N/A
   * - SemaphoreDefinition
     - N/A
     - N/A
   * - SemaphoreWait
     - N/A
     - N/A
   * - SemaphoreSignal
     - N/A
     - N/A
   * - ToCharDate
     - .. code-block:: sql

           TO_CHAR(date_col, 'DD.MM.YYYY')
     - Oracle TO_CHAR function for date formatting.
   * - ToCharDateTimezone
     - .. code-block:: sql

           TO_CHAR(datetime_col, 'YYYY-MM-DD HH24:MI:SS TZH:TZM')
     - Oracle TO_CHAR with timezone information.
   * - ToCharNumberThousandSeparator
     - .. code-block:: sql

           TO_CHAR(num, '999,999,990')
     - Oracle TO_CHAR with G (Group separator) or comma.
   * - ToCharNumberNegativeBrackets
     - .. code-block:: sql

           TO_CHAR(num, '999G990D00PR')
     - PR format element in Oracle TO_CHAR wraps negative numbers in brackets.
   * - ToCharNumberFixedDecimals
     - .. code-block:: sql

           TO_CHAR(num, '999990.00')
     - Oracle TO_CHAR with fixed decimal positions.
   * - ToDate
     - .. code-block:: sql

           TO_DATE('31.12.2023', 'DD.MM.YYYY')
     - Oracle TO_DATE function converts string to date.