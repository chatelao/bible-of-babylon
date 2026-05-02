# Generated from src/SourcePatterns.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SourcePatternsParser import SourcePatternsParser
else:
    from SourcePatternsParser import SourcePatternsParser

# This class defines a complete generic visitor for a parse tree produced by SourcePatternsParser.

class SourcePatternsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SourcePatternsParser#program.
    def visitProgram(self, ctx:SourcePatternsParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#patternDefinition.
    def visitPatternDefinition(self, ctx:SourcePatternsParser.PatternDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#instanceDefinition.
    def visitInstanceDefinition(self, ctx:SourcePatternsParser.InstanceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#anonymousInstance.
    def visitAnonymousInstance(self, ctx:SourcePatternsParser.AnonymousInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#metaDefinition.
    def visitMetaDefinition(self, ctx:SourcePatternsParser.MetaDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#parameterDefinition.
    def visitParameterDefinition(self, ctx:SourcePatternsParser.ParameterDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#assignment.
    def visitAssignment(self, ctx:SourcePatternsParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#type.
    def visitType(self, ctx:SourcePatternsParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#value.
    def visitValue(self, ctx:SourcePatternsParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#listLiteral.
    def visitListLiteral(self, ctx:SourcePatternsParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#block.
    def visitBlock(self, ctx:SourcePatternsParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#instruction.
    def visitInstruction(self, ctx:SourcePatternsParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#callInstruction.
    def visitCallInstruction(self, ctx:SourcePatternsParser.CallInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#assignInstruction.
    def visitAssignInstruction(self, ctx:SourcePatternsParser.AssignInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#returnInstruction.
    def visitReturnInstruction(self, ctx:SourcePatternsParser.ReturnInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SourcePatternsParser#rawInstruction.
    def visitRawInstruction(self, ctx:SourcePatternsParser.RawInstructionContext):
        return self.visitChildren(ctx)



del SourcePatternsParser