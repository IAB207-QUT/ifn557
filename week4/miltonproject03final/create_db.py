from miltontours import models, db, create_app

app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()