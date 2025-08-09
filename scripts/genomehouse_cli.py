import argparse
from genomehouse import sequence_tools, genomic_parsers

def main():
    parser = argparse.ArgumentParser(description="GenomeHouse CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    fasta_parser = subparsers.add_parser("parse-fasta", help="Parse a FASTA file")
    fasta_parser.add_argument("file", help="Path to FASTA file")

    gc_parser = subparsers.add_parser("gc-content", help="Calculate GC content of a sequence")
    gc_parser.add_argument("sequence", help="DNA sequence")

    args = parser.parse_args()
    if args.command == "parse-fasta":
        for header, seq in genomic_parsers.parse_fasta(args.file):
            print(f">{header}\n{seq}")
    elif args.command == "gc-content":
        gc = sequence_tools.gc_content(args.sequence)
        print(f"GC content: {gc:.2f}%")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
