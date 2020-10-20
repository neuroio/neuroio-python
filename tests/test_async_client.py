# from neuroio import AsyncClient, Client
#
#
# def test_async_client_different_user_agent_from_sync_client():
#     neuroio = Client(api_token="helloworld")
#     neuroio_async = AsyncClient(api_token="helloworld")
#     assert (
#         neuroio.api_client.headers["User-Agent"]
#         != neuroio_async.api_client.headers["User-Agent"]
#     )
