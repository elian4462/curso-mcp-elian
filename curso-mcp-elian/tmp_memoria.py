import conversation

conversation.history = []
conversation.MAX_TURNS = 10
print('--- MEMORIA ---')
print(conversation.send('Me llamo Alex y mi color favorito es el verde.'))
print(conversation.send('¿Qué framework de Python vimos en la Clase 1?'))
print(conversation.send('Dame un ejemplo de dato que no cabe en un int.'))
print(conversation.send('¿Qué hace el comando uv init?'))
print(conversation.send('Explica en una frase qué es un token.'))
print(conversation.send('¿Qué significa que una API sea stateless?'))
print(conversation.send('¿Para qué sirve un archivo .env?'))
print(conversation.send('¿Cómo me llamo y cuál es mi color favorito?'))
