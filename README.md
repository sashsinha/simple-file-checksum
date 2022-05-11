<p align="center">
<a href="https://github.com/sashsinha/simple-file-checksum"><img alt="Simple File Checksum Logo" src="https://raw.githubusercontent.com/sashsinha/simple-file-checksum/main/logo.png"></a>
</p>

<h1 align="center">Simple File Checksum</h1>

<h3 align="center">Returns the MD5, SHA1, SHA256, SHA384, or SHA512 checksum of a file</h3>

<br/>

<p align="center">
<a href="https://github.com/sashsinha/simple-file-checksum/actions?query=workflow%3Atests"><img alt="Tests Badge" src="https://github.com/sashsinha/simple-file-checksum/workflows/tests/badge.svg"></a>
<a href="https://raw.githubusercontent.com/sashsinha/simple-file-checksum/main/LICENCE"><img alt="License: MIT" src="https://raw.githubusercontent.com/sashsinha/simple-file-checksum/main/license.svg"></a>
<a href="https://pypi.org/project/simple-file-checksum/"><img src="https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey" alt="Supported Platforms"></a>
<a href="https://pypi.org/project/simple-file-checksum/"><img 
alt="PyPI Supported Versions" src="https://img.shields.io/pypi/pyversions/simple-file-checksum.svg"></a>
<a href="https://pypi.org/project/simple-file-checksum/"><img alt="PyPI" src="https://img.shields.io/pypi/v/simple-file-checksum"></a>
<a href="https://pypi.org/project/simple-file-checksum/"><img alt="PyPI Status" src="https://img.shields.io/pypi/status/simple-file-checksum"></a>
<a href="https://pepy.tech/project/simple-file-checksum"><img alt="Downloads" src="https://pepy.tech/badge/simple-file-checksum"></a>

</p>

## Installation

Run the following to install:

```python
pip3 install simple-file-checksum
```

## Usage

### Python:

```python
>>> from simple_file_checksum import get_checksum
>>> get_checksum("tst/file.txt")
'9e107d9d372bb6826bd81d3542a419d6'
>>> get_checksum("tst/file.txt", algorithm="MD5")
'9e107d9d372bb6826bd81d3542a419d6'
>>> get_checksum("tst/file.txt", algorithm="SHA1")
'2fd4e1c67a2d28fced849ee1bb76e7391b93eb12'
>>> get_checksum("tst/file.txt", algorithm="SHA256")
'd7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592'
>>> get_checksum("tst/file.txt", algorithm="SHA384")
'ca737f1014a48f4c0b6dd43cb177b0afd9e5169367544c494011e3317dbf9a509cb1e5dc1e85a941bbee3d7f2afbc9b1'
>>> get_checksum("tst/file.txt", algorithm="SHA512")
'07e547d9586f6a73f73fbac0435ed76951218fb7d0c8d788a309d785436bbb642e93a252a954f23912547d1e8a3b5ed6e1bfd7097821233fa0538f3db854fee6'
```

### Terminal:

```bash
$ simple-file-checksum tst/file.txt
9e107d9d372bb6826bd81d3542a419d6
$ simple-file-checksum tst/file.txt -a MD5
9e107d9d372bb6826bd81d3542a419d6
$ simple-file-checksum tst/file.txt -a SHA1
2fd4e1c67a2d28fced849ee1bb76e7391b93eb12
$ simple-file-checksum tst/file.txt -a SHA256
d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592
$ simple-file-checksum tst/file.txt -a SHA384
ca737f1014a48f4c0b6dd43cb177b0afd9e5169367544c494011e3317dbf9a509cb1e5dc1e85a941bbee3d7f2afbc9b1
$ simple-file-checksum tst/file.txt -a SHA512
07e547d9586f6a73f73fbac0435ed76951218fb7d0c8d788a309d785436bbb642e93a252a954f23912547d1e8a3b5ed6e1bfd7097821233fa0538f3db854fee6
```

## Developing

To install `simple-file-checksum`, along with the tools you need to develop and run tests, run the following:

```bash
pip3 install -e ".[dev]"
```
