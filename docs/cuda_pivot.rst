CUDA Pivot View
===============

.. list-table:: CUDA Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: cpp

           __device__ int x = 42;
     - Uses __device__ qualifier for GPU memory.
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
     - Standard C-like switch statement.
   * - IfElse
     - .. code-block:: cpp

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - Standard C-like if-else statement.
   * - Loop
     - .. code-block:: cpp

           while (x > 0) {
               x = x - 1;
           }
     - Standard C-like while loop.
   * - FunctionDefinition
     - .. code-block:: cpp

           __device__ int add(int a, int b) {
               return a + b;
           }
     - Functions can be qualified with __device__, __host__, or __global__.
   * - ProcedureDefinition
     - .. code-block:: cpp

           __device__ void log_message(const char *msg) {
               printf("%s\n", msg);
           }
     - Similar to C, procedures use the void return type.
   * - TryCatch
     - N/A
     - CUDA does not support C++ exceptions in device code.
   * - Raise
     - N/A
     - No native exception mechanism in CUDA device code.
   * - Thread
     - .. code-block:: cpp

           kernel<<<grid, block>>>();
     - Launches a grid of threads on the GPU.
   * - SendMessage
     - N/A
     - CUDA threads typically communicate via shared memory or atomics, not explicit message passing.
   * - ReceiveMessage
     - N/A
     - Communication is memory-based.
   * - SingleLineComment
     - .. code-block:: cpp

           // comment
     - Standard C-like single-line comment.
   * - MultiLineComment
     - .. code-block:: cpp

           /* line 1
              line 2 */
     - Standard C-like block comment.
   * - Print
     - .. code-block:: cpp

           printf("Hello, World!\n");
     - CUDA supports printf within device kernels for debugging.
   * - Import
     - .. code-block:: cpp

           #include <cuda_runtime.h>
     - Same as C; used to include CUDA runtime headers.
   * - Constant
     - .. code-block:: cpp

           __constant__ int MAX = 100;
     - The __constant__ qualifier places the variable in the constant memory space of the GPU.
   * - Addition
     - .. code-block:: cpp

           a + b
     - Same as C; device-side math functions are optimized for GPU.
   * - Subtraction
     - .. code-block:: cpp

           a - b
     - Same as C; device-side math functions are optimized for GPU.
   * - Multiplication
     - .. code-block:: cpp

           a * b
     - Same as C; device-side math functions are optimized for GPU.
   * - Division
     - .. code-block:: cpp

           a / b
     - Same as C; device-side math functions are optimized for GPU.
   * - Remainder
     - .. code-block:: cpp

           a % b
     - Same as C; device-side math functions are optimized for GPU.
   * - Floor
     - .. code-block:: cpp

           floor(a)
     - Same as C; device-side math functions are optimized for GPU.
   * - Rounding
     - .. code-block:: cpp

           round(a)
     - Same as C; device-side math functions are optimized for GPU.
   * - Increment
     - .. code-block:: cpp

           a++
     - Same as C; device-side math functions are optimized for GPU.
   * - Decrement
     - .. code-block:: cpp

           a--
     - Same as C; device-side math functions are optimized for GPU.
   * - LeftShift
     - .. code-block:: cpp

           a << b
     - Same as C; device-side math functions are optimized for GPU.
   * - RightShift
     - .. code-block:: cpp

           a >> b
     - Same as C; device-side math functions are optimized for GPU.
   * - BitAnd
     - .. code-block:: cpp

           a & b
     - Standard bitwise operators supported in kernels.
   * - BitOr
     - .. code-block:: cpp

           a | b
     - Standard bitwise operators supported in kernels.
   * - BitXor
     - .. code-block:: cpp

           a ^ b
     - Standard bitwise operators supported in kernels.
   * - BitNot
     - .. code-block:: cpp

           ~a
     - Standard bitwise operators supported in kernels.
   * - Float4VectorMultiplication
     - .. code-block:: cpp

           c.x = a.x * b.x; c.y = a.y * b.y; c.z = a.z * b.z; c.w = a.w * b.w;
     - The float4 type in CUDA is a struct; multiplication is done per-component.
   * - Float4VectorDotProduct
     - .. code-block:: cpp

           float dot = a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w;
     - Manually calculated using the components of the float4 struct.
   * - Float4VectorCrossProduct
     - .. code-block:: cpp

           c.x = a.y*b.z - a.z*b.y; c.y = a.z*b.x - a.x*b.z; c.z = a.x*b.y - a.y*b.x;
     - Manually calculated using the components of the float4 struct.
   * - ForLoop
     - .. code-block:: cpp

           for (int i = 0; i < 10; i++) {
               // body
           }
     - Standard C for loop, usable within kernels.
   * - Equal
     - .. code-block:: cpp

           a == b
     - Standard C operators supported in device code.
   * - NotEqual
     - .. code-block:: cpp

           a != b
     -
   * - GreaterThan
     - .. code-block:: cpp

           a > b
     -