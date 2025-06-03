vis:
	@processing-java --sketch=visualizer --run
encode:
	@python3 encode.py $(ARGS)
decode:
	@python3 decode.py $(ARGS)
