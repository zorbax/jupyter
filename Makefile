default: build

all: build lite marimo

build:
	@jupyter book build jupyter/book/
	@rsync -avz jupyter/book/data jupyter/book/_build/html/

slides: 
	@uvx jupyter-nbconvert --with nbconvert --from nbconvert \
		nbconvert --to slides jupyter/slides/educational_notebooks.ipynb

lite:
	@rsync -avz \
		--exclude "*md" --exclude "*yml" --exclude "_build" --exclude "static" \
		--exclude ".virtual_documents" --exclude ".ipynb_checkpoints" \
		jupyter/book/ jupyter/content/
	@uv pip compile pyproject.toml --no-deps -o jupyter/lite/requirements.txt
	@jupyter lite build --contents jupyter/content/ --output-dir jupyter/lite
	@rsync -avz jupyter/lite/ jupyter/book/_build/html/jupyterlite
	@rm -rf jupyter/content

.PHONY: marimo
marimo:
	@mkdir -p marimo && rsync -avz jupyter/book/data marimo/
	@marimo convert jupyter/book/marimo.ipynb -o marimo/marimo.py
	@marimo export html-wasm marimo/marimo.py -o marimo/marimo.html --mode edit
	@rsync -avz marimo/ jupyter/book/_build/html/marimo


clean:
	@jupyter-book clean jupyter/book/ --all
	@rm -f jupyter/book/_build/html/.buildinfo 
	@echo "Cleaning jupyter/lite..."
	@rm -rf jupyter/lite/* marimo/*
	@touch jupyter/lite/.gitkeep marimo/.gitkeep
	@rm -rf cockle_wasm_env cockle-config.json jupyter/content

serve-book:
	@python -m http.server 8000 -d jupyter/book/_build/html

serve-lite:
	@jupyter lite serve jupyter/lite/

serve-marimo:
	@python -m http.server 8001 -d marimo/marimo.html