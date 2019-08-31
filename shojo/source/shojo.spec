# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['shojo.py'],
             pathex=['D:\\python\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'D:\\shojoinfo\\shojo\\source'],
             binaries=[],
             datas=[],
             hiddenimports=[r'D:\python\Lib\venv\scripts\posix'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='shojo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
