# DSL Examples

These examples validate the DSL draft from `docs/dsl_specification.md` and identify areas for refinement.

## 1. Control Flow (If/Else)

Capturing blocks of code is essential for control flow.

```
pattern IfElse {
    parameter condition: Expression
    parameter then_branch: Block
    parameter else_branch: Block
}

instance CheckBalance of IfElse {
    condition = "balance > 100"
    then_branch = {
        call charge_fee(0)
    }
    else_branch = {
        call charge_fee(10)
    }
}
```

*Gap Identified*: The `Block` type and `{}` syntax for blocks need to be formally defined.

## 2. Concurrency (Message Passing)

Basic message passing can be represented with simple parameters.

```
pattern MessageSend {
    parameter target: Identifier
    parameter payload: Expression
}

instance NotifyUser of MessageSend {
    target = "user_service"
    payload = "registration_complete"
}
```

## 3. Nested Data Structures (Object/Map)

Data formats often require nesting and collections.

```
pattern DataMap {
    parameter entries: List<MapEntry>
}

pattern MapEntry {
    parameter key: String
    parameter value: Expression
}

instance UserProfile of DataMap {
    entries = [
        instance of MapEntry { key = "id", value = 1 },
        instance of MapEntry { key = "active", value = true }
    ]
}
```

*Gap Identified*: Support for `List` types, literal lists `[]`, and anonymous instances (`instance of ...`) as parameter values are missing from v0.1.
