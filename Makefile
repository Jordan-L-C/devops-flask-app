CC = gcc
CFLAGS = -Wall -Wextra -std=c11
PREFIX = /usr/local

conway: main.o life.o
	$(CC) $(CFLAGS) -o conway main.o life.o

main.o: main.c life.h
	$(CC) $(CFLAGS) -c main.c

life.o: life.c life.h
	$(CC) $(CFLAGS) -c life.c

clean:
	rm -f conway main.o life.o

install: conway
	install -d $(PREFIX)/bin
	install -m 755 conway $(PREFIX)/bin/conway

.PHONY: clean install
