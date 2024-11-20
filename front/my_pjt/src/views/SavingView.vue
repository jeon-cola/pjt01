<template>
  <div>
    <h1>Saving Page</h1>
    <div v-if="store.savingList.result?.baseList">
      <div>
        <select v-model="selectedKorCoNm">
          <option value="" disabled selected>은행 선택</option>
          <option value="none">상관 없음</option>
          <option v-for="(value, index) in uniqueKorCoNm" :key="index">{{ value }}</option>
        </select>
        <select v-model="selectedIntrRate" :disabled="!uniqueIntrRate.length">
          <option value="" disabled selected>금리 선택</option>
          <option value="none">상관 없음</option>
          <option v-for="(value, index) in uniqueIntrRate" :key="index">{{ value }}</option>
        </select>
        <select v-model="selectedIntrRate2" :disabled="!uniqueIntrRate2.length">
          <option value="" disabled selected>우대 금리</option>
          <option value="none">상관 없음</option>
          <option v-for="(value, index) in uniqueIntrRate2" :key="index">{{ value }}</option>
        </select>
        <select v-model="selectedIntrRateTypeNm" :disabled="!uniqueIntrRateTypeNm.length">
          <option value="" disabled selected>금리 유형</option>
          <option value="none">상관 없음</option>
          <option v-for="(value, index) in uniqueIntrRateTypeNm" :key="index">{{ value }}</option>
        </select>
        <select v-model="selectedRsrvTypeNm" :disabled="!uniqueRsrvTypeNm.length">
          <option value="" disabled selected>적금 유형</option>
          <option value="none">상관 없음</option>
          <option v-for="(value, index) in uniqueRsrvTypeNm" :key="index">{{ value }}</option>
        </select>
        <select v-model="selectedSaveTrm" :disabled="!uniqueSaveTrm.length">
          <option value="" disabled selected>저축 기간</option>
          <option value="none">상관 없음</option>
          <option v-for="(value, index) in uniqueSaveTrm" :key="index">{{ value }}</option>
        </select>
      </div>
      <hr>
      <ul class="list-group list-group-flush">
        <li 
          class="list-group-item" 
          v-for="(result, index) in filteredData" 
          :key="index"
        >
          <p><strong>은행명:</strong> {{ result.kor_co_nm }}</p>
          <p><strong>상품명:</strong> {{ result.fin_prdt_nm }}</p>
          <p><strong>가입 방법:</strong> {{ result.join_way }}</p>
          <p><strong>만기 후 이율:</strong> {{ result.mtrt_int }}</p>
          <p><strong>특별 조건:</strong> {{ result.spcl_cnd }}</p>
          <p><strong>기타 정보:</strong> {{ result.etc_note }}</p>
          <p><strong>금리:</strong> {{ result.intr_rate }}<strong>%</strong></p>
          <p><strong>우대 금리:</strong> {{ result.intr_rate2 }}<strong>%</strong></p>
          <p><strong>금리 유형:</strong> {{ result.intr_rate_type_nm }}</p>
          <p><strong>적금 유형:</strong> {{ result.rsrv_type_nm }}</p>
          <p><strong>저축 기간:</strong> {{ result.save_trm }}<strong>개월</strong></p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>데이터를 불러오는 중입니다...</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();

// 컴포넌트가 마운트된 후 API 호출
onMounted(() => {
  store.getSaving();
});

const selectedKorCoNm = ref(""); // 회사명
const selectedIntrRate = ref(""); // 금리
const selectedIntrRate2 = ref(""); // 추가 금리
const selectedIntrRateTypeNm = ref(""); // 금리 유형
const selectedRsrvTypeNm = ref(""); // 적금 유형
const selectedSaveTrm = ref(""); // 저축 기간

// 회사명 중복 제거
const uniqueKorCoNm = computed(() => [...new Set(store.filterData2.map(item => item.kor_co_nm))]);

// 금리 중복 제거 (회사명 필터 적용)
const uniqueIntrRate = computed(() => {
  if (selectedKorCoNm.value === 'none' || !selectedKorCoNm.value) {
    return [...new Set(store.filterData2.map(item => item.intr_rate))];
  }
  return [
    ...new Set(
      store.filterData2
        .filter(item => item.kor_co_nm === selectedKorCoNm.value)
        .map(item => item.intr_rate)
    )
  ];
});

