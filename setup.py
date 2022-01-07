from cx_Freeze import setup, Executable

build_exe_options = {"excludes": ["tkinter", "PyQt4.QtSql", "sqlite3", 
                                  "scipy.lib.lapack.flapack",
                                  "PyQt4.QtNetwork",
                                  "PyQt4.QtScript",
                                  "numpy.core._dotblas", 
                                  "PyQt5", "numpy"],
                     "include_files": ["ev_scripts.json", "ev.g4"],
                     "optimize": 2}

setup(
        name = "ev-as",
        version = "1.0",
        options = {"build_exe": build_exe_options},
        description = "Pre-Compiled version of ev-as",
        executables = [Executable("src/ev_parse.py"), Executable("src/ev_as.py")])