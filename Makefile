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

package-reinstall: # force reinstalling into user,s directory
	python3 -m pip install --user dist/*.whl --force-reinstall

lint: # lint project with flake8
	poetry run flake8 brain_games
