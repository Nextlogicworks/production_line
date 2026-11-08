from fastapi import FastAPI
import random
from datetime import datetime

app = FastAPI()


@app.get("/factory")
def get_factory_data():

    production_lines = []

    for number in range(1, 7):

        line_id = f"R-3{number:02d}"

        planned_units = random.randint(250, 600)

        produced_units = random.randint(600, 1200)

        defective_units = random.randint(0,40)

        
        product = {
            "ID": line_id,
            "Planned Units": planned_units,
            "Produced Units": produced_units,
            "Defective Units": defective_units,
        }

        production_lines.append(product)

    return {
        "timestamp": datetime.now().isoformat(),
        "production_lines": production_lines
    }
