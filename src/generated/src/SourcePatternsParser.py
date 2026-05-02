# Generated from src/SourcePatterns.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,166,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,1,2,3,2,68,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,76,8,3,10,3,12,3,79,9,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,3,7,102,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,110,8,8,1,9,1,
        9,1,9,1,9,5,9,116,8,9,10,9,12,9,119,9,9,3,9,121,8,9,1,9,1,9,1,10,
        1,10,5,10,127,8,10,10,10,12,10,130,9,10,1,10,1,10,1,11,1,11,1,11,
        1,11,3,11,138,8,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,146,8,12,10,
        12,12,12,149,9,12,3,12,151,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,
        13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,0,1,1,0,21,22,172,0,36,1,0,0,0,2,41,1,0,
        0,0,4,67,1,0,0,0,6,69,1,0,0,0,8,82,1,0,0,0,10,87,1,0,0,0,12,92,1,
        0,0,0,14,101,1,0,0,0,16,109,1,0,0,0,18,111,1,0,0,0,20,124,1,0,0,
        0,22,137,1,0,0,0,24,139,1,0,0,0,26,154,1,0,0,0,28,159,1,0,0,0,30,
        162,1,0,0,0,32,35,3,2,1,0,33,35,3,4,2,0,34,32,1,0,0,0,34,33,1,0,
        0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,
        1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,42,5,12,0,0,42,43,5,21,0,0,
        43,48,5,1,0,0,44,47,3,8,4,0,45,47,3,10,5,0,46,44,1,0,0,0,46,45,1,
        0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,
        48,1,0,0,0,51,52,5,2,0,0,52,3,1,0,0,0,53,54,5,13,0,0,54,55,5,21,
        0,0,55,56,5,14,0,0,56,57,5,21,0,0,57,62,5,1,0,0,58,61,3,8,4,0,59,
        61,3,12,6,0,60,58,1,0,0,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,
        0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,68,5,2,0,0,66,68,
        3,6,3,0,67,53,1,0,0,0,67,66,1,0,0,0,68,5,1,0,0,0,69,70,5,13,0,0,
        70,71,5,14,0,0,71,72,5,21,0,0,72,77,5,1,0,0,73,76,3,8,4,0,74,76,
        3,12,6,0,75,73,1,0,0,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,
        77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,2,0,0,81,7,1,0,
        0,0,82,83,5,15,0,0,83,84,5,21,0,0,84,85,5,3,0,0,85,86,7,0,0,0,86,
        9,1,0,0,0,87,88,5,16,0,0,88,89,5,21,0,0,89,90,5,3,0,0,90,91,3,14,
        7,0,91,11,1,0,0,0,92,93,5,21,0,0,93,94,5,4,0,0,94,95,3,16,8,0,95,
        13,1,0,0,0,96,102,5,21,0,0,97,98,5,5,0,0,98,99,3,14,7,0,99,100,5,
        6,0,0,100,102,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,0,102,15,1,0,0,
        0,103,110,5,22,0,0,104,110,5,23,0,0,105,110,5,21,0,0,106,110,3,18,
        9,0,107,110,3,6,3,0,108,110,3,20,10,0,109,103,1,0,0,0,109,104,1,
        0,0,0,109,105,1,0,0,0,109,106,1,0,0,0,109,107,1,0,0,0,109,108,1,
        0,0,0,110,17,1,0,0,0,111,120,5,7,0,0,112,117,3,16,8,0,113,114,5,
        8,0,0,114,116,3,16,8,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,1,
        0,0,0,117,118,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,120,112,1,
        0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,5,9,0,0,123,19,1,0,
        0,0,124,128,5,1,0,0,125,127,3,22,11,0,126,125,1,0,0,0,127,130,1,
        0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,128,1,
        0,0,0,131,132,5,2,0,0,132,21,1,0,0,0,133,138,3,24,12,0,134,138,3,
        26,13,0,135,138,3,28,14,0,136,138,3,30,15,0,137,133,1,0,0,0,137,
        134,1,0,0,0,137,135,1,0,0,0,137,136,1,0,0,0,138,23,1,0,0,0,139,140,
        5,17,0,0,140,141,5,21,0,0,141,150,5,10,0,0,142,147,3,16,8,0,143,
        144,5,8,0,0,144,146,3,16,8,0,145,143,1,0,0,0,146,149,1,0,0,0,147,
        145,1,0,0,0,147,148,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,150,
        142,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,5,11,0,0,153,
        25,1,0,0,0,154,155,5,18,0,0,155,156,5,21,0,0,156,157,5,4,0,0,157,
        158,3,16,8,0,158,27,1,0,0,0,159,160,5,19,0,0,160,161,3,16,8,0,161,
        29,1,0,0,0,162,163,5,20,0,0,163,164,5,22,0,0,164,31,1,0,0,0,17,34,
        36,46,48,60,62,67,75,77,101,109,117,120,128,137,147,150
    ]

