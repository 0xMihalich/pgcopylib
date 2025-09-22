# Version History

## 0.2.0.1

* Setup.py code refactor
* Some fixes
* Cast Py_ssize_t data types to Cython data types

## 0.2.0.0

* Full refactor project
* Rewrite code to Cython for more performance
* Change PGCopy to PGCopyReader
* Speed up converter functions
* PGCopyReader now have only read_row generator to read one row and to_rows generator to read all rows
* PGCopyWriter now have methods write_row, from_rows, write and tell. fileobj now is optional.

## 0.1.3

* Rename PGCopyWriter.close() method to PGCopyWriter.finalize()
* Add PGCopyWriter.tell() method

## 0.1.2

* Add size parameter to PGCopy.read() method

## 0.1.1

* Fix read functions
* Add initialize PGCopyWriter from PGCopy object with method writer()

## 0.1.0

* Refactor over 60% code
* Remove self.columns
* Rename self.dtypes to self.pgtypes
* Change self.pgtypes object from PGDataType to PGOid
* Change self.__str__ & self.__repr__ output
* Add write functions
* Add class PGCopyWriter
* Add PGCopy.write method for initialize PGCopyWriter from PGCopy
* Add CHANGELOG.md

## 0.0.3

* Rename project to pgcopylib
* Refactor geometric types move from digits.py to geometrics.py
* Fix README.md
* Remove check -1 value in end of file for optimize PGCopy class initialization
* Publish library to Pip

## 0.0.2

* Add data type parsers
* Add geometric types
* Improve docs
* Rename Colums to Columns

## 0.0.1

First version of the library pgcopy_parser
