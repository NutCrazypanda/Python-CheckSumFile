# Python program to find SHA256,MD5 hash string of a file
import hashlib

#SHA256_check
def sha256_check(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        print(f' SHA256 : {sha256_hash.hexdigest()}')

#MD5 check
def md5_check(filename):
    md5_hash = hashlib.md5()
    with open(filename, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
        print(f' MD5 : {md5_hash.hexdigest()}')

import sys, getopt

def main(argv):
    hash_mode = ''
    filename = ''
    try:
      opts, args = getopt.getopt(argv,"hm:f:",["hash=","file="])
    except getopt.GetoptError:
      print('python checksumfile.py -m <hash:ex md5, sha256> -f <filename>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('python checksumfile.py -m <hash:ex md5, sha256> -f <filename>')
         sys.exit()
      elif opt in ("-m", "--hash"):
         hash_mode = arg
      elif opt in ("-f", "--file"):
         filename = arg

    if hash_mode == "md5":
        md5_check(filename)
    if hash_mode == "sha256":
        sha256_check(filename)


if __name__ == "__main__":
    main(sys.argv[1:])


#python -m PyInstaller --name "checksumfile" "checksumfile.py" --onefile