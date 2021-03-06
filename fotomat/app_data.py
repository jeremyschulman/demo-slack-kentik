# -----------------------------------------------------------------------------
# Public Imports
# -----------------------------------------------------------------------------

from fastapi import FastAPI
from slack_bolt.async_app import AsyncApp


# -----------------------------------------------------------------------------
# Exports
# -----------------------------------------------------------------------------

__all__ = ["api", "app"]

# -----------------------------------------------------------------------------
#                                 GLOBALS
# -----------------------------------------------------------------------------

api = FastAPI()
app = AsyncApp()
