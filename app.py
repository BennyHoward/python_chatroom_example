import os, asyncio
from quart import Quart, send_from_directory, websocket

# Directory by which the static files shall be served from
SERVING_DIRECTORY = os.path.join(os.getcwd(), 'dist')

# Create the collection where the connected users will be stored
connections = set()

# Create the Quart application
app = Quart(__name__)

# Serve the home page
@app.route('/')
async def index():
  return await send_from_directory(SERVING_DIRECTORY, 'index.html')

# Serve static files from the `./dist` folder
@app.route('/<f>')
async def static_file(f):
  return await send_from_directory(SERVING_DIRECTORY, f)

# Simple echoing WebSocket
@app.websocket('/ws')
async def ws():
  # When a new user connects, store the connection
  connections.add(websocket._get_current_object())
  try:
    while True:
      # Await new message comming from the user
      message = await websocket.receive()
      # Once a message is received, send the message to all the other connected users
      for connection in connections:
        await connection.send(f'{message}')
  # When the user disconnects (i.e. close their browser tab) remove the connection from the connection store to prevent memory leaks
  except asyncio.CancelledError:
    connections.remove(websocket._get_current_object())

# Run the application
app.run()
