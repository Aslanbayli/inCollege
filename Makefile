run:
	python main.py
	
reqs:
	pip install -r requirements.txt 

test:
	pytest -vv
