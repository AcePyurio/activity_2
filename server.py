from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
import mysql.connector

# Function to establish a database connection
def connect_to_database():
    return mysql.connector.connect(
        host="db",
        user="root",
        passwd="proot",
        database="restNoteDatabase"
    )

# Function to create the notes table if it doesn't exist
def create_notes_table():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()


class RequestHandler(BaseHTTPRequestHandler):
   
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

   
    def do_GET(self):
       
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        
 
        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()
        
    
        cursor.close()
        connection.close()

       
        self._set_headers()
        self.wfile.write(json.dumps(notes).encode('utf-8'))

    
    def do_POST(self):
        
        content_length = int(self.headers['Content-Length'])
        
      
        post_data = self.rfile.read(content_length)
        note = json.loads(post_data)

        
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (note['title'], note['content']))
        connection.commit()
        
       
        cursor.close()
        connection.close()

      
        self._set_headers(201)
        self.wfile.write(json.dumps({'message': 'created'}).encode('utf-8'))




def run(server_class=HTTPServer, handler_class=NoteHandler, port=8010):
    server_address = ('', port)
    
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {port}...")  
    httpd.serve_forever() 


if __name__ == '__main__':
    
    create_notes_table()
    

    run()