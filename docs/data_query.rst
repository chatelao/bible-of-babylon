Data Query Languages
====================



VariableDeclaration
-------------------


:description: The act of naming a value and optionally specifying its type.


Parameters:

* name: String

* type: String

* initial_value: Number

* syntax: String

* notes: String



.. list-table:: VariableDeclaration Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlVar
     - .. code-block:: sql

           DECLARE @x INT = 42;
     - T-SQL syntax for variable declaration.
   * - XQueryVar
     - .. code-block:: xquery

           let $x := 42
     - XQuery uses 'let' for variable binding.
   * - GraphQlVariableDeclaration
     - .. code-block:: graphql

           $x: Int = 42
     - Variables in GraphQL are prefixed with $ and used in operation definitions.
   * - SparqlVariableDeclaration
     - .. code-block:: sparql

           BIND(42 AS ?x)
     - The BIND clause assigns a value to a variable.
   * - OverpassTurboVariableDeclaration
     - .. code-block:: text

           .setname
     - Overpass QL uses sets (prefixed with .) to store results.



ForEach
-------


:description: Iterating over the elements of a collection.


Parameters:

* syntax: String

* notes: String



.. list-table:: ForEach Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlForEach
     - .. code-block:: sql

           DECLARE cursor_name CURSOR FOR SELECT col FROM table;
           OPEN cursor_name;
           FETCH NEXT FROM cursor_name INTO @item;
           WHILE @@FETCH_STATUS = 0
           BEGIN
               -- body
               FETCH NEXT FROM cursor_name INTO @item;
           END
     - SQL typically uses cursors for row-by-row iteration.
   * - XQueryForEach
     - .. code-block:: xquery

           for $item in $collection
           return $item
     - The FLWOR 'for' clause naturally iterates over items in a sequence.
   * - GraphQlForEach
     - N/A
     - N/A
   * - SparqlForEach
     - N/A
     - N/A
   * - OverpassTurboForEach
     - .. code-block:: text

           foreach .item ( ... )
     - The foreach statement iterates over the elements of a set.



CollectionDefinition
--------------------


:description: Declaring and optionally initializing an ordered sequence of elements.


Parameters:

* name: String

* type: String

* syntax: String

* notes: String



.. list-table:: CollectionDefinition Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlCollectionDefinition
     - .. code-block:: sql

           DECLARE @t TABLE (val INT);
           INSERT INTO @t VALUES (1), (2), (3);
     - Collections are typically represented as table variables or temporary tables.
   * - XQueryCollectionDefinition
     - .. code-block:: xquery

           let $s := (1, 2, 3)
     - Sequences are the primary collection type in XQuery, created using parentheses and commas.
   * - GraphQlCollectionDefinition
     - .. code-block:: graphql

           $l: [Int] = [1, 2, 3]
     - Lists in GraphQL are defined with square brackets.
   * - SparqlCollectionDefinition
     - .. code-block:: sparql

           VALUES ?x { 1 2 3 }
     - VALUES can be used to define a set of values for a variable.
   * - OverpassTurboCollectionDefinition
     - .. code-block:: text

           .a
     - Collections are represented by sets, which store OSM elements.



AssociativeArrayDefinition
--------------------------


:description: Declaring and optionally initializing a collection of key-value pairs.


Parameters:

* name: String

* syntax: String

* notes: String



.. list-table:: AssociativeArrayDefinition Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlAssociativeArrayDefinition
     - .. code-block:: sql

           DECLARE @t TABLE (key_name NVARCHAR(10), val INT);
           INSERT INTO @t VALUES ('a', 1), ('b', 2);
     - Associative mapping is achieved through table structures with key/value columns.
   * - XQueryAssociativeArrayDefinition
     - .. code-block:: xquery

           let $m := map { "a": 1, "b": 2 }
     - Maps were introduced in XQuery 3.1.
   * - GraphQlAssociativeArrayDefinition
     - N/A
     - GraphQL does not have a native associative array type for variables.
   * - SparqlAssociativeArrayDefinition
     - N/A
     - SPARQL does not have a native associative array type.
   * - OverpassTurboAssociativeArrayDefinition
     - N/A
     - Overpass QL does not support associative arrays.



Equal
-----


