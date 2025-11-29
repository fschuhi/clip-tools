import pytest
from src.transformers.poe import transform_poe_chat


def test_transform_poe_chat_multiline():
    input_text = """User:
Are there tried and tested hierarchical statemachines for my Python code?

What are ways to use statemachines?
1. in Python in general
2. for a framework like StreamLit in particular

Assistant:
Yes, there are several well-established hierarchical state machine libraries for Python:"""

    expected_output = """> [!note] User:
> Are there tried and tested hierarchical statemachines for my Python code?
>
> What are ways to use statemachines?
> 1. in Python in general
> 2. for a framework like StreamLit in particular

Assistant:
Yes, there are several well-established hierarchical state machine libraries for Python:"""

    assert transform_poe_chat(input_text) == expected_output


def test_transform_poe_chat_single_line():
    input_text = """User:
Are there tried and tested hierarchical statemachines for my Python code?

Assistant:
Yes, there are several well-established hierarchical state machine libraries for Python:"""

    expected_output = """> [!note] User:
> Are there tried and tested hierarchical statemachines for my Python code?

Assistant:
Yes, there are several well-established hierarchical state machine libraries for Python:"""

    assert transform_poe_chat(input_text) == expected_output
