# iter-together-2

This package has some utilities for iterating over files. 

## Getting Started

```python
from iter_together.utils import iter_together

file_1 = ['hi', 'hello']
file_2 = ['bye', 'goodbye']
results = iter_together(file_1, file_2)
```

## Installation

The code can be installed from GitHub with:

```shell
$ pip install git+https://github.com/vcchatman/iter-together-2.git
```

The code can be installed in development mode with:

```shell
$ git clone  https://github.com/vcchatman/iter-together-2
$ cd iter-together-2
$ pip install --editable .

```

Where `--editable` means the code is symlinked into your virtual environment's site-packages directory.


## License

This code is licensed under the MIT license.