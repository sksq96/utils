root = Path("/storage/data/folder")
with open( root / 'filename.jsonl', 'r') as json_file:
    json_list = list(json_file)

json_list = [json.loads(json_str) for json_str in json_list]
df = pd.json_normalize(json_list)

df.head(2)
