"""
Zepton module template.

Copy this file into modules/<category>/<your_module>.py and edit.
The loader picks it up automatically on the next launch as
"<category>/<your_module>".
"""
import shutil

from core.colors import error, info, success
from core.module_base import BaseModule


class MyModule(BaseModule):
    # --- metadata (shown in 'show modules' and 'info') ---
    name = "My module"
    description = "One line about what this module does."
    author = "your handle"
    category = "misc"

    # --- options (shown in 'show options'; set with 'set NAME value') ---
    options = {
        "TARGET": {
            "value": "",                       # default value
            "required": True,                  # console enforces this before run()
            "description": "What this option is for",
        },
        "VERBOSE": {
            "value": "no",
            "required": False,
            "description": "yes = extra output",
        },
    }

    def run(self):
        # Read options with self.get() — keys are case-insensitive.
        target = self.get("TARGET")
        verbose = self.get("VERBOSE", "no").lower() in ("yes", "true", "1")

        # If you depend on an external binary, check first:
        if not shutil.which("some-tool"):
            error("some-tool not found. Install it with: pkg install some-tool")
            return

        info(f"Working on {target}...")

        # ---- your logic here ----

        if verbose:
            info("extra detail for the curious")
        success("Done.")
