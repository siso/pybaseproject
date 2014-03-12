#!/usr/bin/env sh

export PYTHONPATH=$(dirname $0)/..:$PYTHONPATH
python -m pybaseproject.__main__
