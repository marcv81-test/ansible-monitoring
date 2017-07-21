class FilterModule:

    def filters(self):
        return {
            'escape_influxdb': self.escape_single,
            'escape_json':     self.escape_double,
            'escape_toml':     self.escape_double}

    # Escapes single quotes and backslashes
    # Works for InfluxDB string literals
    def escape_single(self, string):
        return string.replace('\\', '\\\\').replace("'", "\\'")

    # Escapes double quotes and backslashes
    # Works for JSON and TOML strings without control characters
    def escape_double(self, string):
        return string.replace('\\', '\\\\').replace('"', '\\"')
