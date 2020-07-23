from __future__ import absolute_import, print_function
import os
from pathlib import Path
from . import io

def _extract_mls(model, **kwargs):
    if model.__module__.startswith("sklearn"):
        from . import sklearn
        return sklearn.to_mls(model, **kwargs)
    else:
        raise ValueError("Unsupported library")


def export_to_file(model, filename, **kwargs):
    mls = _extract_mls(model, **kwargs)
    with open(filename, 'w') as f:
        f.write(mls)


def export(model, force=False, **kwargs):
    mls = _extract_mls(model)
    io.log_renku_mls(mls, str(model.__hash__()), force)
