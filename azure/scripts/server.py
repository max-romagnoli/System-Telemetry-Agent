from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import webbrowser

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Simulator</title>
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
            padding: 20px 40px; 
            font-size: 24px; 
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #1c2444; 
        }

        select {
            padding: 10px;
            font-size: 18px;
            border-radius: 8px;
            border: 1px solid #ccc;
            margin-bottom: 20px;
        }

        label {
            color: white;
            font-family: Arial, sans-serif;
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
            <img src="https://raw.githubusercontent.com/max-romagnoli/System-Telemetry-Agent/dev/docs/st-agent-logo.png" alt="Logo" id="logo"> 
        </div>
        <h1>System Simulation</h1>
        <label for="scriptSelect" style="color: white; font-family: Arial, sans-serif;">Select Simulation:</label>
        <select id="scriptSelect">
            <option value="simulate_workload.py">High Workload</option>
            <option value="simulate_instance_down.sh">Instance Down</option>
        </select>
        <br>
        <button id="actionButton">Start Simulation</button>
    </div>

    <script>
        let isRunning = false;
        const actionButton = document.getElementById("actionButton");
        const scriptSelect = document.getElementById("scriptSelect");

        actionButton.addEventListener("click", function() {
            fetch('/toggle-script?script=' + scriptSelect.value)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    isRunning = !isRunning;
                    actionButton.textContent = isRunning ? "Stop Simulation" : "Start Simulation";
                    actionButton.style.backgroundColor = isRunning ? "#ff4d4d" : "#29bcbd";
                    console.log(isRunning ? 'Simulation started' : 'Simulation stopped');
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
        elif self.path.startswith('/toggle-script?script='):
            script = self.path.split('=')[1]
            if running_process is None:
                if script == 'simulate_instance_down.sh':
                    running_process = subprocess.Popen(["sh", f"../../docker/{script}"])
                    print("Instance Down Simulation started with PID:", running_process.pid)
                else:
                    running_process = subprocess.Popen(["python3", script])
                    print("Workload Simulation started with PID:", running_process.pid)
            else:
                running_process.terminate()
                running_process.wait()
                print("Simulation stopped")
                running_process = None
            self.send_response(200)
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))
        else:
            self.send_error(404, 'Not Found')

with HTTPServer(('localhost', 5000), RequestHandler) as httpd:
    print("Server started at localhost:5000")
    httpd.serve_forever()
