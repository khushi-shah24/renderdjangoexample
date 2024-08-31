from waitress import serve
import epiphany.wsgi

if __name__ == "__main__":
    print("Starting Waitress server...")
    serve(epiphany.wsgi.application, host='0.0.0.0', port=8000)
    print("Server started on http://0.0.0.0:8000")