:description: Checks if two values are equal.


Parameters:

* syntax: String

* notes: String



.. list-table:: Equal Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlEqual
     - .. code-block:: sql

           a = b
     - Standard SQL equality operator.
   * - XQueryEqual
     - .. code-block:: xquery

           $a = $b
     - General comparison operator; use 'eq' for value comparison of single items.
   * - GraphQlEqual
     - N/A
     - GraphQL does not have a native equality operator in the query language itself.
   * - SparqlEqual
     - .. code-block:: sparql

           FILTER(?a = ?b)
     - Equality is checked within a FILTER or BIND expression.
   * - OverpassTurboEqual
     - .. code-block:: text

           ["name"="Berlin"]
     - Equality is used in attribute filters.



NotEqual
--------


:description: Checks if two values are not equal.


Parameters:

* syntax: String

* notes: String



.. list-table:: NotEqual Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlNotEqual
     - .. code-block:: sql

           a <> b
     - Standard SQL inequality operator; some dialects also support !=.
   * - XQueryNotEqual
     - .. code-block:: xquery

           $a != $b
     - General comparison operator; use 'ne' for value comparison of single items.
   * - GraphQlNotEqual
     - N/A
     - N/A
   * - SparqlNotEqual
     - .. code-block:: sparql

           FILTER(?a != ?b)
     - Inequality check in SPARQL.
   * - OverpassTurboNotEqual
     - .. code-block:: text

           ["name"!="Berlin"]
     - Inequality in attribute filters.



GreaterThan
-----------


:description: Checks if the first value is greater than the second.


Parameters:

* syntax: String

* notes: String



.. list-table:: GreaterThan Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlGreaterThan
     - .. code-block:: sql

           a > b
     -
   * - XQueryGreaterThan
     - .. code-block:: xquery

           $a > $b
     - General comparison operator; use 'gt' for value comparison of single items.
   * - GraphQlGreaterThan
     - N/A
     - N/A
   * - SparqlGreaterThan
     - .. code-block:: sparql

           FILTER(?a > ?b)
     - Greater than comparison in SPARQL.
   * - OverpassTurboGreaterThan
     - N/A
     - Overpass QL has limited support for numeric comparisons in some implementations.



LogicalAnd
----------


:description: Returns true if both boolean operands are true.


Parameters:

* syntax: String

* notes: String





LogicalOr
---------


:description: Returns true if at least one boolean operand is true.


Parameters:

* syntax: String

* notes: String





LogicalXor
----------


:description: Returns true if exactly one boolean operand is true.


Parameters:

* syntax: String

* notes: String





ProcedureDefinition
-------------------


:description: Declaration of a reusable block of code with parameters and no return value.


Parameters:

* name: String

* parameters: List<String>

* body: Block

* syntax: String

* notes: String



.. list-table:: ProcedureDefinition Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlProcedure
     - .. code-block:: sql

           CREATE PROCEDURE log_message @msg NVARCHAR(MAX)
           AS
           BEGIN
               PRINT @msg;
           END
     - T-SQL uses CREATE PROCEDURE for blocks that perform actions.
   * - XQueryProcedure
     - .. code-block:: xquery

           declare function local:log-message(
               $msg as xs:string
           ) as empty-sequence() {
               (); (: side effects in XQuery are implementation-defined or via extensions :)
           };
     - XQuery functions return empty-sequence() to simulate procedures.
   * - GraphQlProcedureDefinition
     - N/A
     - GraphQL does not support procedure definitions.
   * - SparqlProcedureDefinition
     - N/A
     - SPARQL does not support procedure definitions.
   * - OverpassTurboProcedureDefinition
     - N/A
     - N/A



FunctionDefinition
------------------


:description: Declaration of a reusable block of code with parameters and a return value.


Parameters:

* name: String

* parameters: List<String>

* return_type: String

* body: Block

* syntax: String

* notes: String



