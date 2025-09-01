class House:
    def __init__(self,
                 foundation: str,
                 structure: str,
                 roof: str,
                 has_garage: bool,
                 has_garden: bool,
                 has_swimming_pool: bool = False,
                  ):
        self.foundation: str  = foundation
        self.structure: str = structure
        self.roof: str = roof
        self.has_garage: bool = has_garage
        self.has_swimming_pool: bool = has_swimming_pool
        self.has_garden: bool = has_garden

        # Constructor Explosion => Too many constructors
        # Difficult to unserstand and maintain the code