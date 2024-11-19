<template>
  <div>
    <h1>Deposit Page</h1>
    <div v-if="store.depositList.result?.baseList">
      <ul class="list-group list-group-flush">
        <li 
          class="list-group-item" 
          v-for="(result, index) in store.depositList.result.baseList" 
          :key="index"
        >
          <p><strong>은행명:</strong> {{ result.kor_co_nm }}</p>
          <p><strong>상품명:</strong> {{ result.fin_prdt_nm }}</p>
          <p><strong>가입 방법:</strong> {{ result.join_way }}</p>
          <p><strong>만기 후 이율:</strong> {{ result.mtrt_int }}</p>
          <p><strong>특별 조건:</strong> {{ result.spcl_cnd }}</p>
          <p><strong>기타 정보:</strong> {{ result.etc_note }}</p>
          epdlxj{{ store.fillterData }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p>데이터를 불러오는 중입니다...</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted,computed,ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
// store 사용
const store = useCounterStore();
// 컴포넌트가 마운트된 후 API 호출
onMounted(() => {
  store.getDeposit()
});
</script>

<style scoped>
.list-group-item {
  margin-bottom: 10px;
  padding: 15px;
  border: 1px solid #ddd;
}
</style>
