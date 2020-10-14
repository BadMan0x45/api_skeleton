# API Skeleton

API skeleton based on fastapi (python).

## After project generation hook

After project generation, cookiecutter creates venv for project and install build dependencies from `build-requirements.txt`.

## Project structure
```
{{ app_name }}
├── build-requirements.txt
├── {{ app_name }}
│   ├── api
│   │   └── internal_.py
│   ├── config.py
│   ├── main.py
│   ├── routes.py
│   └── services
├── Dockerfile
├── Makefile
├── mypy.ini
├── pyproject.toml
├── README.rst
└── tests
    └── {{ app_name }}
        └── services
            └── test_fapi.py
```