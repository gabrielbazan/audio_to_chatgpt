import json
from typing import Dict, Generator

from audio_transcription import transcribe
from input_files import get_files
from retrieval_plugin_gateway import RetrievalPluginGateway
from settings import (
    DOCUMENT_SOURCE,
    INPUT_FOLDER_PATH,
    YOUTUBE_VIDEO_URL_TEMPLATE,
    DocumentField,
)


def main() -> None:
    # documents = generate_documents()
    # save_cache_file(documents)
    documents = read_from_cache()
    RetrievalPluginGateway.upsert_in_chunks(documents)


def generate_documents() -> Generator[Dict, None, None]:
    return (
        {
            DocumentField.ID: input_file.filename,
            DocumentField.TEXT: transcribe(input_file.path),
            DocumentField.METADATA: {
                DocumentField.Metadata.URL: YOUTUBE_VIDEO_URL_TEMPLATE.format(
                    input_file.filename
                ),
                DocumentField.Metadata.SOURCE: DOCUMENT_SOURCE,
            },
        }
        for input_file in get_files(INPUT_FOLDER_PATH)
    )


def save_cache_file(documents):
    with open("./cache/dataset.json", "w") as f:
        json.dump(documents, f, indent=4)


def read_from_cache():
    with open("./cache/dataset.json", "r") as f:
        return json.load(f)


if __name__ == "__main__":
    main()
