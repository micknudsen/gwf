"""gwf - a pragmatic workflow tool"""

from .core import AnonymousTarget, Target
from .workflow import TargetList, Workflow

__version__ = "1.8.5"

__all__ = ("Target", "AnonymousTarget", "Workflow", "TargetList")
