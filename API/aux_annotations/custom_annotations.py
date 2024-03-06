from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import mapped_column
from sqlalchemy import text


# Postgres specific dialect, do not use it in SQLite
created_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"))]

# Postgres specific dialect, do not use it in SQLite
updated_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.now)]