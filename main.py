from settings import app
from domain.tables import create_tables

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
