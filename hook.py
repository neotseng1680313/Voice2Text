# hook-pydoc.py
from PyInstaller.utils.hooks import collect_submodules

# Collect all submodules from the 'pydoc' module.
hiddenimports = collect_submodules('pydoc')
