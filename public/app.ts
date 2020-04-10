import $ from 'jquery';

const ws: WebSocket = new WebSocket('ws://localhost:5000/ws');

/**
 * Sets the callback for the onmessage event for the websocket
 */
ws.onmessage = (event: MessageEvent): void => {
  $('#ws-messages').append($(`<li class="list-group-item">${String(event.data)}</li>`));
}

/**
 * Sets the event listener on the Send button
 */
$('#send-button').click((): void => {
  const msg: string = String($('#message-to-send').val());
  ws.send(msg);
  $('#message-to-send').val('');
});
