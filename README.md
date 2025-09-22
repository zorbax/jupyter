# Interactive Educational Notebooks

A multi-platform Python learning environment featuring three complementary tools:

- **Jupyter Book**: Static documentation with interactive notebooks
- **JupyterLite**: Browser-based Python execution (Pyodide/WASM)
- **Marimo**: Reactive notebooks with automatic dependency tracking

## Quick Start

```bash
git clone <repository-url>
cd <repository-directory>
uv venv --python 3.12 && source .venv/bin/activate
uv sync
make all
```

## Build Targets

- `make build` - Generate Jupyter Book site
- `make lite` - Build JupyterLite environment  
- `make marimo` - Convert notebooks to Marimo format
- `make all` - Build all platforms
