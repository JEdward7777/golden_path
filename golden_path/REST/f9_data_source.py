import f7_AI_components.f9_Translation_sources.Data1.f10_Data_Abstraction_Tokenizer.abstractor as abs1
import f7_AI_components.f9_Translation_sources.Data2.f10_Data_Abstraction_Tokenizer.abstractor as abs2
import f7_AI_components.f9_Translation_sources.Data3.f10_Data_Abstraction_Tokenizer.abstractor as abs3

abs = [abs1,abs2,abs3]

from flask import Flask, jsonify, request, send_from_directory
import sys

app = Flask(__name__)

#this allows each of the datasources to be selected.
selected_data_source = [1]

@app.route("/")
def index():
  #return f"f9_data_source {selected_data_source[0]} running"
  return send_from_directory( '.', 'index.html' )


@app.route("/get_tokenized_verse" )
def getVerse_tokenized():
    reference = request.args.get('ref')

    try:
        result = abs[selected_data_source[0]-1].getVerse_tokenized( reference )
    except KeyError:
        result = { "error":"Not found", "ref":reference }

    return jsonify(result)

@app.route("/get_verse_references" )
def getVerseReferences():
    references = abs[selected_data_source[0]-1].getVerseReferences()
    return jsonify(references)

def run( data_source_n=1 ):
    selected_data_source[0] = int(data_source_n)
    app.run( host="0.0.0.0" )