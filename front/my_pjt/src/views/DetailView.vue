<template>
  <div>
    <h1>Detail Page</h1>
    <div v-if="store.result">
      {{ store.result.lst }}
      <p><strong>은행명:</strong> {{ store.result.kor_co_nm }}</p>
      <p><strong>상품명:</strong> {{ store.result.fin_prdt_nm }}</p>
      <p><strong>가입 방법:</strong> {{ store.result.join_way }}</p>
      <p><strong>만기 후 이율:</strong> {{ store.result.mtrt_int }}</p>
      <p><strong>특별 조건:</strong> {{ store.result.spcl_cnd }}</p>
      <p><strong>기타 정보:</strong> {{ store.result.etc_note }}</p>
      <p><strong>금리:</strong> {{ store.result.intr_rate }}<strong>%</strong></p>
      <p><strong>우대 금리:</strong> {{ store.result.intr_rate2 }}<strong>%</strong></p>
      <p><strong>금리 유형:</strong> {{ store.result.intr_rate_type_nm }}</p>
      <p><strong>적금 유형:</strong> {{ store.result.rsrv_type_nm }}</p>
      <p><strong>저축 기간:</strong> {{ store.result.save_trm }}<strong>개월</strong></p>
      <input type="submit" value="조하욘">
    </div>

    <div v-else>
      <p>데이터를 불러오는 중입니다...</p>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
console.log(store.result)
</script>