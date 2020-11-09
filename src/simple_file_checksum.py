import os
import platform
import re
import subprocess

SUPPORTED_ALGORITHMS = {"MD5", "SHA1", "SHA256", "SHA384", "SHA512"}
SUPPORTED_OPERATING_SYSTEMS = {"Darwin", "Linux", "Windows"}


def get_checksum(file, algorithm="MD5"):
    def get_md5(operating_system):
        if operating_system == "Darwin":
            md5_checksum_process = subprocess.run(
                ["md5", "-q", file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            return md5_checksum_process.stdout.strip()
        elif operating_system == "Linux":
            md5sum_checksum_process = subprocess.run(
                ["md5sum", file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            return md5sum_checksum_process.stdout.split()[0]
        else:
            certutil_process = subprocess.run(
                ["CertUtil", "-hashfile", file, "MD5"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            return certutil_process.stdout.split("\n")[1]

    def get_sha_checksum(algorithm):
        if operating_system == "Darwin" or operating_system == "Linux":
            variant = re.search(r"\d+", algorithm).group()
            shasum_checksum_process = subprocess.run(
                ["shasum", "-a", variant, file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            return shasum_checksum_process.stdout.split()[0]
        else:
            certutil_process = subprocess.run(
                ["CertUtil", "-hashfile", file, algorithm],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            return certutil_process.stdout.split("\n")[1]

    algorithm = algorithm.upper()
    if algorithm not in SUPPORTED_ALGORITHMS:
        return f"Error: {algorithm} is not a supported algorithm"

    operating_system = platform.system()
    if operating_system not in SUPPORTED_OPERATING_SYSTEMS:
        return f"Error: {operating_system} is not a supported operating system"

    if not os.path.isfile(file):
        return f"Error: {file} is not a valid file"

    if algorithm == "MD5":
        return get_md5(operating_system)
    return get_sha_checksum(algorithm)
