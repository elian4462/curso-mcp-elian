import conversation

conversation.history = []
conversation.MAX_TURNS = 10
print('--- RATE_LIMIT ---')
for i in range(1, 21):
    try:
        print(f'Request {i}: {conversation.send(f"Cuenta hasta {i}.")}')
    except Exception as exc:
        print(f'ERROR_AT_{i}: {type(exc).__name__}: {exc}')
        break
