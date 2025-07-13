USER_MEMORY = {}
USER_SUMMARY = {}

def get_memory(user_id):
    return USER_MEMORY.get(user_id, [])

def add_to_memory(user_id, msg):
    USER_MEMORY.setdefault(user_id, []).append(msg)

def get_summary(user_id):
    return USER_SUMMARY.get(user_id, None)

def set_summary(user_id, summary_msg):
    USER_SUMMARY[user_id] = summary_msg