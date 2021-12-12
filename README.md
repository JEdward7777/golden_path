# golden_path
This is a framework that allows machine translation solutions to be tested against each other with pluggable language sources.

For a more indepth description please view the [write up](./Golden_Path_Application_Framework.pdf) and the [block diagram](./block_diagram.pdf).


## Running F9_data_source
The datasources identified with id 9 in the [block diagram](./block_diagram.pdf) can be accessed with a REST api.  To run it locally on your computer execute the following commands:

### Clone the repo
```bash
git clone --recurse-submodules https://github.com/JEdward7777/golden_path
cd golden_path/golden_path

```

### create venv
```bash
python -m venv venv
source ./venv/bin/activate
```

### install requirements
```bash
pip install -r ./requirements.txt
```

### run F9_data_source
```bash
#1 for hebrew, 2 for greek and 3 for german
python runner.py --f9 1
```

### Fetch data using rest api
> List all verses:
> http://localhost:5000/get_verse_references

> Fetch tokenized verse
> http://localhost:5000/get_tokenized_verse?ref=John3:16

