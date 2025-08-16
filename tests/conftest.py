"""Test configuration and fixtures for the cvxball-client project.

This module contains pytest fixtures that are available to all test modules.
"""

from pathlib import Path

import pytest


@pytest.fixture(name="root_dir")
def root_fixture() -> Path:
    """Provide the root directory of the project.

    Returns:
        Path: The absolute path to the project root directory
    """
    return Path(__file__).parent.parent
