.PHONY: another-app
# make all target are listed in PHONY

# Might be correct, but 'build 'and 'app' are difference
build: main.c
	gcc main.c -o app

# correct no PHONY
app: main.c
	gcc main.c -o app

#incorrect listed in PHONY
another-app: main.c
	gcc main.c -o another-app