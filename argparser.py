import argparse

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument("--model_dir", type=str, required=True)
parser.add_argument("--code_before", type=str, required=True)
parser.add_argument("--depth", type=int, default=10)
parser.add_argument("--breadth", type=int, default=10)
parser.add_argument("--min_tokens", type=int, default=2)
parser.add_argument("--language", type=str, required=True)
parser.add_argument('--train', action="store_true", default=False)
args = parser.parse_args()
