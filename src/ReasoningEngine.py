class ReasoningEngine:
    def __init__(self):
        self.chunks = {}
        self.rules = {}

    def add_chunk(self, chunk):
        self.chunks[chunk.chunk_id] = chunk

    def add_rule(self, rule):
        self.rules[rule.rule_id] = rule

    def match_condition(self, condition, chunk):
        for key, value in condition.items():
            if key not in chunk.properties or chunk.properties[key] != value:
                return False
        return True

    def apply_actions(self, actions, chunk):
        for action in actions:
            if "update" in action:
                chunk.update_property(action["update"]["key"], action["update"]["value"])
            elif "remove" in action:
                chunk.remove_property(action["remove"]["key"])

    def apply_rules(self):
        for rule in self.rules.values():
            for chunk in self.chunks.values():
                if self.match_condition(rule.conditions, chunk):
                    self.apply_actions(rule.actions, chunk)
