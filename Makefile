all:

.PHONY: build

build: pack
	rm -rf dist/*
	poetry build -f wheel

publish: build
	twine upload dist/*whl


bump:
	./bump-version.sh patch
	git push --tags

bump-minor:
	./bump-version.sh minor
	git push --tags

bump-major:
	./bump-version.sh major
	git push --tags

.PHONY: docs

docs:
	mkdocs build

docs-serve:
	mkdocs serve

TD=assets/test-data/downloaded

pack:  
	zuper-cli pack -d $(TD) --include '**/*yaml' -o src/act4e_mcdp/autogen_packed_test_data.py

get-data:
	-rm -rf $(TD)/*
	zuper-ide-imp-create-test-cases \
		--only-single-output \
		--github-username AndreaCensi --source https://github.com/co-design-models/ACT4E-exercises-spring2023  -o $(TD)
