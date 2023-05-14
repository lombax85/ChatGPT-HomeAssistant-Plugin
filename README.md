## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

Configure the plugin:

- Copy the example config file
  
```bash
cp config.py.example config.py
```
- Fill your Home Assistant URL and Bearer Token


To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! 

You can start by asking:

- Please give me the status of the lights
- Please turn on light called "XXX"

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
