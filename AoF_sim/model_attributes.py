# Attributes that apply per-model
base_attributes = {
    'counter': False,
    'elite': False,
    'empower': False,
    'fear': False,
    'fearless': False,
    'fast': False,
    'furious': False,
    'hero': False,
    'impact': 0,
    'joust': False,
    'sergeant': False,
    'specialist': False,
    'tough': 0,
}

# Attributes that apply per-weapon
weapon_attributes = {
    'blast': 0,
    'deadly': 0,
    'lance': False,
    'poison': False,
    'reliable': False,
    'rending': False,
}


# ---- 
#      Attributes that are specific to each army; but
#      translate into some common attribute
# ----
special_attributes = {
    'herald': {
        'ambush': True
    }
}

