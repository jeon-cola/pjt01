<template>
  <div>
    <h1>Exchange Rate</h1>
    <form >
      <input type="text" id="text" v-model="text">
      <input type="submit" value="계산하기">
    </form>
    <hr>
    <div v-for=" result in store.exchangeRateList ">
    
      {{ result.cur_unit }}
      {{ result.cur_nm }}
      {{ result.deal_bas_r }} 원
      <hr>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted,ref,computed } from 'vue';
const store = useCounterStore()
onMounted(()=>{
  store.getExchangeRate()
})
const text = ref(null)
const Exchange = function(){

}
</script>

<style  scoped>

</style>