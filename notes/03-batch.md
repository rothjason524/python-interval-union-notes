# Ordered batch processing for Merge overlapping intervals

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
[
  [
    1,
    3
  ],
  [
    2,
    5
  ],
  [
    8,
    9
  ]
]
```

Result:
```json
[
  [
    1,
    5
  ],
  [
    8,
    9
  ]
]
```

## Case 2

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

Result:
```json
[
  [
    1,
    3
  ]
]
```

## Case 3

Input:
```json
[]
```

Result:
```json
[]
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

Sort by start then grow the current interval. Touching endpoints merge here; each interval must have start less than or equal to end.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
