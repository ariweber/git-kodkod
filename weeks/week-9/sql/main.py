from fastapi import FastAPI, HTTPException
import crud
from pydantic import BaseModel
app = FastAPI()

class SoldierIn(BaseModel):
    name: str
    rank: str | None = None
    unit: str | None = None

@app.get("/soldiers")
def list_soldiers():
    return crud.get_all()

@app.get("/soldiers/{soldier_id}")
def get_soldier(soldier_id: int):
    soldier = crud.get_by_id(soldier_id)
    if soldier is None:
        raise HTTPException(status_code=404, detail=F"{soldier_id} not found")
    return soldier

@app.post("/soldiers", status_code=201)
def add_soldier(body: SoldierIn):
    new_id = crud.create(body.name, body.rank, body.unit)
    return {"id": new_id, "message": "Soldier created"}

@app.put("/soldiers/{soldier_id}")
def edit_soldier(soldier_id: int, body: SoldierIn):
    data = body.model_dump(exclude_none=True)
    success = crud.update(soldier_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Updated"}


@app.delete("/soldiers/{soldier_id}")
def remove_soldier(soldier_id: int):
    success = crud.delete(soldier_id)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Deleted"}


@app.get("/stats/units")
def stats_by_unit():
    return {"by_unit": crud.count_by_unit()}


@app.get("/stats/summary")
def get_sammayy():
    return crud.get_summary()