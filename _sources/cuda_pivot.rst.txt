CUDA Pivot View
===============

.. list-table:: CUDA Pivot Table
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
     - .. code-block:: cpp

           __device__ int x = 42;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses __device__ qualifier for GPU memory.
   * - IfElse
     - .. code-block:: cpp

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C-like if-else statement.
   * - Loop
     - .. code-block:: cpp

           while (x > 0) {
               x = x - 1;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C-like while loop.
   * - FunctionDefinition
     - .. code-block:: cpp

           __device__ int add(int a, int b) {
               return a + b;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Functions can be qualified with __device__, __host__, or __global__.
   * - ProcedureDefinition
     - .. code-block:: cpp

           __device__ void log_message(const char *msg) {
               printf("%s\n", msg);
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Similar to C, procedures use the void return type.
   * - TryCatch
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - CUDA does not support C++ exceptions in device code.
   * - Raise
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - No native exception mechanism in CUDA device code.
   * - Thread
     - .. code-block:: cpp

           kernel<<<grid, block>>>();
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Launches a grid of threads on the GPU.
   * - SendMessage
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - CUDA threads typically communicate via shared memory or atomics, not explicit message passing.
   * - ReceiveMessage
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Communication is memory-based.
   * - SingleLineComment
     - .. code-block:: cpp

           // comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C-like single-line comment.
   * - MultiLineComment
     - .. code-block:: cpp

           /* line 1
              line 2 */
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C-like block comment.
   * - Print
     - .. code-block:: cpp

           printf("Hello, World!\n");
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - CUDA supports printf within device kernels for debugging.
   * - Import
     - .. code-block:: cpp

           #include <cuda_runtime.h>
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; used to include CUDA runtime headers.
   * - SwitchCase
     - .. code-block:: cpp

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Standard C-like switch statement.
   * - Constant
     - .. code-block:: cpp

           __constant__ int MAX = 100;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - The __constant__ qualifier places the variable in the constant memory space of the GPU.
   * - Addition
     - .. code-block:: cpp

           a + b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - Subtraction
     - .. code-block:: cpp

           a - b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - Multiplication
     - .. code-block:: cpp

           a * b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - Division
     - .. code-block:: cpp

           a / b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - Remainder
     - .. code-block:: cpp

           a % b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - Floor
     - .. code-block:: cpp

           floor(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - Rounding
     - .. code-block:: cpp

           round(a)
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - Increment
     - .. code-block:: cpp

           a++
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - Decrement
     - .. code-block:: cpp

           a--
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - LeftShift
     - .. code-block:: cpp

           a << b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - RightShift
     - .. code-block:: cpp

           a >> b
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Same as C; device-side math functions are optimized for GPU.
   * - Bitwise
     - N/A
     - .. code-block:: cpp

           a & b
     - .. code-block:: cpp

           a | b
     - .. code-block:: cpp

           a ^ b
     - .. code-block:: cpp

           ~a
     - .. code-block:: cpp

           a << b
     - .. code-block:: cpp

           a >> b
     - Standard bitwise operators supported in kernels.