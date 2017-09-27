# -*- mode: python -*-

block_cipher = None


a = Analysis(['Splitter.py'],
             pathex=['C:\\Users\\o.zaitsev\\Source\\Repos\\Image_Splitter'],
             binaries=[],
             datas=[],
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
          name='Splitter',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='F:\\MyPython\\Image_Splitter\\icon.ico')
