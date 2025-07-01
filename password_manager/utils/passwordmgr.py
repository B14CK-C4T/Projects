import hashlib

class Hash:
    
    @staticmethod
    def save(file_name,data):
        with open(f"{file_name}.txt", "a") as file:
            file.write(str(data) + "\n")

    @staticmethod
    def create_hash(password):
        m = hashlib.sha256()
        # Ensure password is bytes
        m.update(password)
        out = m.hexdigest()
        return out