.. list-table:: FunctionDefinition Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlFunction
     - .. code-block:: sql

           CREATE FUNCTION add(@a INT, @b INT)
           RETURNS INT AS
           BEGIN
               RETURN @a + @b
           END
     - T-SQL syntax for Scalar-Valued Functions.
   * - XQueryFunction
     - .. code-block:: xquery

           declare function local:add(
               $a as xs:integer,
               $b as xs:integer
           ) as xs:integer {
               $a + $b
           };
     - Functions must be declared in a namespace (e.g., 'local').
   * - GraphQlFunctionDefinition
     - .. code-block:: graphql

           query getUser($id: ID) {
               user(id: $id) {
                   name
               }
           }
     - Operations (query, mutation, subscription) are the closest equivalent to functions.
   * - SparqlFunctionDefinition
     - N/A
     - User-defined functions are implementation-dependent (e.g., via ARQ).
   * - OverpassTurboFunctionDefinition
     - N/A
     - N/A



IfElse
------


:description: Conditional execution of code blocks.


Parameters:

* condition: String

* then_branch: Block

* else_branch: Block

* syntax: String

* notes: String



.. list-table:: IfElse Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlIfElse
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
   * - XQueryIfElse
     - .. code-block:: xquery

           if ($x > 0) then 1 else 0
     - Functional if-then-else expression; both branches are required.
   * - GraphQlIfElse
     - .. code-block:: graphql

           @skip(if: $condition) or @include(if: $condition)
     - Directives provide conditional inclusion of fields.
   * - SparqlIfElse
     - .. code-block:: sparql

           BIND(IF(?x > 0, 1, 0) AS ?res)
     - The IF function returns one of two expressions based on a condition.
   * - OverpassTurboIfElse
     - .. code-block:: text

           if (condition) { ... } else { ... }
     - Control flow statements were added in recent versions of Overpass QL.



SwitchCase
----------


:description: Multi-way branch based on the value of an expression.


Parameters:

* expression: String

* syntax: String

* notes: String



.. list-table:: SwitchCase Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlSwitchCase
     - .. code-block:: sql

           CASE @x
               WHEN 1 THEN 'one'
               WHEN 2 THEN 'two'
               ELSE 'none'
           END
     - The CASE expression is used for conditional logic in SQL.
   * - XQuerySwitchCase
     - .. code-block:: xquery

           switch ($x)
             case 1 return "one"
             case 2 return "two"
             default return "none"
     - The 'switch' expression was introduced in XQuery 3.0.
   * - GraphQlSwitchCase
     - N/A
     - N/A
   * - SparqlSwitchCase
     - .. code-block:: sparql

           COALESCE(IF(?x=1, 'one', 1/0), IF(?x=2, 'two', 1/0), 'none')
     - Multi-way branching can be simulated using nested IFs or COALESCE.
   * - OverpassTurboSwitchCase
     - N/A
     - N/A



Loop
----


:description: Repeated execution of a code block based on a condition.


Parameters:

* condition: String

* body: Block

* syntax: String

* notes: String



.. list-table:: Loop Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlLoop
     - .. code-block:: sql

           WHILE @x > 0
           BEGIN
               SET @x = @x - 1
           END
     - Standard WHILE loop in T-SQL.
   * - XQueryLoop
     - .. code-block:: xquery

           for $i in 1 to $x return $i
     - XQuery uses 'for' expressions for iteration over sequences.
   * - GraphQlLoop
     - N/A
     - GraphQL does not support loops in queries.
   * - SparqlLoop
     - N/A
     - SPARQL is a declarative query language and does not have loops.
   * - OverpassTurboLoop
     - .. code-block:: text

           foreach .a ( ... )
     - The foreach statement iterates over the elements of a set.



ForLoop
-------


:description: Iterating over a range or collection.


Parameters:

* syntax: String

* notes: String



.. list-table:: ForLoop Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlForLoop
     - .. code-block:: sql

           DECLARE @i INT = 0;
           WHILE @i < 10
           BEGIN
               -- body
               SET @i = @i + 1;
           END
     - T-SQL uses WHILE loops; there is no native FOR loop for ranges.
   * - XQueryForLoop
     - .. code-block:: xquery

           for $i in 1 to 10
           return $i
     - Iterates over a sequence and returns a new sequence.
   * - GraphQlForLoop
     - N/A
     - N/A
   * - SparqlForLoop
     - N/A
     - N/A
   * - OverpassTurboForLoop
     - .. code-block:: text

           for ( ... )
     - Overpass QL supports C-style for loops in recent versions.



TryCatch
--------


