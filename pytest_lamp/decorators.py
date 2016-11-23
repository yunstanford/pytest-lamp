import asyncio


def asyncserver(host, port, server_handler=None):
	"""
		an async server for pytest.

		args: host, port, server_handler. Default
		handler provided.
	"""
    def decorator(unittest):

        async def default_handler(reader, writer):
            data = (await reader.read())
            writer.write(data)
            await writer.drain()
            writer.close()

        async def inner(*args, **kwargs):
            import asyncio
            handler = server_handler or default_handler
            server = await asyncio.start_server(handler, host,
                                                port)
            await unittest(*args, **kwargs)
            server.close()

        return inner

    return decorator
