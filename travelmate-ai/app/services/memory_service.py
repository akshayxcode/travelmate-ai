class MemoryService:

    _memory = {}

    @classmethod
    def save(cls, session_id, role, content):

        if session_id not in cls._memory:
            cls._memory[session_id] = []

        cls._memory[session_id].append({
            "role": role,
            "content": content
        })

    @classmethod
    def history(cls, session_id):
        return cls._memory.get(session_id, [])