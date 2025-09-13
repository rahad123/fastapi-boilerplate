async def async_wrapper(async_func):
    try:
        result = await async_func()
        return None, result
    except Exception as e:
        return e, None
