Fortran Pivot View
==================

.. list-table:: Fortran Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: fortran

           integer :: x = 42
     - Static typing; :: is used to separate attributes from the variable name.
   * - IfElse
     - .. code-block:: fortran

           if (x > 0) then
               res = 1
           else
               res = 0
           end if
     - Standard block if-then-else-end if.
   * - SwitchCase
     - .. code-block:: fortran

           select case (x)
           case (1)
               res = 1
           case (2)
               res = 2
           case default
               res = 0
           end select
     - The select case construct is used for branching based on values.
   * - Loop
     - .. code-block:: fortran

           do while (x > 0)
               x = x - 1
           end do
     - Standard do while loop.
   * - ForLoop
     - .. code-block:: fortran

           do i = 1, 10
               ! body
           end do
     - The do loop is used for iteration over ranges.
   * - FunctionDefinition
     - .. code-block:: fortran

           function add(a, b) result(res)
               integer, intent(in) :: a, b
               integer :: res
               res = a + b
           end function add
     - Functions return a value; 'intent(in)' specifies that parameters are read-only.
   * - ProcedureDefinition
     - .. code-block:: fortran

           subroutine log_msg(msg)
               character(len=*), intent(in) :: msg
               print *, msg
           end subroutine log_msg
     - Subroutines are used for procedures that do not return a value.
   * - TryCatch
     - N/A
     - Fortran does not have high-level try-catch blocks; uses iostat for I/O errors.
   * - Raise
     - .. code-block:: fortran

           error stop "Error"
     - The 'error stop' statement terminates execution with an error message (Fortran 2008+).
   * - Thread
     - N/A
     - Fortran uses Coarrays or OpenMP/MPI for parallelism, but not a simple 'thread spawn' primitive.
   * - SendMessage
     - .. code-block:: fortran

           target_var[image] = data
     - Coarrays use distributed memory and assignment to 'images' for communication.
   * - ReceiveMessage
     - .. code-block:: fortran

           sync images(*)
     - Synchronization is used to ensure data consistency in Coarrays.
   * - SingleLineComment
     - .. code-block:: fortran

           ! comment
     - Exclamation mark starts a comment to the end of the line.
   * - MultiLineComment
     - N/A
     - Fortran does not support multi-line comments natively.
   * - Print
     - .. code-block:: fortran

           print *, "Hello World"
     - The print statement with * (default format) outputs to stdout.
   * - Import
     - .. code-block:: fortran

           use math_mod
     - The 'use' statement imports a module's public variables and procedures.
   * - Constant
     - .. code-block:: fortran

           integer, parameter :: MAX = 100
     - The 'parameter' attribute makes the variable a named constant.
   * - Addition
     - .. code-block:: fortran

           a + b
     - Standard arithmetic operator.
   * - Subtraction
     - .. code-block:: fortran

           a - b
     - Standard arithmetic operator.
   * - Multiplication
     - .. code-block:: fortran

           a * b
     - Standard arithmetic operator.
   * - Division
     - .. code-block:: fortran

           a / b
     - Standard arithmetic operator.
   * - Remainder
     - .. code-block:: fortran

           mod(a, b)
     - Built-in function for remainder.
   * - Floor
     - .. code-block:: fortran

           floor(a)
     - Built-in function for the floor of a real number.
   * - Rounding
     - .. code-block:: fortran

           nint(a)
     - Built-in function for the nearest integer.
   * - Increment
     - .. code-block:: fortran

           a = a + 1
     - No native increment operator; uses assignment.
   * - Decrement
     - .. code-block:: fortran

           a = a - 1
     - No native decrement operator; uses assignment.
   * - LeftShift
     - .. code-block:: fortran

           ishft(a, b)
     - The ishft function performs a logical shift.
   * - RightShift
     - .. code-block:: fortran

           ishft(a, -b)
     - Negative shift counts in ishft perform a right shift.
   * - BitAnd
     - .. code-block:: fortran

           iand(a, b)
     - Built-in function for bitwise AND.
   * - BitOr
     - .. code-block:: fortran

           ior(a, b)
     - Built-in function for bitwise OR.
   * - BitXor
     - .. code-block:: fortran

           ieor(a, b)
     - Built-in function for bitwise XOR.
   * - BitNot
     - .. code-block:: fortran

           not(a)
     - Built-in function for bitwise NOT.
   * - Float4VectorMultiplication
     - .. code-block:: fortran

           c = a * b
     - Fortran supports element-wise operations on arrays natively.
   * - Float4VectorDotProduct
     - .. code-block:: fortran

           res = dot_product(a, b)
     - The dot_product intrinsic function calculates the dot product of two vectors.
   * - Float4VectorCrossProduct
     - .. code-block:: fortran

           c = [a(2)*b(3) - a(3)*b(2), &
                a(3)*b(1) - a(1)*b(3), &
                a(1)*b(2) - a(2)*b(1), 0.0]
     - Calculated component-wise using an array constructor.
   * - Equal
     - .. code-block:: fortran

           a == b
     - Alternative syntax: a .eq. b
   * - NotEqual
     - .. code-block:: fortran

           a /= b
     - Alternative syntax: a .ne. b
   * - GreaterThan
     - .. code-block:: fortran

           a > b
     - Alternative syntax: a .gt. b
   * - SetFiltering
     - .. code-block:: fortran

           b = pack(a, a > 0)
     - The pack intrinsic function filters an array based on a mask.
   * - SetJoin
     - .. code-block:: fortran

           do i = 1, n
               do j = 1, m
                   if (a(i)%id == b(j)%id) then
                       ! Join logic
                   end if
               end do
           end do
     - Standard nested DO loops for joining arrays of types.