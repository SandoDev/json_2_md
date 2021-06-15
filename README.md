# Json to MD

Convierte un json a markdown

la idea de esto es construir un modelo con pydantic y convertirlo a docs de mkdocs

## Install

1. Create virtualenv

    virtualenv -p python3 json2md

2. Activate

    source json2md/bin/activate

3. Install requirements

    pip install -r requirements.txt

4. Run mkdocs

    mkdocs serve -a localhost:8005

5. Run project
   1. Modify the `models.py` [Optional]
   2. run in console
        
        python main.py

6. Visualizate in

    http://localhost:8005/test_page/