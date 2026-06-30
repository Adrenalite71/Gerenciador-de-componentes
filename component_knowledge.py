import re

def get_led_specs(color: str):
    """
    Analyzes a color string to determine typical LED specifications.
    Returns a dict with 'voltage' and 'current' or None if no match is found.
    """
    if not color:
        return None

    c_lower = color.lower().strip()
    
    if c_lower in ['vermelho', 'amarelo', 'laranja']:
        return {"voltage": "2.0V", "current": "20mA"}
    
    elif c_lower == 'verde':
        return {"voltage": "2.2V", "current": "20mA"}
    
    elif c_lower in ['azul', 'branco', 'ultravioleta', 'uv']:
        return {"voltage": "3.2V", "current": "20mA"}
        
    return None
