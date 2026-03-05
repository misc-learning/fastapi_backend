from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


shipments = {
    354: {"weight": 0.8, "article": "pen", "status": "placed"},
    1548: {"weight": 1.2, "article": "notebook", "status": "in transit"},
}


@app.get("/shipment/latest")
def get_latest_shipment(shipments: dict[int, dict[str, Any]]) -> dict[str, Any]:
    """Get latest shipment.

    Returns:
        dict[str, Any]: _description_

    """
    max_id = max(shipments.keys())
    return shipments[max_id]


@app.get("/shipment/{id}")
def get_shipment(
    id: int, shipments: dict[int, dict[str, Any]]
) -> dict[str, Any] | HTTPException:
    """Get shipment.

    Args:
        id (int): _description_
        shipments (dict): _description_

    Returns:
        dict[str, Any]: _description_

    """
    if id in shipments:
        return shipments[id]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="ID not found in database"
        )


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    """Get documentation in scalar format.

    Returns:
        _type_: _description_

    """
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar Docs")
