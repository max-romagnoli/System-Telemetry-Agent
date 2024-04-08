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
        <button id="actionButton">Start Simulation</button>
    </div>

    <script>
        let isRunning = false;
        const actionButton = document.getElementById("actionButton");

        actionButton.addEventListener("click", function() {
            fetch('/toggle-simulation')
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
        elif self.path == '/toggle-simulation':
            if running_process is None:
                simulate_workload_process = subprocess.Popen(["python3", "simulate_workload.py"])
                simulate_instance_down_process = subprocess.Popen(["sh", "../../docker/simulate_instance_down.sh"])
                print("Workload Simulation started with PID:", simulate_workload_process.pid)
                print("Instance Down Simulation started with PID:", simulate_instance_down_process.pid)
                running_process = (simulate_workload_process, simulate_instance_down_process)
            else:
                for process in running_process:
                    process.terminate()
                    process.wait()
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
