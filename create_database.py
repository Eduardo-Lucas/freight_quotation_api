from app.database import engine
from app.models import freight

# Create all tables in the database
# This is equivalent to "Create Table" statements in raw SQL.
freight.Base.metadata.create_all(bind=engine)
