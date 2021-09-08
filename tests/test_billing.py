from datetime import datetime

import pytest
import respx

from neuroio.constants import IAM_BASE_URL
from tests.utils import mock_query_params_all_combos


@respx.mock
def test_billing_usage(client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/billing/usage/",
        "limit=20",
        "offset=0",
        "month_from=2020-01",
        "month_to=2020-06",
        "spaces_ids=[4, 5, 6]",
        "event_types=[1, 2, 3]",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.billing.billing_usage(
        limit=20,
        offset=0,
        month_from=datetime(year=2020, month=1, day=1),
        month_to=datetime(year=2020, month=6, day=1),
        spaces_ids=[4, 5, 6],
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_billing_usage_total(client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/billing/usage/total/",
        "month_from=2020-01",
        "month_to=2020-06",
        "event_types=[1, 2, 3]",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.billing.billing_usage_total(
        month_from=datetime(year=2020, month=1, day=1),
        month_to=datetime(year=2020, month=6, day=1),
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_manager_account_billing_usage(client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/accounts/1/billing/usage/",
        "limit=20",
        "offset=0",
        "month_from=2020-01",
        "month_to=2020-06",
        "spaces_ids=[4, 5, 6]",
        "event_types=[1, 2, 3]",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.billing.manager_account_billing_usage(
        limit=20,
        offset=0,
        pk=1,
        month_from=datetime(year=2020, month=1, day=1),
        month_to=datetime(year=2020, month=6, day=1),
        spaces_ids=[4, 5, 6],
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_manager_account_billing_usage_total(client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/accounts/1/billing/usage/total/",
        "pk=1",
        "month_from=2020-01",
        "month_to=2020-06",
        "event_types=[1, 2, 3]",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.billing.manager_account_billing_usage_total(
        pk="1",
        month_from=datetime(year=2020, month=1, day=1),
        month_to=datetime(year=2020, month=6, day=1),
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_billing_usage(async_client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/billing/usage/",
        "limit=20",
        "offset=0",
        "month_from=2020-01",
        "month_to=2020-06",
        "spaces_ids=[4, 5, 6]",
        "event_types=[1, 2, 3]",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.billing.billing_usage(
        limit=20,
        offset=0,
        month_from=datetime(year=2020, month=1, day=1),
        month_to=datetime(year=2020, month=6, day=1),
        spaces_ids=[4, 5, 6],
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_billing_usage_total(async_client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/billing/usage/total",
        "month_from=2020-01",
        "month_to=2020-06",
        "event_types=[1, 2, 3]",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.billing.billing_usage_total(
        month_from=datetime(year=2020, month=1, day=1),
        month_to=datetime(year=2020, month=6, day=1),
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_manager_account_billing_usage(async_client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/accounts/1/billing/usage/",
        "pk=1",
        "limit=20",
        "offset=0",
        "month_from=2020-01",
        "month_to=2020-06",
        "spaces_ids=[4, 5, 6]",
        "event_types=[1, 2, 3]",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.billing.manager_account_billing_usage(
        pk=1,
        limit=20,
        offset=0,
        month_from=datetime(year=2020, month=1, day=1),
        month_to=datetime(year=2020, month=6, day=1),
        spaces_ids=[4, 5, 6],
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_manager_account_billing_usage_total(async_client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/accounts/1/billing/usage/total/",
        "pk=1",
        "month_from=2020-01",
        "month_to=2020-06",
        "event_types=[1, 2, 3]",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.billing.manager_account_billing_usage_total(
        pk=1,
        month_from=datetime(year=2020, month=1, day=1),
        month_to=datetime(year=2020, month=6, day=1),
        event_types=[1, 2, 3],
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1