class SourcePatternsParser ( Parser ):

    grammarFileName = "SourcePatterns.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "':'", "'='", "'List<'",
                     "'>'", "'['", "','", "']'", "'('", "')'", "'pattern'",
                     "'instance'", "'of'", "'meta'", "'parameter'", "'call'",
                     "'assign'", "'return'", "'raw'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "PATTERN", "INSTANCE", "OF", "META", "PARAMETER",
                      "CALL", "ASSIGN", "RETURN", "RAW", "IDENTIFIER", "STRING",
                      "NUMBER", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_patternDefinition = 1
    RULE_instanceDefinition = 2
    RULE_anonymousInstance = 3
    RULE_metaDefinition = 4
    RULE_parameterDefinition = 5
    RULE_assignment = 6
    RULE_type = 7
    RULE_value = 8
    RULE_listLiteral = 9
    RULE_block = 10
    RULE_instruction = 11
    RULE_callInstruction = 12
    RULE_assignInstruction = 13
    RULE_returnInstruction = 14
    RULE_rawInstruction = 15

    ruleNames =  [ "program", "patternDefinition", "instanceDefinition",
                   "anonymousInstance", "metaDefinition", "parameterDefinition",
                   "assignment", "type", "value", "listLiteral", "block",
                   "instruction", "callInstruction", "assignInstruction",
                   "returnInstruction", "rawInstruction" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    PATTERN=12
    INSTANCE=13
    OF=14
    META=15
    PARAMETER=16
    CALL=17
    ASSIGN=18
    RETURN=19
    RAW=20
    IDENTIFIER=21
    STRING=22
    NUMBER=23
    WS=24
    LINE_COMMENT=25
    BLOCK_COMMENT=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SourcePatternsParser.EOF, 0)

        def patternDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.PatternDefinitionContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.PatternDefinitionContext,i)


        def instanceDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.InstanceDefinitionContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.InstanceDefinitionContext,i)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = SourcePatternsParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==13:
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 32
                    self.patternDefinition()
                    pass
                elif token in [13]:
                    self.state = 33
                    self.instanceDefinition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(SourcePatternsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PATTERN(self):
            return self.getToken(SourcePatternsParser.PATTERN, 0)

        def IDENTIFIER(self):
            return self.getToken(SourcePatternsParser.IDENTIFIER, 0)

        def metaDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.MetaDefinitionContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.MetaDefinitionContext,i)


        def parameterDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.ParameterDefinitionContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.ParameterDefinitionContext,i)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_patternDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternDefinition" ):
                listener.enterPatternDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternDefinition" ):
                listener.exitPatternDefinition(self)




    def patternDefinition(self):

        localctx = SourcePatternsParser.PatternDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_patternDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(SourcePatternsParser.PATTERN)
            self.state = 42
            self.match(SourcePatternsParser.IDENTIFIER)
            self.state = 43
            self.match(SourcePatternsParser.T__0)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 46
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 44
                    self.metaDefinition()
                    pass
                elif token in [16]:
                    self.state = 45
                    self.parameterDefinition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(SourcePatternsParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTANCE(self):
            return self.getToken(SourcePatternsParser.INSTANCE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(SourcePatternsParser.IDENTIFIER)
            else:
                return self.getToken(SourcePatternsParser.IDENTIFIER, i)

        def OF(self):
            return self.getToken(SourcePatternsParser.OF, 0)

        def metaDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.MetaDefinitionContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.MetaDefinitionContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.AssignmentContext,i)


        def anonymousInstance(self):
            return self.getTypedRuleContext(SourcePatternsParser.AnonymousInstanceContext,0)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_instanceDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceDefinition" ):
                listener.enterInstanceDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceDefinition" ):
                listener.exitInstanceDefinition(self)




    def instanceDefinition(self):

        localctx = SourcePatternsParser.InstanceDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instanceDefinition)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(SourcePatternsParser.INSTANCE)
                self.state = 54
                self.match(SourcePatternsParser.IDENTIFIER)
                self.state = 55
                self.match(SourcePatternsParser.OF)
                self.state = 56
                self.match(SourcePatternsParser.IDENTIFIER)
                self.state = 57
                self.match(SourcePatternsParser.T__0)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15 or _la==21:
                    self.state = 60
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [15]:
                        self.state = 58
                        self.metaDefinition()
                        pass
                    elif token in [21]:
                        self.state = 59
                        self.assignment()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 65
                self.match(SourcePatternsParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.anonymousInstance()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnonymousInstanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTANCE(self):
            return self.getToken(SourcePatternsParser.INSTANCE, 0)

        def OF(self):
            return self.getToken(SourcePatternsParser.OF, 0)

        def IDENTIFIER(self):
            return self.getToken(SourcePatternsParser.IDENTIFIER, 0)

        def metaDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.MetaDefinitionContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.MetaDefinitionContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.AssignmentContext,i)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_anonymousInstance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymousInstance" ):
                listener.enterAnonymousInstance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymousInstance" ):
                listener.exitAnonymousInstance(self)




    def anonymousInstance(self):

        localctx = SourcePatternsParser.AnonymousInstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_anonymousInstance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SourcePatternsParser.INSTANCE)
            self.state = 70
            self.match(SourcePatternsParser.OF)
            self.state = 71
            self.match(SourcePatternsParser.IDENTIFIER)
            self.state = 72
            self.match(SourcePatternsParser.T__0)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==21:
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 73
                    self.metaDefinition()
                    pass
                elif token in [21]:
                    self.state = 74
                    self.assignment()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(SourcePatternsParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetaDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def META(self):
            return self.getToken(SourcePatternsParser.META, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(SourcePatternsParser.IDENTIFIER)
            else:
                return self.getToken(SourcePatternsParser.IDENTIFIER, i)

        def STRING(self):
            return self.getToken(SourcePatternsParser.STRING, 0)

        def getRuleIndex(self):
            return SourcePatternsParser.RULE_metaDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetaDefinition" ):
                listener.enterMetaDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetaDefinition" ):
                listener.exitMetaDefinition(self)




    def metaDefinition(self):

        localctx = SourcePatternsParser.MetaDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_metaDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(SourcePatternsParser.META)
            self.state = 83
            self.match(SourcePatternsParser.IDENTIFIER)
            self.state = 84
            self.match(SourcePatternsParser.T__2)
            self.state = 85
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(SourcePatternsParser.PARAMETER, 0)

        def IDENTIFIER(self):
            return self.getToken(SourcePatternsParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(SourcePatternsParser.TypeContext,0)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_parameterDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterDefinition" ):
                listener.enterParameterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterDefinition" ):
                listener.exitParameterDefinition(self)




    def parameterDefinition(self):

        localctx = SourcePatternsParser.ParameterDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameterDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(SourcePatternsParser.PARAMETER)
            self.state = 88
            self.match(SourcePatternsParser.IDENTIFIER)
            self.state = 89
            self.match(SourcePatternsParser.T__2)
            self.state = 90
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SourcePatternsParser.IDENTIFIER, 0)

        def value(self):
            return self.getTypedRuleContext(SourcePatternsParser.ValueContext,0)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = SourcePatternsParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(SourcePatternsParser.IDENTIFIER)
            self.state = 93
            self.match(SourcePatternsParser.T__3)
            self.state = 94
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SourcePatternsParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(SourcePatternsParser.TypeContext,0)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = SourcePatternsParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(SourcePatternsParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(SourcePatternsParser.T__4)
                self.state = 98
                self.type_()
                self.state = 99
                self.match(SourcePatternsParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SourcePatternsParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(SourcePatternsParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(SourcePatternsParser.IDENTIFIER, 0)

        def listLiteral(self):
            return self.getTypedRuleContext(SourcePatternsParser.ListLiteralContext,0)


        def anonymousInstance(self):
            return self.getTypedRuleContext(SourcePatternsParser.AnonymousInstanceContext,0)


        def block(self):
            return self.getTypedRuleContext(SourcePatternsParser.BlockContext,0)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = SourcePatternsParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(SourcePatternsParser.STRING)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(SourcePatternsParser.NUMBER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.match(SourcePatternsParser.IDENTIFIER)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.listLiteral()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.anonymousInstance()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.ValueContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.ValueContext,i)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)




    def listLiteral(self):

        localctx = SourcePatternsParser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(SourcePatternsParser.T__6)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14688386) != 0):
                self.state = 112
                self.value()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 113
                    self.match(SourcePatternsParser.T__7)
                    self.state = 114
                    self.value()
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 122
            self.match(SourcePatternsParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.InstructionContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.InstructionContext,i)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = SourcePatternsParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(SourcePatternsParser.T__0)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0):
                self.state = 125
                self.instruction()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(SourcePatternsParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callInstruction(self):
            return self.getTypedRuleContext(SourcePatternsParser.CallInstructionContext,0)


        def assignInstruction(self):
            return self.getTypedRuleContext(SourcePatternsParser.AssignInstructionContext,0)


        def returnInstruction(self):
            return self.getTypedRuleContext(SourcePatternsParser.ReturnInstructionContext,0)


        def rawInstruction(self):
            return self.getTypedRuleContext(SourcePatternsParser.RawInstructionContext,0)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = SourcePatternsParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_instruction)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.callInstruction()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.assignInstruction()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.returnInstruction()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.rawInstruction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(SourcePatternsParser.CALL, 0)

        def IDENTIFIER(self):
            return self.getToken(SourcePatternsParser.IDENTIFIER, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourcePatternsParser.ValueContext)
            else:
                return self.getTypedRuleContext(SourcePatternsParser.ValueContext,i)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_callInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallInstruction" ):
                listener.enterCallInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallInstruction" ):
                listener.exitCallInstruction(self)




    def callInstruction(self):

        localctx = SourcePatternsParser.CallInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_callInstruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(SourcePatternsParser.CALL)
            self.state = 140
            self.match(SourcePatternsParser.IDENTIFIER)
            self.state = 141
            self.match(SourcePatternsParser.T__9)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14688386) != 0):
                self.state = 142
                self.value()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 143
                    self.match(SourcePatternsParser.T__7)
                    self.state = 144
                    self.value()
                    self.state = 149
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 152
            self.match(SourcePatternsParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(SourcePatternsParser.ASSIGN, 0)

        def IDENTIFIER(self):
            return self.getToken(SourcePatternsParser.IDENTIFIER, 0)

        def value(self):
            return self.getTypedRuleContext(SourcePatternsParser.ValueContext,0)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_assignInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignInstruction" ):
                listener.enterAssignInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignInstruction" ):
                listener.exitAssignInstruction(self)




    def assignInstruction(self):

        localctx = SourcePatternsParser.AssignInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(SourcePatternsParser.ASSIGN)
            self.state = 155
            self.match(SourcePatternsParser.IDENTIFIER)
            self.state = 156
            self.match(SourcePatternsParser.T__3)
            self.state = 157
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SourcePatternsParser.RETURN, 0)

        def value(self):
            return self.getTypedRuleContext(SourcePatternsParser.ValueContext,0)


        def getRuleIndex(self):
            return SourcePatternsParser.RULE_returnInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnInstruction" ):
                listener.enterReturnInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnInstruction" ):
                listener.exitReturnInstruction(self)




    def returnInstruction(self):

        localctx = SourcePatternsParser.ReturnInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_returnInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(SourcePatternsParser.RETURN)
            self.state = 160
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RawInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAW(self):
            return self.getToken(SourcePatternsParser.RAW, 0)

        def STRING(self):
            return self.getToken(SourcePatternsParser.STRING, 0)

        def getRuleIndex(self):
            return SourcePatternsParser.RULE_rawInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRawInstruction" ):
                listener.enterRawInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRawInstruction" ):
                listener.exitRawInstruction(self)




    def rawInstruction(self):

        localctx = SourcePatternsParser.RawInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_rawInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(SourcePatternsParser.RAW)
            self.state = 163
            self.match(SourcePatternsParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
