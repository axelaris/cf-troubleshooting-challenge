#!/bin/bash
set +x
echo -n "Preparing Lab environment... "
for i in `find . -type d`; do
	pushd $i >/dev/null
	find . -d 1 -name *tgz | xargs -I % tar -xzf %
	popd >/dev/null
done
echo "Done"