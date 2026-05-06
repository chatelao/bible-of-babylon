Java Bitcode Pivot Chapter
==========================

.. list-table:: Java Bitcode Pivot Table
   :widths: auto
   :header-rows: 1

   * - Pattern
     - Syntax
     - Notes
   * - VariableDeclaration
     - ::

           bipush 42
           istore_1
     - Variables are typically stored in local variable slots; 'istore_1' stores an integer in slot 1.
   * - IfElse
     - ::

               iload_1
               ifle L_else
               iconst_1
               ireturn
           L_else:
               iconst_0
               ireturn
     - Uses comparison instructions (like ifle) and labels for control flow.
   * - Loop
     - ::

           L_loop:
               iload_1
               ifle L_end
               iinc 1 -1
               goto L_loop
           L_end:
     - Implemented using labels, conditional branches, and jumps.
   * - FunctionDefinition
     - ::

           .method public static add(II)I
               .limit stack 2
               .limit locals 2
               iload_0
               iload_1
               iadd
               ireturn
           .end method
     - Defined using the .method directive (Jasmin syntax); arguments are loaded from local slots.
   * - TryCatch
     - ::

           .catch java/lang/Exception from L_start to L_end using L_handler
           L_start:
               invokestatic do_something()V
           L_end:
               goto L_done
           L_handler:
               astore_1
               aload_1
               invokestatic handle(Ljava/lang/Exception;)V
           L_done:
     - Exception handlers are defined via a catch table mapping ranges to labels.
   * - Raise
     - ::

           new java/lang/RuntimeException
           dup
           ldc "Error"
           invokespecial java/lang/RuntimeException/<init>(Ljava/lang/String;)V
           athrow
     - Uses 'athrow' instruction to raise an object from the stack as an exception.
   * - Thread
     - ::

           new java/lang/Thread
           dup
           # lambda or runnable
           invokespecial java/lang/Thread/<init>(Ljava/lang/Runnable;)V
           invokevirtual java/lang/Thread/start()V
     - Threads are objects; start() is invoked to begin execution.
   * - SendMessage
     - ::

           aload_1 # queue
           bipush 42
           invokestatic java/lang/Integer/valueOf(I)Ljava/lang/Integer;
           invokeinterface java/util/concurrent/BlockingQueue/put(Ljava/lang/Object;)V 2
     - Typically involves calling methods on concurrent collection objects.
   * - ReceiveMessage
     - ::

           aload_1 # queue
           invokeinterface java/util/concurrent/BlockingQueue/take()Ljava/lang/Object; 1
           astore_2 # msg
           aload_2
           invokestatic handle(Ljava/lang/Object;)V
     - Blocks by calling take() on a BlockingQueue.
   * - SingleLineComment
     - ::

           ; comment
     - Jasmin and other JVM assemblers typically use the semicolon for comments.
   * - MultiLineComment
     - N/A
     - Java Bytecode assemblers usually do not support native multi-line comments.
   * - Print
     - ::

           getstatic java/lang/System/out Ljava/io/PrintStream;
           ldc "Hello, World!"
           invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
     - Calls PrintStream.println on the System.out static field.
   * - Import
     - N/A
     - Bytecode refers to classes by their fully qualified names; there is no 'import' directive in the bytecode itself.
   * - SwitchCase
     - ::

           iload_1
           tableswitch 1
             1: L_case1
             2: L_case2
             default: L_default
     - Uses 'tableswitch' (for contiguous values) or 'lookupswitch' (for sparse values).
   * - Constant
     - ::

           .field public static final MAX I = 100
     - Constants are defined as fields with the 'final' access flag.