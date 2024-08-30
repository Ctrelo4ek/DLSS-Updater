# -*- mode: python ; coding: utf-8 -*-

import pefile
import psutil
import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

block_cipher = None

dlss_updater_imports = collect_submodules('dlss_updater')
dlss_updater_datas = collect_data_files('dlss_updater')

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('latest_dll/nvngx_dlss.dll', 'latest_dll'),
        ('dlss_updater', 'dlss_updater'),
        ('release_notes.txt', '.')
    ],
    hiddenimports=[
        'pefile', 'psutil', 'importlib.metadata', 'packaging', 'importlib_metadata'
    ] + dlss_updater_imports,
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='DLSS_Updater',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='DLSS_Updater',
)