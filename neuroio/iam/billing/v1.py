from datetime import datetime
from typing import List, Union

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync
from neuroio.constants import sentinel
from neuroio.utils import request_query_processing


class Billing(APIBase):
    def billing_usage(
        self,
        limit: int = 20,
        offset: int = 0,
        spaces_ids: Union[List[int], object] = sentinel,
        event_types: Union[List[int], object] = sentinel,
        month_from: Union[datetime, object] = sentinel,
        month_to: Union[datetime, object] = sentinel,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        with self.get_client() as client:
            return client.get(url="/v1/billing/usage/", params=data)

    def billing_usage_total(
        self,
        event_types: Union[List[int], object] = sentinel,
        month_from: Union[datetime, object] = sentinel,
        month_to: Union[datetime, object] = sentinel,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        with self.get_client() as client:
            return client.get(url="/v1/billing/usage/total/", params=data)

    def manager_account_billing_usage(
        self,
        pk: str,
        limit: int = 20,
        offset: int = 0,
        spaces_ids: Union[List[int], object] = sentinel,
        event_types: Union[List[int], object] = sentinel,
        month_from: Union[datetime, object] = sentinel,
        month_to: Union[datetime, object] = sentinel,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        with self.get_client() as client:
            return client.get(
                url=f"/v1/accounts/{pk}/billing/usage/", params=data
            )

    def manager_account_billing_usage_total(
        self,
        pk: str,
        spaces_ids: Union[List[int], object] = sentinel,
        event_types: Union[List[int], object] = sentinel,
        month_from: Union[datetime, object] = sentinel,
        month_to: Union[datetime, object] = sentinel,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        with self.get_client() as client:
            return client.get(
                url=f"/v1/accounts/{pk}/billing/usage/total/", params=data
            )


class BillingAsync(APIBaseAsync):
    async def billing_usage(
        self,
        limit: int = 20,
        offset: int = 0,
        spaces_ids: Union[List[int], object] = sentinel,
        event_types: Union[List[int], object] = sentinel,
        month_from: Union[datetime, object] = sentinel,
        month_to: Union[datetime, object] = sentinel,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        async with self.get_client() as client:
            return await client.get(url="/v1/billing/usage/", params=data)

    async def billing_usage_total(
        self,
        event_types: Union[List[int], object] = sentinel,
        month_from: Union[datetime, object] = sentinel,
        month_to: Union[datetime, object] = sentinel,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        async with self.get_client() as client:
            return await client.get(url="/v1/billing/usage/total", params=data)

    async def manager_account_billing_usage(
        self,
        pk: str,
        limit: int = 20,
        offset: int = 0,
        spaces_ids: Union[List[int], object] = sentinel,
        event_types: Union[List[int], object] = sentinel,
        month_from: Union[datetime, object] = sentinel,
        month_to: Union[datetime, object] = sentinel,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        async with self.get_client() as client:
            return await client.get(
                url=f"/v1/accounts/{pk}/billing/usage/", params=data
            )

    async def manager_account_billing_usage_total(
        self,
        pk: str,
        event_types: Union[List[int], object] = sentinel,
        month_from: Union[datetime, object] = sentinel,
        month_to: Union[datetime, object] = sentinel,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        async with self.get_client() as client:
            return await client.get(
                url=f"/v1/accounts/{pk}/billing/usage/total", params=data
            )
