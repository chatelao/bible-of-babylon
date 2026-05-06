Appendix: Pattern Comparison Matrices
=====================================



Programming Languages Matrix
============================

.. list-table:: Pattern Comparison Matrix
   :widths: auto
   :header-rows: 1

   * - Language
     - VariableDeclaration
     - FunctionDefinition
     - IfElse
     - Loop
     - TryCatch
     - Raise
     - Thread
     - SendMessage
     - ReceiveMessage
     - SingleLineComment
     - MultiLineComment
     - Print
     - Import
     - SwitchCase
     - Constant
   * - C
     - ::

           int x = 42;
     - ::

           int add(int a, int b) {
               return a + b;
           }
     - ::

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - ::

           while (x > 0) {
               x = x - 1;
           }
     - N/A
     - ::

           exit(1);
     - N/A
     - N/A
     - N/A
     - ::

           // comment
     - ::

           /* line 1
              line 2 */
     - ::

           printf("Hello, World!\n");
     - ::

           #include <stdio.h>
     - ::

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - ::

           const int MAX = 100;
   * - Java
     - ::

           int x = 42;
     - ::

           public int add(int a, int b) {
               return a + b;
           }
     - ::

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - ::

           while (x > 0) {
               x = x - 1;
           }
     - ::

           try {
               do_something();
           } catch (Exception e) {
               handle(e);
           }
     - ::

           throw new RuntimeException("Error");
     - ::

           new Thread(() -> { do_work(); }).start();
     - ::

           queue.put(42);
     - ::

           int msg = queue.take(); handle(msg);
     - ::

           // comment
     - ::

           /* line 1
              line 2 */
     - ::

           System.out.println("Hello, World!");
     - ::

           import java.util.List;
     - ::

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - ::

           public static final int MAX = 100;
   * - Rust
     - ::

           let x: i32 = 42;
     - ::

           fn add(a: i32, b: i32) -> i32 {
               a + b
           }
     - ::

           if x > 0 {
               1
           } else {
               0
           }
     - ::

           while x > 0 {
               x -= 1;
           }
     - ::

           match do_something() {
               Ok(v) => v,
               Err(e) => handle(e)
           }
     - ::

           panic!("Error");
     - ::

           thread::spawn(|| { do_work(); });
     - ::

           tx.send(42).unwrap();
     - ::

           let msg = rx.recv().unwrap(); handle(msg);
     - ::

           // comment
     - ::

           /* line 1
              line 2 */
     - ::

           println!("Hello, World!");
     - ::

           use std::collections::HashMap;
     - ::

           match x {
               1 => 1,
               2 => 2,
               _ => 0,
           }
     - ::

           const MAX: i32 = 100;
   * - Python
     - ::

           x = 42
     - ::

           def add(a, b):
               return a + b
     - ::

           1 if x > 0 else 0
     - ::

           while x > 0: x = x - 1
     - ::

           try:
               do_something()
           except Exception as e:
               handle(e)
     - ::

           raise Exception("Error")
     - N/A
     - N/A
     - N/A
     - ::

           # comment
     - ::

           """ line 1
               line 2 """
     - ::

           print("Hello, World!")
     - ::

           import math
     - ::

           match x:
               case 1:
                   return 1
               case 2:
                   return 2
               case _:
                   return 0
     - ::

           MAX = 100
   * - PHP
     - ::

           $x = 42;
     - ::

           function add(int $a, int $b): int {
               return $a + $b;
           }
     - ::

           if ($x > 0) {
               return 1;
           } else {
               return 0;
           }
     - ::

           while ($x > 0) {
               $x = $x - 1;
           }
     - ::

           try {
               do_something();
           } catch (Exception $e) {
               handle($e);
           }
     - ::

           throw new Exception("Error");
     - N/A
     - N/A
     - N/A
     - ::

           // comment
     - ::

           /* line 1
              line 2 */
     - ::

           echo "Hello, World!";
     - ::

           require 'utils.php';
     - ::

           switch ($x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - ::

           define('MAX', 100);
   * - Bash
     - ::

           x=42
     - ::

           add() {
               echo $(($1 + $2))
           }
     - ::

           if [ $x -gt 0 ]; then
               exit 1
           else
               exit 0
           fi
     - ::

           while [ $x -gt 0 ]; do
               x=$((x-1))
           done
     - ::

           do_something || handle_error
     - ::

           exit 1
     - N/A
     - N/A
     - N/A
     - ::

           # comment
     - N/A
     - ::

           echo "Hello, World!"
     - ::

           source utils.sh
     - ::

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
     - ::

           readonly MAX=100
   * - PowerShell
     - ::

           $x = 42
     - ::

           function add($a, $b) {
               return $a + $b
           }
     - ::

           if ($x -gt 0) {
               return 1
           } else {
               return 0
           }
     - ::

           while ($x -gt 0) {
               $x = $x - 1
           }
     - ::

           try {
               do_something
           } catch {
               handle_error($_)
           }
     - ::

           throw "Error"
     - N/A
     - N/A
     - N/A
     - ::

           # comment
     - ::

           <# line 1
              line 2 #>
     - ::

           Write-Host "Hello, World!"
     - ::

           Import-Module ActiveDirectory
     - ::

           switch ($x) {
               1 { "one" }
               2 { "two" }
               default { "none" }
           }
     - ::

           Set-Variable -Name MAX -Value 100 -Option ReadOnly
   * - Cmd
     - ::

           set x=42
     - ::

           :add
           set /a res=%~1+%~2
           exit /b %res%
     - ::

           if %x% GTR 0 (exit /b 1) else (exit /b 0)
     - ::

           :loop
           if %x% GTR 0 (set /a x=x-1 & goto loop)
     - ::

           do_something || call :handle_error
     - ::

           exit /b 1
     - N/A
     - N/A
     - N/A
     - ::

           REM comment
     - N/A
     - ::

           echo Hello, World!
     - ::

           call other.cmd
     - ::

           if "%x%"=="1" (goto :one) else if "%x%"=="2" (goto :two) else (goto :none)
     - ::

           set MAX=100
   * - SQL
     - ::

           DECLARE @x INT = 42;
     - ::

           CREATE FUNCTION add(@a INT, @b INT)
           RETURNS INT AS
           BEGIN
               RETURN @a + @b
           END
     - ::

           IF @x > 0
           BEGIN
               RETURN 1
           END
           ELSE
           BEGIN
               RETURN 0
           END
     - ::

           WHILE @x > 0
           BEGIN
               SET @x = @x - 1
           END
     - ::

           BEGIN TRY
               EXEC do_something;
           END TRY
           BEGIN CATCH
               EXEC handle_error;
           END CATCH
     - ::

           THROW 50000, 'Error', 1;
     - N/A
     - N/A
     - N/A
     - ::

           -- comment
     - ::

           /* line 1
              line 2 */
     - ::

           PRINT 'Hello, World!';
     - N/A
     - ::

           CASE @x
               WHEN 1 THEN 'one'
               WHEN 2 THEN 'two'
               ELSE 'none'
           END
     - ::

           DECLARE @MAX INT = 100;
   * - Erlang
     - ::

           X = 42.
     - ::

           add(A, B) -> A + B.
     - ::

           if X > 0 -> 1; true -> 0 end
     - ::

           loop(0) -> ok; loop(X) when X > 0 -> loop(X - 1).
     - ::

           try
               do_something()
           catch
               error:Reason -> handle(Reason)
           end
     - ::

           error("Error")
     - ::

           Pid = spawn(fun() -> do_work() end).
     - ::

           Pid ! hello.
     - ::

           receive hello -> handle_hello() end.
     - ::

           % comment
     - N/A
     - ::

           io:format("Hello, World!~n").
     - ::

           -include("header.hrl").
     - ::

           case X of
               1 -> one;
               2 -> two;
               _ -> none
           end
     - ::

           -define(MAX, 100).
   * - Lisp
     - ::

           (defparameter x 42)
     - ::

           (defun add (a b) (+ a b))
     - ::

           (if (> x 0) 1 0)
     - ::

           (loop while (> x 0) do (setq x (1- x)))
     - ::

           (handler-case (do_something) (error (c) (handle c)))
     - ::

           (error "Error")
     - N/A
     - N/A
     - N/A
     - ::

           ; comment
     - ::

           #| line 1
              line 2 |#
     - ::

           (format t "Hello, World!~%")
     - ::

           (use-package :iter)
     - ::

           (case x
             (1 "one")
             (2 "two")
             (t "none"))
     - ::

           (defconstant +max+ 100)
   * - XQuery
     - ::

           let $x := 42
     - ::

           declare function local:add(
               $a as xs:integer,
               $b as xs:integer
           ) as xs:integer {
               $a + $b
           };
     - ::

           if ($x > 0) then 1 else 0
     - ::

           for $i in 1 to $x return $i
     - ::

           try {
               do_something()
           } catch * {
               handle($err)
           }
     - ::

           fn:error(fn:QName('http://example.com/errors', 'MY_ERROR'), 'Error')
     - N/A
     - N/A
     - N/A
     - ::

           (: comment :)
     - ::

           (: line 1
              line 2 :)
     - ::

           "Hello, World!"
     - ::

           import module namespace utils = "http://example.com/utils";
     - ::

           switch ($x)
             case 1 return "one"
             case 2 return "two"
             default return "none"
     - ::

           declare variable $MAX as xs:integer := 100;
   * - CSS
     - ::

           --x: 42;
     - N/A
     - ::

           @media (min-width: 0px) { .element { color: red; } }
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - N/A
     - ::

           /* line 1
              line 2 */
     - ::

           .element::before { content: "Hello, World!"; }
     - ::

           @import "base.css";
     - N/A
     - ::

           --MAX: 100;
   * - CUDA
     - ::

           __device__ int x = 42;
     - ::

           __device__ int add(int a, int b) {
               return a + b;
           }
     - ::

           if (x > 0) {
               return 1;
           } else {
               return 0;
           }
     - ::

           while (x > 0) {
               x = x - 1;
           }
     - N/A
     - N/A
     - ::

           kernel<<<grid, block>>>();
     - N/A
     - N/A
     - ::

           // comment
     - ::

           /* line 1
              line 2 */
     - ::

           printf("Hello, World!\n");
     - ::

           #include <cuda_runtime.h>
     - ::

           switch (x) {
               case 1:
                   return 1;
               case 2:
                   return 2;
               default:
                   return 0;
           }
     - ::

           __constant__ int MAX = 100;
   * - X86
     - ::

           x   dd 42
     - ::

           add_func:
               add eax, ebx
               ret
     - ::

               cmp eax, 0
               jle .else
               mov eax, 1
               jmp .end
           .else:
               mov eax, 0
           .end:
     - ::

           .loop:
               cmp ecx, 0
               jle .end
               dec ecx
               jmp .loop
           .end:
     - N/A
     - ::

               int 3
     - ::

               push offset do_work
               call CreateThread
     - ::

               push msg
               push thread_id
               call PostThreadMessage
     - ::

               call GetMessage
     - ::

           ; comment
     - N/A
     - ::

           push offset hello_msg
           call printf
     - ::

           include 'macros.inc'
     - ::

               cmp eax, 1
               je .case1
               cmp eax, 2
               je .case2
               jmp .default
           .case1:
               ; ...
           .case2:
               ; ...
           .default:
               ; ...
     - ::

           MAX equ 100
   * - Riscv
     - ::

           x:  .word 42
     - ::

           add:
               add a0, a0, a1
               ret
     - ::

               blez t0, .else
               li a0, 1
               j .end
           .else:
               li a0, 0
           .end:
     - ::

           .loop:
               blez t0, .end
               addi t0, t0, -1
               j .loop
           .end:
     - N/A
     - ::

               ebreak
     - ::

               li a7, 220 # clone syscall
               ecall
     - ::

               li a7, 139 # rt_sigqueueinfo
               ecall
     - ::

               li a7, 128 # rt_sigtimedwait
               ecall
     - ::

           # comment
     - N/A
     - ::

               la a0, hello_msg
               call printf
     - ::

           .include "macros.s"
     - ::

               li t1, 1
               beq t0, t1, .case1
               li t1, 2
               beq t0, t1, .case2
               j .default
     - ::

           .equiv MAX, 100
   * - Prolog
     - ::

           X = 42.
     - ::

           add(A, B, Res) :- Res is A + B.
     - ::

           (X > 0 -> Result = 1 ; Result = 0)
     - ::

           loop(0) :- !.
           loop(X) :- X > 0, X1 is X - 1, loop(X1).
     - ::

           catch(do_something, E, handle(E))
     - ::

           throw(error(Error))
     - ::

           thread_create(do_work, Id, []).
     - ::

           thread_send_message(Id, hello).
     - ::

           thread_get_message(hello).
     - ::

           % comment
     - ::

           /* line 1\n   line 2 */
     - ::

           writeln('Hello, World!').
     - ::

           use_module(library(math)).
     - ::

           (   X = 1 -> writeln('one')
           ;   X = 2 -> writeln('two')
           ;   writeln('none')
           )
     - ::

           max(100).



Data Formats Matrix
===================

.. list-table:: Pattern Comparison Matrix
   :widths: auto
   :header-rows: 1

   * - Language
     - BasicTypes
     - Collection
     - Mapping
     - Metadata
     - SingleLineComment
     - MultiLineComment
     - SchemaLink
     - Header
   * - JSON
     - ::

           "Hello"
     - ::

           [1, "two", true]
     - ::

           {"key": "value", "num": 42}
     - N/A
     - N/A
     - N/A
     - ::

           "\$schema": "http://json-schema.org/draft-07/schema#"
     - N/A
   * - XML
     - ::

           <tag>Hello</tag>
     - ::

           <list>
             <item>1</item>
             <item>2</item>
           </list>
     - ::

           <object>
             <key>value</key>
             <num>42</num>
           </object>
     - ::

           <element attr="value">Content</element>
     - ::

           <!-- comment -->
     - ::

           <!--
             line 1
             line 2
           -->
     - ::

           <root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="http://example.com schema.xsd">
     - ::

           <?xml version="1.0" encoding="UTF-8"?>
   * - YAML
     - ::

           Hello or 'Hello' or "Hello"
     - ::

           - 1
           - two
           - true
     - ::

           key: value
           num: 42
     - ::

           !!str "value" or !custom { key: val }
     - ::

           # comment
     - ::

           # line 1
           # line 2
     - ::

           # yaml-language-server: \$schema=<url_or_path>
     - ::

           %YAML 1.2
           ---
   * - TOML
     - ::

           "Hello"
     - ::

           [1, 2, 3]
     - ::

           key = "value"
           num = 42
     - N/A
     - ::

           # comment
     - ::

           # line 1
           # line 2
     - N/A
     - N/A
   * - CSV
     - ::

           Hello or "Hello"
     - ::

           1,two,true
     - ::

           Name,Age
           Alice,30
     - N/A
     - N/A
     - N/A
     - N/A
     - ::

           Name,Age,City
   * - Fixlength
     - ::

           Fixed width string (e.g., 'Hello     ')
     - ::

           Field1Field2Field3
     - ::

           Pos 1-10: Name, 11-15: Age
     - N/A
     - N/A
     - N/A
     - N/A
     - ::

           H2026052400001
