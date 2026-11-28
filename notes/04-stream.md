# Streaming Merge overlapping intervals with JSON Lines

`stream.py` reads one JSON value per physical line and emits one result envelope per line. Unlike `batch.py`, it does not keep all inputs or results in memory. A line number starts at one so errors can be traced back to the source file.

```sh
python3 stream.py < samples/stream.jsonl
```

The sample uses the same reviewed cases to demonstrate the protocol change without silently changing the algorithm. Sort by start then grow the current interval. Touching endpoints merge here; each interval must have start less than or equal to end.

Blank lines are invalid JSON and produce error envelopes. A final line without a newline is still processed. Oversized lines are drained through their newline in bounded chunks and reported once, so their remainder cannot be mistaken for a new record. A limit of one MiB applies per line; output size and algorithm complexity remain the caller's responsibility.

A failure does not stop subsequent records. Exit status 1 indicates at least one failed record, and output is flushed after each result to support a pipe. There is deliberately no parallel execution or network access. For large workloads, add application-specific time and output-size limits before deploying this educational code as a service.

This completes the prepared curriculum. Further updates require a newly authored lesson; no date-only changes or repeated commits are scheduled.
