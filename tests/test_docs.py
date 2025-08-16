"""Tests for validating code examples in documentation.

This module contains tests that extract and run Python code blocks from the README.md
file to ensure they are valid and working as expected.
"""

import doctest
import re

import pytest


@pytest.fixture()
def docstring(root_dir):
    """Extract Python code blocks from README.md and prepare them for doctest.

    Args:
        root_dir: Pytest fixture providing the project root directory

    Returns:
        A string containing all Python code blocks from README.md
    """
    # Read the README.md file
    with open(root_dir / "README.md") as f:
        content = f.read()

    # Extract Python code blocks (assuming they are in triple backticks)
    blocks = re.findall(r"```python(.*?)```", content, re.DOTALL)

    code = "\n".join(blocks).strip()

    # Add a docstring wrapper for doctest to process the code
    docstring = f"\n{code}\n"

    return docstring


def test_blocks(docstring, capfd):
    """Test that code blocks in the README.md file are valid and can be executed.

    This test extracts Python code blocks from the README.md file and runs them
    through doctest to ensure they execute without errors.

    Args:
        docstring: Fixture providing the code blocks from README.md
        capfd: Pytest fixture for capturing stdout/stderr
    """
    try:
        doctest.run_docstring_examples(docstring, globals())
    except doctest.DocTestFailure as e:
        # If a DocTestFailure occurs, capture it and manually fail the test
        pytest.fail(f"Doctests failed: {e}")

    # Capture the output after running doctests
    captured = capfd.readouterr()

    # If there is any output (error message), fail the test
    if captured.out:
        pytest.fail(f"Doctests failed with the following output:\n{captured.out} and \n{docstring}")
