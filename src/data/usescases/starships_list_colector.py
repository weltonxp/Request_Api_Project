from typing import Dict, List, Type
from src.domain.usecases import StarshipsListColectorInterface
from src.infra import SwapiApiConsumer

class StarshipsListColector(StarshipsListColectorInterface):
    ''' StarshipsListColector usecase '''

    def __init__(self, api_consumer: Type[SwapiApiConsumer]) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        response = self.__api_consumer.get_starships(page)
        print(response)