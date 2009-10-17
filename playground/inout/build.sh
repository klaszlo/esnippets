#!/bin/sh -e
echo "building inout.edj..."
edje_cc\
	-id edje/default/images\
	-id ../../resources/images\
	-fd ../../resources/fonts\
	edje/default/inout.edc\
	-o inout.edj
