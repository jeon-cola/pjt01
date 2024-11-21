<script setup>
import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';
import { ref } from 'vue';
import { useKakao } from 'vue3-kakao-maps';

useKakao('cad4bc53cce81b2c6d4a0125d893b604', ['services']);

const map = ref(null);
const markerList = ref([]);
const searchKeyword = ref('삼성 하남 공장');

const onLoadKakaoMap = (mapRef) => {
  map.value = mapRef;
  setTimeout(() => {
    map.value.relayout(); // 레이아웃 갱신
  }, 100);
  searchNearbyBanks();
};

const searchPlaces = (keyword) => {
  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(keyword, placesSearchCB);
};

const searchNearbyBanks = () => {
  if (!window.kakao || !window.kakao.maps || !kakao.maps.services.Places) {
    console.error('카카오 맵 서비스가 로드되지 않았습니다.');
    return;
  }

  const ps = new kakao.maps.services.Places();
  const center = map.value.getCenter();
  ps.keywordSearch('은행', placesSearchCB, {
    location: new kakao.maps.LatLng(center.getLat(), center.getLng()),
    radius: 5000,
  });
};

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
          content: `<div class="info-window">${place.place_name}</div>`,
          visible: false,
        },
      };
    });

    map.value?.setBounds(bounds);
  } else {
    window.alert('검색 결과가 없습니다');
    console.error('검색 결과가 없습니다.');
  }
};

const onClickMapMarker = (markerItem) => {
  markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
};

const onSearch = () => {
  searchPlaces(searchKeyword.value);
};
</script>

<template>
  <div class="map-container">
    <div class="search-container">
      <div class="search-bar">
        <input
          v-model="searchKeyword"
          placeholder="검색어를 입력하세요"
        />
        <button @click="onSearch">검색</button>
        <button @click="searchNearbyBanks">근처 은행</button>
      </div>
    </div>

    <KakaoMap
      class="kakao-map"
      :lat="37.566826"
      :lng="126.9786567"
      style="width: 100%; height: 100%;"
      @onLoadKakaoMap="onLoadKakaoMap"
    >
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

<style scoped>
/* 전체 화면 */
.map-container {
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
}

.kakao-map {
  width: 100%;
  height: 100%;
}

/* 검색창 컨테이너 */
.search-container {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  background: rgba(255, 255, 255, 0.95);
  padding: 20px 25px;
  border-radius: 30px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

/* 검색 바 */
.search-bar {
  display: flex;
  gap: 15px;
  align-items: center;
}

.search-bar input {
  flex: 1;
  padding: 12px 15px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 25px;
  outline: none;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.search-bar input:focus {
  border-color: #5dade2;
  box-shadow: 0 0 5px rgba(93, 173, 226, 0.7);
}

.search-bar button {
  padding: 12px 20px;
  font-size: 14px;
  color: white;
  background-color: #5dade2;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.search-bar button:hover {
  background-color: #3498db;
  transform: scale(1.05);
}

/* 인포윈도우 스타일 */
.info-window {
  background: rgba(255, 255, 255, 0.95);
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 14px;
  text-align: center;
  color: #333;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  max-width: 200px;
}
</style>
