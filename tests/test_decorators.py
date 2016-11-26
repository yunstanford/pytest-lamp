import asyncio
import pytest
from pytest_lamp import asyncserver


@pytest.mark.asyncio
@asyncserver('127.0.0.1', 8080)
async def test_async_server_decorator():
    loop = asyncio.get_event_loop()
    reader, writer = await asyncio.open_connection(
                    '127.0.0.1', 8080, loop=loop)
    message = "pytest-lamp"
    writer.write(message.encode("ascii"))
    await writer.drain()
    writer.write_eof()
    await  writer.drain()
    data = (await reader.read()).decode("utf-8")
    writer.close()
    assert message == data
