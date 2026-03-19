create-practice:
ifndef PRACTICE
	$(error must pass val PRACTICE)
endif
	@echo "Creating practice"
	mkdir -p $(PRACTICE)

remove-practice:
	rm -rf $(PRACTICE)

help:
	@echo "This makefile for-level activity"



# mkdir demo-practice
# mkdir demo-practice/src
# mkdir demo-practice/tests
# mkdir demo-practice/docs
# touch demo-practice/README.md