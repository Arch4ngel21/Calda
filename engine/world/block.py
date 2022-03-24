
class Block:
    def __init__(self, x: int, y: int, block_name: str, is_passable: bool = False):
        self.is_passable: bool = is_passable
        self.block_name: str = block_name
        # self.rectangle -> do reprezentacji na ekranie
