#!/bin/bash
export DEST="./.exvim.1"
export TOOLS="/Users/zhangzhu/.vim/tools/"
export TMP="${DEST}/_symbols"
export TARGET="${DEST}/symbols"
sh ${TOOLS}/shell/bash/update-symbols.sh
