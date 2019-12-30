# -*- mode: python -*-

block_cipher = None


a = Analysis(['board_gui.py'],
             pathex=['C:\\Users\\Mr. Escobedo\\Desktop\\exp\\j_freeze'],
             binaries=[],
             datas=[("jeopardy.ico", ".")],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='board_gui',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='jeopardy.ico')
