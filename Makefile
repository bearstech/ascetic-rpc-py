proto:
	protoc --python_out=. *.proto

clean:
	rm -rf bin lib .Python
	find . -name "__pycache__" -exec rm -rf {} \;
