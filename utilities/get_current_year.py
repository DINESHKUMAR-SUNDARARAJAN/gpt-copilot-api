def get_current_year(**kwargs) -> dict:
    from datetime import datetime
    return {"year": datetime.now().year}