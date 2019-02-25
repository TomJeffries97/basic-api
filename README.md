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

'GET /api/notes/all'

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

*Response*

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

### Look up notes

'GET /api/notes?id=<id number>'
 or 'Get /api/notes?user=<user name>'

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

### Delete Note

'DELETE /api/notes?id=<id number>'

*Response*

-'404 Not Found' if the note doesn't exist
-'200 OK' on success

### Edit Note

'PUT /api/notes?id=<id number>
 
 *argument*
 
 {"messagee": "new message to save in the note"}
 
 *response* 
 
 - '200 OK' on success
 - "Error: No id field provided. Please specify an id"
 
 ### Archive Note
 
 'PUT /api/notes?id=<id number>
  
 *response* 
 
 - "note archived" '200 OK' on success
 - "Error: No id field provided. Please specify an id"
 
 ### View Archived Notes 
 
 'GET /api/notes/archive'
 
 *response* 
 
 - '200 Ok' on success
 
 displays all archived notes in the json format as before.


## Discussion on code

I used the code by running the file through a command prompt, and then sending requests via postman.
The code was run through the usual IP address 127.0.0.1:5000.

I decided to create the api using python, as it was the language I was most comfortable using. Therefore this dictated what I could use to implement the api. As this was my first attempt at creating an api, and I had no previous experience creating one, I googled what modules would be useful. I decide on using the webfram Flask, as it is a simple microframe for beginners, which would suit me and the project I was completing.
There are a few decision that I have made throughout my code, which are a personal choice, and could be changed to match the way the designer would like the program to run. For example, when deleting a note, the list of saved notes is returned to the user, to prove the note was deleted. 
I also decided to take the ability to set the id and date of the note away from the user. I did this so that the user could not accidentally write over a saved note, and so that the date would always be correct. The date also updates, when the note is editted. This however does come with its drawbacks. When a note is deleted, that id is left available, however the program just incements the id, meaning that there will be continuously free ids, a problem I would eliminate with more time to work on the project.
If I were to spend more time on the project, beside the previously mentioned problem, I would also implement a database for the notes. Currenty all data is lost upon closing the file, however by integrating a database to the web application, all inputted data would be saved and later retrieved. I would also like to improve the method on posting data to the api. Currently it is quite slow and not user friendly to have to send the data through the body of the request using the api testing application. It would be better to input the data on the website, however this would take a lot of research for me to implement.
