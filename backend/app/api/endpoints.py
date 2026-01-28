# backend/app/api/endpoints.py

from fastapi import APIRouter, HTTPException
from app.schemas.api_spec import APISpecUpload, APISpecResponse
from app.services.spec_parser import SpecParser

router = APIRouter()
spec_parser = SpecParser()

@router.post("/api/specs/upload", response_model=APISpecResponse)
def upload_api_spec(upload: APISpecUpload):
    """Upload and parse an OpenAPI specification"""
    try:
        # Parse the spec
        parsed_data = spec_parser.parse_spec(upload.spec)
        
        # Store it
        spec_id = spec_parser.store_spec(upload.name, upload.spec, parsed_data)
        
        return APISpecResponse(
            id=spec_id,
            name=upload.name,
            status="parsed",
            endpoints_count=parsed_data["total_endpoints"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing spec: {str(e)}")

@router.get("/api/specs/{spec_id}")
def get_spec(spec_id: str):
    """Get parsed spec details"""
    spec = spec_parser.get_spec(spec_id)
    if not spec:
        raise HTTPException(status_code=404, detail="Spec not found")
    return spec["parsed_data"]