from ..core import Command as Command
from ..errors import DistutilsExecError as DistutilsExecError
from ..sysconfig import customize_compiler as customize_compiler
from _typeshed import Incomplete

LANG_EXT: Incomplete

class config(Command):
    description: str
    user_options: Incomplete
    compiler: Incomplete
    cc: Incomplete
    include_dirs: Incomplete
    libraries: Incomplete
    library_dirs: Incomplete
    noisy: int
    dump_source: int
    temp_files: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def try_cpp(self, body: Incomplete | None = None, headers: Incomplete | None = None, include_dirs: Incomplete | None = None, lang: str = 'c'):
        """Construct a source file from 'body' (a string containing lines
        of C/C++ code) and 'headers' (a list of header files to include)
        and run it through the preprocessor.  Return true if the
        preprocessor succeeded, false if there were any errors.
        ('body' probably isn't of much use, but what the heck.)
        """
    def search_cpp(self, pattern, body: Incomplete | None = None, headers: Incomplete | None = None, include_dirs: Incomplete | None = None, lang: str = 'c'):
        """Construct a source file (just like 'try_cpp()'), run it through
        the preprocessor, and return true if any line of the output matches
        'pattern'.  'pattern' should either be a compiled regex object or a
        string containing a regex.  If both 'body' and 'headers' are None,
        preprocesses an empty file -- which can be useful to determine the
        symbols the preprocessor and compiler set by default.
        """
    def try_compile(self, body, headers: Incomplete | None = None, include_dirs: Incomplete | None = None, lang: str = 'c'):
        """Try to compile a source file built from 'body' and 'headers'.
        Return true on success, false otherwise.
        """
    def try_link(self, body, headers: Incomplete | None = None, include_dirs: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, lang: str = 'c'):
        """Try to compile and link a source file, built from 'body' and
        'headers', to executable form.  Return true on success, false
        otherwise.
        """
    def try_run(self, body, headers: Incomplete | None = None, include_dirs: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, lang: str = 'c'):
        """Try to compile, link to an executable, and run a program
        built from 'body' and 'headers'.  Return true on success, false
        otherwise.
        """
    def check_func(self, func, headers: Incomplete | None = None, include_dirs: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, decl: int = 0, call: int = 0):
        '''Determine if function \'func\' is available by constructing a
        source file that refers to \'func\', and compiles and links it.
        If everything succeeds, returns true; otherwise returns false.

        The constructed source file starts out by including the header
        files listed in \'headers\'.  If \'decl\' is true, it then declares
        \'func\' (as "int func()"); you probably shouldn\'t supply \'headers\'
        and set \'decl\' true in the same call, or you might get errors about
        a conflicting declarations for \'func\'.  Finally, the constructed
        \'main()\' function either references \'func\' or (if \'call\' is true)
        calls it.  \'libraries\' and \'library_dirs\' are used when
        linking.
        '''
    def check_lib(self, library, library_dirs: Incomplete | None = None, headers: Incomplete | None = None, include_dirs: Incomplete | None = None, other_libraries=[]):
        """Determine if 'library' is available to be linked against,
        without actually checking that any particular symbols are provided
        by it.  'headers' will be used in constructing the source file to
        be compiled, but the only effect of this is to check if all the
        header files listed are available.  Any libraries listed in
        'other_libraries' will be included in the link, in case 'library'
        has symbols that depend on other libraries.
        """
    def check_header(self, header, include_dirs: Incomplete | None = None, library_dirs: Incomplete | None = None, lang: str = 'c'):
        """Determine if the system header file named by 'header_file'
        exists and can be found by the preprocessor; return true if so,
        false otherwise.
        """

def dump_file(filename, head: Incomplete | None = None) -> None:
    """Dumps a file content into log.info.

    If head is not None, will be dumped before the file content.
    """
