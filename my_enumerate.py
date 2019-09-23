def my_enumerate(container, count=0):
    my_count = count
    for item in container:
        yield my_count, item
        my_count += 1
