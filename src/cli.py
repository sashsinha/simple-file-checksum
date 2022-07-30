import argparse
import sys

from simple_file_checksum import get_checksum


def main():
  parser = argparse.ArgumentParser(description="returns the checksum of a file")
  parser.add_argument("file",
                      type=str,
                      help="path to the file you want the checksum of")
  parser.add_argument(
      "-a",
      "--algorithm",
      default="MD5",
      type=str.upper,
      help=
      "checksum algorithm, one of MD5 (default), SHA1, SHA256, SHA384 or SHA512",
  )
  parser.add_argument("-v",
                      "--version",
                      action="version",
                      version="simple_file_checksum 1.2.2")
  args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])
  print(get_checksum(args.file, args.algorithm))


if __name__ == "__main__":
  main()
