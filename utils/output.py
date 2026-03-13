def save_results(filename, data):
    """Save results to file"""
    if data is None:
        data = ""
    with open(filename, 'w') as f:
        f.write(str(data))
