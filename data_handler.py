import pickle

class DataHandler:
    def save(self, trackables):
        with open('trackables.pkl', 'wb') as f:
            pickle.dump(trackables, f)

    def load(self):
        try:
            with open('trackables.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}
