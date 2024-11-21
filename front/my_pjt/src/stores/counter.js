import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios'; 

export const useCounterStore = defineStore('counter', () => {
  const exchangeRateList=ref([])
  const filterData = ref([])
  const filterData2 = ref([])
  const result = ref(([]))
  const goToDetail = function(lst){
    result.value=lst
  }
  const send_deposit = function(){
    console.log(2)
    axios.get('http://localhost:8000/fin/send_deposit/')
    .then((response) => {
      filterData.value = response.data
      console.log('성공')
    })
    .catch((error) => {
      console.log(error)
    })
  }
  
  const send_saving = function(){
    console.log(2)
    axios.get('http://localhost:8000/fin/send_saving/')
    .then((response) => {
      filterData2.value = response.data
      console.log('성공')
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const getSaving = function() {
    axios.get('http://localhost:8000/fin/saving/')
    .then((response) => {
      console.log('응답 데이터:', response.data)
    })
    .catch((error) => {
      console.error('에러 발생:', error.message);
    });
  };
  const getDeposit = function() {
    axios.get('http://localhost:8000/fin/deposit/')
    .then((response) => {
      console.log('응답데이텅',response.data)
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
  return { getDeposit,getSaving,exchangeRateList,getExchangeRate,filterData,filterData2,goToDetail,result,send_deposit,send_saving};
});
