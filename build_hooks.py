import subprocess
import sys
from pathlib import Path
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        """Initialize the build hook."""
        api_compiler_dir = Path("compiler/api")
        errors_compiler_dir = Path("compiler/errors")

        print("Running API compiler...")
        subprocess.check_call([sys.executable, "compiler.py"], cwd=api_compiler_dir)

        print("Running errors compiler...")
        subprocess.check_call([sys.executable, "compiler.py"], cwd=errors_compiler_dir)

        return build_data