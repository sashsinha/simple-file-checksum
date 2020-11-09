import platform
from simple_file_checksum import get_checksum
from unittest import mock


def test_get_checksum_invalid_file_path_returns_error_message():
    assert (
        get_checksum("invalid/path/to/file") ==
        "Error: invalid/path/to/file is not a valid file"
    )


def test_get_checksum_valid_file_path_invalid_algorithm_returns_error_message():
    assert (
        get_checksum("tst/file.txt", algorithm="SHA224") ==
        "Error: SHA224 is not a supported algorithm"
    )


def test_get_checksum_unsupported_operating_system_returns_error_message():
    with mock.patch("platform.system", mock.MagicMock(return_value="Java")):
        assert (
            get_checksum("tst/file.txt") ==
            "Error: Java is not a supported operating system"
        )


def test_get_checksum_valid_file_path_returns_md5_checksum_by_default():
    assert (get_checksum("tst/file.txt") == "9e107d9d372bb6826bd81d3542a419d6")


def test_get_checksum_valid_file_path_returns_sha1_checksum_when_specified():
    assert (
        get_checksum("tst/file.txt", algorithm="SHA1") ==
        "2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"
    )


def test_get_checksum_valid_file_path_returns_sha256_checksum_when_specified():
    assert (
        get_checksum("tst/file.txt", algorithm="SHA256") ==
        "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"
    )


def test_get_checksum_valid_file_path_returns_sha384_checksum_when_specified():
    assert (
        get_checksum("tst/file.txt", algorithm="SHA384") ==
        "ca737f1014a48f4c0b6dd43cb177b0afd9e5169367544c494011e3317dbf9a509cb1e5dc1e85a941bbee3d7f2afbc9b1"
    )


def test_get_checksum_valid_file_path_returns_sha512_checksum_when_specified():
    assert (
        get_checksum("tst/file.txt", algorithm="SHA512") ==
        "07e547d9586f6a73f73fbac0435ed76951218fb7d0c8d788a309d785436bbb642e93a252a954f23912547d1e8a3b5ed6e1bfd7097821233fa0538f3db854fee6"
    )
