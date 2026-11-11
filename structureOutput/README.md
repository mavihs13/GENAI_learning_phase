# Structured Output

## What
Covers using Pydantic to define and validate structured data models — the foundation for getting structured JSON output from LLMs.

## Tech
- `pydantic` — data validation and schema definition

## Files

### `pydentic_Demo.py`
- **What**: Defines a `Student` Pydantic model and validates a dictionary against it.
- **How**: `class Student(BaseModel)` declares typed fields; `Student(**dict)` validates and parses the input.
- **When**: Use to understand how Pydantic enforces types and structure — the same mechanism LangChain uses internally for structured LLM output.

## Key Concepts
- `BaseModel` — base class for all Pydantic models
- Field type annotations (`str`, `int`) — Pydantic validates that input matches these types at runtime
- `**dict` unpacking — passes a dictionary as keyword arguments to the model constructor
- This pattern extends to LangChain's `with_structured_output()` — where you pass a Pydantic model to force the LLM to return structured JSON matching your schema