:description: Handling exceptions or errors within a block of code.


Parameters:

* try_body: Block

* exception_type: String

* error_variable: String

* catch_body: Block

* syntax: String

* notes: String



.. list-table:: TryCatch Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlTryCatch
     - .. code-block:: sql

           BEGIN TRY
               EXEC do_something;
           END TRY
           BEGIN CATCH
               EXEC handle_error;
           END CATCH
     - T-SQL supports BEGIN TRY...END TRY and BEGIN CATCH...END CATCH blocks.
   * - XQueryTryCatch
     - .. code-block:: xquery

           try {
               do_something()
           } catch * {
               handle($err)
           }
     - XQuery 3.0+ supports try-catch; $err is a variable containing error information.
   * - GraphQlTryCatch
     - N/A
     - Errors are returned in the 'errors' field of the response.
   * - SparqlTryCatch
     - N/A
     - Errors in expressions (like division by zero) result in the value being unbound.
   * - OverpassTurboTryCatch
     - N/A
     - N/A



Raise
-----


:description: Explicitly triggering an exception or error.


Parameters:

* exception_type: String

* message: String

* syntax: String

* notes: String



.. list-table:: Raise Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlRaise
     - .. code-block:: sql

           THROW 50000, 'Error', 1;
     - The THROW statement raises an exception and transfers execution to a CATCH block.
   * - XQueryRaise
     - .. code-block:: xquery

           fn:error(fn:QName('http://example.com/errors', 'MY_ERROR'), 'Error')
     - The fn:error() function signals a dynamic error.
   * - GraphQlRaise
     - N/A
     - N/A
   * - SparqlRaise
     - N/A
     - N/A
   * - OverpassTurboRaise
     - N/A
     - N/A



Thread
------


:description: Creating and running a new thread of execution.


Parameters:

* body: Block

* syntax: String

* notes: String



.. list-table:: Thread Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - GraphQlThread
     - N/A
     - N/A
   * - SparqlThread
     - N/A
     - N/A
   * - OverpassTurboThread
     - N/A
     - N/A



SendMessage
-----------


:description: Sending a message to another process or thread.


Parameters:

* recipient: String

* message: String

* syntax: String

* notes: String



.. list-table:: SendMessage Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - GraphQlSendMessage
     - N/A
     - N/A
   * - SparqlSendMessage
     - N/A
     - N/A
   * - OverpassTurboSendMessage
     - N/A
     - N/A



ReceiveMessage
--------------


:description: Receiving a message from another process or thread.


Parameters:

* match_pattern: String

* body: Block

* syntax: String

* notes: String



.. list-table:: ReceiveMessage Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - GraphQlReceiveMessage
     - .. code-block:: graphql

           subscription { ... }
     - Subscriptions allow receiving real-time updates.
   * - SparqlReceiveMessage
     - N/A
     - N/A
   * - OverpassTurboReceiveMessage
     - N/A
     - N/A



MutexDefinition
---------------


:description: Declaring and optionally initializing a mutual exclusion object.


Parameters:

* name: String

* syntax: String

* notes: String



.. list-table:: MutexDefinition Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlMutexDefinition
     - N/A
     - Database locks (e.g., SELECT ... FOR UPDATE) are used instead of mutexes.



MutexLock
---------


:description: Acquiring a lock on a mutex, blocking if it is already held.


Parameters:

* syntax: String

* notes: String



.. list-table:: MutexLock Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlMutexLock
     - N/A
     - N/A



MutexUnlock
-----------


:description: Releasing a held lock on a mutex.


Parameters:

* syntax: String

* notes: String



.. list-table:: MutexUnlock Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlMutexUnlock
     - N/A
     - N/A



SemaphoreDefinition
-------------------


:description: Declaring and initializing a semaphore with a specific count.


Parameters:

* name: String

* initial_value: Number

* syntax: String

* notes: String



.. list-table:: SemaphoreDefinition Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlSemaphoreDefinition
     - N/A
     - N/A



SemaphoreWait
-------------


:description: Decreasing the semaphore count, blocking if the count is zero.


Parameters:

* syntax: String

* notes: String



.. list-table:: SemaphoreWait Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlSemaphoreWait
     - N/A
     - N/A



SemaphoreSignal
---------------


