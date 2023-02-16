import sys
import argparse
from glob import glob
from pathlib import Path

if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Convert BRUK individual files into the combined file (one para per line)"
    )

    parser.add_argument("infiles", help="Input glob-like mask to pick the files", default="corpus/data/good/*.txt")
    parser.add_argument(
        "outfile", nargs="?", type=argparse.FileType("w"), default=sys.stdout, help="Output file to combined corpus"
    )

    args: argparse.Namespace = parser.parse_args()

    for p in map(Path, glob(args.infiles)):
        with p.open("r") as fp_in:
            for l in map(str.strip, fp_in):
                if l:
                    l = l.replace("\t", " ").replace("ʘ", "о")
                    args.outfile.write(f"{l}\n")
