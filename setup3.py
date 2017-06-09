from cx_Freeze import setup, Executable

build_options = {
                 'optimize':2,
                 'packages': ['peewee', 'src','ttk'],
                 }

common_exe_options = {
                      'script'             : 'gui.py',
                     }

executable = Executable(**common_exe_options)

setup(name='Invasodado',
      version='0.8',
      description='wowza!',
      options = {'build_exe': build_options,
                 'bdist_msi': build_options},
      executables=[executable])
