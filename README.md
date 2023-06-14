# tap-dadjokes

`tap-dadjokes` is a Singer tap for DadJokes on https://icanhazdadjoke.com.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Configuration

### Accepted Config Options

<!--
Developer TODO: Provide a list of config options accepted by the tap.

This section can be created by copy-pasting the CLI output from:

```
tap-dadjokes --about --format=markdown
```
-->

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-dadjokes --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

<!--
Developer TODO: If your tap requires special access on the source system, or any special authentication requirements, provide those here.
-->

No authentication required.

## Usage

You can easily run `tap-dadjokes` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-dadjokes --version
tap-dadjokes --help
tap-dadjokes --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-dadjokes` CLI interface directly using `poetry run`:

```bash
poetry run tap-dadjokes --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-dadjokes
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-dadjokes --version
# OR run a test `elt` pipeline:
meltano elt tap-dadjokes target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
