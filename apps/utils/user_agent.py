from user_agents import parse


class UserAgent:
    """
    Wrapper class around 'user_agents' lib

    return instance, created by 'user_agents' lib instead of UserAgent class instance
    this allows to use class constructor notation follow in project

    """
    def __new__(cls, ua_str):
        return parse(ua_str)
