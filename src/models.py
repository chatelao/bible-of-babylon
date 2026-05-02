from dataclasses import dataclass, field
from typing import List, Union, Optional, Any

@dataclass
class Metadata:
    key: str
    value: str

@dataclass
class Type:
    name: str
    inner_type: Optional['Type'] = None

@dataclass
class Parameter:
    name: str
    type: Type

@dataclass
class Pattern:
    name: str
    metadata: List[Metadata] = field(default_factory=list)
    parameters: List[Parameter] = field(default_factory=list)

@dataclass
class Instruction:
    pass

@dataclass
class Identifier:
    name: str

@dataclass
class ListLiteral:
    elements: List[Any] = field(default_factory=list)

@dataclass
class CallInstruction(Instruction):
    name: str
    arguments: List[Any] = field(default_factory=list)

@dataclass
class AssignInstruction(Instruction):
    target: str
    value: Any

@dataclass
class ReturnInstruction(Instruction):
    value: Any

@dataclass
class RawInstruction(Instruction):
    snippet: str

@dataclass
class Block:
    instructions: List[Instruction] = field(default_factory=list)

@dataclass(kw_only=True)
class AnonymousInstance:
    pattern_name: str
    metadata: List[Metadata] = field(default_factory=list)
    assignments: List['Assignment'] = field(default_factory=list)

@dataclass
class Assignment:
    name: str
    value: Any

@dataclass(kw_only=True)
class Instance(AnonymousInstance):
    name: str

@dataclass
class Program:
    patterns: List[Pattern] = field(default_factory=list)
    instances: List[Instance] = field(default_factory=list)
