from typing import List

def parse_music(music_string: str) -> List[int]:
    # Define the mapping from note strings to beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual note representations
    notes = music_string.split()
    
    # Translate each note to its corresponding beat count
    beats = [note_to_beats[note] for note in notes]
    
    return beats
