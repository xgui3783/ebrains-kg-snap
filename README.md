# KG snap util

## Example

```python
import os

os.environ["AUTH_TOKEN"] = "ey..."

from ebrains_kg_snap.snapshot_ds import snap
from pathlib import Path

snap(Path("foo"))

```

## License

MIT
