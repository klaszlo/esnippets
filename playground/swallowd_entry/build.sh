#!/bin/sh -e
echo "building people.edj..."
edje_cc\
	-id edje/default/images\
	-id ../../resources/images\
	-fd ../../resources/fonts\
	edje/default/people.edc\
	-o people.edj
