from create import create_app
import webbrowser
import threading

app = create_app()

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000/")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(port=8000) # Enable debug mode for development
