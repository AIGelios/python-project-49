# Makefile
install: # installation
	poetry install

brain-games: # running
	poetry run brain-games

build: # making build
	poetry build

publish: # 'publishing' with dry run
	poetry publish --dry-run

package-install: # installing package into user's directory
	python3 -m pip install --user dist/*.whl
