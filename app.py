import os

from main import create_app

if __name__ == '__main__':
    env = os.getenv("PYTHON_DOCKER_ENV", "dev")
    app = create_app(env)
    app.run(host="0.0.0.0")
