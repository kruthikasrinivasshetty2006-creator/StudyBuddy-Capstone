# Resource Fetcher Agent: Fetches study resources

def fetch_resources(topic):
    print(f"Resource Fetcher Agent: fetching resources for '{topic}'")
    return [f"{topic} - Resource 1", f"{topic} - Resource 2"]

if _name_ == "_main_":
    fetch_resources("Math")
