import sqlalchemy

metadata = sqlalchemy.MetaData()

pets_table = sqlalchemy.Table(
    "pets",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("type_pets", sqlalchemy.String(16)),
    sqlalchemy.Column("age", sqlalchemy.Date()),
    sqlalchemy.Column("type_pets", sqlalchemy.String(16)),
    sqlalchemy.Column("photos", sqlalchemy.Boolean),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
)

pets_photos = sqlalchemy.Table(
    "photos",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("urls", sqlalchemy.String(100)),
    sqlalchemy.Column("pets", sqlalchemy.ForeignKey("pets.id")),
)