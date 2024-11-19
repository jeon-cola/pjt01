import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios'; 

export const useCounterStore = defineStore('counter', () => {
  const depositList=ref([])
  const savingList=ref([])
  const exchangeRateList=ref([])
  const filterData = ref([])
  const filterGo = function(){
    depositList.value.result.baseList.forEach(i => {
        depositList.value.result.optionList.forEach(j=>{
            if (i.fin_co_no === j.fin_co_no) {
                filterData.value.push({i,j})
  }
})
});
}
  const getSaving = function() {
    axios.get('http://localhost:8000/fin/saving/')
    .then((response) => {
      console.log('응답 데이터:', response.data),
      savingList.value=response.data
      console.log(savingList.value)
    })
    .catch((error) => {
      console.error('에러 발생:', error.message);
    });
  };
  const getDeposit = function() {
    axios.get('http://localhost:8000/fin/deposit/')
    .then((response) => {
      depositList.value=response.data
      filterGo()
      console.log('1',filterData)
    })
    .catch((error) => {
      console.error('에러 발생:', error.message);
    });
  };
  const getExchangeRate = function() {
    axios.get('http://localhost:8000/fin/exchange_rate/')
    .then((response) => {
      console.log('응답 데이터:', response.data),
      exchangeRateList.value=response.data
    })
    .catch((error) => {
      console.error('에러 발생:', error.message);
    });
  };
  return { getDeposit,depositList,getSaving,savingList,exchangeRateList,getExchangeRate};
});
