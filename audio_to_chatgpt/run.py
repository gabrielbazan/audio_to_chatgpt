from typing import Dict, List

from input_files import get_files
from retrieval_plugin_gateway import RetrievalPluginGateway
from settings import (
    DOCUMENT_SOURCE,
    INPUT_FOLDER_PATH,
    YOUTUBE_VIDEO_URL_TEMPLATE,
    DocumentField,
)
from speech_recognition import SpeechRecognition


def main() -> None:
    documents = generate_documents()
    RetrievalPluginGateway.retrieve(documents)


def generate_documents() -> List[Dict]:
    return [
        {
            DocumentField.ID: input_file.filename,
            DocumentField.TEXT: SpeechRecognition.transcribe(input_file.path),
            DocumentField.METADATA: {
                DocumentField.Metadata.URL: YOUTUBE_VIDEO_URL_TEMPLATE.format(
                    input_file.filename
                ),
                DocumentField.Metadata.SOURCE: DOCUMENT_SOURCE,
            },
        }
        for input_file in get_files(INPUT_FOLDER_PATH)
    ]


if __name__ == "__main__":
    main()
