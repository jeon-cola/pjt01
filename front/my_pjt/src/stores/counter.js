import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios'; 

export const useCounterStore = defineStore('counter', () => {
  const depositList=ref([])
  const savingList=ref([])
  const exchangeRateList=ref([])
  const filterData = ref([])
  const result = ref(([]))
  const goToDetail = function(lst){
    result.value=lst
  }
  const filterGo = function(){
    depositList.value.result.baseList.forEach(i => {
        depositList.value.result.optionList.forEach(j=>{
            if (i.fin_prdt_cd === j.fin_prdt_cd) {
                filterData.value.push({
                  kor_co_nm: i.kor_co_nm,
                  fin_prdt_nm: i.fin_prdt_nm,
                  join_way:i.join_way,
                  mtrt_int:i.mtrt_int,
                  spcl_cnd:i.spcl_cnd,
                  etc_note:i.etc_note,
                  intr_rate: j.intr_rate,
                  intr_rate2:j.intr_rate2,
                  intr_rate_type_nm:j.intr_rate_type_nm,
                  save_trm:j.save_trm
                })
  }
})
});
}
const filterData2 = ref([])
const filterGo2 = function(){
  savingList.value.result.baseList.forEach(i => {
      savingList.value.result.optionList.forEach(j=>{
          if (i.fin_prdt_cd === j.fin_prdt_cd) {
              filterData2.value.push({
                kor_co_nm: i.kor_co_nm,
                  fin_prdt_nm: i.fin_prdt_nm,
                  join_way:i.join_way,
                  mtrt_int:i.mtrt_int,
                  spcl_cnd:i.spcl_cnd,
                  etc_note:i.etc_note,
                  intr_rate: j.intr_rate,
                  intr_rate2:j.intr_rate2,
                  intr_rate_type_nm:j.intr_rate_type_nm,
                  rsrv_type_nm:j.rsrv_type_nm,
                  save_trm:j.save_trm
              })
}
})
});
}
  const getSaving = function() {
    axios.get('http://localhost:8000/fin/saving/')
    .then((response) => {
      console.log('응답 데이터:', response.data),
      savingList.value=response.data
      filterGo2()
      console.log('필터링 데이터',filterData2)
    })
    .catch((error) => {
      console.error('에러 발생:', error.message);
    });
  };
  const getDeposit = function() {
    axios.get('http://localhost:8000/fin/deposit/')
    .then((response) => {
      console.log('응답데이텅',response.data)
      depositList.value=response.data
      filterGo()
      console.log('1',filterData.value)
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
  return { getDeposit,depositList,getSaving,savingList,exchangeRateList,getExchangeRate,filterData,filterGo,filterData2,filterGo2,goToDetail,result};
});
