# cvxball-client

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Created with qCradle](https://img.shields.io/badge/Created%20with-qCradle-blue?style=flat-square)](https://github.com/tschm/experiments)

## Getting Started

### **Set Up Environment**

Construct a cloud of $200$ points with

```python
>>> import numpy as np
>>> data = {"input": np.random.randn(200, 2)}
```

```python
>>> from np.flight import Client

>>> # Connect to the server
>>> with Client("grpc+tls://cvxball-710171668953.us-central1.run.app:443") as client:
...     # The server will return a dictionary of numpy arrays
...     results = client.compute(command="test", data=data)
```

Here is a complete [demo](demo.py).
