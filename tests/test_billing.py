import pytest
import respx

from neuroio.constants import IAM_BASE_URL
from tests.utils import mock_query_params_all_combos


@respx.mock
def test_usage(client):
    month_from = "2018-06"
    month_to = "2020-06"
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/billing/usage",
        "limit=20",
        "offset=0",
        f"month_from={month_from}",
        f"month_to={month_to}",
        "spaces_ids=4,5,6".replace(",", "%2C"),
        "event_types=1,2,3".replace(",", "%2C"),
        json={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.billing.usage(
        limit=20,
        offset=0,
        month_from=month_from,
        month_to=month_to,
        spaces_ids=[4, 5, 6],
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_usage_total(client):
    month_from = "2018-06"
    month_to = "2020-06"
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/billing/usage/total",
        f"month_from={month_from}",
        f"month_to={month_to}",
        "event_types=1,2,3".replace(",", "%2C"),
        json={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.billing.usage_total(
        month_from=month_from,
        month_to=month_to,
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_usage(async_client):
    month_from = "2018-06"
    month_to = "2020-06"
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/billing/usage",
        "limit=20",
        "offset=0",
        f"month_from={month_from}",
        f"month_to={month_to}",
        "spaces_ids=4,5,6".replace(",", "%2C"),
        "event_types=1,2,3".replace(",", "%2C"),
        json={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.billing.usage(
        limit=20,
        offset=0,
        month_from=month_from,
        month_to=month_to,
        spaces_ids=[4, 5, 6],
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_usage_total(async_client):
    month_from = "2018-06"
    month_to = "2020-06"
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/billing/usage/total",
        f"month_from={month_from}",
        f"month_to={month_to}",
        "event_types=1,2,3".replace(",", "%2C"),
        json={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.billing.usage_total(
        month_from=month_from,
        month_to=month_to,
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1
