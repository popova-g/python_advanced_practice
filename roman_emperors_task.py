def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}

    for emperor, success in args:
        if success:
            successful_emperors[emperor] = kwargs[emperor]
        else:
            unsuccessful_emperors[emperor] = kwargs[emperor]

    sorted_successful_emperors = sorted(
        successful_emperors.items(), key=lambda x: (-x[1], x[0])
    )
    sorted_unsuccessful_emperors = sorted(
        unsuccessful_emperors.items(), key=lambda x: (x[1], x[0])
    )

    result = [f"Total number of emperors: {len(args)}"]

    if successful_emperors:
        result.append("Successful emperors:")
        for name, details in sorted_successful_emperors:
            result.append(f"****{name}: {details}")
    if unsuccessful_emperors:
        result.append("Unsuccessful emperors:")
        for name, details in sorted_unsuccessful_emperors:
            result.append(f"****{name}: {details}")

    return "\n".join(result)
