Bash Pivot View
===============

.. list-table:: Bash Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: bash

           x=42
     - No spaces around the assignment operator.
   * - IfElse
     - .. code-block:: bash

           if [ $x -gt 0 ]; then
               exit 1
           else
               exit 0
           fi
     - Uses if-then-else-fi structure; brackets are for test command.
   * - Loop
     - .. code-block:: bash

           while [ $x -gt 0 ]; do
               x=$((x-1))
           done
     - Uses while-do-done structure.
   * - FunctionDefinition
     - .. code-block:: bash

           add() {
               echo $(($1 + $2))
           }
     - Parameters are accessed via $1, $2, etc.; return values are typically exit codes or printed to stdout.
   * - ProcedureDefinition
     - .. code-block:: bash

           log_message() {
               echo "$1"
           }
     - In Bash, all functions are effectively procedures; return values are exit codes.
   * - TryCatch
     - .. code-block:: bash

           do_something || handle_error
     - Shells often use command chaining (||) for basic error handling based on exit codes; $? stores the exit status.
   * - Raise
     - .. code-block:: bash

           exit 1
     - Terminates the script or subshell with a non-zero exit code.
   * - SingleLineComment
     - .. code-block:: bash

           # comment
     - Bash only supports single-line comments starting with #.
   * - MultiLineComment
     - N/A
     - Bash does not have a native multi-line comment syntax; multiple single-line comments are used.
   * - Print
     - .. code-block:: bash

           echo "Hello, World!"
     - The echo command outputs text followed by a newline.
   * - Import
     - .. code-block:: bash

           source utils.sh
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
     - Uses case-in-esac structure; patterns end with ) and blocks end with ;;.
   * - Constant
     - .. code-block:: bash

           readonly MAX=100
     - The 'readonly' command prevents the variable from being redefined or unset.
   * - Addition
     - .. code-block:: bash

           ((a + b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Subtraction
     - .. code-block:: bash

           ((a - b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Multiplication
     - .. code-block:: bash

           ((a * b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Division
     - .. code-block:: bash

           ((a / b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Remainder
     - .. code-block:: bash

           ((a % b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Floor
     - .. code-block:: bash

           echo "a / 1" | bc
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Rounding
     - .. code-block:: bash

           printf "%.0f" "$a"
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Increment
     - .. code-block:: bash

           ((a++))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - Decrement
     - .. code-block:: bash

           ((a--))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - LeftShift
     - .. code-block:: bash

           ((a << b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - RightShift
     - .. code-block:: bash

           ((a >> b))
     - Arithmetic expansion handles integers; bc or printf used for floating point operations.
   * - BitAnd
     - .. code-block:: bash

           ((a & b))
     - Bitwise operations within double parentheses.
   * - BitOr
     - .. code-block:: bash

           ((a | b))
     - Bitwise operations within double parentheses.
   * - BitXor
     - .. code-block:: bash

           ((a ^ b))
     - Bitwise operations within double parentheses.
   * - BitNot
     - .. code-block:: bash

           ((~a))
     - Bitwise operations within double parentheses.
   * - Float4VectorMultiplication
     - .. code-block:: bash

           for i in {0..3}; do c[$i]=$(echo "${a[$i]} * ${b[$i]}" | bc); done
     - Requires external tools like bc for floating-point arithmetic.
   * - Float4VectorDotProduct
     - .. code-block:: bash

           dot=0; for i in {0..3}; do dot=$(echo "$dot + (${a[$i]} * ${b[$i]})" | bc); done
     - Requires bc for floating-point accumulation.
   * - Float4VectorCrossProduct
     - .. code-block:: bash

           c[0]=$(echo "${a[1]}*${b[2]} - ${a[2]}*${b[1]}" | bc)
           c[1]=$(echo "${a[2]}*${b[0]} - ${a[0]}*${b[2]}" | bc)
           c[2]=$(echo "${a[0]}*${b[1]} - ${a[1]}*${b[0]}" | bc)
           c[3]=0
     - Requires bc for floating-point calculations.