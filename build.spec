# -*- mode: python ; coding: utf-8 -*-

import os
os.environ['QT_DEBUG_PLUGINS'] = '1'

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[('voice.ico', 'voice.ico')],
    hiddenimports=[
        'sip',
        'pydoc',
        'nltk',
        'nltk.collocations',
        'nltk.metrics',
        'nltk.util',
        'transformers',
        'language_tool_python',
        'jieba',
        'docx',
        'speech_recognition',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'nltk.corpus.reader',  # 添加其他 nltk 模块
        'nltk.corpus.util',
        'nltk.data',
        'nltk.tokenize',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['pydoc'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
