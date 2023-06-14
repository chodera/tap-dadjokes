"""Stream type classes for tap-dadjokes."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_dadjokes.client import DadJokesStream

class SearchStream(DadJokesStream):
    """Define custom stream."""

    name = "search"
    path = "/search"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("joke", th.StringType),
    ).to_dict()
