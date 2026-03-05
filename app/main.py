from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


shipments = {
    354: {"weight": 0.8, "article": "pen", "status": "placed"},
    1548: {"weight": 1.2, "article": "notebook", "status": "in transit"},
}


@app.get("/shipment/latest")
def get_latest_shipment(
    shipments: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    """Get latest shipment.

    Returns:
        dict[str, Any]: _description_

    """
    max_id = max(shipments.keys())
    return shipments[max_id]


@app.get("/shipment/{id}")
def get_shipment(
    id: int,
    shipments: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    """Get shipment.

    Args:
        id (int): _description_
        shipments (dict): _description_

    Returns:
        dict[str, Any]: _description_

    """
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="ID not found in database"
        )

    return shipments[id]


@app.get("shipment/{field}")
def get_shipment_field(
    field: str,
    id: int,
) -> dict[str, Any]:
    """Get a specific field of shipment e.g. content or weight.

    Args:
        field (str): _description_
        id (int): _description_

    Returns:
        dict[str, Any]: _description_

    """
    return {field: shipments[id][field]}


# we can use same endpoint for get and post, e.g here it is shipment
@app.post("/shipment")
def post_shipment(
    article: str,
    weight: float,
) -> dict[str, int]:
    """Post shipment.

    Args:
        article (str): _description_
        weight (float): _description_

    Raises:
        HTTPException: _description_

    Returns:
        dict[str, int]: _description_

    """
    if weight > 30:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Weight greater than 30 kg is not acceptable",
        )

    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {"article": article, "weight": weight, status: "placed"}  # type: ignore

    return {"id": new_id}


@app.put("shipment")
def put_shipment(
    id: int,
    article: str,
    weight: float,
    status: str,
) -> dict[str, Any]:
    """Update shipment.

    Args:
        id (int): _description_
        article (str): _description_
        weight (float): _description_
        status (str): _description_

    Returns:
        dict[str, Any]: _description_

    """
    shipments[id] = {"article": article, "weight": weight, status: "out for delivery"}
    return shipments[id]


@app.patch("shipment")
def patch_shipment(
    id: int,
    body: dict[str, Any],
) -> dict[str, Any]:
    """Update shipment.

    Args:
        id (int): _description_
        body (dict[str, Any]): _description_

    Returns:
        dict[str, Any]: _description_

    """
    shipment = shipments[id]

    if body:
        shipment.update(body)
    # if article:
    #     shipment["article"] = article
    # if weight:
    #     shipment["weight"] = weight
    # if status:
    #     shipment["status"] = status

    shipments[id] = shipment

    return shipments[id]


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    """Get documentation in scalar format.

    Returns:
        _type_: _description_

    """
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar Docs")
