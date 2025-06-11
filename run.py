from app.server import app
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6000))
    app.run(host='0.0.0.0', port=port)
