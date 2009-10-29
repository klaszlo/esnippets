#!/bin/sh -e
echo "building gui.edj..."
edje_cc\
	gui.edc\
	-o gui.edj

