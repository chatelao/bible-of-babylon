Java Bytecode Pivot View
========================

.. list-table:: Java Bytecode Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Plus
     - Minus
     - Times
     - Divide
     - Mod
     - Increment
     - Decrement
     - Lshift
     - Rshift
     - Bit and
     - Bit or
     - Bit xor
     - Bit not
     - Bit lshift
     - Bit rshift
     - Notes
   * - VariableDeclaration
     - .. code-block:: jasm

           .field private static x I = 42
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - In Jasmin syntax, static fields represent global-like variables.
   * - IfElse
     - .. code-block:: jasm

               getstatic MyClass/x I
               ifgt LabelThen
               iconst_0
               ireturn
           LabelThen:
               iconst_1
               ireturn
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Implemented using stack operations and branch instructions (ifgt).
   * - Loop
     - .. code-block:: jasm

           LoopStart:
               getstatic MyClass/x I
               ifle LoopEnd
               getstatic MyClass/x I
               iconst_1
               isub
               putstatic MyClass/x I
               goto LoopStart
           LoopEnd:
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Loops are built with labels and jump instructions (goto, ifle).
   * - FunctionDefinition
     - .. code-block:: jasm

           .method public static add(II)I
               .limit stack 2
               .limit locals 2
               iload_0
               iload_1
               iadd
               ireturn
           .end method
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Methods define stack and local variable limits; parameters are accessed by index.
   * - TryCatch
     - .. code-block:: jasm

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
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Exception handlers are defined via .catch directives for specific code ranges.
   * - Raise
     - .. code-block:: jasm

               new java/lang/RuntimeException
               dup
               ldc "Error"
               invokespecial java/lang/RuntimeException/<init>(Ljava/lang/String;)V
               athrow
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Exceptions are instantiated and then thrown using the athrow instruction.
   * - Print
     - .. code-block:: jasm

               getstatic java/lang/System/out Ljava/io/PrintStream;
               ldc "Hello, World!"
               invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Calls println on the static System.out field.
   * - Thread
     - .. code-block:: jasm

               new java/lang/Thread
               dup
               new MyRunnable
               dup
               invokespecial MyRunnable/<init>()V
               invokespecial java/lang/Thread/<init>(Ljava/lang/Runnable;)V
               invokevirtual java/lang/Thread/start()V
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Involves instantiating a Thread object with a Runnable and calling start().
   * - SendMessage
     - .. code-block:: jasm

               aload_0 ; queue
               bipush 42
               invokestatic java/lang/Integer/valueOf(I)Ljava/lang/Integer;
               invokevirtual java/util/concurrent/BlockingQueue/put(Ljava/lang/Object;)V
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Typically uses standard Java concurrent collections like BlockingQueue.
   * - ReceiveMessage
     - .. code-block:: jasm

               aload_0 ; queue
               invokevirtual java/util/concurrent/BlockingQueue/take()Ljava/lang/Object;
               checkcast java/lang/Integer
               invokevirtual java/lang/Integer/intValue()I
               istore_1 ; msg
               iload_1
               invokestatic MyClass/handle(I)V
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Blocking retrieval from a concurrent collection.
   * - SingleLineComment
     - .. code-block:: jasm

           ; comment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Jasmin uses semicolons for single-line comments.
   * - MultiLineComment
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Java Bitcode (Jasmin) does not have a native multi-line comment syntax; multiple semicolons are used.
   * - Import
     - .. code-block:: jasm

           Ljava/util/List;
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Internal descriptors are used to reference external classes.
   * - SwitchCase
     - .. code-block:: jasm

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
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Uses lookupswitch or tableswitch instructions for multi-way branching.
   * - Constant
     - .. code-block:: jasm

           .field public static final MAX I = 100
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Constants are represented as static final fields.
   * - ProcedureDefinition
     - .. code-block:: jasm

           .method public static logMessage(Ljava/lang/String;)V
               .limit stack 2
               .limit locals 1
               getstatic java/lang/System/out Ljava/io/PrintStream;
               aload_0
               invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
               return
           .end method
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Methods with a 'V' return descriptor are procedures; 'return' instruction is used for void return.
   * - Arithmetic
     - N/A
     - .. code-block:: jasm

           iadd
     - .. code-block:: jasm

           isub
     - .. code-block:: jasm

           imul
     - .. code-block:: jasm

           idiv
     - .. code-block:: jasm

           irem
     - .. code-block:: jasm

           iinc index, 1
     - .. code-block:: jasm

           iinc index, -1
     - .. code-block:: jasm

           ishl
     - .. code-block:: jasm

           ishr
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - Stack-based arithmetic instructions for integers.
   * - Bitwise
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - .. code-block:: jasm

           iand
     - .. code-block:: jasm

           ior
     - .. code-block:: jasm

           ixor
     - .. code-block:: jasm

           iconst_m1
           ixor
     - .. code-block:: jasm

           ishl
     - .. code-block:: jasm

           ishr
     - Stack-based bitwise instructions; NOT is implemented as XOR with -1.