:description: Increasing the semaphore count, potentially unblocking a waiting thread.


Parameters:

* syntax: String

* notes: String



.. list-table:: SemaphoreSignal Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlSemaphoreSignal
     - N/A
     - N/A



SingleLineComment
-----------------


:description: Way to add non-executable explanatory text to a single line of source code.


Parameters:

* syntax: String

* notes: String



.. list-table:: SingleLineComment Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlSingleLineComment
     - .. code-block:: sql

           -- comment
     - Standard SQL single-line comment.
   * - XQuerySingleLineComment
     - .. code-block:: xquery

           (: comment :)
     - XQuery uses (: :) for single-line comments.
   * - GraphQlSingleLineComment
     - .. code-block:: graphql

           # comment
     - Standard GraphQL comment.
   * - SparqlSingleLineComment
     - .. code-block:: sparql

           # comment
     - SPARQL comments start with #.
   * - OverpassTurboSingleLineComment
     - .. code-block:: text

           // comment
     - C-style single-line comments.



MultiLineComment
----------------


:description: Way to add non-executable explanatory text spanning multiple lines of source code.


Parameters:

* syntax: String

* notes: String



.. list-table:: MultiLineComment Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlMultiLineComment
     - .. code-block:: sql

           /* line 1
              line 2 */
     - Standard SQL multi-line comment.
   * - XQueryMultiLineComment
     - .. code-block:: xquery

           (: line 1
              line 2 :)
     - XQuery uses (: :) for multi-line comments.
   * - GraphQlMultiLineComment
     - .. code-block:: graphql

           """ comment """
     - Block strings can be used as multi-line descriptions/comments.
   * - SparqlMultiLineComment
     - N/A
     - SPARQL does not support multi-line comments.
   * - OverpassTurboMultiLineComment
     - .. code-block:: text

           /* comment */
     - C-style multi-line comments.



Print
-----


:description: Outputting text to the console or standard output.


Parameters:

* value: String

* syntax: String

* notes: String



.. list-table:: Print Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlPrint
     - .. code-block:: sql

           PRINT 'Hello, World!';
     - T-SQL PRINT statement outputs a message to the client.
   * - XQueryPrint
     - .. code-block:: xquery

           "Hello, World!"
     - In XQuery, a string literal is often the result of an expression and is automatically serialized to output.
   * - GraphQlPrint
     - N/A
     - N/A
   * - SparqlPrint
     - N/A
     - Results are returned as bindings or a graph.
   * - OverpassTurboPrint
     - .. code-block:: text

           out;
     - The out statement produces the result of the query.



Import
------


:description: Including external modules, packages, or files into the current scope.


Parameters:

* module_name: String

* syntax: String

* notes: String



.. list-table:: Import Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlImport
     - N/A
     - Standard SQL does not have a native 'import' keyword for code; database objects are globally accessible or schema-qualified.
   * - XQueryImport
     - .. code-block:: xquery

           import module namespace utils = "http://example.com/utils";
     - Imports a library module by its namespace URI.
   * - GraphQlImport
     - N/A
     - Schema stitching or federation is used to combine schemas.
   * - SparqlImport
     - .. code-block:: sparql

           PREFIX dc: <http://purl.org/dc/elements/1.1/>
     - PREFIX defines a namespace prefix.
   * - OverpassTurboImport
     - .. code-block:: text

           [out:json];
     - Settings (like output format) are specified at the beginning of the script.



Constant
--------


:description: Declaration of an immutable value that remains unchanged throughout the program's execution.


Parameters:

* name: String

* type: String

* value: String

* syntax: String

* notes: String



.. list-table:: Constant Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlConstant
     - .. code-block:: sql

           DECLARE @MAX INT = 100;
     - T-SQL variables are not strictly constant, but can be treated as such within a batch or procedure.
   * - XQueryConstant
     - .. code-block:: xquery

           declare variable $MAX as xs:integer := 100;
     - In XQuery, variables declared in the prolog are immutable by default.
   * - GraphQlConstant
     - N/A
     - N/A
   * - SparqlConstant
     - .. code-block:: sparql

           VALUES ?MAX { 100 }
     - VALUES can be used to provide constant values for variables.
   * - OverpassTurboConstant
     - .. code-block:: text

           {{key=value}}
     - Overpass Turbo (the web interface) supports mustache-style constants.



