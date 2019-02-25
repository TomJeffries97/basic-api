# basic-api
A simple api used as a note taker. It has the capability to save, edit and delete notes, as well as searching the list of notes for an individual note. It also has the capability to archive a note.

## Usage

All responses will have form:
'''json
{
	"property": "Mixed type holding the content of the response",
	"message": "Description of the note"
}

Subsequent response definitions will only detail the expected value od the 'data field'

### List of all notes

*Definitions*

'GET api/notes/all'

*Response*

-'200 OK' on success

'''json
[
	{
		"identifier": "FirstNote",
		"title" : "My first note",
		"date" : "18.02.2019",
		"time" : "18:49",
		"content" : "Hello world, this is my first note",
	}
]
'''

### Save new note

'POST /notes'

*Arguments*

- '"id":int' globally unique identifier to search for the note, determined by the program
- '"title":string' more common name for the note
- '"date":string' The date the note was created, or updated, determined by the program
- '"mesasage":string' The main body of the note, containing the message meant for the reader

*Response"

- '201 Created' on success

'''json
{		
	"identifier": "FirstNote",
	"title" : "My first note",
	"date" : "18.02.2019",
	"time" : "18:49",
	"content" : "Hello world, this is my first note",
}
'''

## Look up notes

'GET api/notes?id=<id number>'
 or 'Get api/notes?user=<user name>'

*Response*

- '404 Not Found' if the note doesn't exist
- '200 OK' on success

''' json
{		
	"identifier": "FirstNote",
	"title" : "My first note",
	"date" : "18.02.2019",
	"time" : "18:49",
	"content" : "Hello world, this is my first note",
}
'''

## Delete Note

'DELETE api/notes?id=<id number>'

*Response*

-'404 Not Found' if the note doesn't exist
-'200 OK' on success

## Edit Note

'PUT api/notes?id=<id number>
 
 *argument*
 
 {"messagee": "new message to save in the note"}
 
 *response* 
 
 - '200 OK' on success
 - "Error: No id field provided. Please specify an id"
 
 ## Archive Note
 
 'PUT api/notes?id=<id number>
  
 *response* 
 
 - "note archived" '200 OK' on success
 - "Error: No id field provided. Please specify an id"
 
 ## View Archived Notes 
 
 'GET api/notes/archive'
 
 *response* 
 
 - '200 Ok' on success
 
 displays all archived notes in the json format as before.
