from board import create_app, config

if __name__ == "__main__":
    app = create_app()
    app.run(debug=bool(config.debug), host=config.listen, port=int(config.port))
