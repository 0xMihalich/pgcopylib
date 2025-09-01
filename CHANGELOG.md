# Version History

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
