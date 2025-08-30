"""
The Exercise class demonstrates the State Design Pattern for a Media Player.
"""
from media_player import MediaPlayer
from paused_state import PausedState
from stopped_state import StoppedState

class Exercise:
    def main(self):
        media_player: MediaPlayer = MediaPlayer()

        choice: str = input("Enter your choice: ").lower()

        match choice:
            case "play":
                media_player.play()
            case "pause":
                media_player.state = PausedState()
                media_player.pause()
            case "stop":
                media_player.state = StoppedState()
                media_player.stop()
            case _:
                print("Invadid choice")

        media_player.display_sate()

if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()
