"""DadJokes tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_dadjokes import streams

class TapDadJokes(Tap):
    """DadJokes tap class."""

    name = "tap-dadjokes"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "user_agent",
            th.StringType,
            description="Setting a custom User-Agent header for your code helps to be able to better monitor the usage of the API and identify potential bad actors.",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.DadJokesStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.SearchStream(self),
        ]


if __name__ == "__main__":
    TapDadJokes.cli()
