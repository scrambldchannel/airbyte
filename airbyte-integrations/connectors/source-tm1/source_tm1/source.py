from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import logging
from airbyte_cdk import AirbyteLogger
from airbyte_cdk.models import SyncMode
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from TM1py import TM1Service

logger = logging.getLogger("airbyte")

class SourceTM1(AbstractSource):

    def _get_auth_dict(self, config: Mapping[str, Any]):

        # just do basic auth for now
        host = config.get("host")
        port = config.get("port")
        username = config.get("username")
        password = config.get("password")

        return {
            "address": host,
            "port": port,
            # "ssl": True,
            "user": username,
            "password": password,
        }


    def check_connection(self, logger: AirbyteLogger, config: Mapping[str, Any]) -> Tuple[bool, Optional[Any]]:
        
        try:
            auth = self._get_auth_dict(config)
            with TM1Service(**auth) as tm1:

                name = tm1.server.get_server_name()

            return True, None

        except Exception as e:
            return (
                False,
                f"Got an exception while trying to set up the connection: {e}. "
                f"Check the connection information provided and try again.",
            )

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:

        pass