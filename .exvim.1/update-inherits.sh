#!/bin/bash
export DEST="./.exvim.1"
export TOOLS="/Users/zhangzhu/.vim/tools/"
export TMP="${DEST}/_inherits"
export TARGET="${DEST}/inherits"
sh ${TOOLS}/shell/bash/update-inherits.sh
