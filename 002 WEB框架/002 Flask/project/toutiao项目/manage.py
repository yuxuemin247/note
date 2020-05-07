from flask_migrate import  Migrate, MigrateCommand

from flask_script import Manager

from app import create_app, db

app = create_app()
migrate =Migrate()
migrate.init_app(app,db=db)
manager = Manager(app=app)
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()
