import os
import platform
import subprocess

SUPPORTED_ALGORITHMS = frozenset({"MD5", "SHA1", "SHA256", "SHA384", "SHA512"})
SUPPORTED_OPERATING_SYSTEMS = frozenset({"Darwin", "Linux", "Windows"})


def get_checksum(file, algorithm="MD5"):

  def checksum(algorithm):
    if operating_system == "Windows":
      certutil_process = subprocess.run(
          ["CertUtil", "-hashfile", file, algorithm],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          universal_newlines=True,
      )
      return certutil_process.stdout.split("\n")[1]
    checksum_process = subprocess.run(
        ["openssl", "dgst", f"-{algorithm}", file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    return checksum_process.stdout.split()[-1]

  algorithm = algorithm.upper()
  if algorithm not in SUPPORTED_ALGORITHMS:
    return f"Error: {algorithm} is not a supported algorithm"

  operating_system = platform.system()
  if operating_system not in SUPPORTED_OPERATING_SYSTEMS:
    return f"Error: {operating_system} is not a supported operating system"

  if not os.path.isfile(file):
    return f"Error: {file} is not a valid file"

  return checksum(algorithm)
