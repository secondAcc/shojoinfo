# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['shojo.py'],
    pathex=['D:\\shojoinfo\\shojo\\source'],
    binaries=[],
    datas=[('./resources','./resources'),
            ('./subprograms','./programs'),
            ('./uifiles','./uifiles')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
    cipher=block_cipher)
exe = EXE(pyz,
 a.scripts,
 exclude_binaries=True,
 name='run',
 debug=False,
 strip=False,
 upx=True,
 console=False )
coll = COLLECT(exe,
      a.binaries,
      a.zipfiles,
      a.datas,
      strip=False,
      upx=True,
      name='run')