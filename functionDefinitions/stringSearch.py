def stringSearch(sourceArray, searchArray):
    result = []
    for src_id, src_str in sourceArray:
        for search_id, search_str in searchArray:
            if src_id <= search_id and src_str in search_str:
                result.append((src_id, src_str))
                break  # stop once we find a match for this source tuple
    return result
