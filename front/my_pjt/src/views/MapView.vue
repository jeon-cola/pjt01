<script setup>
import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';
import { ref, onMounted } from 'vue';
import { useKakao } from 'vue3-kakao-maps';

// 카카오 API 키 설정 및 'services' 라이브러리 추가
useKakao('cad4bc53cce81b2c6d4a0125d893b604', ['services']);

const map = ref(null);
const markerList = ref([]);
const searchKeyword = ref('역삼역 맛집');

// 카카오 맵 로드 시 초기화
const onLoadKakaoMap = (mapRef) => {
  map.value = mapRef;
  searchPlaces(searchKeyword.value);
};

// 장소 검색
const searchPlaces = (keyword) => {
  if (!window.kakao || !window.kakao.maps || !kakao.maps.services.Places) {
    console.error('카카오 맵 서비스가 로드되지 않았습니다.');
    return;
  }

  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(keyword, placesSearchCB);
};

// 장소 검색 콜백 함수
const placesSearchCB = (data, status) => {
  if (status === kakao.maps.services.Status.OK) {
    const bounds = new kakao.maps.LatLngBounds();

    markerList.value = data.map((place) => {
      bounds.extend(new kakao.maps.LatLng(Number(place.y), Number(place.x)));
      return {
        key: place.id,
        lat: place.y,
        lng: place.x,
        infoWindow: {
          content: place.place_name,
          visible: false,
        },
      };
    });

    map.value?.setBounds(bounds);
  } else {
    console.error('검색 결과가 없습니다.');
  }
};

// 마커 클릭 시 인포윈도우 토글
const onClickMapMarker = (markerItem) => {
  markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
};

// 검색 버튼 동작
const onSearch = () => {
  searchPlaces(searchKeyword.value);
};
</script>

<template>
  <div>
    <!-- 검색 입력 및 버튼 -->
    <div>
      <input
        type="text"
        v-model="searchKeyword"
        placeholder="검색어를 입력하세요"
      />
      <button @click="onSearch">검색</button>
    </div>

    <!-- 카카오 맵 -->
    <KakaoMap
      :lat="37.566826"
      :lng="126.9786567"
      @onLoadKakaoMap="onLoadKakaoMap"
    >
      <!-- 마커 리스트 -->
      <KakaoMapMarker
        v-for="marker in markerList"
        :key="marker.key"
        :lat="marker.lat"
        :lng="marker.lng"
        :infoWindow="marker.infoWindow"
        :clickable="true"
        @onClickKakaoMapMarker="onClickMapMarker(marker)"
      />
    </KakaoMap>
  </div>
</template>
