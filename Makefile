.PHONY: test test_one test_syntax
	
test:
	python -m unittest

test_one:
	python -m unittest tests.tests.TestWikiLinks.testLinkText

test_syntax:
	python -m unittest tests.tests_syntax
