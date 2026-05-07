Bash Pivot View
===============

.. list-table:: Bash Pivot Table
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
     - .. code-block:: bash

           x=42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - No spaces around the assignment operator.
   * - IfElse
     - .. code-block:: bash

           if [ $x -gt 0 ]; then
               exit 1
           else
               exit 0
           fi
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses if-then-else-fi structure; brackets are for test command.
   * - Loop
     - .. code-block:: bash

           while [ $x -gt 0 ]; do
               x=$((x-1))
           done
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses while-do-done structure.
   * - FunctionDefinition
     - .. code-block:: bash

           add() {
               echo $(($1 + $2))
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Parameters are accessed via $1, $2, etc.; return values are typically exit codes or printed to stdout.
   * - ProcedureDefinition
     - .. code-block:: bash

           log_message() {
               echo "$1"
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - In Bash, all functions are effectively procedures; return values are exit codes.
   * - TryCatch
     - .. code-block:: bash

           do_something || handle_error
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Shells often use command chaining (||) for basic error handling based on exit codes; $? stores the exit status.
   * - Raise
     - .. code-block:: bash

           exit 1
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Terminates the script or subshell with a non-zero exit code.
   * - SingleLineComment
     - .. code-block:: bash

           # comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Bash only supports single-line comments starting with #.
   * - MultiLineComment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Bash does not have a native multi-line comment syntax; multiple single-line comments are used.
   * - Print
     - .. code-block:: bash

           echo "Hello, World!"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The echo command outputs text followed by a newline.
   * - Import
     - .. code-block:: bash

           source utils.sh
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The 'source' (or .) command executes a script in the current shell context.
   * - SwitchCase
     - .. code-block:: bash

           case $x in
               1)
                   echo "one"
                   ;;
               2)
                   echo "two"
                   ;;
               *)
                   echo "none"
                   ;;
           esac
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses case-in-esac structure; patterns end with ) and blocks end with ;;.
   * - Constant
     - .. code-block:: bash

           readonly MAX=100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The 'readonly' command prevents the variable from being redefined or unset.
   * - Addition
     - .. code-block:: bash

           ((a + b))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Subtraction
     - .. code-block:: bash

           ((a - b))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Multiplication
     - .. code-block:: bash

           ((a * b))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Division
     - .. code-block:: bash

           ((a / b))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Remainder
     - .. code-block:: bash

           ((a % b))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Floor
     - .. code-block:: bash

           echo "a / 1" | bc
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Rounding
     - .. code-block:: bash

           printf "%.0f" "$a"
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Increment
     - .. code-block:: bash

           ((a++))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Decrement
     - .. code-block:: bash

           ((a--))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - LeftShift
     - .. code-block:: bash

           ((a << b))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - RightShift
     - .. code-block:: bash

           ((a >> b))
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Bitwise
     - N/A
     - .. code-block:: bash

           ((a & b))
     - .. code-block:: bash

           ((a | b))
     - .. code-block:: bash

           ((a ^ b))
     - .. code-block:: bash

           ((~a))
     - .. code-block:: bash

           ((a << b))
     - .. code-block:: bash

           ((a >> b))
     - Bitwise operations within double parentheses.