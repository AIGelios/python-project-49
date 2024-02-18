install:
	poetry install

test:
	poetry run pytest .

coverage:
	poetry run pytest --cov=brain_games/games --cov-report xml

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

build:
	make check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

update: install build publish package-reinstall
