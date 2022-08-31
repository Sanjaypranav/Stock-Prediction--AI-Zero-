virtual-env:
	conda create -n zero python=3.9

install:
	make virtual-env
	conda activate zero
	pip install -r requirements.txt