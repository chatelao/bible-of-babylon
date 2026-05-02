grammar SourcePatterns;

// Parser Rules

program
    : (patternDefinition | instanceDefinition)* EOF
    ;

patternDefinition
    : PATTERN IDENTIFIER '{' (metaDefinition | parameterDefinition)* '}'
    ;

instanceDefinition
    : INSTANCE IDENTIFIER OF IDENTIFIER '{' (metaDefinition | assignment | ',')* '}'
    | anonymousInstance
    ;

anonymousInstance
    : INSTANCE OF IDENTIFIER '{' (metaDefinition | assignment | ',')* '}'
    ;

metaDefinition
    : META IDENTIFIER ':' (STRING | IDENTIFIER)
    ;

parameterDefinition
    : PARAMETER IDENTIFIER ':' type
    ;

assignment
    : IDENTIFIER '=' value
    ;

type
    : IDENTIFIER
    | 'List<' type '>'
    ;

value
    : STRING
    | NUMBER
    | IDENTIFIER
    | listLiteral
    | anonymousInstance
    | block
    ;

listLiteral
    : '[' (value (',' value)* ','?)? ']'
    ;

block
    : '{' instruction* '}'
    ;

instruction
    : callInstruction
    | assignInstruction
    | returnInstruction
    | rawInstruction
    ;

callInstruction
    : CALL IDENTIFIER '(' (value (',' value)* ','?)? ')'
    ;

assignInstruction
    : ASSIGN IDENTIFIER '=' value
    ;

returnInstruction
    : RETURN value
    ;

rawInstruction
    : RAW STRING
    ;

// Lexer Rules

PATTERN: 'pattern';
INSTANCE: 'instance';
OF: 'of';
META: 'meta';
PARAMETER: 'parameter';
CALL: 'call';
ASSIGN: 'assign';
RETURN: 'return';
RAW: 'raw';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' ( '\\' . | ~["\\\r\n] )* '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;

WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
