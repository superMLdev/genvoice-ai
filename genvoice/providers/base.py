class VideoProviderBase:
    def generate(self, script: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")