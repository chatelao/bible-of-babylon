# Generated from src/SourcePatterns.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SourcePatternsParser import SourcePatternsParser
else:
    from SourcePatternsParser import SourcePatternsParser

# This class defines a complete listener for a parse tree produced by SourcePatternsParser.
class SourcePatternsListener(ParseTreeListener):

    # Enter a parse tree produced by SourcePatternsParser#program.
    def enterProgram(self, ctx:SourcePatternsParser.ProgramContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#program.
    def exitProgram(self, ctx:SourcePatternsParser.ProgramContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#patternDefinition.
    def enterPatternDefinition(self, ctx:SourcePatternsParser.PatternDefinitionContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#patternDefinition.
    def exitPatternDefinition(self, ctx:SourcePatternsParser.PatternDefinitionContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#instanceDefinition.
    def enterInstanceDefinition(self, ctx:SourcePatternsParser.InstanceDefinitionContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#instanceDefinition.
    def exitInstanceDefinition(self, ctx:SourcePatternsParser.InstanceDefinitionContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#anonymousInstance.
    def enterAnonymousInstance(self, ctx:SourcePatternsParser.AnonymousInstanceContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#anonymousInstance.
    def exitAnonymousInstance(self, ctx:SourcePatternsParser.AnonymousInstanceContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#metaDefinition.
    def enterMetaDefinition(self, ctx:SourcePatternsParser.MetaDefinitionContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#metaDefinition.
    def exitMetaDefinition(self, ctx:SourcePatternsParser.MetaDefinitionContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#parameterDefinition.
    def enterParameterDefinition(self, ctx:SourcePatternsParser.ParameterDefinitionContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#parameterDefinition.
    def exitParameterDefinition(self, ctx:SourcePatternsParser.ParameterDefinitionContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#assignment.
    def enterAssignment(self, ctx:SourcePatternsParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#assignment.
    def exitAssignment(self, ctx:SourcePatternsParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#type.
    def enterType(self, ctx:SourcePatternsParser.TypeContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#type.
    def exitType(self, ctx:SourcePatternsParser.TypeContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#value.
    def enterValue(self, ctx:SourcePatternsParser.ValueContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#value.
    def exitValue(self, ctx:SourcePatternsParser.ValueContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#listLiteral.
    def enterListLiteral(self, ctx:SourcePatternsParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#listLiteral.
    def exitListLiteral(self, ctx:SourcePatternsParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#block.
    def enterBlock(self, ctx:SourcePatternsParser.BlockContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#block.
    def exitBlock(self, ctx:SourcePatternsParser.BlockContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#instruction.
    def enterInstruction(self, ctx:SourcePatternsParser.InstructionContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#instruction.
    def exitInstruction(self, ctx:SourcePatternsParser.InstructionContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#callInstruction.
    def enterCallInstruction(self, ctx:SourcePatternsParser.CallInstructionContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#callInstruction.
    def exitCallInstruction(self, ctx:SourcePatternsParser.CallInstructionContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#assignInstruction.
    def enterAssignInstruction(self, ctx:SourcePatternsParser.AssignInstructionContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#assignInstruction.
    def exitAssignInstruction(self, ctx:SourcePatternsParser.AssignInstructionContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#returnInstruction.
    def enterReturnInstruction(self, ctx:SourcePatternsParser.ReturnInstructionContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#returnInstruction.
    def exitReturnInstruction(self, ctx:SourcePatternsParser.ReturnInstructionContext):
        pass


    # Enter a parse tree produced by SourcePatternsParser#rawInstruction.
    def enterRawInstruction(self, ctx:SourcePatternsParser.RawInstructionContext):
        pass

    # Exit a parse tree produced by SourcePatternsParser#rawInstruction.
    def exitRawInstruction(self, ctx:SourcePatternsParser.RawInstructionContext):
        pass



del SourcePatternsParser