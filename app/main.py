from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    """Get latest shipment.

    Returns:
        dict[str, Any]: _description_

    """
    return {"id": 354, "weight": 0.8, "article": "pen", "status": "placed"}


@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:
    """Get shipment.

    Args:
        id (int): _description_

    Returns:
        dict[str, Any]: _description_

    """
    return {"id": id, "weight": 1.2, "article": "notebook", "status": "in transit"}


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    """Get documentation in scalar format.

    Returns:
        _type_: _description_

    """
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar Docs")
