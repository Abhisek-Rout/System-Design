"""
The Exercise class allows users to input shape attributees and provides functioanlity to manage these shapes using the Momento pattern 
"""
from graphic_editor import GraphicEditor
from care_taker import CareTaker

class Exercise:
    def main(self):
        graph_editor: GraphicEditor = GraphicEditor()
        care_taker: CareTaker = CareTaker()

        custom_input = [
            ("Circle", 3, 4, "Red", 10),
            ("Square", 8, 1, "Blue", 13),
            ("Triangle", 4, 4, "Yellow", 8)
        ]
        for item in custom_input:
            shape: str = item[0]
            x: int = item[1]
            y: int = item[2]
            color: str = item[3]
            size: int = item[4]

            # Update the graphic editor with the new shape attributes
            graph_editor.set_shape(shape_type=shape, x=x, y=y, color=color, size=size)

            # Save the current state of the graphic editor to the history
            momento = graph_editor.save()
            care_taker.save_state(momento)

        # Fetch the current shape
        print(graph_editor.get_shape())

        # Implement the undo operation to revert to the previous shape state
        care_taker.undo(graph_editor)

        # Output the current shape attributes after the undo operatio to verify the restored state
        print(graph_editor.get_shape())

if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()