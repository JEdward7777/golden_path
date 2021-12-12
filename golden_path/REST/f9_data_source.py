import f7_AI_components.f9_Translation_sources.Data1.f10_Data_Abstraction_Tokenizer.abstractor as abs
from flask import Flask, jsonify, request
import sys

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello, World!"


@app.route("/get_tokenized_verse" )
def getVerse_tokenized():
    reference = request.args.get('ref')

    try:
        result = abs.getVerse_tokenized( reference )
    except KeyError:
        result = { "error":"Not found", "ref":reference }

    return jsonify(result)

@app.route("/get_verse_references" )
def getVerseReferences():
    references = abs.getVerseReferences()
    return jsonify(references)

def run():
    app.run()