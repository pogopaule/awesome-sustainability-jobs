from functools import reduce

flat_map = lambda f, xs: reduce(lambda a, b: a + b, map(f, xs))


def denormalize(job):
    result = []
    for location in job["geo"]:
        job_copy = job.copy()
        del job_copy["geo"]
        job_copy["country"] = location["country"]
        job_copy["geo"] = {"lat": location["lat"], "long": location["long"]}
        result.append(job_copy)

    return result
