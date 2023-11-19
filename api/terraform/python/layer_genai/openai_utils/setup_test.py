# -*- coding: utf-8 -*-
"""Test setup.py."""
import subprocess
import unittest


class TestSetup(unittest.TestCase):
    """Test setup.py."""

    def test_setup_syntax(self):
        """Test setup.py syntax."""
        result = subprocess.run(["python", "setup.py", "check"], capture_output=True, text=True, check=False)
        assert result.returncode == 0, f"setup.py failed with output:\n{result.stdout}\n{result.stderr}"
        assert not result.stderr, "Expected no error output"


if __name__ == "__main__":
    unittest.main()
