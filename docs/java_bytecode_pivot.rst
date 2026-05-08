Java Bytecode Pivot View
========================

.. list-table:: Java Bytecode Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - .. code-block:: jasmin

           .field private static x I = 42
     - In Jasmin syntax, static fields represent global-like variables.
   * - IfElse
     - .. code-block:: jasmin

               getstatic MyClass/x I
               ifgt LabelThen
               iconst_0
               ireturn
           LabelThen:
               iconst_1
               ireturn
     - Implemented using stack operations and branch instructions (ifgt).
   * - Loop
     - .. code-block:: jasmin

           LoopStart:
               getstatic MyClass/x I
               ifle LoopEnd
               getstatic MyClass/x I
               iconst_1
               isub
               putstatic MyClass/x I
               goto LoopStart
           LoopEnd:
     - Loops are built with labels and jump instructions (goto, ifle).
   * - FunctionDefinition
     - .. code-block:: jasmin

           .method public static add(II)I
               .limit stack 2
               .limit locals 2
               iload_0
               iload_1
               iadd
               ireturn
           .end method
     - Methods define stack and local variable limits; parameters are accessed by index.
   * - TryCatch
     - .. code-block:: jasmin

           .catch java/lang/Exception from TryStart to TryEnd using CatchHandler
           TryStart:
               invokestatic MyClass/do_something()V
           TryEnd:
               goto Done
           CatchHandler:
               astore_1
               aload_1
               invokestatic MyClass/handle(Ljava/lang/Exception;)V
           Done:
     - Exception handlers are defined via .catch directives for specific code ranges.
   * - Raise
     - .. code-block:: jasmin

               new java/lang/RuntimeException
               dup
               ldc "Error"
               invokespecial java/lang/RuntimeException/<init>(Ljava/lang/String;)V
               athrow
     - Exceptions are instantiated and then thrown using the athrow instruction.
   * - Print
     - .. code-block:: jasmin

               getstatic java/lang/System/out Ljava/io/PrintStream;
               ldc "Hello, World!"
               invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
     - Calls println on the static System.out field.
   * - Thread
     - .. code-block:: jasmin

               new java/lang/Thread
               dup
               new MyRunnable
               dup
               invokespecial MyRunnable/<init>()V
               invokespecial java/lang/Thread/<init>(Ljava/lang/Runnable;)V
               invokevirtual java/lang/Thread/start()V
     - Involves instantiating a Thread object with a Runnable and calling start().
   * - SendMessage
     - .. code-block:: jasmin

               aload_0 ; queue
               bipush 42
               invokestatic java/lang/Integer/valueOf(I)Ljava/lang/Integer;
               invokevirtual java/util/concurrent/BlockingQueue/put(Ljava/lang/Object;)V
     - Typically uses standard Java concurrent collections like BlockingQueue.
   * - ReceiveMessage
     - .. code-block:: jasmin

               aload_0 ; queue
               invokevirtual java/util/concurrent/BlockingQueue/take()Ljava/lang/Object;
               checkcast java/lang/Integer
               invokevirtual java/lang/Integer/intValue()I
               istore_1 ; msg
               iload_1
               invokestatic MyClass/handle(I)V
     - Blocking retrieval from a concurrent collection.
   * - SingleLineComment
     - .. code-block:: jasmin

           ; comment
     - Jasmin uses semicolons for single-line comments.
   * - MultiLineComment
     - N/A
     - Java Bitcode (Jasmin) does not have a native multi-line comment syntax; multiple semicolons are used.
   * - Import
     - .. code-block:: jasmin

           Ljava/util/List;
     - Internal descriptors are used to reference external classes.
   * - SwitchCase
     - .. code-block:: jasmin

               getstatic MyClass/x I
               lookupswitch
                   1: Label1
                   2: Label2
                   default: LabelDefault
           Label1:
               ; ...
           Label2:
               ; ...
           LabelDefault:
               ; ...
     - Uses lookupswitch or tableswitch instructions for multi-way branching.
   * - Constant
     - .. code-block:: jasmin

           .field public static final MAX I = 100
     - Constants are represented as static final fields.
   * - ProcedureDefinition
     - .. code-block:: jasmin

           .method public static logMessage(Ljava/lang/String;)V
               .limit stack 2
               .limit locals 1
               getstatic java/lang/System/out Ljava/io/PrintStream;
               aload_0
               invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
               return
           .end method
     - Methods with a 'V' return descriptor are procedures; 'return' instruction is used for void return.
   * - Addition
     - .. code-block:: jasmin

           iadd
     - Stack-based arithmetic instructions for integers.
   * - Subtraction
     - .. code-block:: jasmin

           isub
     - Stack-based arithmetic instructions for integers.
   * - Multiplication
     - .. code-block:: jasmin

           imul
     - Stack-based arithmetic instructions for integers.
   * - Division
     - .. code-block:: jasmin

           idiv
     - Stack-based arithmetic instructions for integers.
   * - Remainder
     - .. code-block:: jasmin

           irem
     - Stack-based arithmetic instructions for integers.
   * - Floor
     - N/A
     - Stack-based arithmetic instructions for integers.
   * - Rounding
     - N/A
     - Stack-based arithmetic instructions for integers.
   * - Increment
     - .. code-block:: jasmin

           iinc index, 1
     - Stack-based arithmetic instructions for integers.
   * - Decrement
     - .. code-block:: jasmin

           iinc index, -1
     - Stack-based arithmetic instructions for integers.
   * - LeftShift
     - .. code-block:: jasmin

           ishl
     - Stack-based arithmetic instructions for integers.
   * - RightShift
     - .. code-block:: jasmin

           ishr
     - Stack-based arithmetic instructions for integers.
   * - BitAnd
     - .. code-block:: jasmin

           iand
     - Stack-based bitwise instructions; NOT is implemented as XOR with -1.
   * - BitOr
     - .. code-block:: jasmin

           ior
     - Stack-based bitwise instructions; NOT is implemented as XOR with -1.
   * - BitXor
     - .. code-block:: jasmin

           ixor
     - Stack-based bitwise instructions; NOT is implemented as XOR with -1.
   * - BitNot
     - .. code-block:: jasmin

           iconst_m1
           ixor
     - Stack-based bitwise instructions; NOT is implemented as XOR with -1.
   * - Float4VectorMultiplication
     - .. code-block:: jasmin

           fload_1
           fload_2
           fmul
     - Java Bytecode uses fmul for individual floats; vectorization is typically handled by the JIT.
   * - Float4VectorDotProduct
     - .. code-block:: jasmin

           fload_1 ; a[i]
           fload_2 ; b[i]
           fmul
           fadd
     - Dot product is built by repeating fmul and fadd instructions on the stack.
   * - Float4VectorCrossProduct
     - .. code-block:: jasmin

           fload 1 ; ay
           fload 6 ; bz
           fmul
           fload 2 ; az
           fload 5 ; by
           fmul
           fsub ; -> cx
           fload 2 ; az
           fload 4 ; bx
           fmul
           fload 0 ; ax
           fload 6 ; bz
           fmul
           fsub ; -> cy
           fload 0 ; ax
           fload 5 ; by
           fmul
           fload 1 ; ay
           fload 4 ; bx
           fmul
           fsub ; -> cz
     - Calculated component-wise using stack operations.