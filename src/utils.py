from functools import reduce


def map_reduce(map_function, lst):
    """
    Implementation of map-reduce where the reduce is /a b -> a+b
    :param map_function: the function that is applied on every element of list before reduction
    :param lst: the non-empty list to be map-reduced
    :return: map-reduced list
    """
    if not lst:
        raise Exception("lst can not be empty")
    return reduce(lambda a, b: a + b, map(map_function, lst))


def denormalize(job):
    result = []
    for location in job["geo"]:
        job_copy = job.copy()
        del job_copy["geo"]
        job_copy["country"] = location["country"]
        job_copy["geo"] = {"lat": location["lat"], "long": location["long"]}
        result.append(job_copy)

    return result
