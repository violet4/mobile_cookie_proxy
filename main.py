from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import argparse
from http.cookies import SimpleCookie

class SecureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        cookie = SimpleCookie()
        cookie[self.server.cookie_name] = self.server.cookie_value
        cookie[self.server.cookie_name]['secure'] = True
        cookie[self.server.cookie_name]['httponly'] = True

        self.send_response(200)
        self.send_header('Set-Cookie', cookie[self.server.cookie_name].OutputString())
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Secure connection established and cookie set!")


def main():
    parser = argparse.ArgumentParser(description='HTTPS Server with Session Cookie')
    parser.add_argument('--host', default='192.168.1.121', help='Host address')
    parser.add_argument('--port', type=int, default=443, help='Port number')
    parser.add_argument('--cert', required=True, help='Path to SSL certificate')
    parser.add_argument('--key', required=True, help='Path to SSL private key')
    parser.add_argument('--cookie-name', required=True, help='Session cookie name')
    parser.add_argument('--cookie-value', required=True, help='Session cookie value')

    args = parser.parse_args()

    httpd = HTTPServer((args.host, args.port), SecureHandler)
    httpd.cookie_name = args.cookie_name
    httpd.cookie_value = args.cookie_value

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(args.cert, args.key)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f'Server running on https://{args.host}:{args.port}')
    httpd.serve_forever()

if __name__ == '__main__':
    main()