Addition
--------


:description: Addition of two numeric values.


Parameters:

* syntax: String

* notes: String



.. list-table:: Addition Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlAddition
     - .. code-block:: sql

           a + b
     - Standard SQL arithmetic functions.
   * - XQueryAddition
     - .. code-block:: xquery

           a + b
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlAddition
     - N/A
     - N/A
   * - SparqlAddition
     - .. code-block:: sparql

           ?a + ?b
     - Arithmetic operators in SPARQL.
   * - OverpassTurboAddition
     - N/A
     - N/A



Subtraction
-----------


:description: Subtraction of two numeric values.


Parameters:

* syntax: String

* notes: String



.. list-table:: Subtraction Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlSubtraction
     - .. code-block:: sql

           a - b
     - Standard SQL arithmetic functions.
   * - XQuerySubtraction
     - .. code-block:: xquery

           a - b
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlSubtraction
     - N/A
     - N/A
   * - SparqlSubtraction
     - .. code-block:: sparql

           ?a - ?b
     - Arithmetic operators in SPARQL.
   * - OverpassTurboSubtraction
     - N/A
     - N/A



Multiplication
--------------


:description: Multiplication of two numeric values.


Parameters:

* syntax: String

* notes: String



.. list-table:: Multiplication Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlMultiplication
     - .. code-block:: sql

           a * b
     - Standard SQL arithmetic functions.
   * - XQueryMultiplication
     - .. code-block:: xquery

           a * b
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlMultiplication
     - N/A
     - N/A
   * - SparqlMultiplication
     - .. code-block:: sparql

           ?a * ?b
     - Arithmetic operators in SPARQL.
   * - OverpassTurboMultiplication
     - N/A
     - N/A



Division
--------


:description: Division of two numeric values.


Parameters:

* syntax: String

* notes: String



.. list-table:: Division Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlDivision
     - .. code-block:: sql

           a / b
     - Standard SQL arithmetic functions.
   * - XQueryDivision
     - .. code-block:: xquery

           a div b
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlDivision
     - N/A
     - N/A
   * - SparqlDivision
     - .. code-block:: sparql

           ?a / ?b
     - Arithmetic operators in SPARQL.
   * - OverpassTurboDivision
     - N/A
     - N/A



Remainder
---------


:description: The remainder after division of one number by another (modulo).


Parameters:

* syntax: String

* notes: String



.. list-table:: Remainder Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlRemainder
     - .. code-block:: sql

           a % b
     - Standard SQL arithmetic functions.
   * - XQueryRemainder
     - .. code-block:: xquery

           a mod b
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlRemainder
     - N/A
     - N/A
   * - SparqlRemainder
     - N/A
     - N/A
   * - OverpassTurboRemainder
     - N/A
     - N/A



Floor
-----


:description: The largest integer less than or equal to a given number.


Parameters:

* syntax: String

* notes: String



.. list-table:: Floor Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlFloor
     - .. code-block:: sql

           FLOOR(a)
     - Standard SQL arithmetic functions.
   * - XQueryFloor
     - .. code-block:: xquery

           floor(a)
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlFloor
     - N/A
     - N/A
   * - SparqlFloor
     - .. code-block:: sparql

           floor(?a)
     - Standard SPARQL function.
   * - OverpassTurboFloor
     - N/A
     - N/A



Rounding
--------


:description: Rounding a number to the nearest integer.


Parameters:

* syntax: String

* notes: String



.. list-table:: Rounding Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlRounding
     - .. code-block:: sql

           ROUND(a, 0)
     - Standard SQL arithmetic functions.
   * - XQueryRounding
     - .. code-block:: xquery

           round(a)
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlRounding
     - N/A
     - N/A
   * - SparqlRounding
     - .. code-block:: sparql

           round(?a)
     - Standard SPARQL function.
   * - OverpassTurboRounding
     - N/A
     - N/A



Increment
---------


:description: Increasing the value of a variable by one.


Parameters:

* syntax: String

* notes: String



