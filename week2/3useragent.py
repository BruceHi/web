from fake_useragent import UserAgent

# 去除 ssl 验证
ua = UserAgent(verify_ssl=False)

print(f'Chrome browser: {ua.chrome}')

print(f'ie: {ua.ie}')

print(f'safari: {ua.safari}')

print(f'random browser: {ua.random}')
