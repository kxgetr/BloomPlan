import argparse
import json
import sys
from pathlib import Path

def analyze(data):
    import math
    n, p = (data['items'], data['probability'])
    if n <= 0 or not 0 < p < 1:
        raise ValueError('invalid target')
    m = math.ceil(-n * math.log(p) / math.log(2) ** 2)
    return dict(bits=m, hashes=max(1, round(m / n * math.log(2))))

def main():
    parser = argparse.ArgumentParser(description='Hedef yanlış pozitif olasılığına göre Bloom filtre boyutu ve hash sayısı önerir.')
    parser.add_argument('file', nargs='?', help='UTF-8 JSON input file (default: stdin)')
    args = parser.parse_args()
    try:
        raw = Path(args.file).read_text(encoding='utf-8-sig') if args.file else sys.stdin.read()
        result = analyze(json.loads(raw))
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (SyntaxError, ValueError, KeyError, TypeError, OSError, IndexError, ArithmeticError) as error:
        parser.exit(2, f'Invalid input: {error}\n')
if __name__ == '__main__':
    main()
