<template>
  <div>
    <h1>Exchange Rate</h1>
      <select v-model="selectCurrent">
        <option  v-for=" result in store.exchangeRateList" :key="result.cur_unit" :value='result'>
          {{result.cur_nm}}
        </option>
      </select>

    <form v-if="selectCurrent">
      <input type="text" id="text" v-model="text" :placeholder='selectCurrent.cur_unit'><br>
      <input type="text" id="text2" v-model="text2" placeholder="원">
    </form>
    
    <hr>
    <div v-if="selectCurrent">
      <p>{{ selectCurrent.cur_nm }} {{ selectCurrent.cur_unit }}</p>
      <p>{{ exchangeCost }} 원</p>
      <p>{{ exchangeCost2 }} {{ selectCurrent.cur_unit }}</p>
    </div>
    <hr>

  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted,ref,computed, getCurrentInstance } from 'vue';
const store = useCounterStore()
onMounted(()=>{
  store.getExchangeRate()
})
const text = ref(null)
const selectCurrent = ref(null)
const text2 = ref(null)

const exchangeCost = computed(()=>{
  if (selectCurrent.value && text.value) {
    let dealBaseR=selectCurrent.value.deal_bas_r
    if (dealBaseR.includes(',')){
      dealBaseR = Number(dealBaseR.replace(/,/g, ''))
    } else {
      dealBaseR = Number(dealBaseR)
    }

    const amount = Number(text.value)
    return dealBaseR*amount
  }
  return 0
})

const exchangeCost2 = computed(()=>{
  if (selectCurrent.value && text2.value) {
    let dealBaseR2=selectCurrent.value.deal_bas_r
    if (dealBaseR2.includes(',')){
      dealBaseR2 = Number(dealBaseR2.replace(/,/g, ''))
    } else {
      dealBaseR2 = Number(dealBaseR2)
    }

    const amount2 = Number(text2.value)
    return (amount2/dealBaseR2)
  }
  return 0
})
</script>

<style  scoped>

</style>