.. list-table:: Increment Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlIncrement
     - .. code-block:: sql

           a + 1
     - Standard SQL arithmetic functions.
   * - XQueryIncrement
     - .. code-block:: xquery

           a + 1
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlIncrement
     - N/A
     - N/A
   * - SparqlIncrement
     - .. code-block:: sparql

           ?a + 1
     - N/A
   * - OverpassTurboIncrement
     - N/A
     - N/A



Decrement
---------


:description: Decreasing the value of a variable by one.


Parameters:

* syntax: String

* notes: String



.. list-table:: Decrement Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlDecrement
     - .. code-block:: sql

           a - 1
     - Standard SQL arithmetic functions.
   * - XQueryDecrement
     - .. code-block:: xquery

           a - 1
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlDecrement
     - N/A
     - N/A
   * - SparqlDecrement
     - .. code-block:: sparql

           ?a - 1
     - N/A
   * - OverpassTurboDecrement
     - N/A
     - N/A



LeftShift
---------


:description: Shifting the bits of a number to the left.


Parameters:

* syntax: String

* notes: String



.. list-table:: LeftShift Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlLeftShift
     - N/A
     - Standard SQL arithmetic functions.
   * - XQueryLeftShift
     - N/A
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlLeftShift
     - N/A
     - N/A
   * - SparqlLeftShift
     - N/A
     - N/A
   * - OverpassTurboLeftShift
     - N/A
     - N/A



RightShift
----------


:description: Shifting the bits of a number to the right.


Parameters:

* syntax: String

* notes: String



.. list-table:: RightShift Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlRightShift
     - N/A
     - Standard SQL arithmetic functions.
   * - XQueryRightShift
     - N/A
     - Uses 'div' for division and 'idiv' for integer division.
   * - GraphQlRightShift
     - N/A
     - N/A
   * - SparqlRightShift
     - N/A
     - N/A
   * - OverpassTurboRightShift
     - N/A
     - N/A



BitAnd
------


:description: Bitwise AND operation.


Parameters:

* syntax: String

* notes: String



.. list-table:: BitAnd Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlBitAnd
     - .. code-block:: sql

           a & b
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - XQueryBitAnd
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - GraphQlBitAnd
     - N/A
     - N/A
   * - SparqlBitAnd
     - N/A
     - N/A
   * - OverpassTurboBitAnd
     - N/A
     - N/A



BitOr
-----


:description: Bitwise OR operation.


Parameters:

* syntax: String

* notes: String



.. list-table:: BitOr Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlBitOr
     - .. code-block:: sql

           a | b
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - XQueryBitOr
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - GraphQlBitOr
     - N/A
     - N/A
   * - SparqlBitOr
     - N/A
     - N/A
   * - OverpassTurboBitOr
     - N/A
     - N/A



BitXor
------


:description: Bitwise XOR operation.


Parameters:

* syntax: String

* notes: String



.. list-table:: BitXor Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlBitXor
     - .. code-block:: sql

           a ^ b
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - XQueryBitXor
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - GraphQlBitXor
     - N/A
     - N/A
   * - SparqlBitXor
     - N/A
     - N/A
   * - OverpassTurboBitXor
     - N/A
     - N/A



BitNot
------


:description: Bitwise NOT operation (bitwise complement).


Parameters:

* syntax: String

* notes: String



.. list-table:: BitNot Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlBitNot
     - .. code-block:: sql

           ~a
     - Bitwise support varies by SQL dialect; T-SQL supports &, |, ^, ~.
   * - XQueryBitNot
     - N/A
     - Standard XQuery does not have native bitwise operators.
   * - GraphQlBitNot
     - N/A
     - N/A
   * - SparqlBitNot
     - N/A
     - N/A
   * - OverpassTurboBitNot
     - N/A
     - N/A



Float4VectorMultiplication
--------------------------


:description: Element-wise multiplication of two 4-component floating-point vectors.


Parameters:

* syntax: String

* notes: String



.. list-table:: Float4VectorMultiplication Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlFloat4VectorMultiplication
     - .. code-block:: sql

           SELECT a1*b1, a2*b2, a3*b3, a4*b4
     - SQL typically operates on columns; vector operations are dialect-specific.
   * - XQueryFloat4VectorMultiplication
     - .. code-block:: xquery

           for $i in 1 to 4 return $a[$i] * $b[$i]
     - Uses a for expression to iterate over indices.
   * - GraphQlFloat4VectorMultiplication
     - N/A
     - N/A
   * - SparqlFloat4VectorMultiplication
     - N/A
     - N/A
   * - OverpassTurboFloat4VectorMultiplication
     - N/A
     - N/A



