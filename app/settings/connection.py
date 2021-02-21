def connect_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/cearch'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False