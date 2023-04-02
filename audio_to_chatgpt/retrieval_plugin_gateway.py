from requests import Session
from requests.adapters import HTTPAdapter, Retry
from settings import (
    AUTHORIZATION_HEADER_NAME,
    AUTHORIZATION_TYPE_BEARER,
    RETRIEVAL_PLUGIN_BEARER_TOKEN,
    RETRIEVAL_PLUGIN_RETRIES,
    RETRIEVAL_PLUGIN_RETRY_BACKOFF_FACTOR,
    RETRIEVAL_PLUGIN_SCHEMA,
    RETRIEVAL_PLUGIN_UPSERT_CHUNK_SIZE,
    RETRIEVAL_PLUGIN_UPSERT_DOCUMENTS_KEY,
    RETRIEVAL_PLUGIN_UPSERT_ENDPOINT,
)


class RetrievalPluginGateway:
    @staticmethod
    def retrieve(documents):
        retries = Retry(
            total=RETRIEVAL_PLUGIN_RETRIES,
            backoff_factor=RETRIEVAL_PLUGIN_RETRY_BACKOFF_FACTOR,
        )

        session = Session()
        session.mount(RETRIEVAL_PLUGIN_SCHEMA, HTTPAdapter(max_retries=retries))

        chunk = []

        for document in documents:
            chunk.append(document)

            if len(chunk) == RETRIEVAL_PLUGIN_UPSERT_CHUNK_SIZE:
                RetrievalPluginGateway.upsert(session, chunk)
                chunk = []

        if chunk:
            RetrievalPluginGateway.upsert(session, chunk)

    @staticmethod
    def upsert(session, documents):
        authorization = f"{AUTHORIZATION_TYPE_BEARER} {RETRIEVAL_PLUGIN_BEARER_TOKEN}"

        response = session.post(
            RETRIEVAL_PLUGIN_UPSERT_ENDPOINT,
            headers={AUTHORIZATION_HEADER_NAME: authorization},
            json={
                RETRIEVAL_PLUGIN_UPSERT_DOCUMENTS_KEY: documents,
            },
        )

        response.raise_for_status()