Float4VectorDotProduct
----------------------


:description: Scalar product of two 4-component floating-point vectors.


Parameters:

* syntax: String

* notes: String



.. list-table:: Float4VectorDotProduct Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlFloat4VectorDotProduct
     - .. code-block:: sql

           SELECT a1*b1 + a2*b2 + a3*b3 + a4*b4
     - Calculated by manually summing component-wise products.
   * - XQueryFloat4VectorDotProduct
     - .. code-block:: xquery

           sum(for $i in 1 to 4 return $a[$i] * $b[$i])
     - Uses the built-in sum() function over a sequence of products.
   * - GraphQlFloat4VectorDotProduct
     - N/A
     - N/A
   * - SparqlFloat4VectorDotProduct
     - N/A
     - N/A
   * - OverpassTurboFloat4VectorDotProduct
     - N/A
     - N/A



Float4VectorCrossProduct
------------------------


:description: 3D cross product of two 4-component floating-point vectors (using the first three components).


Parameters:

* syntax: String

* notes: String



.. list-table:: Float4VectorCrossProduct Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlFloat4VectorCrossProduct
     - .. code-block:: sql

           SELECT a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1, 0.0
     - Computed using column-wise arithmetic.
   * - XQueryFloat4VectorCrossProduct
     - .. code-block:: xquery

           ($a[2]*$b[3] - $a[3]*$b[2], $a[3]*$b[1] - $a[1]*$b[3], $a[1]*$b[2] - $a[2]*$b[1], 0.0)
     - Uses sequence indexing (1-indexed).
   * - GraphQlFloat4VectorCrossProduct
     - N/A
     - N/A
   * - SparqlFloat4VectorCrossProduct
     - N/A
     - N/A
   * - OverpassTurboFloat4VectorCrossProduct
     - N/A
     - N/A



SetFiltering
------------


:description: Filtering elements from a collection based on a condition (e.g., WHERE clause).


Parameters:

* syntax: String

* notes: String



.. list-table:: SetFiltering Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlSetFiltering
     - .. code-block:: sql

           SELECT * FROM table WHERE condition;
     - The WHERE clause is used to filter records.
   * - XQuerySetFiltering
     - .. code-block:: xquery

           for $x in $collection
           where $x/condition
           return $x
     - The where clause in a FLWOR expression filters sequences.
   * - GraphQlSetFiltering
     - .. code-block:: graphql

           user(id: 42)
     - Filtering is typically done via field arguments.
   * - SparqlSetFiltering
     - .. code-block:: sparql

           FILTER(?x > 0)
     - The FILTER clause restricts the solutions.
   * - OverpassTurboSetFiltering
     - .. code-block:: text

           node["name"="Berlin"];
     - Filters elements by tags or location.



SetJoin
-------


:description: Combining elements from two collections based on a related column or condition (e.g., JOIN ... ON).


Parameters:

* syntax: String

* notes: String



.. list-table:: SetJoin Comparison
   :widths: auto
   :header-rows: 1

   * - Language
     - Syntax
     - Notes
   * - SqlSetJoin
     - .. code-block:: sql

           SELECT * FROM tableA JOIN tableB ON tableA.id = tableB.id;
     - Standard SQL INNER JOIN.
   * - XQuerySetJoin
     - .. code-block:: xquery

           for $a in $colA, $b in $colB
           where $a/id = $b/id
           return <res>{$a, $b}</res>
     - Join is performed using multiple 'for' clauses and a 'where' filter.
   * - GraphQlSetJoin
     - .. code-block:: graphql

           user { posts { title } }
     - Joins are expressed through nested selection sets.
   * - SparqlSetJoin
     - .. code-block:: sparql

           ?s ?p ?o . ?s ?p2 ?o2
     - Joins are performed by using the same variable in different triple patterns.
   * - OverpassTurboSetJoin
     - .. code-block:: text

           (node(area); way(area););
     - Unions and recursion (e.g., node(w)) are used to combine sets.