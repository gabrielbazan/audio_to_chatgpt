# Audio to ChatGPT

**Train ChatGPT with audio.**

This component recognizes speech from your audio files and feeds it to a 
[ChatGPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin) instance.

This project has been generated with [create_app](https://github.com/application-creators/create_app).


## How to use

1. Place your mp3 files in [audio_to_chatgpt/input](/audio_to_chatgpt/input)
2. In the [variables.env](/variables.env) file, put the Retrieval Plugin bearer token in the RETRIEVAL_PLUGIN_BEARER_TOKEN variable
3. Make sure the Retrieval Plugin and its datastore are running
4. Build the Docker image:
    ```bash
   make docker_build
    ```
5. Run the Docker image:
    ```bash
   make docker_run
    ```
