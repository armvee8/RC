import argparse
import subprocess
import sys 
from encoder import encode_sentence, encode_ascii_tags, generate_bytes 
def main(): 
    parser = argparse.ArgumentParser(description = "Lightweight CLI tool to convert a string to invisible unicode, or to generate a certain amount of bytes in invisible unicode.")

    
    subparsers = parser.add_subparsers(dest="command",required=True)

    #adds sub-command encode
    encode_parser = subparsers.add_parser("encode")
    encode_parser.add_argument("sentence", type=str)

    #adds sub-command ascii-tags
    ascii_tags_parser = subparsers.add_parser("encode-ascii-tags")
    ascii_tags_parser.add_argument("sentence", type=str) 
    #adds sub-command generate
    generate_parser = subparsers.add_parser("generate")
    generate_parser.add_argument("byte_amount", type=int)

    args = parser.parse_args()
    
    if args.command == "encode":
        result = encode_sentence(args.sentence)
    # check for printable ascii range in here as well to fix traceback error 
    elif args.command == "encode-ascii-tags":
        try: 
            result = encode_ascii_tags(args.sentence)
        except ValueError as error: 
            parser.error(str(error))

    elif args.command == "generate":
        if args.byte_amount <= 0:
            parser.error('Amount of bytes must be positive.')

        result = generate_bytes(args.byte_amount)
        sys.stdout.write(result) 
    sys.stdout.write(result) #print() adds a newline so we use sys.stdout
    clipboard_copy(result)
    print("Invisible unicode is copied to your clipboard. You can also copy it from the line immediately returned.", file=sys.stderr)
def clipboard_copy(result):
    subprocess.run(["pbcopy"], input=result,text=True,encoding="utf-8",check=True) 
if __name__ == "__main__":
    main() 
