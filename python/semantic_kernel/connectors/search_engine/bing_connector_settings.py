# Copyright (c) Microsoft. All rights reserved.

from typing import ClassVar

from pydantic import SecretStr

from semantic_kernel.kernel_pydantic import KernelBaseSettings


class BingSettings(KernelBaseSettings):
    """Bing Connector settings.

    The settings are first loaded from environment variables with the prefix 'BING_'. If the
    environment variables are not found, the settings can be loaded from a .env file with the
    encoding 'utf-8'. If the settings are not found in the .env file, the settings are ignored;
    however, validation will fail alerting that the settings are missing.

    Optional settings for prefix 'BING_' are:
    - api_key: SecretStr - The Bing API key (Env var BING_API_KEY)

    """

    env_prefix: ClassVar[str] = "BING_"

    api_key: SecretStr | None = None
