<template>
  <div>
    <h1>Deposit Page</h1>
    <div v-if="filteredData.length>0">
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
      <select v-model="selectedSaveTrm" :disabled="!uniqueSaveTrm.length">
        <option value="" disabled selected>저축 기간</option>
        <option value="none">상관 없음</option>
        <option v-for="(value, index) in uniqueSaveTrm" :key="index">{{ value }}</option>
      </select>
      <hr>
      <ul class="list-group list-group-flush">
        <li
          class="list-group-item" 
          v-for="(result, index) in filteredData" 
          :key="index"
          @click="goToDetail(result)"
        >
          <p><strong>은행명:</strong> {{ result.kor_co_nm }}</p>
          <p><strong>상품명:</strong> {{ result.fin_prdt_nm }}</p>
          <p><strong>금리:</strong> {{ result.intr_rate }}<strong>%</strong></p>
          <p><strong>우대 금리:</strong> {{ result.intr_rate2 }}<strong>%</strong></p>
          <p><strong>금리 유형:</strong> {{ result.intr_rate_type_nm }}</p>
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
import { useRouter } from 'vue-router';
const router = useRouter()

const store = useCounterStore();

// API 호출
onMounted(() => {
  store.getDeposit();
});

const selectedKorCoNm = ref(""); // 회사명
const selectedIntrRate = ref(""); // 금리
const selectedIntrRate2 = ref(""); // 추가 금리
const selectedIntrRateTypeNm = ref(""); // 금리 유형
const selectedSaveTrm = ref(""); // 저축 기간

// 회사명 중복 제거 (모든 데이터 기준)
const uniqueKorCoNm = computed(() => [...new Set(store.filterData.map(item => item.kor_co_nm).sort())]);

// 금리 중복 제거 (회사명 필터 적용)
const uniqueIntrRate = computed(() => {
  if (selectedKorCoNm.value === 'none' || !selectedKorCoNm.value) {
    return [...new Set(store.filterData.map(item => item.intr_rate).sort())];
  }
  return [
    ...new Set(
      store.filterData
        .filter(item => item.kor_co_nm === selectedKorCoNm.value)
        .map(item => item.intr_rate).sort()
    )
  ];
});

// 추가 금리 중복 제거 (회사명 + 금리 필터 적용)
const uniqueIntrRate2 = computed(() => {
  if (selectedKorCoNm.value === 'none' || selectedIntrRate.value === 'none' || !selectedKorCoNm.value || !selectedIntrRate.value) {
    return [...new Set(store.filterData.map(item => item.intr_rate2).sort())];
  }
  return [
    ...new Set(
      store.filterData
        .filter(item => 
          item.kor_co_nm === selectedKorCoNm.value &&
          item.intr_rate === Number(selectedIntrRate.value)
        )
        .map(item => item.intr_rate2).sort()
    )
  ];
});

// 금리 유형 중복 제거 (회사명 + 금리 + 추가 금리 필터 적용)
const uniqueIntrRateTypeNm = computed(() => {
  if (selectedKorCoNm.value === 'none' || selectedIntrRate.value === 'none' || selectedIntrRate2.value === 'none' || !selectedKorCoNm.value || !selectedIntrRate.value || !selectedIntrRate2.value) {
    return [...new Set(store.filterData.map(item => item.intr_rate_type_nm).sort())];
  }
  return [
    ...new Set(
      store.filterData
        .filter(item =>
          item.kor_co_nm === selectedKorCoNm.value &&
          item.intr_rate === Number(selectedIntrRate.value) &&
          item.intr_rate2 === Number(selectedIntrRate2.value)
        )
        .map(item => item.intr_rate_type_nm).sort()
    )
  ];
});

// 저축 기간 중복 제거 (모든 필터 적용)
const uniqueSaveTrm = computed(() => {
  if (selectedKorCoNm.value === 'none' || selectedIntrRate.value === 'none' || selectedIntrRate2.value === 'none' || selectedIntrRateTypeNm.value === 'none' || !selectedKorCoNm.value || !selectedIntrRate.value || !selectedIntrRate2.value || !selectedIntrRateTypeNm.value) {
    return [...new Set(store.filterData.map(item => item.save_trm).sort())];
  }
  return [
    ...new Set(
      store.filterData
        .filter(item =>
          item.kor_co_nm === selectedKorCoNm.value &&
          item.intr_rate === Number(selectedIntrRate.value) &&
          item.intr_rate2 === Number(selectedIntrRate2.value) &&
          item.intr_rate_type_nm === selectedIntrRateTypeNm.value
        )
        .map(item => item.save_trm).sort()
    )
  ];
});

// 필터된 데이터
const filteredData = computed(() => {
  return store.filterData.filter(item => {
    return (
      (selectedKorCoNm.value === 'none' || !selectedKorCoNm.value || item.kor_co_nm === selectedKorCoNm.value) &&
      (selectedIntrRate.value === 'none' || !selectedIntrRate.value || item.intr_rate === Number(selectedIntrRate.value)) &&
      (selectedIntrRate2.value === 'none' || !selectedIntrRate2.value || item.intr_rate2 === Number(selectedIntrRate2.value)) &&
      (selectedIntrRateTypeNm.value === 'none' || !selectedIntrRateTypeNm.value || item.intr_rate_type_nm === selectedIntrRateTypeNm.value) &&
      (selectedSaveTrm.value === 'none' || !selectedSaveTrm.value || item.save_trm === Number(selectedSaveTrm.value))
    ); 
  }).sort();
});
const goToDetail = async (result) => {
  await store.goToDetail(result); 
  router.push({ name: 'detail' }); 
};
</script>


<style scoped>
.list-group-item {
  margin-bottom: 10px;
  padding: 15px;
  border: 1px solid #ddd;
}
</style>
