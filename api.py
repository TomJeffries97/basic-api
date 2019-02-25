"""
@author: Thomas Jeffries
Email: TAJ16@ic.ac.uk
"""

import flask
import datetime
from flask import Flask, request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
now = datetime.datetime.now()


notes = [
	{'id': 1,
	 'title' : 'My first note',
	 'date' : now.strftime("%d-%m-%Y"),
	 'user' : "Tom",
	 'messages' : 'Hello world, this is my first note'}
]

archived_notes = []

@app.route('/', methods=['GET'])
def home():
    return "<h1>Note Taker</h1><p>This site is a prototype API taking notes and editing notes.</p>"

@app.route('/api/notes/all', methods=['GET'])
def api_all():
    return jsonify(notes)
	
@app.route('/api/notes', methods=['GET'])
def api_search():
    # create an empty list for the results
    results = []
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, check for a user and try again
    # if no search field provided, question it.

    if 'id' in request.args:
        id = int(request.args['id'])
        # Loop through the data and match results that fit the requested ID.
        # IDs are unique, but other fields might return many results
        for note in notes:
            if note['id'] == id:
                results.append(note)
    elif 'user' in request.args:
        user = (request.args['user'])
        for note in notes:
            if note['user'] == user:
                results.append(note)
    else:
        return "Error: No search field provided. Please specify an id."

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/notes', methods=['POST'])
def create_note():
    message = request.json['message']
    if not message:
        return "Error: No message given."
    id = notes[-1]['id'] + 1
    
    note = {'id': id, 
	'title': request.json['title'], 
	'date': now.strftime("%d-%m-%Y"), 
	'user': request.json['user'], 
	'message': request.json['message']}
    notes.append(note)
    return jsonify({'notes': notes}), 201

@app.route('/api/notes', methods=['DELETE'])
def delete_note():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
    return jsonify({'notes': notes}), 200

@app.route('/api/notes', methods=['PUT'])
def edit_note():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    for note in notes:
        if note['id'] == id:
            if request.json['message'] is not None:
                note['message'] = request.json['message']
                note['date'] = now.strftime("%d-%m-%Y")
    return jsonify(note),200
			
@app.route('/api/notes/archive', methods=['PUT'])
def archive_note():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    for note in notes:
        if note['id'] == id:
            archived_notes.append(note)
            notes.remove(note)
    return "note archived" , 200
	
@app.route('/api/notes/archive', methods=['GET'])
def get_archive():
    results = []
    if 'id' in request.args:
        id = int(request.args['id'])
        for note in archived_notes:
            if note['id'] == id:
                results.append(note)
        return jsonify(results)
    else:
        return jsonify(archived_notes)

	
app.run()
