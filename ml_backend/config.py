import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="ml_backend",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="ml_backend_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from ml_backend.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export ml_backend_KEY=value
export ml_backend_KEY="@int 42"
export ml_backend_KEY="@jinja {{ this.db.uri }}"
export ml_backend_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
ml_backend_ENV=production ml_backend run
```

Read more on https://dynaconf.com
"""
