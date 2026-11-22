# JSON command-line interface for Merge overlapping intervals

The core function now has a reusable command-line entry point. It reads a single JSON document from standard input and prints a single JSON result to standard output. Diagnostics go to standard error, with exit status 2 on invalid input.

```sh
python3 cli.py < samples/single.json
```

Input:

```json
[
  [
    1,
    2
  ],
  [
    2,
    3
  ]
]
```

Expected output:

```json
[
  [
    1,
    3
  ]
]
```

This case complements the first example. Sort by start then grow the current interval. Touching endpoints merge here; each interval must have start less than or equal to end.

The wrapper reads at most one MiB plus one byte to detect oversized input, serializes the result before printing, and rejects non-finite JSON numbers in output. This bounds input bytes, not algorithmic running time: do not expose the process directly to untrusted public traffic. Arguments are JSON data and are never evaluated as Python source.

Try an incomplete JSON value to observe exit status 2. An empty input file is invalid JSON, whereas a JSON empty string or list may be valid for the particular recipe. Keep standard output free of debug messages so another tool can consume it.
