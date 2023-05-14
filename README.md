# Home Assistant ChatGPT Plugin

A Home Assistant Plugin for managing lights and switches in your home, using OpenAI's ChatGPT. You can turn lights and switches on and off, and change the color of lights.

## Installation and Setup

1. **Install the required packages**: Run the following command to install required packages:

```bash
pip install -r requirements.txt
```

2. **Configure the plugin:**

- Copy the example config file:
  
```bash
cp config.py.example config.py
```
- Fill in your Home Assistant URL and Bearer Token

```
headers = {
    "Authorization": "Bearer YOUR_HOME_ASSISTANT_TOKEN",
    "Content-Type": "application/json",
}
home_assistant_url = "http://YOUR_HOME_ASSISTANT_IP:PORT"
```


3. **Run the plugin:** Start the local server by running the following command:

```bash
python main.py
```

## Plugin Installation in OpenAI Chat

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter `localhost:5003` as the URL the server is running on locally, then click "Find manifest file".

The Home Assistant ChatGPT Plugin should now be installed and enabled!

## Usage Examples

You can interact with the plugin by sending commands such as:

- Please give me the status of the lights
- Please turn on light called "XXX"

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
