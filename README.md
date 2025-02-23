# cvxball-client

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Created with qCradle](https://img.shields.io/badge/Created%20with-qCradle-blue?style=flat-square)](https://github.com/tschm/experiments)

## Getting Started

### **Set Up Environment**

```bash
make install
```

Construct a cloud of $200$ points with

```python
>>> import numpy as np
>>> data = {"input": np.random.randn(200, 2)}
```

```python
>>> from np.flight import Client

# Connect to the server
>>> with Client("grpc+tls://cvxball-710171668953.us-central1.run.app:443") as client:
...     # The server will return a dictionary of numpy arrays
...     results = client.compute(command="test", data=data)
```

This installs/updates [uv](https://github.com/astral-sh/uv),
creates your virtual environment and installs dependencies.

## Contributing

- Fork the repository
- Create your feature branch (git checkout -b feature/amazing-feature)
- Commit your changes (git commit -m 'Add some amazing feature')
- Push to the branch (git push origin feature/amazing-feature)
- Open a Pull Request
