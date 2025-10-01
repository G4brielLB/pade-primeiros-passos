import os
from pade.web.flask_server import db, app, login_manager


def main():
    # Ensure DB is initialized
    with app.app_context():
        db.create_all()

    # Optional: allow skipping login via env flag (default: disabled login)
    secure = os.environ.get('PADE_WEB_SECURE', '0') in ('1', 'true', 'True')
    with app.app_context():
        login_manager._login_disabled = not secure

    # Pick port from env or fallback
    try:
        port = int(os.environ.get('PADE_WEB_PORT', '5001'))
    except ValueError:
        port = 5001

    host = os.environ.get('PADE_WEB_HOST', '0.0.0.0')

    print(f"[PADE WEB] Starting Flask at http://{host}:{port} (secure={secure})")
    app.run(host=host, port=port, debug=False)


if __name__ == '__main__':
    main()
