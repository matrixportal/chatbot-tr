const express = require('express')
const app = express()
const port = 5000

const { PythonShell } = require('python-shell')

// create a new PythonShell instance
let pyshell = new PythonShell('chatbot.py')

// create an array to store messages
let messages = []

// create a single message listener
pyshell.on('message', function (message) {
  console.log(`Received message: ${message}`)
  messages.push(message)
})

app.use(express.static('public'))

app.get('/', (req, res) => {
  res.send(`
    <html>
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="/styles.css">
      </head>
      <body>
        <h1>Chatbot</h1>
        <form action="/chat" method="GET">
          <input type="text" name="msg" placeholder="Type your message here" />
          <button type="submit">Send</button>
        </form>
        <div id="messages"></div>
      </body>
    </html>
  `)
})

app.get('/chat', (req, res) => {
  const sentence = req.query.msg
  pyshell.send(sentence)

  // wait for messages to arrive
  const intervalId = setInterval(() => {
    if (messages.length > 0) {
      // send all messages as the HTTP response
      res.send(`
        <html>
          <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" type="text/css" href="/styles.css">
          </head>
          <body>
          <link rel="stylesheet" type="text/css" href="style.css">
            <h1>Chatbot</h1>
            <form action="/chat" method="GET">
              <input type="text" name="msg" placeholder="Type your message here" />
              <button type="submit">Send</button>
            </form>
            <div id="messages">
              ${messages.map(message => `<p>${message}</p>`).join('')}
            </div>
          </body>
        </html>
      `)

      // clear the messages array
      messages = []

      // clear the interval
      clearInterval(intervalId)
    }
  }, 100)
})

app.listen(port, () => {
  console.log(`Chatbot server listening on port ${port}`)
})
