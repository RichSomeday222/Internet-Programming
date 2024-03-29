from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote_plus


def get_body_params(body):
    if not body:
        return {}
    parameters = body.split("&")

    # split each parameter into a (key, value) pair, and escape both
    def split_parameter(parameter):
        k, v = parameter.split("=", 1)
        k_escaped = unquote_plus(k)
        v_escaped = unquote_plus(v)
        return k_escaped, v_escaped

    body_dict = dict(map(split_parameter, parameters))
    print(f"Parsed parameters as: {body_dict}")
    # return a dictionary of the parameters
    return body_dict


def submission_to_table(item) -> dict[str, str]:
    
    html_str = "<tr>"
    html_str += f"<td>{item.get('event', '')}</td>"
    html_str += f"<td>{item.get('day', '')}</td>"
    html_str += f"<td>{item.get('start', '')}</td>"
    html_str += f"<td>{item.get('end', '')}</td>"
    html_str += f"<td>{item.get('phone', '')}</td>"
    html_str += f"<td>{item.get('location', '')}</td>"
    html_str += f"<td>{item.get('exin', '')}</td>"
    html_str += f"<td>{item.get('url', '')}</td>"
    html_str += "</tr>"

    
    result = {"html": html_str}
    return result


    """TODO: Takes a dictionary of form parameters and returns an HTML table row

    An example input dictionary might look like: 
    {
     'event': 'Sleep',
     'day': 'Sun',
     'start': '01:00',
     'end': '11:00', 
     'phone': '1234567890', 
     'location': 'Home',
     'extra': 'Have a nice dream', 
     'url': 'https://example.com'
    }
    """
  


# NOTE: Please read the updated function carefully, as it has changed from the
# version in the previous homework. It has important information in comments
# which will help you complete this assignment.
def handle_req(url, body=None):
    """
    The url parameter is a *PARTIAL* URL of type string that contains the path
    name and query string.

    If you enter the following URL in your browser's address bar:
    `http://localhost:4131/MyForm.html?name=joe` then the `url` parameter will have
    the value "/MyForm.html?name=joe"

    This function should return two strings in a list or tuple. The first is the
    content to return, and the second is the content-type.
    """

    # Get rid of any query string parameters
    url, *_ = url.split("?", 1)
    # Parse any form parameters submitted via POST
    parameters = get_body_params(body)

    if url == "/MySchedule.html":
        return open("static/MySchedule.html").read(), "text/html"
    if url == "/Eventlog.html":
        return open("static/EventLog.html").read(), "text/html"
    if url == "/MyForm.html":
        return open("static/MyForm.html").read(), "text/html"
    elif url == "/AboutMe.html":
        return open("static/AboutMe.html").read(), "text/html"
    elif url == "/img/gophers-mascot.png":
        return open("static/img/gophers-mascot.png", "br").read(), "image/png"
    # NOTE: These files may be different for your server, but we include them to
    # show you examples of how yours may look. You may need to change the paths
    # to match the files you want to serve. Before you do that, make sure you
    # understand what the code is doing, specifically with the MIME types and
    # opening some files in binary mode, i.e. `open(..., "br")`.
    elif url == "/css/style.css":
        return open("static/css/style.css").read(), "text/css"
    elif url == "/css/AboutMe.css":
        return open("static/css/AboutMe.css").read(), "text/css"
    elif url == "/css/form.css":
        return open("static/css/form.css").read(), "text/css"
    elif url == "/css/MSstyle.css":
        return open("static/css/MSstyle.css").read(), "text/css"
    elif url == "/js/AboutMe.js":
        return open("static/js/AboutMe.js").read(), "text/javascript"
    elif url == "/js/MyForm.js":
        return open("static/js/MyForm.js").read(), "text/javascript"
    elif url == "/js/MySchedule.js":
        return open("static/js/MySchedule.js").read(), "text/javascript"
    elif url == "/js/script.js":
        return open("static/js/script.js").read(), "text/javascript"
    elif url == "/img/Dan1.jpeg":
        return open("static/img/Dan1.jpeg", "br").read(), "image/jpeg"
    elif url == "/img/Lind.jpg":
        return open("static/img/Lind.jpg", "br").read(), "image/jpg"
    elif url == "/img/Tate.png":
        return open("static/img/Tate.png", "br").read(), "image/png"
    elif url == "/img/zoom.jpg":
        return open("static/img/zoom.jpg", "br").read(), "image/jpg"
    elif url == "/img/vanCleve.jpg":
        return open("static/img/vanCleve.jpg", "br").read(), "image/jpg"
    elif url == "/img/Burton.jpg":
        return open("static/img/Burton.jpg", "br").read(), "image/jpg"
    elif url == "/img/Apartment.jpg":
        return open("static/img/Apartment.jpg", "br").read(), "image/jpg"
    elif url == "/img/breakfast.jpg":
        return open("static/img/breakfast.jpg", "br").read(), "image/jpg"
    elif url == "/img/Smith.jpg":
        return open("static/img/Smith.jpg", "br").read(), "image/jpg"
    elif url == "/img/track.jpg":
        return open("static/img/track.jpg", "br").read(), "image/jpg"
    elif url == "/img/Molecular.jpg":
        return open("static/img/Molecular.jpg", "br").read(), "image/jpg"
    elif url == "/img/anderson.jpg":
        return open("static/img/anderson.jpg", "br").read(), "image/jpg"
    
    
    # TODO: Add update the HTML below to match your other pages and
    # implement the `submission_to_table`.
    if url == "/EventLog.html":
        submission_result = submission_to_table(parameters)
        html_content = submission_result['html']  

        
        message = f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title> Event Submission </title>
            </head>
            <body>
                <header>
                  <nav>
                      <a href="/MySchedule.html">My Schedule</a>
                      <a href="/MyForm.html">Form Input</a>
                      <a href="/AboutMe.html">About Me</a>
                  </nav>
                </header>
                <h1> My New Events </h1>
                <div>
                    <table>
                        <thead>
                            <tr>
                                <th>Event</th>
                                <th>Day</th>
                                <th>Start</th>
                                <th>End</th>
                                <th>Phone</th>
                                <th>Location</th>
                                <th>Extra Info</th>
                                <th>URL</th>
                            </tr>
                        </thead>
                        <tbody>
                            {html_content}  
                        </tbody>
                    </table>
                </div>
            </body>
            </html>
        """

        return message, "text/html; charset=utf-8"
    else:
        return open("static/html/404.html").read(), "text/html; charset=utf-8"


# You shouldn't change content below this. It would be best if you just left it alone.


class RequestHandler(BaseHTTPRequestHandler):
    def __c_read_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        body = str(body, encoding="utf-8")
        return body

    def __c_send_response(self, message, response_code, headers):
        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # Send the first line of response.
        self.protocol_version = "HTTP/1.1"
        self.send_response(response_code)

        # Send headers (plus a few we'll handle for you)
        for key, value in headers.items():
            self.send_header(key, value)
        self.send_header("Content-Length", len(message))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)

    def do_GET(self):
        # Call the student-edited server code.
        message, content_type = handle_req(self.path)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        self.__c_send_response(
            message,
            200,
            {
                "Content-Type": content_type,
                "Content-Length": len(message),
                "X-Content-Type-Options": "nosniff",
            },
        )

    def do_POST(self):
        body = self.__c_read_body()
        message, content_type = handle_req(self.path, body)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        self.__c_send_response(
            message,
            200,
            {
                "Content-Type": content_type,
                "Content-Length": len(message),
                "X-Content-Type-Options": "nosniff",
            },
        )


def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ("", PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()


run()
