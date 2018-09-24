#!/bin/bash
export DEST="./.exvim.1"
export TOOLS="/Users/zhangzhu/.vim/tools/"
export IS_EXCLUDE=-not
export FOLDERS="__pycache__"
export FILE_SUFFIXS=".*"
export TMP="${DEST}/_files"
export TARGET="${DEST}/files"
export ID_TARGET="${DEST}/idutils-files"
bash ${TOOLS}/shell/bash/update-filelist.sh
