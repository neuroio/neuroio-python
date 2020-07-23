import itertools

import respx


def mock_query_params_all_combos(
    base_url: str,
    *args,
    query_type: str = "get",
    status_code: int = 200,
    content=None,
):
    combos = list(itertools.permutations(args))

    return [
        getattr(respx, query_type)(
            f"{base_url}/?{'&'.join(combo)}",
            status_code=status_code,
            content=content,
        )
        for combo in combos
    ]
