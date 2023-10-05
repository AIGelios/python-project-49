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

package-uninstall: # removing installed packet from system
	python3 -m pip uninstall hexlet-code

package-reinstall: # force reinstalling into user,s directory
	python3 -m pip install --user dist/*.whl --force-reinstall

update: # total maintenance
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl --force-reinstall

lint: # lint project with flake8
	poetry run flake8 brain_games
