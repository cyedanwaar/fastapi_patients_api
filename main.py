from fastapi import FastAPI, Path, Query, HTTPException
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def safe_getter(key, default=0):
    return lambda x: x.get(key, 0)

@app.get("/")
def hello():
    return{'message': 'Patient Management System API'}

@app.get("/about")
def about():
    return {'message': 'A fully functional API to manage your patient records'}


@app.get('/patients')
def view():
    data = load_data()
    return data

@app.get('/patients/{patient_id}')
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example='P001')):
    data: dict = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail='Patient not found')


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='Sort in asc or desc order')):
    
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field. Select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order. Select from asc, desc')
    

    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(),
                        key=safe_getter(sort_by),
                        reverse=sort_order)

    return sorted_data
     



