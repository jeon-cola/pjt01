import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios'; 

export const useCounterStore = defineStore('counter', () => {
  const depositList=ref([])
  const savingList=ref([])
  const exchangeRateList=ref([])
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
    console.log('-----------')
    axios.get('http://localhost:8000/fin/deposit/')
    .then((response) => {
      console.log('응답 데이터:', response.data),
      depositList.value=response.data
      console.log(depositList.value)
    })
    .catch((error) => {
      console.error('에러 발생:', error.message);
    });
  };
  const getExchangeRate = function() {
    console.log('-----------')
    axios.get('http://localhost:8000/fin/exchange_rate/')
    .then((response) => {
      console.log('응답 데이터:', response.data),
      exchangeRateList.value=response.data
      console.log(exchangeRateList.value)
    })
    .catch((error) => {
      console.error('에러 발생:', error.message);
    });
  };
  return { getDeposit,depositList,getSaving,savingList,exchangeRateList,getExchangeRate};
});
