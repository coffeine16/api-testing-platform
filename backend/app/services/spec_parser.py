# backend/app/services/spec_parser.py

from typing import Dict, Any, List
import uuid

class SpecParser:
    def __init__(self):
        self.specs = {}  # In-memory storage for now
    
    def parse_spec(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Parse OpenAPI spec and extract key information"""
        
        # Basic validation
        if "openapi" not in spec and "swagger" not in spec:
            raise ValueError("Invalid OpenAPI/Swagger spec")
        
        # Extract endpoints
        endpoints = []
        paths = spec.get("paths", {})
        
        for path, methods in paths.items():
            for method, details in methods.items():
                if method.upper() in ["GET", "POST", "PUT", "DELETE", "PATCH"]:
                    endpoints.append({
                        "path": path,
                        "method": method.upper(),
                        "summary": details.get("summary", ""),
                        "parameters": details.get("parameters", [])
                    })
        
        return {
            "endpoints": endpoints,
            "total_endpoints": len(endpoints),
            "title": spec.get("info", {}).get("title", "Unnamed API"),
            "version": spec.get("info", {}).get("version", "1.0.0")
        }
    
    def store_spec(self, name: str, spec: Dict[str, Any], parsed_data: Dict[str, Any]) -> str:
        """Store spec and return ID"""
        spec_id = str(uuid.uuid4())
        self.specs[spec_id] = {
            "id": spec_id,
            "name": name,
            "original_spec": spec,
            "parsed_data": parsed_data
        }
        return spec_id
    
    def get_spec(self, spec_id: str) -> Dict[str, Any]:
        """Retrieve stored spec"""
        return self.specs.get(spec_id)