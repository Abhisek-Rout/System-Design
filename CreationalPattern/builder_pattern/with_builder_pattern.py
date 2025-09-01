class House:
    class HouseBuilder:
        def __init__(self, foundation: str, structure: str, roof: str):
            self.foundation = foundation
            self.structure = structure
            self.roof = roof

            # Set the default value of optional fields
            self.has_garden = False
            self.has_swimming_pool = False
            self.has_garage = False
        
        ## Define the optional parameters
        def set_garden(self, has_garden: bool):
            self.has_garden = has_garden
            return self

        def set_swimming_pool(self, has_swimming_pool: bool):
            self.has_swimming_pool = has_swimming_pool
            return self

        def set_garage(self, has_garage: bool):
            self.has_garage = has_garage
            return self

        def build(self):
            return House(self)
        
    def __init__(self, builder: HouseBuilder):
        self.foundation: str  = builder.foundation
        self.structure: str = builder.structure
        self.roof: str = builder.roof
        self.has_garage: bool = builder.has_garage
        self.has_swimming_pool: bool = builder.has_swimming_pool
        self.has_garden: bool = builder.has_garden

    def __str__(self):
        return (f"House(foundation={self.foundation}, structure={self.structure}, roof={self.roof}, "
                f"garage={self.has_garage}, swimming_pool={self.has_swimming_pool}, garden={self.has_garden})")



class WithBuilderPattern:
    def main(self):
        house: House = (
                            House.HouseBuilder(structure="Wooden",
                                          foundation="Concrete",
                                          roof="Tile")
                                    .set_garage(False)
                                    .set_garden(True)
                                    .set_swimming_pool(True)
                                    .build()
        )
        print(house)


if __name__ == "__main__":
    obj: WithBuilderPattern = WithBuilderPattern()
    obj.main()