class handler:
    def __init__(self, criteria: int, payload):
        self.criteria = criteria
        self.payload = payload
    
    def test(self, event):
        return self.criteria == event
    
    def run(self, event, frame):
        self.payload(event, frame)