"""
psycopg3 types package
"""

# Copyright (C) 2020-2021 The Psycopg Team

from typing import TYPE_CHECKING

from . import bool
from . import date
from . import json
from . import none
from . import text
from . import uuid
from . import array
from . import range
from . import network
from . import numeric
from . import composite

from .._typeinfo import TypeInfo as TypeInfo  # exported here

if TYPE_CHECKING:
    from ..proto import AdaptContext


def register_default_globals(ctx: "AdaptContext") -> None:
    bool.register_default_globals(ctx)
    date.register_default_globals(ctx)
    json.register_default_globals(ctx)
    none.register_default_globals(ctx)
    text.register_default_globals(ctx)
    uuid.register_default_globals(ctx)
    array.register_default_globals(ctx)
    range.register_default_globals(ctx)
    network.register_default_globals(ctx)
    numeric.register_default_globals(ctx)
    composite.register_default_globals(ctx)

    # Must come after all the types are registered
    array.register_all_arrays(ctx)
