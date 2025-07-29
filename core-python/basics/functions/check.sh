#!/bin/bash

echo edit..
black $1
echo done

echo "compile start.."
python3.12 -m py_compile $1
echo "compiled"

echo "type test start.."
mypy $1
echo "done"

echo "script run.."
python3.12 $1
echo "\n+++DONE+++"
