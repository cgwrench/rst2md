# [rst2md][]

## Overview

[rst2md][] is a custom writer for Python's [Docutils][] document processing 
system which converts [reStructuredText][] documents to [Markdown][].

**Note**: This project is still in early development. See the file TODO for the
immediate roadmap.

## License

[rst2md][] is released under the permissive [BSD 2-Clause License][], see the 
file LICENSE for the license text.

## Installation

Currently there is not an installation script. The most straightforward way to 
get rst2md.py working is to:

  - ensure that [Docutils][] is installed,
  
  - copy, move or link the file *markdown.py*, located in the repository
    root directory, to *docutils/writiers/* in the standard Docutils package
	and the file *rst2md.py*, located under *tools/*, to anywhere on your PATH 
	(or PYTHONPATH).

## Contributing

Comments and enhancements are very welcome.

Report any issues or feature requests on the [GitHub bug 
tracker](https://github.com/cgwrench/rst2md/issues). Please include a minimal 
(not-) working example which reproduces the bug and, if appropriate, the 
Docutils traceback information (obtained by running `rst2md.py` with the 
`--traceback` option). Please do not request features already being worked 
towards (see the TODO file).

Code contributions are encouraged: please feel free to [fork the
project](https://github.com/cgwrench/rst2md/fork) and submit pull requests.

## More information

- [reStructuredText markup syntax][reStructuredText]
- [Markdown syntax][Markdown]
- [Docutils project homepage][Docutils] and [documentation](http://docutils.sourceforge.net/docs/index.html).

<!-- References: -->

[rst2md]: https://github.com/cgwrench/rst2md "rst2md GitHub page."

[BSD 2-Clause License]: http://opensource.org/licenses/bsd-license.php 
    "BSD 2-Clause License text."
	
[Docutils]: http://docutils.sourceforge.net/ "The Docutils project homepage."
	
[reStructuredText]: http://docutils.sourceforge.net/rst.html
    "ReStructuredText markup syntax homepage."

[Markdown]: http://daringfireball.net/projects/markdown/ 
    "The Markdown project homepage."
	
