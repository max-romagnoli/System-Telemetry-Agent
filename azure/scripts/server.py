from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import webbrowser

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Start/Stop Script</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #040404; 
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
        }

        h1 {
            color: white;
            margin-bottom: 20px;
        }

        button {
            background-color: #29bcbd;
            color: white;
            padding: 15px 30px; 
            font-size: 18px; 
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #1c2444; 
        }

        #logo-container {
            margin-bottom: 30px; 
        }

        #logo {
            width: 400px; 
        }
    </style>
</head>
<body>
    <div class="container">
        <div id="logo-container">
            <img src="/docs/st-agent-logo.png" alt="Logo" id="logo"> 
        </div>
        <h1>Start/Stop Script</h1>
        <button id="startButton">Start Script</button>
        <button id="stopButton">Stop Script</button>
    </div>

    <script>
        document.getElementById("startButton").addEventListener("click", function() {
            fetch('/start-script')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    console.log('Script started');
                })
                .catch(error => console.error('There was a problem with the fetch operation:', error));
        });

        document.getElementById("stopButton").addEventListener("click", function() {
            fetch('/stop-script')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    console.log('Script stopped');
                })
                .catch(error => console.error('There was a problem with the fetch operation:', error));
        });
    </script>
</body>
</html>
"""
running_process = None

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global running_process
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
        elif self.path == '/start-script':
            if running_process is None:
                running_process = subprocess.Popen(["python3", "simulate_workload.py"])
                print("Script started with PID:", running_process.pid)
                self.send_response(200)
                self.end_headers()
                self.wfile.write("OK".encode('utf-8'))
            else:
                self.send_error(400, 'Script is already running')
        elif self.path == '/stop-script':
            if running_process is not None:
                running_process.terminate()
                running_process = None
                print("Script stopped")
                self.send_response(200)
                self.end_headers()
                self.wfile.write("OK".encode('utf-8'))
            else:
                self.send_error(400, 'No script is running')
        elif self.path == '/docs/st-agent-logo.png':
            with open('/home/leila/System-Telemetry-Agent/docs/st-agent-logo.png', 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', 'image/png')
                self.end_headers()
                self.wfile.write(f.read())
        else:
            self.send_error(404, 'Not Found')

with HTTPServer(('localhost', 5000), RequestHandler) as httpd:
    print("Server started at localhost:5000")
    webbrowser.open('http://localhost:5000')
    httpd.serve_forever()