// 추가 금리 중복 제거 (회사명 + 금리 필터 적용)
const uniqueIntrRate2 = computed(() => {
  if (selectedKorCoNm.value === 'none' || selectedIntrRate.value === 'none' || !selectedKorCoNm.value || !selectedIntrRate.value) {
    return [...new Set(store.filterData2.map(item => item.intr_rate2))];
  }
  return [
    ...new Set(
      store.filterData2
        .filter(item => 
          item.kor_co_nm === selectedKorCoNm.value &&
          item.intr_rate === Number(selectedIntrRate.value)
        )
        .map(item => item.intr_rate2)
    )
  ];
});

// 금리 유형 중복 제거 (회사명 + 금리 + 추가 금리 필터 적용)
const uniqueIntrRateTypeNm = computed(() => {
  if (selectedKorCoNm.value === 'none' || selectedIntrRate.value === 'none' || selectedIntrRate2.value === 'none' || !selectedKorCoNm.value || !selectedIntrRate.value || !selectedIntrRate2.value) {
    return [...new Set(store.filterData2.map(item => item.intr_rate_type_nm))];
  }
  return [
    ...new Set(
      store.filterData2
        .filter(item =>
          item.kor_co_nm === selectedKorCoNm.value &&
          item.intr_rate === Number(selectedIntrRate.value) &&
          item.intr_rate2 === Number(selectedIntrRate2.value)
        )
        .map(item => item.intr_rate_type_nm)
    )
  ];
});

// 적금 유형 중복 제거 (모든 필터 적용)
const uniqueRsrvTypeNm = computed(() => {
  if (selectedKorCoNm.value === 'none' || selectedIntrRate.value === 'none' || selectedIntrRate2.value === 'none' || selectedIntrRateTypeNm.value === 'none' || !selectedKorCoNm.value || !selectedIntrRate.value || !selectedIntrRate2.value || !selectedIntrRateTypeNm.value) {
    return [...new Set(store.filterData2.map(item => item.rsrv_type_nm))];
  }
  return [
    ...new Set(
      store.filterData2
        .filter(item =>
          item.kor_co_nm === selectedKorCoNm.value &&
          item.intr_rate === Number(selectedIntrRate.value) &&
          item.intr_rate2 === Number(selectedIntrRate2.value) &&
          item.intr_rate_type_nm === selectedIntrRateTypeNm.value
        )
        .map(item => item.rsrv_type_nm)
    )
  ];
});

// 저축 기간 중복 제거 (모든 필터 적용)
const uniqueSaveTrm = computed(() => {
  if (selectedKorCoNm.value === 'none' || selectedIntrRate.value === 'none' || selectedIntrRate2.value === 'none' || selectedIntrRateTypeNm.value === 'none' || selectedRsrvTypeNm.value === 'none' || !selectedKorCoNm.value || !selectedIntrRate.value || !selectedIntrRate2.value || !selectedIntrRateTypeNm.value || !selectedRsrvTypeNm.value) {
    return [...new Set(store.filterData2.map(item => item.save_trm))];
  }
  return [
    ...new Set(
      store.filterData2
        .filter(item =>
          item.kor_co_nm === selectedKorCoNm.value &&
          item.intr_rate === Number(selectedIntrRate.value) &&
          item.intr_rate2 === Number(selectedIntrRate2.value) &&
          item.intr_rate_type_nm === selectedIntrRateTypeNm.value &&
          item.rsrv_type_nm === selectedRsrvTypeNm.value
        )
        .map(item => item.save_trm)
    )
  ];
});

// 필터된 데이터
const filteredData = computed(() => {
  return store.filterData2.filter(item => {
    return (
      (selectedKorCoNm.value === 'none' || !selectedKorCoNm.value || item.kor_co_nm === selectedKorCoNm.value) &&
      (selectedIntrRate.value === 'none' || !selectedIntrRate.value || item.intr_rate === Number(selectedIntrRate.value)) &&
      (selectedIntrRate2.value === 'none' || !selectedIntrRate2.value || item.intr_rate2 === Number(selectedIntrRate2.value)) &&
      (selectedIntrRateTypeNm.value === 'none' || !selectedIntrRateTypeNm.value || item.intr_rate_type_nm === selectedIntrRateTypeNm.value) &&
      (selectedRsrvTypeNm.value === 'none' || !selectedRsrvTypeNm.value || item.rsrv_type_nm === selectedRsrvTypeNm.value) &&
      (selectedSaveTrm.value === 'none' || !selectedSaveTrm.value || item.save_trm === Number(selectedSaveTrm.value))
    );
  });
});
</script>
