from glob import glob
from os.path import basename
from os.path import splitext
from setuptools import setup


def long_description():
  with open("README.md") as file_handle:
    readme_text = file_handle.read()
  return readme_text


setup(
    name="simple-file-checksum",
    version="1.3.1",
    description=
    "Returns the MD5, SHA1, SHA256, SHA384, or SHA512 checksum of a file.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/sashsinha/simple-file-checksum",
    author="Sash Sinha",
    author_email="sashsinha1@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.9",
    extras_require={"dev": ["pytest>=3.9", "pytest-cov", "tox==4.22.0"]},
    entry_points={"console_scripts": ["simple-file-checksum=cli:main"]},
)
