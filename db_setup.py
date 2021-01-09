import serenity
import sqlalchemy
from serenity import app


engine = sqlalchemy.engine.create_engine(app.CONNECTION_STRING)
serenity.resolvers.BaseModel.metadata.drop_all(engine)
serenity.resolvers.BaseModel.metadata.create_all(engine)
