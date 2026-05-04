import sys
import os

# Add src/generated to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'generated')))

from SourcePatternsParser import SourcePatternsParser
from SourcePatternsVisitor import SourcePatternsVisitor
from .models import (
    Program, Pattern, Instance, AnonymousInstance, Metadata, Parameter,
    Type, Assignment, Block, Instruction, CallInstruction, AssignInstruction,
    ReturnInstruction, RawInstruction, Identifier, ListLiteral
)

class SourcePatternsTransformer(SourcePatternsVisitor):

    def visitProgram(self, ctx: SourcePatternsParser.ProgramContext):
        patterns = []
        instances = []
        for child in ctx.children:
            res = self.visit(child)
            if isinstance(res, Pattern):
                patterns.append(res)
            elif isinstance(res, Instance):
                instances.append(res)
        return Program(patterns=patterns, instances=instances)

    def visitPatternDefinition(self, ctx: SourcePatternsParser.PatternDefinitionContext):
        name = ctx.IDENTIFIER().getText()
        metadata = []
        parameters = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            res = self.visit(child)
            if isinstance(res, Metadata):
                metadata.append(res)
            elif isinstance(res, Parameter):
                parameters.append(res)
        return Pattern(name=name, metadata=metadata, parameters=parameters)

    def visitInstanceDefinition(self, ctx: SourcePatternsParser.InstanceDefinitionContext):
        if ctx.anonymousInstance():
            return self.visit(ctx.anonymousInstance())

        name = ctx.IDENTIFIER(0).getText()
        pattern_name = ctx.IDENTIFIER(1).getText()
        metadata = []
        assignments = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            res = self.visit(child)
            if isinstance(res, Metadata):
                metadata.append(res)
            elif isinstance(res, Assignment):
                assignments.append(res)
        return Instance(name=name, pattern_name=pattern_name, metadata=metadata, assignments=assignments)

    def visitAnonymousInstance(self, ctx: SourcePatternsParser.AnonymousInstanceContext):
        pattern_name = ctx.IDENTIFIER().getText()
        metadata = []
        assignments = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            res = self.visit(child)
            if isinstance(res, Metadata):
                metadata.append(res)
            elif isinstance(res, Assignment):
                assignments.append(res)
        return AnonymousInstance(pattern_name=pattern_name, metadata=metadata, assignments=assignments)

    def visitMetaDefinition(self, ctx: SourcePatternsParser.MetaDefinitionContext):
        key = ctx.IDENTIFIER(0).getText()
        if ctx.STRING():
            value = ctx.STRING().getText()[1:-1]
        else:
            value = ctx.IDENTIFIER(1).getText()
        return Metadata(key=key, value=value)

    def visitParameterDefinition(self, ctx: SourcePatternsParser.ParameterDefinitionContext):
        name = ctx.IDENTIFIER().getText()
        param_type = self.visit(ctx.type_())
        return Parameter(name=name, type=param_type)

    def visitAssignment(self, ctx: SourcePatternsParser.AssignmentContext):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.value())
        return Assignment(name=name, value=value)

    def visitType(self, ctx: SourcePatternsParser.TypeContext):
        if ctx.getChildCount() == 1:
            return Type(name=ctx.IDENTIFIER().getText())
        else:
            # List<type>
            inner_type = self.visit(ctx.type_())
            return Type(name="List", inner_type=inner_type)

    def visitValue(self, ctx: SourcePatternsParser.ValueContext):
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        if ctx.NUMBER():
            val = ctx.NUMBER().getText()
            return float(val) if '.' in val else int(val)
        if ctx.IDENTIFIER():
            return Identifier(name=ctx.IDENTIFIER().getText())
        if ctx.listLiteral():
            return self.visit(ctx.listLiteral())
        if ctx.anonymousInstance():
            return self.visit(ctx.anonymousInstance())
        if ctx.block():
            return self.visit(ctx.block())
        return None

    def visitListLiteral(self, ctx: SourcePatternsParser.ListLiteralContext):
        elements = [self.visit(v) for v in ctx.value()]
        return ListLiteral(elements=elements)

    def visitBlock(self, ctx: SourcePatternsParser.BlockContext):
        instructions = [self.visit(i) for i in ctx.instruction()]
        return Block(instructions=instructions)

    def visitInstruction(self, ctx: SourcePatternsParser.InstructionContext):
        return self.visitChildren(ctx)

    def visitCallInstruction(self, ctx: SourcePatternsParser.CallInstructionContext):
        name = ctx.IDENTIFIER().getText()
        arguments = [self.visit(v) for v in ctx.value()]
        return CallInstruction(name=name, arguments=arguments)

    def visitAssignInstruction(self, ctx: SourcePatternsParser.AssignInstructionContext):
        target = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.value())
        return AssignInstruction(target=target, value=value)

    def visitReturnInstruction(self, ctx: SourcePatternsParser.ReturnInstructionContext):
        value = self.visit(ctx.value())
        return ReturnInstruction(value=value)

    def visitRawInstruction(self, ctx: SourcePatternsParser.RawInstructionContext):
        snippet = ctx.STRING().getText()[1:-1]
        return RawInstruction(snippet=snippet)
