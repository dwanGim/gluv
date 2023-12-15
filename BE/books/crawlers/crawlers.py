import os
from urllib.parse import urlencode
import requests
import copy

class AladinCrawler:
    # Base URL 및 Endpoint
    url = "http://www.aladin.co.kr"
    endpoint = "/ttb/api/ItemList.aspx" 

    params = {
        # QueryType: 검색 유형 (신간 전체 리스트)
        'QueryType': 'ItemNewAll', 
        # MaxResults: 최대 결과 수
        'MaxResults' : 10, 
        # start: 시작 위치
        'start' : 1, 
        # SearchTarget: 검색 대상 (도서)
        'SearchTarget' : 'Book',
        # sort: 정렬 기준 (최신순)
        'sort' :'latest',
        # output: 응답 형식 (JSON 형식)
        'output' : 'JS',
        # Version: 응답 형식 버전
        'Version' : '20131101',
    }
    
    def get_api_key(self):
        '''
        API 키를 환경 변수에서 가져오는 메서드
        '''
        return os.getenv("ttbkey")
    
    def request(self):
        '''
        API에 요청을 보내는 메서드
        '''
        params = copy.deepcopy(self.params)
        params['ttbkey'] = self.get_api_key()
        url = f'{self.url}{self.endpoint}?{urlencode(params)}'
        return requests.get(url)
    
    def crawl(self):
        '''
        크롤링을 수행하는 메서드
        '''
        return self.request()
    
